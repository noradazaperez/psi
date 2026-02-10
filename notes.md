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

    Para poner a correr la base de datos:
    ```bash 
    sudo systemctl restart postgresql

    ```

    Para hacer una migración
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
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

    * para empezar el servidor de dev:
    ```bash
    python3 manage.py runserver 8001
    ```

    * para acceder a la página de administración:
    ```bash
        http://localhost:8000/admin
    ```

    * Advanced Configuration
    - List Views:
        - add additional fields/information displayed for each record
        - add filters to select which records are listed
        - add additional options to the actions menu in list views and choose where this menu is displayed on the from

        * We define a **ModelAdmin** class
        ```python
            # Define the admin class
            class AuthorAdmin(admin.ModelAdmin):
                pass

            # Register the admin class with the associated model
            admin.site.register(Author, AuthorAdmin)
        ```
        Another syntax
        ```python
            # Register the Admin classes for Book using the decorator
            @admin.register(Book)
            class BookAdmin(admin.ModelAdmin):
                pass

            # Register the Admin classes for BookInstance using the decorator
            @admin.register(BookInstance)
            class BookInstanceAdmin(admin.ModelAdmin):
                pass
        ```

        * Filtering
        ```python
            class BookInstanceAdmin(admin.ModelAdmin):
                list_filter = ('status', 'due_back')    

        ```

    - Detail Views:
        - choose which fields to display (or exclude), along with their order, grouping, whether they are editable, the widget used, orientation etc.
        - add related fields to a record to allow inline editing

        * Controlling which fields are displayed and laid out
        *Fields* attribute = those fields that are to be displayed on the form, in order.
        In a tuple = horizontally
        *Exclude* attribute = 
        ```python
            class AuthorAdmin(admin.ModelAdmin):
                list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

                fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

        ```

        *Section* : *fieldsets* attribute.
        ```python
            @admin.register(BookInstance)
            class BookInstanceAdmin(admin.ModelAdmin):
                list_filter = ('status', 'due_back')

                fieldsets = (
                    (None, {
                        'fields': ('book', 'imprint', 'id')
                    }),
                    ('Availability', {
                        'fields': ('status', 'due_back')
                    }),
                )

        ```

        * Inline editing of associated records
        Sometimes it can make sense to be able to add associated records at the same time.
        ```python
            class BooksInstanceInline(admin.TabularInline):
                model = BookInstance

            @admin.register(Book)
            class BookAdmin(admin.ModelAdmin):
                list_display = ('title', 'author', 'display_genre')

                inlines = [BooksInstanceInline]
        ```
    
    * Home Page:
    - URLs: Note: Whenever Django encounters the import function django.urls.include(), it splits the URL string at the designated end character and sends the remaining substring to the included URLConf module for further processing.

**Despliegue** 
1. Acceso Github
2. Whitenoise/Gunicorn
3. Build.sh -> pip install
4. Web application
5. Gunicorn Project.WSGI application
6. Environment 
    * Database_URL
    * SECRET_KEY DEBUG
