from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Brand(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField((""), upload_to='uploads/', height_field=None, width_field=None, max_length=None)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_brands')
    created_at = models.DateTimeField(default=timezone.now)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_brands')
    updated_at = models.DateTimeField(default=timezone.now)

    def soft_delete(self):
        self.deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    code = models.CharField(max_length=20)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_categories')
    created_at = models.DateTimeField(default=timezone.now)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_categoriess')
    updated_at = models.DateTimeField(default=timezone.now)

    def soft_delete(self):
        self.deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    code = models.CharField(max_length=20)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_sub_categories')
    created_at = models.DateTimeField(default=timezone.now)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_sub_categories')
    updated_at = models.DateTimeField(default=timezone.now)

    def soft_delete(self):
        self.deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to='uploads/')


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    sub_category =models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    variant = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    images = models.ManyToManyField(ProductImage, blank=True)
    code = models.CharField(max_length=20)
    hsn_sac = models.CharField(max_length=80)
    unit = models.CharField(max_length=50)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_products')
    created_at = models.DateTimeField(default=timezone.now)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_products')
    updated_at = models.DateTimeField(default=timezone.now)

    def soft_delete(self):
        self.deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name