## venv

python3 -m venv p1_env; source p1_env/bin/activate
pip3 install -r P1/requirements.txt

## Setup
1. Create proyect
```bash
django-admin startproject locallibrary
cd locallibrary
```
2. Create app 
```bash
python3 manage.py startapp catalog
```

3. Add app to proyect:
    
    3.1. In settings.py of the proyect folder
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Add our new application
    'catalog.apps.CatalogConfig', # This object was created for us in /catalog/apps.py
]
```

4. Manage database
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

5. Run the developement server
```bash
python3 manage.py runserver
```

6. Ver sección de bases de datos para ver cómo cambiarla a usar postgre y usuarios y etc

7. Configurar el servido de archivos estáticos
    
    7.1. Make sure that django.contrib.staticfiles is included in your INSTALLED_APPS.

    7.2. In your settings file , define STATIC_URL. Es la dirección relativa desde la carpeta donde está la app

    7.3. Para usarlo en los templates:
```HTML
<!-- Add additional CSS in static file -->
{% load static %}
<link rel="stylesheet" href="{% static '¡dirección desde la carpeta configurada con STATIC_URL al archivo!' %}" />
```

        - La primera fila carga el tag static
        - La segunda es cómo usarla dentro del archivo


## urls.py
Resumen: 

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLConf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
        Dentro de blog/urls.py los links empezarán con blog/ (i.e. si en blog/urls.py tengo path('hello/', ...), se referirá a los links localhost/blog/hello)
Redirecting
    urlpatterns += [
        path('', RedirectView.as_view(url='catalog/', permanent=True)),
    ]

NOTA: existe una función re_path que te permite matchear la url con regex
    (*)re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    Todas las variables se pasarán como strings
    Regex in python intro:
| Symbol 	    | Meaning |
|---------------|---------|
| ^ 	        | Match the beginning of the text
| $ 	        | Match the end of the text
| \d 	        | Match a digit (0, 1, 2, … 9)
| \w 	        | Match a word character, e.g., any upper- or lower-case character in the alphabet, digit or the underscore character (_)
| + 	        | Match one or more of the preceding character. For example, to match one or more digits you would use \d+. To match one or more "a" characters, you could use a+
| * 	        | Match zero or more of the preceding character. For example, to match nothing or a word you could use \w*
| ( ) 	        | Capture the part of the pattern inside the parentheses. Any captured values will be passed to the view as unnamed parameters (if multiple patterns are captured, the associated parameters will be supplied in the order that the captures were declared).
| (?P<name>...) | Capture the pattern (indicated by ...) as a named variable (in this case "name"). The captured values are passed to the view with the name specified. Your view must therefore declare a parameter with the same name!
| [ ] 	        | Match against one character in the set. For example, [abc] will match on 'a' or 'b' or 'c'. [-\w] will match on the '-' character or any word character. 

### path
El primer parámetro es la dirección en el link
    it is a string defining a URL pattern to match.
    This string might include a named variable (in angle brackets), e.g., 'catalog/<id>/'. This pattern will match a URL like catalog/any_chars/ and pass any_chars to the view as a string with the parameter name id
        También puedes especificar el tipo de dato like so:
        'catalog/<int:id>'
        El nombre dado a la variable es el que el class_based view se esperará. i.e. si lo quieres usar, tienes q llamarlo id
            Si escribes tu propia función no hace falta
El segundo parámetro es la función que habría que llamar
    Normalmente, empezará con views. al estár la función contenida en el archivo views (views.¡tu función!)
El tercer parámetro es un diccionario que pasará al view
    Se pasará como argumento con nombre, a no ser que una variable del link tenga el mismo nombre que una del diccionario. En ese caso se pasará el diccionario
El name parameter es el nombre de este mapping particular
    You can use the name to "reverse" the mapper
        i.e., to dynamically create a URL that points to the resource that the mapper is designed to handle
    (*) <a href="{% url 'index' %}">Home</a>.
        El link que quedará guardado al lado de href es el que apunta a la función a la que apunte el mapping llamado index
        

## views.py
Useful function:
    get_object_or_404()
        Está en django.shortcuts
        (*) book = get_object_or_404(Book, pk=primary_key)

The render() function accepts the following parameters:
- the original request object, which is an HttpRequest.
- an HTML template with placeholders for the data.
- a context variable, which is a Python dictionary, containing the data to insert into the placeholders.

### Useful generic classes for views
**ListView**
```python
from django.views import generic

