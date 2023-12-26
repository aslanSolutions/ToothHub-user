import { createApp } from 'vue';
import App from './App.vue';
import './index.css'



import router from './router'
import store from './store';

const app = createApp(App);
app.use(router);
app.use(store);
app.use(VueGoogleMaps, {
    load: {
      key: 'AIzaSyA70fTDcp3dluL9ScZ0nOi7xc25tuwUIDc',
    },
  })




app.mount('#app');
