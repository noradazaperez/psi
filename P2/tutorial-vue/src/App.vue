<!-- App.vue -->
<template>
    <div id="app" class="container">
    <div class="row">
        <div class="col-md-12"><h1>Personas</h1></div>
    </div>
    <div class="row">
        <div class="col-md-12">
          <formulario-persona @add-persona="agregarPersona"/> 
          <tabla-personas :personas="personas" />
        </div>
    </div>
    </div>
</template>

<script setup>
import TablaPersonas from '@/components/TablaPersonas.vue'
// NUEVO:
import FormularioPersona from '@/components/FormularioPersona.vue'
import { ref } from 'vue';

// definicion del componente
defineOptions({
  // nombre del componente
  name: 'app',
});
// Declaracion de una variable reactiva "personas" usando "ref"
const personas = ref([
  {
    id: 1,
    nombre: 'Jon',
    apellido: 'Nieve',
    email: 'jon@email.com',
  },
  {
    id: 2,
    nombre: 'Tyrion',
    apellido: 'Lannister',
    email: 'tyrion@email.com',
  },
  {
    id: 3,
    nombre: 'Daenerys',
    apellido: 'Targaryen',
    email: 'daenerys@email.com',
  },
]);

const agregarPersona = (persona) => {
  console.log("App", persona);
  let id = 0;
  if (personas.value.length > 0) {
    id = personas.value[personas.value.length - 1].id + 1;
  }
  personas.value = [...personas.value, {...persona, id}];
}
</script>

<style>
    /* Estilos globales para todos los elementos button en la aplicacion */
    button {
    background: #009435;
    border: 1px solid #009435;
    }
</style>
