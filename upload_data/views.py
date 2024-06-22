from rest_framework.parsers import FormParser, MultiPartParser
from upload_data.serializers import UploadDataSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import pandas as pd
from upload_data.models import RestaurantCSV
from business_profile.models import BusinessProfile
from django.db import connection, transaction
from django.core.files.storage import default_storage


def create_db(file_path, user, business_profile):
    df = pd.read_csv(file_path, delimiter=',')
    list_of_csv = [list(row) for row in df.values]
    connection.autocommit = False
    transaction.set_autocommit(False)
    try:
        objects = []
        for rows in list_of_csv:
            obj = RestaurantCSV(
                year=rows[0],
                month_no=rows[1],
                month_nm=rows[2],
                quarter=rows[3],
                year_month=rows[4],
                week=rows[5],
                week_ending_mon_sun_dt=rows[6],
                min_order_datetime=rows[7],
                kpi=rows[8],
                menu_category=rows[9],
                menu_group=rows[10],
                menu_item=rows[11],
                actual=rows[12],
                user=user,
                business_profile=business_profile,
            )
            objects.append(obj)

        RestaurantCSV.objects.bulk_create(objects, batch_size=1000)

        transaction.commit()
    except Exception as e:
        transaction.rollback()
        # todo delete the uploaded file from the server if data entry is unsuccessful.
        default_storage.delete(file_path)
        print(e)
        return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    finally:
        connection.autocommit = True


class FileUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = UploadDataSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            upload_file = serializer.save(user=self.request.user)
            business_profile = BusinessProfile.objects.get(business_owner=self.request.user,
                                                           id=self.request.data.get('business_profile_id'))
            create_db(upload_file.file.path, self.request.user, business_profile)

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
