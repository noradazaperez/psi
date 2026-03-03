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
- Agrega un bucle al componente
```html
      <tbody>
        <!-- Iteracion sobre el array de personas utilizando v-for -->
        <tr v-for="persona in personas" :key="persona.id">
          <!-- Celda de datos para el nombre de la persona -->
          <td>{{ persona.nombre }}</td>
          <!-- Celda de datos para el apellido de la persona -->
          <td>{{ persona.apellido }}</td>
          <!-- Celda de datos para el correo electronico de la persona -->
          <td>{{ persona.email }}</td>
        </tr>
      </tbody>

```

### Creación de formularios

- Crea un formulario con `Vue.js`
    * campo input 
    * botón submit que nos permita enviar los datos
- Agrega el formulario a la aplicación
    * Añadir dentro de <template> como:

```html
<template>
    <div id="app" class="container">
    <div class="row">
        <div class="col-md-12"><h1>Personas</h1></div>
    </div>
    <div class="row">
        <div class="col-md-12">
          <formulario-persona /> <!-- NUEVO -->
          <tabla-personas :personas="personas" />
        </div>
    </div>
    </div>
</template>

import FormularioPersona from '@/components/FormularioPersona.vue'
```

- Enlaza los campos del formulario con su estado
    * v-model - enlazará el valor de los campos con susrepectivas variables de estado
```html
            <div class="form-group">
              <!-- Etiqueta y campo de entrada para el apellido con binding bidireccional v-model -->
              <label>Apellido</label>
              <input v-model="persona.apellido" type="text" class="form-control" />
            </div>
```

- Agrega un método de envío al formulario

    * agregar un **evento** - **event listener**
    * click en el botón de envío - @submit o v-on:submit
    * @mouseover o v-on:mouseover
    * @click o v-on:click

- Emitir eventos del formulario a la aplicación
    * El método `$emit`- envía el nombre del evento y los datos que deseemos
    * Con el método `defineEmits` - declaramos los eventos que emitirá el componente y obtenemos un método que podremos usar para emitir el evento cuando sea necesario
    * nombre de evento = kebab-case siempre

- Recibe eventos de la tabla en la aplicación
    * Debemos capturar los datos en la aplicación
    1. Agregamos la propiedad `@add-persona` en la etiqueta `formulario-persona` 
    2. En ella asociamos un nuevo método 
    ```html
    <formulario-persona @add-persona="agregarPersona"/>

    ```
    3. Creamos el método agregarPersona en el script de `App.vue`
        * método de propagación ... útil para combinar objetos y arrays 



### Validaciones con `Vue.js`
- Propiedades computadas de `Vue.js`
    * Los datos se suelen validar mediante **propiedades computadas**
    * Funciones que se ejecutan automáticamente cuando se modifica el estado de alguna propiedad
- Se agrega en el interior del método setUp del componente FormularioPersona

- Sentencias condicionales con `Vue.js`
    * Se agregue la clase CSS has-error a los campos en función de si han fallado o no
        - La sentencia `:class="{'is-invalid': procesando && nombreInvalido}"` añade la clase is-valid si procesando 
        y nombreInvalido valen true

    * `v-if` : hace que el elemento en el que se incluya solamente se muestre si la condición especificada se evalúa como true


- Referencias con `Vue.js`
    * El foco + cursor se sitúen en el primer elemento del formulario 

### Elimina elementos con Vue.js
- Agregar una columna en la tabla que permita borrar una línea en la tabla
```html
        <td>
            <!-- &#x1F5D1; is the wastebasket icon. Icons available at https://codepoints.net -->
            <button class="btn btn-danger">&#x1F5D1; Eliminar</button>
        </td>

```
- Añadir un método para borrar el elemento en `App.vue`
- Hemos usado el método filter, que conservará aquellos elementos del array
    personas cuyo id no sea el indicado. Y con esto, si consultas el navegador, podrás
    comprobar que las personas se eliminan de la tabla al pulsar el botón de su respectiva
    fila:

- **Agrega mensajes informativos**: 

### Edita elementos con `Vue.js`:

1. Añadir un botón
```html
<button class="btn btn-info ml-2" @click="editarPersona(persona)">&#x1F58A; Editar</button>
```

2. Añadir un método de edición

```html
const editando = ref(null);
const personaEditada = ref(null);
const editarPersona = (persona) => {
    personaEditada.value = { ...persona };
    editando.value = persona.id;
};

```

3. Añadir campo de edición
4. Agrega un botón de edición
5. Emite el evento de guardado
6. Agrega un método que cancele la dición
7. Recibe el evento de actualización en la aplicación
* En app.vue tengo que definiri actualizarpersona

```html
<!-- App.vue -->
const actualizarPersona = (id, personaActualizada) => {
    try {
        personas.value = personas.value.map(persona =>
        persona.id === id ? personaActualizada : persona);
    }
    catch(error){
        console.error(error);
    }
}

```

### Testing de la aplicación `Vue.js`


- Abrir entorno de Cypress
```bash
npx cypress open
```

- *Nota*: Si en algún momento recibes un error indicando que Cypress no se puede conectar
al servidor (porque está usando el puerto 4173 en lugar del 5173), simplemente debes
cambiar la variable baseUrl del fichero cypress.config.js.


### Estilo de la aplicación `Vue.js`

- Se va a validar el estilo de la práctica utilizando la librería ESLint

- Incluir en el archivo `package.json`:

```
"lint": 
```

- Crear el archivo `.eslintrc.js`
- Ejecutamos: 
```bash
npm run lint
```


### Build + Deploy de la aplicación `Vue.js`
* Build de la aplicación: `npm run build`
* 



