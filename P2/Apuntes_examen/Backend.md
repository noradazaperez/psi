Setup en django para poder usarlo de backend:
1. Tener instalado estas aplicaciones en el venv
```
django-cors-headers==4.3.1
djangorestframework==3.14.0
```
2. Crear la aplicación de la api

**En settings.py**
3. Añadir a INSTALLED_APPS
```python
    'api.apps.ApiConfig', # la aplicación donde correremos la api (crearla)
    'rest_framework',
    'corsheaders'
```

4. Añadir a MIDDLEWARE (primera fila):
```python
    'corsheaders.middleware.CorsMiddleware',
```
5. Crear lista de dominios que pueden acceder al servidor:
```python
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = [
    'http://localhost:5173',
]
```
**Ya no en settings.py**
6. Configurar la base de datos

7. Migrar los cambios

8. Hacer un serializer

9. Cambiar el proyecto de vue para q conecte con el backend

# serializers
Poner en archivo serializers.py 

```python
# serializers.py
from .models import Persona
from rest_framework import serializers

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        # fields = ['id', 'nombre', 'apellido', 'email']
        fields = '__all__'
```

```python
# views.py
from django.shortcuts import render

from .models import Persona
from .serializers import PersonaSerializer
from rest_framework import viewsets

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
```

```python
# urls.py (de persona)
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
# En el router vamos agnadiendo los endpoints a los viewsets
router.register('personas', views.PersonaViewSet) # ahora en /api/v1/personas se accede a todas las personas (junto con el path de #1)

urlpatterns = [
    path('api/v1/', include(router.urls)), #1
    path('admin/', admin.site.urls),
]
```

# Limitar el acceso a la api:

```python
# persona/settings.py
# in your project you do NOT need to add these lines to settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
}
```

convierte el API a sólo lectura para visitantes no autenticados
    Sólo los usuarios identificados podrán acceder a las acciones de creación, modificación y borrado