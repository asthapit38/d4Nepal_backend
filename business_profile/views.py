from .models import BusinessProfile
from .serializers import BusinessProfileSerializer
from rest_framework import generics
from kpi.models import Kpi
from business_type.models import BusinessType
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response


class BusinessProfileListCreate(generics.ListCreateAPIView):
    serializer_class = BusinessProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BusinessProfile.objects.filter(business_owner=self.request.user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            business_type_id = self.request.data.get('business_type_id')
            business_type = get_object_or_404(BusinessType, id=business_type_id)
            business = serializer.save(business_owner=self.request.user, business_type=business_type)
            kpis = self.request.data.get('kpi', [])
            kpi = Kpi.objects.filter(id__in=kpis)
            business.kpi.add(*kpi)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BusinessProfileUpdate(generics.UpdateAPIView):
    serializer_class = BusinessProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BusinessProfile.objects.filter(business_owner=self.request.user)

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save(business_owner=self.request.user)
        else:
            print(serializer.errors)


class BusinessProfileDelete(generics.DestroyAPIView):
    serializer_class = BusinessProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BusinessProfile.objects.filter(business_owner=self.request.user)


class BusinessProfileList(generics.ListAPIView):
    serializer_class = BusinessProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BusinessProfile.objects.filter(business_owner=self.request.user)
