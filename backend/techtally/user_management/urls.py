from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user_management.views import AddressViewSet, CustomerViewSet, ProfileUserViewSet, VendorViewSet

router = DefaultRouter()
router.register(r'address', AddressViewSet, basename='address')
router.register(r'customer', CustomerViewSet, basename='customer')
router.register(r'profile_user', ProfileUserViewSet, basename='profile_user')
router.register(r'vendor', VendorViewSet, basename='vendor')

urlpatterns = [
    path('', include(router.urls)),
]
