import { createApp } from 'vue';
import App from './App.vue';
import './index.css'
import router from './router'
import store from './store';
import 'mapbox-gl/dist/mapbox-gl.css';
import { MglMap, MglMarker, MglNavigationControl, MglGeolocateControl } from 'vue-mapbox';



const app = createApp(App);
app.use(router);
app.use(store);
app.component('MglMap', MglMap);
app.component('MglMarker', MglMarker);
app.component('MglNavigationControl', MglNavigationControl);
app.component('MglGeolocateControl', MglGeolocateControl);






app.mount('#app');
