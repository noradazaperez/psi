<!-- src/components/TablaPersonas.vue -->

<template>
  <!-- Contenedor principal del componente -->
  <div id="tabla-personas">
    <!-- Tabla HTML para mostrar la informacion de personas -->
    <div v-if="!personas.length" class="alert alert-info" role="alert">
      No se han encontrado personas
    </div>
    <div v-else>
      <table class="table">
      <!-- Encabezado de la tabla -->
      <thead>
        <!-- nombres de columnas -->
        <tr>
          <th>Nombre</th>
          <th>Apellido</th>
          <th>Email</th>
        </tr>
      </thead>
      <!-- Cuerpo de la tabla con datos dinamicos -->
      <tbody>
        <!-- Iteracion sobre el array de personas utilizando v-for -->
        <tr v-for="persona in personas" :key="persona.id">
          <td v-if="editando === persona.id">
            <input id="persona.nombre" v-model="persona.nombre" type="text" class="form-control" data-cy="persona-nombre">
          </td>
          <td v-else>
            {{ persona.nombre }}
          </td>
          <td v-if="editando === persona.id">
            <input v-model="persona.apellido" type="text" class="form-control">
          </td>
          <td v-else>
            {{ persona.apellido }}
          </td>
          <td v-if="editando === persona.id">
            <input v-model="persona.email" type="email" class="form-control">
          </td>
          <td v-else>
            {{ persona.email }}
          </td>
          <td> <!-- &#x1F5D1; is the wastebasket icon. Icons available at https://codepoints.net -->
            <button class="btn btn-danger" @click="$emit('delete-persona', persona.id)" >
              &#x1F5D1; Eliminar</button>
            <button class="btn btn-info ml-2" @click="editarPersona(persona)">
              &#x1F58A; Editar</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
</template>

<script setup>
  import { ref } from 'vue';
  // definicion del componente
  defineOptions({
    // nombre del componente
    name: 'tabla-personas',
  });

  // declaramos y damos valor por defecto para la propiedad personas
  const props = defineProps({
    personas: {type: Array, default: []},
  });

  const editando = ref(null);
  const personaEditada = ref(null);
  
  const editarPersona = (persona) => {
    personaEditada.value = { ...persona };
    editando.value = persona.id;
  };
</script>

<style scoped>
  /* Estilos especificos del componente con el modificador "scoped" */
</style>
