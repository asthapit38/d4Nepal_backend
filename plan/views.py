from rest_framework import generics
from rest_framework import status
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.permissions import IsAuthenticated

from .models import Plan
from .serializers import PlanSerializer


# Create your views here.
class PlanListCreate(generics.ListCreateAPIView):
    serializer_class = PlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise ValidationError(
                {'error': 'You must be authenticated to create a plan.'},
                code=status.HTTP_401_UNAUTHORIZED
            )

        return Plan.objects.all()

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied('You must be authenticated to create a plan.')

        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)


class PlanDeleteView(generics.DestroyAPIView):
    serializer_class = PlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Plan.objects.all()


class PlanUpdateView(generics.UpdateAPIView):
    serializer_class = PlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Plan.objects.all()

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
