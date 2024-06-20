from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import KPIListSerializer
from business_profile.models import BusinessProfile
from rest_framework.response import Response
from upload_data.models import RestaurantCSV
from rest_framework import status
from django.shortcuts import get_object_or_404

class GetBusinessStats(APIView):
    serializer_class = KPIListSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        user = self.request.user
        return get_object_or_404(BusinessProfile, business_owner=user, pk=pk)

    def get(self, request, pk):
        business_profile = self.get_object(pk)
        business_kpis = business_profile.kpi.values_list('name', flat=True)
        business_type = business_profile.business_type.name

        if business_type == 'Restaurant':
            data = RestaurantCSV.objects.filter(business_profile_id=business_profile.id).values('kpi', 'actual')
            # Group the data by 'kpi' and calculate the sum of 'actual' for each group
            response_data = []
            for kpi_name in business_kpis:
                kpi_data = [item for item in data if item['kpi'] == kpi_name]
                kpi_sum = sum(item['actual'] for item in kpi_data)
                response_data.append({'name': kpi_name, 'value': round(kpi_sum, 2)})

            serializer = self.serializer_class(data={'kpi': response_data})

            if serializer.is_valid():
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif business_type == 'Grocery/Mart':
            return Response({'message': 'Not implemented yet'}, status=status.HTTP_200_OK)

        else:
            return Response({'message': 'Not implemented yet'}, status=status.HTTP_400_BAD_REQUEST)