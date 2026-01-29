# psi

[Enlace tutorial django](http://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django)
[Enlace repositorio profes](https://github.com/rmarabini/psi-alumnos/tree/2025-26/)

## Activar el venv
source ../../p1_env/bin/activate

## Coverage
> coverage erase
> coverage run --omit="*/test*" --source=catalog manage.py test catalog.tests
> coverage report -m -i

## No olvidar
- Para alcanzar una cobertura del 100 % se programará un fichero llamado test_additional.py con tests creados por el estudiante que garanticen alcanzar la máxima cobertura. Este fichero se situar´a en la carpeta catalog/tests.
- Pasar lo de flake8

## Pregs

- He tenido que cambiar el código proporcionado en el tutorial para pasar un test (código de una parte que yo no he modificado ni tenía que modificar), he hecho bien?
    - En el código dado era "date of birth" y ellos pedían que fuera "birth"
        - Código original: date_of_birth = models.DateField(null=True, blank=True)