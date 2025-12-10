from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    """Empresa cliente.

    Campos:
    - name: nombre de la empresa
    - address: dirección
    - rut: identificador fiscal (único)
    - created_at: fecha de creación (auto)
    """
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    rut = models.CharField(max_length=12, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.rut})'


class Equipment(models.Model):
    """Equipo asociado a una empresa.

    Relación: pertenece a `Company`.
    """
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='equipments')
    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=100, unique=True)
    critical = models.BooleanField(default=False)
    installed_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.serial_number}'


class Technician(models.Model):
    """Técnico vinculado a un usuario del sistema.

    Cada técnico referencia a un `User` del sistema.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='technician_profile')
    full_name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name


class MaintenancePlan(models.Model):
    """Plan de mantención para un equipo.

    - equipment: equipo objetivo
    - frequency_days: intervalo en días
    - active: bandera de estado
    """
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='maintenance_plans')
    name = models.CharField(max_length=255)
    frequency_days = models.PositiveIntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} ({self.equipment.serial_number})'


class WorkOrder(models.Model):
    """Orden de trabajo de mantención.

    Campos principales: plan, equipment, technician, status, fechas y notas.
    """
    STATUS_CHOICES = [
        ('scheduled', 'Programada'),
        ('in_progress', 'En progreso'),
        ('completed', 'Completada'),
        ('cancelled', 'Cancelada'),
    ]

    plan = models.ForeignKey(MaintenancePlan, on_delete=models.SET_NULL, null=True, blank=True, related_name='work_orders')
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='work_orders')
    technician = models.ForeignKey(Technician, on_delete=models.SET_NULL, null=True, blank=True, related_name='work_orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    scheduled_date = models.DateField()
    completed_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'OT {self.id} - {self.equipment.serial_number} - {self.status}'
