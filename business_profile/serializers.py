from rest_framework import serializers
from .models import BusinessProfile
from subscriptions.models import Subscription
from kpi.serializers import KpiSerializer
from business_type.serializers import BusinessTypeSerializer


class BusinessProfileSerializer(serializers.ModelSerializer):
    kpi = KpiSerializer(many=True, read_only=True)
    type = BusinessTypeSerializer(read_only=True)

    class Meta:
        model = BusinessProfile
        fields = ('id', 'name', 'business_owner', 'business_type', 'kpi', 'type')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['kpi'] = KpiSerializer(instance.kpi.all(), many=True).data
        return representation

    def validate(self, data):
        user = self.context['request'].user
        subscription = Subscription.objects.filter(customer=user).first()

        print(f"self: {self.context['request']}")
        print(f"data: {data}")

        if not subscription:
            raise serializers.ValidationError("You need to subscribe to a plan to create a business profile.")

        if 'kpi' in data and len(data['kpi']) > subscription.plan.kpi:
            raise serializers.ValidationError("You are not allowed to select more kpis than the plan you have "
                                              "subscribed to.")
        else:
            return data

    def create(self, validated_data):
        return super().create(validated_data)