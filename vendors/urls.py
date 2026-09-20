from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import register_vendorstore, store_view
from .viewsets import VendorStoreViewSet

router = DefaultRouter()
router.register(r'stores', VendorStoreViewSet, basename='store')

urlpatterns = [
    path('register-store/', register_vendorstore, name='register-store'),
    path('store/<int:store_id>/', store_view, name='store'),

    # ModelViewSet → /vendors/api/stores/
    path('api/', include(router.urls)),
]
