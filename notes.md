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
Restart development server
```bash
python3 manage.py runserver
```

## Base de datos

    En el archivo settings.py

    ```python
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

## URLs

* The path() function defines the following:
  * A URL pattern, which is an empty string: ''. 
  * A view function that will be called if the URL pattern is detected: views.index, which is the function named index() in the views.py file
  * a 'name' parameter = unique identifier for this particular URL mapping
    * use the name to reverse the mapper. ie. dynamically create a URL that points to the resource that the mapper is designed to handle 
  
  ```python
  urlpatterns = [
    path('', views.index, name='index')
  ]
  ```

  To link to our home page from any other page:
  ```python
  <a href="{% url 'index' %}">Home<\a>
  ```

### *View*: function that
  * processes an HTTP request
  * fetches the required data from the database
  * renders the data in an HTML page using an HTML template
  * returns the generated HTML in an HTTP response to display the page to the user
    * *render()* function accepts the following parameters:
      * the original request object, which is an HttpRequest
      * an HTML template with placeholders for the data
      * a context variable, with the data to insert into the placeholders
  
  - To **fetch the number of records**: Book.objects.all()
  - To **filter**: BookInstance.objects.filter(status__exact='a')
  
### *Template*: text file that defines the structure or layout of a file
*  in the index view that we just added, the render() function will expect to find the file index.html in /django-locallibrary-tutorial/catalog/templates/ and will raise an error if the file is not present.

* **Extend Templates**: we first specify the base temaplte using the extends template tag. Then we declare what sections from the template we want to replace (if any), using block/endblock sections

```html
{% extends "base_generic.html" %}

{% block content %}
  <h1>Local Library Home</h1>
  <p>
    Welcome to LocalLibrary, a website developed by
    <em>Mozilla Developer Network</em>!
  </p>
{% endblock %}

```
* You can easily recognize template variables and template tags (functions) - variables are enclosed in double braces ({{ num_books }}), and tags are enclosed in single braces with percentage signs ({% extends "base_generic.html" %}).

### Referencing static files in templates
* Specify the locaiton in your templates relative to the STATIC_URL global setting
* Within the template you first call the load template tag specifying "static" to add the template library, as shown in the code sample below. You can then use the static template tag and specify the relative URL to the required file.

```html
<!-- Add additional CSS in static file -->
{% load static %}
<link rel="stylesheet" href="{% static 'css/styles.css' %}" />
```

Add an image into the page in a similar way:
```html
{% load static %}
<img
  src="{% static 'images/local_library_model_uml.png' %}"
  alt="UML diagram"
  style="width:555px;height:540px;" />
```

### Linking to URLs
The base template above introduced the url template tag. It accepts the name of a path() function called in your urls.py. 
```html
<li><a href="{% url 'index' %}">Home</a></li>
```
