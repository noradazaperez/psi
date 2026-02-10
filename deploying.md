He decidido dejar de tomar apuntes y sólo hacer para controlar los errores.
NOTAS:
    https://testdriven.io/blog/django-render/
        Seguir este tutorial


1. Cambiar variables de settings.py 
    - DEBUG = False
    - SECRET_KEY
        Ocultarla
    Ponerlas en un .env
2. En settings.py cambiar la base de datos a usar:
3. Configurar los ficheros estáticos
    STATIC_URL, STATIC_ROOT
    - Añadir whitenoise al middleware


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