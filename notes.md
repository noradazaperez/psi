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
  ```html
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
    field__lookup=value pattern like:
    * status__exact
    * status__iexact - case insensitive
    * status__in=['a','b']
    * status__contains='a'
  
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

## Generic list and detail views

### Generic List
- Views can be implementd as a class. We accss the appropriate view function by calling thee class method as_view()
- The generic view will query the database to get all records for the specified model then render a template located at /django-locallibrary-tutorial/catalog/templates/catalog/book_list.html

- **Note**: The generic views look for templates in */application_name/the_model_name_list.html*

```python
class BookListView(generic.ListView):
    model = Book
```
```python
class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list' # your own name for the list as a template variable
    queryset = Book.objects.filter(title__icontains='war')[:5]
    template_name = 'books/my_arbitrary_template_name_list.html' # specify your own template name/location

```

### Overriding methods in class-based views
- `get_queryset()`- change the list of records returned
- `get_context_data()` - pass additional context variables to the template. Follow this pattern:
1. First get the existing context from superclass
2. Then add your new context information
3. Then return the new (updated) context

```python
class BookListView(generic.ListView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['some_data'] = 'this is just some data'
        return context

```

- The view passes the context (list of books) by default as `object_list` and `book_list` aliases
### Conditional Execution

```html
{% if book_list %}
{% else %}
    <p>There are no books<\p>
{% endif %}
```

### For Loops
Empty tag to definee what happens if the book list is empty

```html
{% for book in book_list %}
    <li> <\li>
{% empty %}
{% endfor %}
```

### Accessing variables
The code inside the loops creates a list item.
- Access the *fields* of the associated book record
- Call *functions* in the model from within our template. This works provided thee function does not havee arguments 


### Detail View
```python
class BookDetailView(generic.DetailView):
    model = Book
```

- All you need to do is create a template called `/catalog/book_detail.html`
- The view will pass it the database information for the spcific Book record
- `book.bookinstance_set.all()` : return the set of BookInstance records associated with a particular Book.
    * Declare a ForeignKey field only in the "many" side of the relationship
    * Django constructs a "reverse lookup" : 
        lower-cast the model name where the foreign key is declared + _set

        - all() : get all the records 
        - filter() : geet a subset of records in code 
- `copy.get_status_display` : since BookInstance.status is a choices field, Django automatically creates a method `get_foo_display` for every choices field foo in a model. 

### Pagination
- Pagination built into the generic class-based list views 

```python
class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

```

## Sessions Framework
- Session: attribute you can read and write as many times as you like in your view
- Updating some information within session data > explicitly mark the session as having been modified
```python
request.session['my_car']['wheels'] = 'alloy'
request.session.modified = True
```
```python
my_car = request.session['my_car']
my_car = request.session.get('my_car', 'mini')
request.session['my_car'] = 'mini'
del request.session['my_car']
```

## Authentication and Permissions
- Enable authentication: 
- Creating users and groups: 
    * Create users programmatically: 
    ```python
    from django.contrib.auth.models import User

    user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')
    user.first_name = 'Tyrone'
    user.last_name = 'Citizen'
    user.save()
    ```
- Authentication View: login, log out, and password management.
- Password reset templates.

- Qué podemos hacer para controlar selctivamente el contenido que el usuario ve basado en si ha iniciado sesión o no
```html
{% if user.is_authenticated %}
```

- Nótese también cómo hemos añadido ?next={{request.path}} al final de las URLs. 
    * añadir el párametro URL next que contiene la dirección (URL) de la página actual, al final de la URL enlazada
    * Después de que el usuario haya iniciado o cerrado sesión con éxito, las vistas usarán el valor de este "next" para redirigir al usuario de vuelta a la página donde pincharon primeramente el enlace de inicio/cierre de sesión.

- If you're using function-based views, the easiest way to restrict access to your functions is to apply the login_required decorator to your view function, as shown below. If the user is logged in then your view code will execute as normal. If the user is not logged in, this will redirect to the login URL defined in the project settings (settings.LOGIN_URL), passing the current absolute path as the next URL parameter. 