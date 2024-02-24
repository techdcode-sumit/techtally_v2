from rest_framework import serializers
from purchase_management.models import Purchase, PurchaseProduct, Inventory

class PurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchase
        fields = '__all__'


class PurchaseProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseProduct
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = '__all__'