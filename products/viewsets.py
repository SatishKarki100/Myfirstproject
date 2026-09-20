from rest_framework import viewsets, permissions, filters
from .models import Products
from .serializers import ProductsSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    """
    CRUD for products.
    Supports search by name and filter by store id: ?store=1
    """
    queryset = Products.objects.select_related('store').all()
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'name', 'id']
    ordering = ['-id']

    def get_queryset(self):
        qs = Products.objects.select_related('store').all()
        store_id = self.request.query_params.get('store')
        if store_id:
            qs = qs.filter(store_id=store_id)
        return qs
