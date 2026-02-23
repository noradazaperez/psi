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

En un archivo, usar el @ en las direcciones hace referencia al directorio src 

# Estructura de un archivo Vue.js
```html
<template>
<!-- Aqui ira el marcado HTML del componente -->
</template>
<script>
// Importamos las funciones necesarias de Vue
const { createApp, ref } = Vue;
// Creamos una aplicacion Vue
const app = createApp({
// Aqui podrias definir opciones para el
// componente
});
</script>
<style scoped>
<!-- CSS, el modificador scoped hace que sólo afecten a esta página -->
</style>
```

### propiedades

**En la parte del script**
```javascript
// declaramos y damos valor por defecto para las propiedades
const props = defineProps({
  personas: {type: Array, default: () => []},
});
```

**En el template**
```html 
<!-- Iteracion sobre el array de personas utilizando v-for -->
<tr v-for="persona in personas" :key="persona.id">
<!-- Celda de datos para el nombre de la persona -->
<td>{{ persona.nombre }}</td>
<!-- Celda de datos para el apellido de la persona -->
<td>{{ persona.apellido }}</td>
<!-- Celda de datos para el correo electronico de la persona -->
<td>{{ persona.email }}</td>
</tr>
```

# Componentes
**Persona**
Crear en la carpeta src/components
El nombre de archivo debe ser PascalCase
El nombre del componente dentro del archivo debe estar en kebab-case

### En el fichero del componente
Estructura del script
```javascript
// definicion del componente
defineOptions({
  // nombre del componente
  name: 'tabla-personas',
});

// declaramos y damos valor por defecto para las propiedades que recibirá el componente
const props = defineProps({
  personas: {type: Array, default: () => []},
});
```

### Usar componente

**Importarlo**
```javascript
import ¡nombre componente (en PascalCase)! from '@/components/¡nombre componente (PascalCase)!.vue'
```

**Renderizarlo**
Agregar <¡nombre del componente en kebab-case! :¡nombre variable a pasarle al componente!="¡nombre de variable definida en el script q pasarás!"/>
    (*) <tabla-personas :personas="personas" />
    NOTA: se puede poner v-bind delante de los ':', es como la versión larga de pasar el argumento

### Formularios

Ver @/components/FormularioPersonas.vue

# Script 

**Variables**
Crear variables reactivas (q un cambio en su valor comporte una nueva renderización del HTML)
```javascript
import { ref } from 'vue';

// Declaracion de una variable reactiva "personas" usando "ref"
const personas = ref([
  {
    id: 1,
    nombre: 'Jon',
  },
  {
    id: 2,
    nombre: 'Tyrion',
  },
]);
```

# Frameworks
Te predefinen algunos elementos q puedas usar

**Bootstrap**
Añadirlo al proyecto:
En src/main.js:
```javascript
import "../node_modules/bootstrap/dist/js/bootstrap.js";
import '../node_modules/bootstrap/dist/css/bootstrap.min.css'
```

E instalarlo en node, desde la raíz del proyecto:
```bash
npm install bootstrap@5.3.3
npm install @popperjs/core@2.11.8
```