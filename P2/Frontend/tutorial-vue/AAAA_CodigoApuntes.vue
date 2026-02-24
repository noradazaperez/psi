<!-- App.vue -->
<template>
    <div id="app" class="container">
    <div class="row">
        <div class="col-md-12"><h1>Personas</h1></div>
    </div>
    <div class="row">
        <div class="col-md-12">
          <formulario-persona @add-persona="agregarPersona" />
          <tabla-personas :personas="personas" />
        </div>
    </div>
    </div>
</template>

<script setup>
import TablaPersonas from '@/components/TablaPersonas.vue'
import FormularioPersona from '@/components/FormularioPersona.vue'
import { ref } from 'vue';

// definicion del componente
defineOptions({
  // nombre del componente
  name: 'app',
});
const personas = ref([]);

// definimos una funcion de nombre agregarPersona que agrega una nueva persona al array
const agregarPersona = (persona) => {
  // actualizamos el valor del array creando un nuevo array con los valores existentes y agregando la nueva persona
  personas.value = [...personas.value, persona];
};
</script>

<style>
    /* Estilos globales para todos los elementos button en la aplicacion */
    button {
    background: #009435;
    border: 1px solid #009435;
    }
</style>
