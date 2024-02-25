from rest_framework import serializers
from product_management.models import Brand, Category, SubCategory, Product, ProductImage

class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

        
class ProductSerializer(serializers.ModelSerializer):

    images = ProductImageSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = '__all__'