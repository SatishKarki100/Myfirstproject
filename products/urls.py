from django.urls import path
from .views import add_product, product_details

app_name = 'products'

urlpatterns = [
    path('add-product/', add_product, name='add-product'),
    path('product-details/<int:product_id>/', product_details, name='product-details'),
]
