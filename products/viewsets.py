from rest_framework import viewsets, permissions, filters
from .models import Products
from .serializers import ProductsSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.select_related('vendor').all()
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'name', 'id']
    ordering = ['-id']

    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user)
