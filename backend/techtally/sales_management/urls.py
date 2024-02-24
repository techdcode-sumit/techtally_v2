from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sales_management.views import SalesViewSet, SalesInvoiceViewSet, SalesInvoiceProductViewSet

router = DefaultRouter()
router.register(r'sales', SalesViewSet, basename='sales')
router.register(r'sales_invoice', SalesInvoiceViewSet, basename='sales_invoice')
router.register(r'sales_invoice_product', SalesInvoiceProductViewSet, basename='sales_invoice_product')

urlpatterns = [
    path('', include(router.urls)),
]
