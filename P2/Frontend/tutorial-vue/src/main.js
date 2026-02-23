// Importa la funcion createApp de la biblioteca Vue
import { createApp } from 'vue'

// Importa el componente principal App desde el archivo App.vue
import App from './App.vue'

// IMPORTANTE: Puedes querer limpiar el archivo main.css por defecto
// ya que las opciones por defecto pueden no satisfacerte.
import './assets/main.css'

// Crea una instancia de la aplicacion Vue y monta el
// componente App en el elemento con el ID 'app'
createApp(App).mount('#app')

app.config.devtools = true // Enable devtools in production (use with caution)

// Las dos lineas siguientes haran que Bootstrap este disponible para tu
// aplicacion si Bootstrap ha sido instalado.

// Importa el archivo JavaScript de Bootstrap desde node_modules
import "../node_modules/bootstrap/dist/js/bootstrap.js"
// Importa el archivo CSS de Bootstrap desde node_modules
import "../node_modules/bootstrap/dist/css/bootstrap.min.css"