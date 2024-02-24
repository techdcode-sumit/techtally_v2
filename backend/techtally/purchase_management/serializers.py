from rest_framework import serializers
from purchase_management.models import Purchase, PurchaseProduct, Inventory

class PurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        purchase = Purchase
        fields = '__all__'


class PurchaseProductSerializer(serializers.ModelSerializer):

    class Meta:
        purchase_roduct = PurchaseProduct
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        inventory = Inventory
        fields = '__all__'