from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Address(models.Model):
    address_line_1 = models.TextField()
    address_line_2 = models.TextField()
    city = models.CharField(max_length=80)
    district = models.CharField(max_length=80)
    state = models.CharField(max_length=80)
    country = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=80)
    is_deleted = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_addresses')
    created_at = models.DateTimeField(default=timezone.now)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_addresses')
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=200)
    email_id = models.EmailField(null=True, blank=True)
    mob_no = models.CharField(max_length=50, null=True, blank=True)
    gst_no = models.CharField(max_length=20, null=True, blank=True)
    is_deleted = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_customers')
    created_at = models.DateTimeField(default=timezone.now)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_customers')
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    

class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    addresses = models.ManyToManyField(Address)
    mob_no = models.CharField(max_length=50, null=True, blank=True)
    is_deleted = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.user.username
    
    
class Vendor(models.Model):
    name = models.CharField(max_length=50)
    adreess =models.ManyToManyField(Address)
    email_id = models.EmailField(null=True, blank=True)
    mob_no = models.CharField(max_length=50, null=True, blank=True)
    gst_no = models.CharField(max_length=20, null=True, blank=True)
    is_deleted = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_vendors')
    created_at = models.DateTimeField(default=timezone.now)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_vendors')
    updated_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name