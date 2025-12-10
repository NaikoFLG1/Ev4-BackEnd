from django.contrib import admin
from .models import Company, Equipment, Technician, MaintenancePlan, WorkOrder

admin.site.register([Company, Equipment, Technician, MaintenancePlan, WorkOrder])
