import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'
import { zhCn } from 'element-plus/es/locales.mjs'


const app = createApp(App)

app.use(ElementPlus, {
    locale: zhCn,
})

app.mount('#app')
