from rest_framework import generics
from .models import BusinessType
from .serializers import BusinessTypeSerializer
from kpi.models import Kpi
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class BusinessTypeList(generics.ListAPIView):
    serializer_class = BusinessTypeSerializer

    def get_queryset(self):
        return BusinessType.objects.all()


class BusinessTypeCreate(generics.CreateAPIView):
    serializer_class = BusinessTypeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.is_valid():
            business_type = serializer.save()
            kpi_ids = self.request.data.get('kpi_ids', [])
            kpis = Kpi.objects.filter(id__in=kpi_ids)
            business_type.kpi.add(*kpis)
        else:
            print(serializer.errors)


class BusinessTypeRetrieve(generics.RetrieveAPIView):
    serializer_class = BusinessTypeSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        print(self.kwargs.get('id'))
        business_type_id = self.kwargs.get('id')
        return BusinessType.objects.all().filter(id=business_type_id)

