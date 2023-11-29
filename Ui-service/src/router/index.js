import { createRouter, createWebHistory } from 'vue-router';
import DDashboard from '../views/Dentist/DDashboard.vue';
import Dashboard from '../views/Dashboard.vue';
import Appointments from '../views/Appointments.vue';
import Dentists from '../views/Dentists.vue';
import Patients from '../views/Patients.vue';
import Revenue from '../views/Revenue.vue';
import Settings from '../views/Settings.vue';

const routes = [

  {
    path: '/Dashboard',
    name: 'DDashboard',
    component: DDashboard,
  },
  
  {
    path: '/',
    name: 'Dashboard',
    component: Dashboard,
  },
  {
    path: '/Appointments',
    name: 'Appointments',
    component: Appointments,
  },
  {
    path: '/Dentists',
    name: 'Dentists',
    component: Dentists,
  },
  {
    path: '/Patients',
    name: 'Patients',
    component: Patients,
  },
  {
    path: '/Revenue',
    name: 'Revenue',
    component: Revenue,
  },
  {

    path: '/Settings',
    name: 'Settings',
    component: Settings,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router