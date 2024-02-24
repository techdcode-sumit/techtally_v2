from rest_framework import serializers
from product_management.models import Brand, Category, SubCategory, Product

class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        brand = Brand
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        category = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        sub_category = SubCategory
        fields = '__all__'

        
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        product = Product
        fields = '__all__'