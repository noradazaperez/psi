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

Las variables de la clase son los atributos en la base de datos, declarar uno:
    (*) my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    The order that fields are declared will affect their default order if a model is rendered in a form
    Possible fields:
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
        primary_key
            Es boolean
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

Metadatos:

class Meta: [todas las opciones](https://docs.djangoproject.com/en/5.0/ref/models/options/)
    ordering = ['title', '-publish_date']
            the books would be sorted alphabetically by title, from A-Z, and then by publication date inside each title, from newest to oldest
        control the default ordering of records returned when you query the model type. You do this by specifying the match order in a list of field names to the ordering attribute
        you can prefix the field name with a minus symbol (-) to reverse the sorting order

Métodos
    Minimally, in every model you should define the standard Python class method __str__() to return a human-readable string for each object. This string is used to represent individual records in the administration site (and anywhere else you need to refer to a model instance). Often this will return a title or name field from the model.
```python
def get_absolute_url(self):
    """Returns the URL to access a particular instance of the model."""
    return reverse('model-detail-view', args=[str(self.id)])
```
        Note: Assuming you will use URLs like /my-application/my-model-name/2 to display individual records for your model (where "2" is the id for a particular record), you will need to create a URL mapper to pass the response and id to a "model detail view" (which will do the work required to display the record). The reverse() function above is able to "reverse" your URL mapper (in the above case named 'model-detail-view') in order to create a URL of the right format.

        Of course to make this work you still have to write the URL mapping, view, and template!
