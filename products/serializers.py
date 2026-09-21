from rest_framework import serializers
from .models import Products


class ProductsSerializer(serializers.ModelSerializer):
    vendor_name = serializers.CharField(source='vendor.username', read_only=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = [
            'id', 'name', 'price', 'description',
            'vendor', 'vendor_name', 'image', 'image_url',
        ]
        read_only_fields = ['id', 'vendor']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None
