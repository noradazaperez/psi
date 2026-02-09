# psi

Dejado en la parte 8, justo encima de permissions

[Enlace tutorial django](http://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django)
[Enlace repositorio profes](https://github.com/rmarabini/psi-alumnos/tree/2025-26/)

## Hacer todo el setup
cd ../..; python3 -m venv p1_env; source p1_env/bin/activate; cd UnidadH/psi/P1; pip3 install -r requirements.txt; cd locallibrary

## Info nuestra app 
(nombreusuario/contraseña)
- el super user es alumnodb/alumnodb
- Usuario normal: albertu/mycrazyemail

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
- Cerrar servidor postgresql

## Errores
Activar sql:
sudo systemctl restart postgresql

## Pregs resueltas

- Soy incapaz de conectarme a la base de datos
    - sudo systemctl restart postgresql

## Material al q tendremos acceso:
    - Lo q hayamos subido a moodle
        - Podemos añadir lo q queramos
        - Su recomendación: resolver el examen y poner nuestra resolución en moodle

## Pregs
- He hecho lo siguiente a requirements.txt para q me funcione en local
    #psycopg2==2.9.10
    psycopg2-binary==2.9.10
    - En el original el # está swapped
    - Si no, no me compila porq no tengo los ficheros de C necesarios
    @ Si los pones sin binario, lo tiene q compilar y, por eso, no funciona
    @ Si funciona el binario, quedarse con el binario
- Creo q uno de los tests está mal, lo he cambiado a:
    result = finders.find('css/styles.css')
    (le he quitado la 's' al final de style)
    @ No cambiar el test
- Hay que hacer lo de flake8?
    - Es q me saltan muchísimos errores de las partes q te dan ellos
    @ Sólo modificar las cosas que hayamos tocado (si es sólo una línea, sólo esa línea)
- Necesidades especiales es en el 6a, ¿cuento yo?
    @ No cuento