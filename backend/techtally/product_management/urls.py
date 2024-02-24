from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product_management.views import BrandViewSet, CategoryViewSet, SubCategoryViewSet, ProductViewSet


router = DefaultRouter()
router.register(r'brand', BrandViewSet, basename='brand')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'sub_category', SubCategoryViewSet, basename='sub_category')
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
