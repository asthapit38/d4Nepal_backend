from rest_framework import serializers
from .models import BusinessType
from kpi.serializers import KpiSerializer


class BusinessTypeSerializer(serializers.ModelSerializer):
    kpi = KpiSerializer(many=True, read_only=True)
    class Meta:
        model = BusinessType
        fields = ('id', 'name', 'description', 'kpi')

    def validate(self, data):
        if self.context['request'].user.is_superuser:
            return data
        else:
            raise serializers.ValidationError('You are not allowed to create a business type')

    def create(self, validated_data):
        return super().create(validated_data)