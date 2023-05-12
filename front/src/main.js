import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
import router from './router'
import store from './store'

import Toast from "vue-toastification"
import "vue-toastification/dist/index.css"

const app = createApp(App)

app.use(router)
app.use(store)
app.use(Toast, {
    transition: "Vue-Toastification__fade",
    maxToasts: 20,
    newestOnTop: true
})
app.mount('#app')