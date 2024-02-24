from rest_framework import serializers
from user_management.models import Address, Customer, ProfileUser, Vendor

class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        address = Address
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        customer = Customer
        fields = '__all__'


class ProfileUserSerializer(serializers.ModelSerializer):

    class Meta:
        profile_user = ProfileUser
        fields = '__all__'

        
class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        vendor = Vendor
        fields = '__all__'