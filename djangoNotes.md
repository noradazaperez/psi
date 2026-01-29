### venv

python3 -m venv p1_env; source p1_env/bin/activate
pip3 install -r P1/requirements.txt

### Setup
Create proyect
```bash
django-admin startproject locallibrary
cd locallibrary
```

Create app 
```bash
python3 manage.py startapp catalog
```

Add app to proyect:

In settings.py of the proyect folder

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

Manage database
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

Run the developement server
```bash
python3 manage.py runserver
```


### urls.py
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

Note: The route in path() is a string defining a URL pattern to match. This string might include a named variable (in angle brackets), e.g., 'catalog/<id>/'. This pattern will match a URL like catalog/any_chars/ and pass any_chars to the view as a string with the parameter name id

### models

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

#### Usar los modelos

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


## Errores y soluciones
django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
    Eso es que no has explicado que settings file usar, correr:
    export DJANGO_SETTINGS_MODULE=¡link a los ajustes!
        El link es (*) locallibrary.settings
    
    Acceder al shell
        python3 manage.py shell