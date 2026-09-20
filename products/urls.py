from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import add_product, product_details
from .viewsets import ProductsViewSet

app_name = 'products'

router = DefaultRouter()
router.register(r'products', ProductsViewSet, basename='product')

urlpatterns = [
    path('add-product/<int:store_id>/', add_product, name='add-product'),
    path('product-details/<int:product_id>/', product_details, name='product-details'),

    # ModelViewSet → /products/api/products/
    path('api/', include(router.urls)),
]
