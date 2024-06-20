from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Kpi
from . import serializers
from rest_framework import status
from rest_framework.response import Response


class KpiListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.KpiSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Kpi.objects.all()

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied('You must be authenticated to create a kpi.')

        if serializer.is_valid():
            serializer.save(created_by=self.request.user)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KpiDeleteView(generics.DestroyAPIView):
    serializer_class = serializers.KpiSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Kpi.objects.filter(id=pk)

    def perform_destroy(self, instance):
        if not self.request.user.is_authenticated:
            raise PermissionDenied('You must be authenticated to delete a kpi.')

        instance.delete()


class KpiUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.KpiSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Kpi.objects.filter(id=pk)

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

