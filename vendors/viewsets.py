from rest_framework import viewsets, permissions
from .models import VendorStore
from .serializers import VendorStoreSerializer


class VendorStoreViewSet(viewsets.ModelViewSet):
    queryset = VendorStore.objects.select_related('user').all()
    serializer_class = VendorStoreSerializer
    permission_classes = [permissions.IsAuthenticated]

