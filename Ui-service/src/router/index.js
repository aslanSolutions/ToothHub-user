import { createRouter, createWebHistory } from 'vue-router';
import DDashboard from '../views/Dentist/DDashboard.vue';
import Dashboard from '../views/Dashboard.vue';
import Appointments from '../views/Appointments.vue';
import Dentists from '../views/Dentists.vue';
import Patients from '../views/Patients.vue';
import Revenue from '../views/Revenue.vue';
import Settings from '../views/Settings.vue';
import Home from '../views/Home.vue';
import Sidebar from '../components/Sidebar.vue';
import Navbar from '../components/Shared/navbar/navbar.vue';

const routes = [

  {
    path: '/Dashboard',
    name: 'DDashboard',
    component: DDashboard,
  },
  
  {
    path: '/',
    name: 'Home',
    components: {
      default: Home,
      navbar: Navbar
    },
  },
  {
    path: '/Dashboard',
    name: 'Dashboard',
    components: {
      default: Dashboard,
      sidebar: Sidebar,
    },
  },
  {
    path: '/Appointments',
    name: 'Appointments',
    components: {
      default: Appointments,
      sidebar: Sidebar,
    },
  },
  {
    path: '/Dentists',
    name: 'Dentists',
    components: {
      default: Dentists,
      sidebar: Sidebar,
    },
  },
  {
    path: '/Patients',
    name: 'Patients',
    components: {
      default: Patients,
      sidebar: Sidebar,
    },
  },
  {
    path: '/Revenue',
    name: 'Revenue',
    components: {
      default: Revenue,
      sidebar: Sidebar,
    },
  },
  {
    path: '/Settings',
    name: 'Settings',
    components: {
      default: Settings,
      sidebar: Sidebar,
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
