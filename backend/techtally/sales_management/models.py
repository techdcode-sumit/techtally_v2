from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from user_management.models import Customer, Address
from product_management.models import Product


class SalesInvoice(models.Model):
    invoice_no = models.CharField(max_length=80)
    invoice_date = models.DateTimeField()
    total_amount = models.CharField(max_length=80)
    cgst = models.CharField(max_length=80)
    sgst = models.CharField(max_length=80)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_sales_invoices')
    created_at = models.DateTimeField(default=timezone.now)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_sales_invoices')
    updated_at = models.DateTimeField(default=timezone.now)

    def soft_delete(self):
        self.deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Sales(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    customer_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True, related_name='customer_address_sales')
    shipping_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True, related_name='shipping_address_sales')
    sales_invoice =  models.ForeignKey(SalesInvoice, on_delete=models.SET_NULL, null=True, blank=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_sales')
    created_at = models.DateTimeField(default=timezone.now)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_sales')
    updated_at = models.DateTimeField(default=timezone.now)

    def soft_delete(self):
        self.deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class SalesInvoiceProduct(models.Model):
    sales_invoice =  models.ForeignKey(SalesInvoice, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.CharField(max_length=80)
    rate = models.CharField(max_length=80)
    cgst = models.CharField(max_length=80)
    sgst = models.CharField(max_length=80)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_sales_invoice_products')
    created_at = models.DateTimeField(default=timezone.now)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_sales_invoice_products')
    updated_at = models.DateTimeField(default=timezone.now)

    def soft_delete(self):
        self.deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name