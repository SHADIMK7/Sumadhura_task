# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Vendor, Product, Vehicle, QualityCheck


class RegistrationSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = User
        fields = ['username','email','password']

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    quality_check = serializers.SerializerMethodField('get_quality_check')

    def get_quality_check(self, obj):
        try:
            quality_check = QualityCheck.objects.get(vehicle=obj)
            return quality_check.passed
        except QualityCheck.DoesNotExist:
            return False
    
    class Meta:
        model = Vehicle
        fields = ['vehicle_number', 'vehicle_type', 'dc_number', 'po_number', 'vendor', 'product', 'checked_out', 'quality_check']
        read_only_fields = ['checked_out']

        

class QualityCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityCheck
        fields = '__all__'
