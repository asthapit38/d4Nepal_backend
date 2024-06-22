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
import logging
logger = logging.getLogger(__name__)


def create_db(file_path, user, business_profile):
    logger.info(f"Starting to process file: {file_path}")
    try:
        df = pd.read_csv(file_path, delimiter=',')
        logger.info(f"CSV file read successfully. Shape: {df.shape}")
        with transaction.atomic():
            objects = [
                RestaurantCSV(
                    year=row[0],
                    month_no=row[1],
                    month_nm=row[2],
                    quarter=row[3],
                    year_month=row[4],
                    week=row[5],
                    week_ending_mon_sun_dt=row[6],
                    min_order_datetime=row[7],
                    kpi=row[8],
                    menu_category=row[9],
                    menu_group=row[10],
                    menu_item=row[11],
                    actual=row[12],
                    user=user,
                    business_profile=business_profile,
                )
                for row in df.values
            ]
            RestaurantCSV.objects.bulk_create(objects, batch_size=1000)
        logger.info("Data successfully inserted into database")
    except pd.errors.EmptyDataError:
        logger.error("The CSV file is empty")
        raise
    except pd.errors.ParserError as e:
        logger.error(f"Error parsing CSV file: {str(e)}")
        raise
    except Exception as e:
        logger.exception(f"Unexpected error in create_db: {str(e)}")
        raise
    finally:
        if default_storage.exists(file_path):
            default_storage.delete(file_path)
            logger.info(f"Deleted file: {file_path}")


class FileUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = UploadDataSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                upload_file = serializer.save(user=self.request.user)
                business_profile = BusinessProfile.objects.get(
                    business_owner=self.request.user,
                    id=self.request.data.get('business_profile_id')
                )
                logger.info(f"File uploaded: {upload_file.file.path}")
                create_db(upload_file.file.path, self.request.user, business_profile)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                logger.error(f"Serializer errors: {serializer.errors}")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except BusinessProfile.DoesNotExist:
            logger.error("Business profile not found")
            return Response({"error": "Business profile not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.exception(f"Unexpected error in FileUploadAPIView: {str(e)}")
            return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
