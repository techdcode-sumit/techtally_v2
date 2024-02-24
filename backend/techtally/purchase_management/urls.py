from django.urls import path, include
from rest_framework.routers import DefaultRouter
from purchase_management.views import PurchaseViewSet, PurchaseProductViewSet, InventoryViewSet

router = DefaultRouter()
router.register(r'purchase', PurchaseViewSet, basename='purchase')
router.register(r'purchase_product', PurchaseProductViewSet, basename='purchase_product')
router.register(r'inventory', InventoryViewSet, basename='inventory')

urlpatterns = [
    path('', include(router.urls)),
]
