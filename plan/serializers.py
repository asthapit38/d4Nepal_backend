from rest_framework import serializers
from .models import Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'name', 'price', 'description', 'business_per_account', 'has_unlimited_business', 'kpi', 'visual_graph']