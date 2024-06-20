from django.contrib.auth.models import User
from rest_framework import serializers


class KPISerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    value = serializers.FloatField()


class KPIListSerializer(serializers.Serializer):
    kpi = KPISerializer(many=True)

