He decidido dejar de tomar apuntes y sólo hacer para controlar los errores.
NOTAS:
    https://testdriven.io/blog/django-render/
        Seguir este tutorial
    En Render te definen RENDER_EXTERNAL_HOSTNAME
        Es la maquina donde está corriendo en ese momento se usa en ALLOWED_HOSTS
    Lo de wsgi, la primera palabra a poner es el nombre del proyecto (en nuestro caso es locallibrary)
        Es literalmente 

1. Cambiar variables de settings.py 
    - DEBUG = False
    - SECRET_KEY
        Ocultarla
    Ponerlas en un .env
2. En settings.py cambiar la base de datos a usar
    Cambiar: DATABASES['default'] = dj_database_url.config(
        conn_max_age=500,
        conn_health_checks=True,
    )

3. Configurar los ficheros estáticos
    STATIC_URL, STATIC_ROOT
    - Añadir whitenoise al middleware
4. Cambiar allowed hosts

Para poder crear super usuarios:
    Poner q en local use el database de neon 
    Hacer ahí los cambios 
    Ahora todo se corresponderá con lo q ves en la web 
    Para q deje de usar el database de neon poner unset

- Comprobar que está listo para deployment
    python3 manage.py check --deploy

### dotenv

Variables defined as KEY=VALUE in the file are imported when the key is used in os.environ.get('<KEY>'', '<DEFAULT VALUE>')

Importar los módulos necesarios 
    ```python
    # Support env variables from .env file if defined
    import os
    from dotenv import load_dotenv
    env_path = load_dotenv(os.path.join(BASE_DIR, '.env'))
    load_dotenv(env_path)
    ```

Establecer las variables en terminal
    ```bash
    export DJANGO_DEBUG=False
    ```