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

# Desplegar django

No necesitamos configurar nada de whitenoise porq no tenemos ficheros estáticos

1. En settings.py cambiar las siguientes variables a coger valores de env
    DATABASE_URL 
    DEBUG
    SECRET_KEY
        QUITARLA DE GH!!!!
    1.1 Importar env 
    ```python
    import os
    # Support env variables from .env file if defined
    from dotenv import load_dotenv

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    env_path = load_dotenv(os.path.join(BASE_DIR, '.env'))
    load_dotenv(env_path)
    ```
    1.2 Importar dj_database_url
    ```python
    import dj_database_url
    ```
    1.3 Importar la variable específica del env 
    ```python
    SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY',
                            '&p5l=p3q8_a+-$4w1f^lt3lx1c@d*p4x$ymm_rn7pwb87')

    DEBUG = os.environ.get('DEBUG', 'True') == 'True'

    DATABASES = {
        'default': dj_database_url.config(
            conn_max_age=600,
            conn_health_checks=True,
        ),
    }

    # No olvidar import dj_database_url

    db_from_env = dj_database_url.config(
                                        default=os.environ.get('DATABASE_URL'),
                                        conn_max_age=500)

    DATABASES['default'].update(db_from_env)
    ```
    1.4 Crear el .env en local con los valores
    DATABASE_URL = 'postgres://alumnodb:alumnodb@localhost:5432/psi'
    DEBUG = 'True'
        
2. Cambiar lo de ALLOWED_HOSTS
    ```python
    ALLOWED_HOSTS = []

    RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
    if RENDER_EXTERNAL_HOSTNAME:
        ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
    ```

3. Ir a render y darle a crear proyecto 
    Build command q sea pip install -r requirements.txt
    Start command guinicorn ¡nombre proyecto!.wsgi.¡nombre aplicación!
4. Crear variables de environment
    SECRET_KEY     Decirle q te la genere
    DATABASE_URL -> Ahora la añadiremos
5. Ir a neon.tech, crear base de datos.
6. Darle a connect a esa base de datos, copiar url
7. Meter ese url en render
8. PUSH