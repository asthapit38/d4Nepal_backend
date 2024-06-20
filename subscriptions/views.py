from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Subscription
from .serializers import SubscriptionSerializer
from rest_framework import status
from rest_framework.response import Response
from plan.models import Plan
from django.shortcuts import get_object_or_404


# Create your views here.
class SubscriptionListCreate(generics.ListCreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    # [TODO - Prevent multiple active subscriptions for a customer]

    def get_queryset(self):
        return Subscription.objects.filter(customer=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        plan_id = self.request.data.get('plan_id')
        plan = get_object_or_404(Plan, id=plan_id)
        serializer.save(customer=self.request.user, plan=plan)


class SubscriptionDeleteView(generics.DestroyAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Subscription.objects.filter(customer=self.request.user)


class SubscriptionUpdateView(generics.UpdateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Subscription.objects.filter(customer=self.request.user)

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save(customer=self.request.user)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
