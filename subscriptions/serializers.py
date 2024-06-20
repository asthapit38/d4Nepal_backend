from rest_framework import serializers
from .models import Subscription
from plan.serializers import PlanSerializer
from plan.models import Plan

class SubscriptionSerializer(serializers.ModelSerializer):
    plan_details = PlanSerializer(source='plan', read_only=True)
    plan_id = serializers.PrimaryKeyRelatedField(queryset=Plan.objects.all(), write_only=True)

    class Meta:
        model = Subscription
        fields = ('id', 'customer', 'plan_details', 'plan_id', 'start_date', 'end_date', 'status', 'created_at')
        extra_kwargs = {
            'customer': {'read_only': True},
        }

    def validate(self, data):
        user = self.context['request'].user
        active_subscription = Subscription.objects.filter(customer=user, status='active').first()
        if active_subscription:
            raise serializers.ValidationError({"non_field_errors": ["You already have an active subscription."]})
        return data

    def create(self, validated_data):
        plan_id = validated_data.pop('plan_id')
        validated_data['plan'] = plan_id
        return super().create(validated_data)