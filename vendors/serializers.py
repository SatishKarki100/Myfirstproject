from rest_framework import serializers
from .models import VendorStore


class VendorStoreSerializer(serializers.ModelSerializer):
    owner_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = VendorStore
        fields = [
            'id', 'user', 'owner_username',
            'store_name', 'description', 'business_email',
        ]
        read_only_fields = ['id', 'user']
