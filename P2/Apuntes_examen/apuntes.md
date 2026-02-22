## Apuntes P2

- Para ejecutar el servidor de desarrollo:
```bash
npm install
npm run dev
```

- Estructura de proyecto:
* `main.js` que es llamado desde `index.html`
    - Siempre debe importar:
        * metodo createApp
        * codigo principal de la aplicación, localizado en el archivo App.vue

- Estructura de un archivo Vue.js
1. Seccion template: agregaremos el codigo HTML de la aplicación
2. Sección script: agrgaremos el codigo JavaScript
3. Sección style: agregaremos el codigo CSS

```html
<template>
</template>

<script>
    // Importamos las funciones necesarias de Vue
    const { createApp, ref } = Vue;

    const app = createApp({
        // aqui podrias definir opciones para el composnente
    });
</script>

<style scoped>
    <!-- aqui irian las reglas del estilo del componente -->
</style>


```

### Creacion de componentes
- Crea una componente: añade eel .vue en components/
- Agrega el componente a la app
    - importar el componente en la app. Escribiendo en script:
    ```html
        import TablaPersonas from '@/components/TablaPresonas.vue'
    ```
    - usamos @ para referenciar al directorio src
    - agregamos el componente a la propiedad components:
- Agrega datos al componente
    - Datos se transfieren como propiedades y se incluyen como `:nombre="datos"`
