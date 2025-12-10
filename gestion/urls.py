from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CompanyViewSet, EquipmentViewSet, TechnicianViewSet,
    MaintenancePlanViewSet, WorkOrderViewSet, HealthView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')
router.register(r'equipments', EquipmentViewSet, basename='equipment')
router.register(r'technicians', TechnicianViewSet, basename='technician')
router.register(r'maintenance-plans', MaintenancePlanViewSet, basename='maintenanceplan')
router.register(r'work-orders', WorkOrderViewSet, basename='workorder')

urlpatterns = [
    path('', include(router.urls)),
    path('health/', HealthView.as_view(), name='health'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
