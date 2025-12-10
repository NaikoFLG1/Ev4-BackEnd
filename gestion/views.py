from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Company, Equipment, Technician, MaintenancePlan, WorkOrder
from serializers import (
    CompanySerializer, EquipmentSerializer, TechnicianSerializer,
    MaintenancePlanSerializer, WorkOrderSerializer
)

class CompanyViewSet(viewsets.ModelViewSet):
    """CRUD para empresas."""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EquipmentViewSet(viewsets.ModelViewSet):
    """CRUD para equipos."""
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TechnicianViewSet(viewsets.ModelViewSet):
    """CRUD para técnicos."""
    queryset = Technician.objects.all()
    serializer_class = TechnicianSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MaintenancePlanViewSet(viewsets.ModelViewSet):
    """CRUD para planes de mantención."""
    queryset = MaintenancePlan.objects.all()
    serializer_class = MaintenancePlanSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class WorkOrderViewSet(viewsets.ModelViewSet):
    """CRUD para órdenes de trabajo."""
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HealthView(APIView):
    """Endpoint de prueba para validar el servicio."""
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return Response({"status": "ok", "service": "maintenance_api"})
