from rest_framework import serializers
from sales_management.models import SalesInvoice, Sales, SalesInvoiceProduct

class SalesInvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalesInvoice
        fields = '__all__'


class SalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sales
        fields = '__all__'


class SalesInvoiceProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalesInvoiceProduct
        fields = '__all__'