class BookListView(generic.ListView):
    model = Book
```

The generic view will query the database to get all records for the specified model (Book) then render a template located at /¡application_name!/¡the_model_name!_list.html inside the application's /¡application_name!/templates/ directory (in this case /catalog/templates/catalog/book_list.html).

Within the template you can access the list of books with the template variable named object_list OR  ¡the model name!_list.

Atributos q se pueden añadir:
    context_object_name  
        Nombre de la variable con los objetos q se pasará al template
    queryset
        Lista de elementos que se pasará al template
        (*) queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    template_name 
        Especificar el nombre del template y su localización

Métodos que se pueden sobreescribir:
    get_queryset(self)
        Debe retornar la lista que quieres que se pase al template
    get_context_data(self, **kwargs)
        Para pasarle más información al template
        Hace falta seguir el siguiente proceso:
            First get the existing context from our superclass. 
            Then add your new context information.
            Then return the new (updated) context.
        (*)
        ```python
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context
        ```
**DetailView**
```python
from django.views import generic

class BookDetailView(generic.DetailView):
    model = Book
``` 
    automáticamente asume que el parámetro pasado es el pk de un record del modelo
    El template debería llamarse: /¡application_name!/¡the_model_name!_detail.html
    El objeto específico consultado se llamará ¡the_model_name!

### Templates

Si la app se ha generado con startapp el programa se esperará que los templates estén en la carpeta ¡nombre aplicación!/templates

variables are enclosed in double braces
    (*) {{ num_books }}
    También puedes acceder a los subelementos de la variable con punto (*) {{ book.author }}
    Esto también te permite llamar a métodos pero <(*)>, no puedes pasarle argumentos a los métodos
tags are enclosed in single braces with percentage signs (*) {% extends "base_generic.html" %}

Cargar contenido estático
    Within the template you first call the load template tag specifying "static" to add the template library. 
    You can then use the static template tag and specify the relative URL to the required file.
    <!-- Add additional CSS in static file -->
    {% load static %} 
    <link rel="stylesheet" href="{% static 'css/styles.css' %}" />
Añadir comentarios
    {# ¡comentario! #}
Añadir links a otras páginas de tu proyecto
    <a href="{% url '¡nombre del mapping!' %}"> ¡Display word del link!</a>
    Ver la sección path, el tercer argumento, para el nombre del mapping
    No olvidar las comitas después del url!!!
    Para pasarle argumentos es:
        <a href="{% url '¡nombre del mapping!' '¡argumento 1!' %}"> ¡Display word del link!</a>

**Programación en templates**
if
```html
    {% if ¡condición! %}
    <!-- ¡lo q quieras! -->
    {% elif ¡condición! %}
    <!-- ¡lo q quieras! -->
    {% else %}
    <!-- ¡lo q quieras! -->
    {% endif %}
```
    Condición puede ser una variable que quieres comprobar si está vacía o definida

for
```html
    {% for ¡nombre! in ¡lista! %}
    <!-- ¡lo q quieras! -->
    {% endfor %}
```
    También puedes añadir una cláusula empty
```html
    {% for ¡nombre! in ¡lista! %}
        <!-- code here -->
    {% empty %}
        <!-- código que se ejecutará sólo si la lista es vacía -->
    {% endfor %}
```
    Otros elementos útiles:
        forloop.last
            El último elemento q ha procesado el bucle, es una variable
    Ejemplo de for con listas:
```html 
<ul>
  {% for book in book_list %}
    <li>
        <a href="{{ book.get_absolute_url }}">{{ book.title }}</a>
        ({{book.author}})
    </li>
  {% empty %}
    <p>There are no books in the library.</p>
  {% endfor %}
