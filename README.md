Queda terminar de entender lo de BookInstanceInline y hacer los apuntes de eso estoy leyendo de [aquí](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.inlines)

Estoy justo antes de los ejercicios de la parte 4

# psi

[Enlace tutorial django](http://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django)
[Enlace repositorio profes](https://github.com/rmarabini/psi-alumnos/tree/2025-26/)

## Hacer todo el setup
cd ../..; python3 -m venv p1_env; source p1_env/bin/activate; cd UnidadH/psi/P1; pip3 install -r requirements.txt; cd locallibrary

## Base de datos
Se debe utilizar en todo momento psi como nombre de la base de datos asociada al proyecto, y alumnodb como usuario y contraseña correspondientes
En djangoNotes, la parte de bases de datos pone el setup que hay que hacer

## Coverage
> coverage erase
> coverage run --omit="*/test*" --source=catalog manage.py test catalog.tests
> coverage report -m -i

## No olvidar
- Para alcanzar una cobertura del 100 % se programará un fichero llamado test_additional.py con tests creados por el estudiante que garanticen alcanzar la máxima cobertura. Este fichero se situar´a en la carpeta catalog/tests.
- Pasar lo de flake8

## Errores
Activar sql:
sudo systemctl restart postgresql

## Pregs

- He tenido que cambiar el código proporcionado en el tutorial para pasar un test (código de una parte que yo no he modificado ni tenía que modificar), he hecho bien?
    - En el código dado era "date of birth" y ellos pedían que fuera "birth"
        - Código original: date_of_birth = models.DateField(null=True, blank=True)
- Soy incapaz de conectarme a la base de datos