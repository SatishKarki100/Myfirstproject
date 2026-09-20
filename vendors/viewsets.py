from rest_framework import viewsets, permissions
from .models import VendorStore
from .serializers import VendorStoreSerializer


class VendorStoreViewSet(viewsets.ModelViewSet):
    """
    CRUD for vendor stores.
    On create, store is linked to the logged-in user.
    """
    queryset = VendorStore.objects.select_related('user').all()
    serializer_class = VendorStoreSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return VendorStore.objects.select_related('user').all()
        return VendorStore.objects.select_related('user').filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
