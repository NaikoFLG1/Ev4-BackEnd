# Mantención Biobío - API REST

API RESTful para la gestión de empresas clientes, equipos, técnicos, planes de mantención y órdenes de trabajo
de la Región del Biobío. Está pensada para ser consumida por aplicaciones web y móviles mediante JSON y autenticación JWT.

## Tecnologías principales
- Django
- Django REST Framework (DRF)
- djangorestframework-simplejwt (JWT)
- drf-spectacular (OpenAPI / Swagger)

## Requisitos
- Python 3.10+ (se probó con 3.13 en entorno local)
- Virtualenv / venv recomendado
- Dependencias principales en `requirements.txt` (instalar con `pip install -r requirements.txt`).

Paquetes clave:
- Django
- djangorestframework
- djangorestframework-simplejwt
- drf-spectacular

## Pasos para ejecutar la API (local)

1. Crear y activar entorno virtual:

```bash
python -m venv venv
# Windows PowerShell
venv\Scripts\Activate.ps1
# Windows CMD
venv\Scripts\activate.bat
# Unix
source venv/bin/activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Crear migraciones y aplicar:

```bash
python "manage.py" makemigrations
python "manage.py" migrate
```

4. Crear superusuario (opcional):

```bash
python "manage.py" createsuperuser
```

5. Ejecutar servidor de desarrollo:

```bash
python "manage.py" runserver
```

6. Ejecutar pruebas unitarias / de integración (opcional):

```bash
python "manage.py" test
```

## Endpoints de ejemplo

- `GET /api/health/` — endpoint de estado. Respuesta JSON: `{ "status": "ok", "service": "maintenance_api" }`.
- `GET /api/companies/` — listar empresas (paginado si corresponde). Permite lectura anónima.
- `POST /api/companies/` — crear empresa (requiere autenticación). Campos JSON: `name`, `address`, `rut`.
- `POST /api/auth/token/` — obtener tokens JWT. Payload JSON: `{ "username": "<user>", "password": "<pass>" }`.
- `GET /api/docs/` — interfaz Swagger UI con documentación OpenAPI.

Ejemplo: obtener token y crear empresa (curl):

```bash
# Obtener token
curl -X POST http://127.0.0.1:8000/api/auth/token/ -H "Content-Type: application/json" -d '{"username":"testuser","password":"pass123"}'

# Respuesta: {"access":"<JWT>", "refresh":"<REFRESH>"}

# Crear empresa usando el access token
curl -X POST http://127.0.0.1:8000/api/companies/ \
  -H "Authorization: Bearer <JWT>" \
  -H "Content-Type: application/json" \
  -d '{"name":"MiEmpresa","address":"Calle 1","rut":"12345678-9"}'
```

## Notas importantes

- Cambiar `SECRET_KEY` en `mantencion_biobio/settings.py` antes de desplegar a producción.
- Ajustar `ALLOWED_HOSTS` y poner `DEBUG = False` en producción.
- Se añadió soporte para autenticación JWT y documentación OpenAPI (drf-spectacular).

## Estructura relevante

- `mantencion_biobio/settings.py` — configuración del proyecto y DRF.
- `mantencion_biobio/urls.py` — incluye rutas de la API y documentación (`/api/`).
- `gestion/models.py` — modelos: `Company`, `Equipment`, `Technician`, `MaintenancePlan`, `WorkOrder`.
- `gestion/serializers.py` — serializers para cada modelo (validaciones básicas incluidas).
- `gestion/views.py` — viewsets y endpoint de health.
- `gestion/urls.py` — router y rutas de autenticación.

## Contacto / Notas de la entrega

Proyecto desarrollado como trabajo para la asignatura TI3041 (Programación Backend). Incluye pruebas rápidas (`gestion/tests.py`) y documentación básica.
