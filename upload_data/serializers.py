from rest_framework import serializers
from .models import UploadData


class UploadDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadData
        fields = ('file', 'user', 'created_at', 'updated_at')
        extra_kwargs = {
            'user': {'read_only': True},
        }
