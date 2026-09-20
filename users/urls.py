from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import register_view, login_view, profile_view
from .api_views import (
    RegisterAPIView,
    MyTokenObtainPairView,
    LogoutAPIView,
    MeAPIView,
)
from .viewsets import UserViewSet
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    # Template views
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),

    # JWT auth endpoints
    path('api/register/', RegisterAPIView.as_view(), name='api-register'),
    path('api/login/', MyTokenObtainPairView.as_view(), name='api-login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('api/logout/', LogoutAPIView.as_view(), name='api-logout'),
    path('api/me/', MeAPIView.as_view(), name='api-me'),

    # ModelViewSet routes → /users/api/users/
    path('api/', include(router.urls)),
]
