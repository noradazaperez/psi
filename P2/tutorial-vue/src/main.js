// importa la función createApp desde la biblioteca Vue
import { createApp } from 'vue'
//import { createPinia } from 'pinia'

import App from './App.vue'
//import router from './router'

// IMPORTANTE: Puedes querer limpiar el archivo main.css por defecto
// ya que las opciones por defecto pueden no satisfacerte.
//import './assets/main.css'

const app = createApp(App)

//app.use(createPinia())
//app.use(router)

app.mount('#app')

import "../node_modules/bootstrap/dist/js/bootstrap.js"
import "../node_modules/bootstrap/dist/css/bootstrap.min.css"
