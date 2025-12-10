from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Company, Equipment, Technician, MaintenancePlan, WorkOrder

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'address', 'rut', 'created_at']


class EquipmentSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())

    class Meta:
        model = Equipment
        fields = ['id', 'company', 'name', 'serial_number', 'critical', 'installed_at']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class TechnicianSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Technician
        fields = ['id', 'user', 'full_name', 'specialty', 'phone']


class MaintenancePlanSerializer(serializers.ModelSerializer):
    equipment = serializers.PrimaryKeyRelatedField(queryset=Equipment.objects.all())

    class Meta:
        model = MaintenancePlan
        fields = ['id', 'equipment', 'name', 'frequency_days', 'active']


class WorkOrderSerializer(serializers.ModelSerializer):
    plan = serializers.PrimaryKeyRelatedField(queryset=MaintenancePlan.objects.all(), allow_null=True, required=False)
    equipment = serializers.PrimaryKeyRelatedField(queryset=Equipment.objects.all())
    technician = serializers.PrimaryKeyRelatedField(queryset=Technician.objects.all(), allow_null=True, required=False)

    class Meta:
        model = WorkOrder
        fields = ['id', 'plan', 'equipment', 'technician', 'status', 'scheduled_date', 'completed_at', 'notes']
