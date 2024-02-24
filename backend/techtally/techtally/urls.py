from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/product_management/', include('product_management.urls')),
    path('api/user_management/', include('user_management.urls')),
    path('api/purchase_management/', include('purchase_management.urls')),
    path('api/sales_management/', include('sales_management.urls')),
]
