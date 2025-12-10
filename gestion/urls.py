from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CompanyViewSet, EquipmentViewSet, TechnicianViewSet,
    MaintenancePlanViewSet, WorkOrderViewSet, HealthView
)

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')
router.register(r'equipments', EquipmentViewSet, basename='equipment')
router.register(r'technicians', TechnicianViewSet, basename='technician')
router.register(r'maintenance-plans', MaintenancePlanViewSet, basename='maintenanceplan')
router.register(r'work-orders', WorkOrderViewSet, basename='workorder')

urlpatterns = [
    path('', include(router.urls)),
    path('health/', HealthView.as_view(), name='health'),
]
