**DJANGO**

* fichero settings.py 
    DATABASES = por defecto sqlite

## Ficheros
* settings_py : configuración del proyecto
* urls.py : rutas del proyecto
* wsgi.py : despliegue del proyecto
* asgi.py : despliegue del proyecto
* manage.py : utilidades para gestionar el proyecto - create applications, work with databases, and start the devlopment web server

## Setup

```bash
cd ../..
python3 -m venv p1_env
source p1_env/bin/activate
cd UnidadH/psi/P1
pip3 install -r requirements.txt
cd locallibrary

```

## Base de datos

    En el archivo settings.py
    ```
    import dj_database_url
    db_from_env =
    dj_database_url.config(default=’postgres://alumnodb:alumnodb@localhost:5432/psi’,
    conn_max_age=500)
    DATABASES[’default’].update(db_from_env)

    ```

    Para crear la base de datos:
    ```bash
    createdb -U alumnodb -h localhost psi

    ```
    Para borrar la base de datos:
    ```bash
    dropdb -U alumnodb -h localhost psi

    ```


    * modelos 
        * clase en django que será una tabla en la base de datos
    python manage.py makemigrations > genera un script que crea las tablas 
    para ejecutarla: python migrations/migrate.py (creo)

    * para entrar a la base de datos: sqlite3 db.sqlite3
    * para ver esquema de la bd: .schema hello_greeting

    para escribir python:
    python manage.py shell 
        ```python

        from hello.models import Greeting 
        g = Greeting(name='pepe', message='hola')
        print(g)
        g.save()

        ```

## Admin Page
    La aplicación de Django admin utiliza tus modelos para crear una interfaz de administración web que permite a los usuarios agregar, editar y eliminar registros en la base de datos de manera sencilla.
    
    * para registrar el modelo en admin:
    ```python
        from django.contrib import admin
        from .models import Greeting

        admin.site.register(Greeting)
    ```
    * para crear un superusuario:
    ```python
        python manage.py createsuperuser
    ```
    * para acceder a la página de administración:
    ```bash
        http://localhost:8000/admin
    ```

    
