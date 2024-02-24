from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from user_management.models import Vendor
from product_management.models import Product

class Purchase(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True)
    invoice_no = models.CharField(max_length=80)
    invoice_date = models.DateTimeField()
    purchase_order_no = models.CharField(max_length=80, null=True, blank=True)
    place_of_supply = models.CharField(max_length=80, null=True, blank=True)
    is_deleted = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_purchases')
    created_at = models.DateTimeField(default=timezone.now)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_purchases')
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class PurchaseProduct(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    product_description = models.TextField()
    quantity = models.CharField(max_length=80)
    rate = models.CharField(max_length=80)
    cgst = models.CharField(max_length=80)
    sgst = models.CharField(max_length=80)
    is_deleted = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_purchase_products')
    created_at = models.DateTimeField(default=timezone.now)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_purchase_products')
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    purchase_product = models.ForeignKey(PurchaseProduct, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    product_description = models.TextField()
    quantity = models.CharField(max_length=80)
    rate = models.CharField(max_length=80)
    cgst = models.CharField(max_length=80)
    sgst = models.CharField(max_length=80)
    is_deleted = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_inventories')
    created_at = models.DateTimeField(default=timezone.now)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_inventories')
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name