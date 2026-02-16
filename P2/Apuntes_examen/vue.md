# Setup

npm install vue@3.4
npm init vue@3.4 tutorial-vue
    Crea una nueva aplicación con nombre tutorial-vue
    Se creará la aplicación en el directorio llamado tutorial-vue
cd tutorial-vue
npm install
    Instala las depencias y los módulos
npm run dev
    Empieza a correr la aplicación

# Explicación general de la estructura de ficheros
Código en el directorio src
La raíz del proyecto es el fichero index.html

index.html
    Sólo el código dentro del div con id 'app' tendrá acceso a las variables definidas por Vue.js
main.js
    monta las diferentes aplicaciones de las que consta tu proyecto de Vue.js
    siempre debe importar
        - el método createApp
        - el código principal de la aplicación, localizado en el archivo App.vue
    Elementos en el código:
        createApp(App)
            Crea la aplicación
        mount('#app')
            “renderiza” en un elemento HTML de nuestra página la aplicación
            El elemento será el div q tenga id 'app'