from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Graph
from . import serializers
from django.core.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.response import Response


# Create your views here.
class GraphListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.GraphSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Graph.objects.all()

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied('You must be authenticated to create a graph.')

        if serializer.is_valid():
            serializer.save(created_by=self.request.user)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GraphDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.GraphSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Graph.objects.filter(id=pk)

    def perform_destroy(self, instance):
        if not self.request.user.is_authenticated:
            raise PermissionDenied('You must be authenticated to delete a graph.')
        instance.delete()


class GraphUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.GraphSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Graph.objects.filter(id=pk)

    def perform_update(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied('You must be authenticated to update a graph.')
        if serializer.is_valid():
            serializer.save(created_by=self.request.user)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