</ul>
```

**Configurar**
Se hace cambiando la variable TEMPLATES de settings.py
    DIRS 
        Modificando esta variable se pueden especificar otras carpetas donde encontrar templates
    APP_DIRS
        Cuando es True le dice a django que busque templates dentro de una carpeta templates dentro de cada aplicación y no sólo en la carpeta grande del proyecto


**Herencia de clases**
Un template padre puede tener bloques que los templates hijos modifiquen. 

Los bloques tienen esta estructura:
    ```html
    {% block ¡nombre del bloque! %}
    ¡Código default que tendrá el bloque si los hijos no lo modifican!
    {% endblock %}
    ```
    Estos bloques pueden estar dentro de títulos y etc

Para heredar de otro archivo
    ```html
    {% extends "¡nombre del archivo terminando en .html!" %}
    ```

Para sobreescribir un bloque, es igual que declararlo, añadiendo los tags de block y endblock con el nombre

## models

models to represent selection-list options (e.g., like a drop down list of choices), rather than hard coding the choices into the website itself

Django allows you to define relationships that are one to one (OneToOneField), one to many (ForeignKey) and many to many (ManyToManyField)
    (*) genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    (*) author = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)
        You must use the name of the model as a string if the associated class has not yet been defined in this file before it is referenced!
    By default on_delete=models.CASCADE, which means that if the author was deleted, this book would be deleted too! We use RESTRICT here, but we could also use PROTECT to prevent the author being deleted while any book uses it or SET_NULL to set the book's author to Null if the record is deleted.

Las variables de la clase son los atributos en la base de datos, declarar uno:
    (*) my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    The order that fields are declared will affect their default order if a model is rendered in a form
    Possible parameters:
        max_length
        help_text
        verbose_name
            Para poner el label, i.e. el nombre que tendrán en forms
            Si no se pone nada, será el nombre del atributo con espacios en lugar de _ y la primera letra en mayúscula
        default
            default value
        blank
            if true, the field is allowed to be blank in the forms
            This is often used with null=True   
        choices
            A group of choices for this field. If this is provided, the default corresponding form widget will be a select box with these choices instead of the standard text field.
        unique
            If True, ensures that the field value is unique across the database
            It prevents prevents records being created with exactly the same name, but does not check for lowercase or other possible variations
        primary_key
            Es boolean
        choices
            Lista de key/value pairs
            The value in a key/value pair is a display value that a user can select, while the keys are the values that are actually saved if the option is selected
    Field types: [lista completa](https://docs.djangoproject.com/en/5.0/ref/models/fields/#field-types)
        CharField
        TextField
            Para textos largos
        IntergerField
        DateField DateTimeField
        EmailField
        FileField
        ImageField
        AutoField
            Es un IntergerField que aumenta automáticamente cuando se añade un elemento
        ForeignKey
        ManyToManyField
        UUIDField
            Used for the id field to set it as the primary_key for this model. This type of field allocates a globally unique value for each instance (one for every book you can find in the library)

Metadatos:

class Meta: [todas las opciones](https://docs.djangoproject.com/en/5.0/ref/models/options/)
    ordering = ['title', '-publish_date']
            the books would be sorted alphabetically by title, from A-Z, and then by publication date inside each title, from newest to oldest
        control the default ordering of records returned when you query the model type. You do this by specifying the match order in a list of field names to the ordering attribute
        you can prefix the field name with a minus symbol (-) to reverse the sorting order
    constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insensitive_unique',
                violation_error_message = "Genre already exists (case insensitive match)"
            ),
    ]

Métodos
    Minimally, in every model you should define the standard Python class method __str__() to return a human-readable string for each object. This string is used to represent individual records in the administration site (and anywhere else you need to refer to a model instance). Often this will return a title or name field from the model.
```python
def get_absolute_url(self):
    """Returns the URL to access a particular instance of the model."""
    return reverse('model-detail-view', args=[str(self.id)])
```
        Note: Assuming you will use URLs like /my-application/my-model-name/2 to display individual records for your model (where "2" is the id for a particular record), you will need to create a URL mapper to pass the response and id to a "model detail view" (which will do the work required to display the record). The reverse() function above is able to "reverse" your URL mapper (in the above case named 'model-detail-view') in order to create a URL of the right format.

        Of course to make this work you still have to write the URL mapping, view, and template!

```python
# Create a new record using the model's constructor.
record = MyModelName(my_field_name="Instance #1")

# Save the object into the database.
record.save()

# Change record by modifying the fields, then calling save().
record.my_field_name = "New Instance Name"
record.save()

# Get all records of a model
Book.objects.all()

# We use the format field_name__match_type
wild_books = Book.objects.filter(title__contains='wild')
number_wild_books = wild_books.count()
```

### Usar los modelos

Filtros: 
    Filter on a field that defines a one-to-many relationship to another model (e.g., a ForeignKey)
        You can "index" to fields within the related model with additional double underscores.
        (*)
        ```python
            # Will match on: Fiction, Science fiction, non-fiction etc.
            books_containing_genre = Book.objects.filter(genre__name__icontains='fiction')
        ```
    Posibles tipos: [lista completa](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#field-lookups)
        icontains (case insensitive)
        iexact (case-insensitive exact match)
        exact (case-sensitive exact match)
        in
        gt (greater than)
        startswith


# Bases de datos

Una vez instaladas las dependencias, se debe modificar la variable DATABASES del fichero settings.py de la siguiente manera:

```python
import dj_database_url

db_from_env = dj_database_url.config(default='postgres://alumnodb:alumnodb@localhost:5432/psi', conn_max_age=500)

DATABASES['default'].update(db_from_env)
```

Para borrar la base de datos se puede usar el comando 
```bash
dropdb -U alumnodb -h localhost psi
```

Para crear la base de datos
```bash
createdb -U alumnodb -h localhost psi
```
Crear la base de datos, es necesario volver a poblarla ejecutando el script populate_catalog.py.

NOTA: las bases de datos creadas usando PostgreSQL no se borran al apagar el ordenador del laboratorio. Es recomendable borrarlas de una vez a otra

# Admin page 

Registrar modelos en la página de admin. Por ejemplo, para dejarte añadir y modificar instancias de los modelos
```python
from .models import ¡modelo!

admin.site.register(¡modelo, como clase, con la primera letra en mayúscula!)
```

Crear superusuario
```bash
python3 manage.py createsuperuser
```

## Customize 
To change how a model is displayed in the admin interface you define a ¡Model name. El nombre del modelo va en mayúsucla!Admin class (which describes the layout) and register it with the model
(*) AuthorAdmin
```python
# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
```
Ambas maneras sirven para registrar el adminclass. Para usar esto, hay que comentar la línea donde se importa de manera normal

Things you can add or change with these classes:
list_display
    (*) list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    Te permite estaer qué campos se enseñan cuando se muestran las instancias en formato lista
    Es un parámetro de clase y se especifican los campos igualándolo a una tupla.
    Los parámetros deben aparecer en la tupla en el orden en el que quieres que aparezcan en la lista
        Si alguno de los atributos especificados es un foreign key, te pondrá su __str__
        No se permite asociar un atributo a un ManyToManyField, pero sí que puedes asociarlo a una función que devuelva un string
            A esta función se le puede añadir un atributo "short_description" que será el nombre de la columna a la que lo asociará
            (*)
            ```python
                def display_genre(self):
                    """Create a string for the Genre. This is required to display genre in Admin."""
                    return ', '.join(genre.name for genre in self.genre.all()[:3])

                display_genre.short_description = 'Genre'
            ```
list_filter
    (*) list_filter = ('status', 'due_back')
    Para hacer filtros
fields
    (*) fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    fields attribute lists just those fields that are to be displayed on the form, in order.
    Fields are displayed vertically by default, but will display horizontally if you further group them in a tuple (as shown in the "date" fields above).
fieldsets
    (*) fieldsets = (
            (None, {
                'fields': ('book', 'imprint', 'id')
            }),
            ('Availability', {
                'fields': ('status', 'due_back')
            }),
        )
    You can add "sections" to group related model information within the detail form, using the fieldsets attribute.
    Each section has its own title (or None, if you don't want a title) and an associated tuple of fields in a dictionary
inlines [Más información](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.inlines)
    (*) inlines = [BookInstanceInline]
    Te permite editar instancias asociadas a la vez (por ejemplo, que pueda añadir una instancia de libro cada vez que añado un libro)
    Instancias la variable con una lista de clases Inline, que tienes que declarar antes
    Clases inline
        Declarar: 
            (*)
            class BooksInstanceInline(admin.TabularInline):
                model = BookInstance
        Variables que se pueden añadir:
            extra
                Cuando se pone a 0 te enseña sólo instancias con datos, no te da la opción de generar una a no ser que le des al botón


# Errores y soluciones
django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
    Eso es que no has explicado que settings file usar, correr:
    export DJANGO_SETTINGS_MODULE=¡link a los ajustes!
        El link es (*) locallibrary.settings
    
    Acceder al shell
        python3 manage.py shell