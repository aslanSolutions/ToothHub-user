import { createRouter, createWebHistory } from 'vue-router';
import { jwtDecode } from 'jwt-decode';
import store from '../store';

// Dashboard of users
import DDashboard from '../views/Dentist/DDashboard.vue';
import DAppointments from '@/components/Dentist/Dashboard/DAppointments.vue';
import PDashboard from '../views/Patient/Dashboard.vue';
import Dashboard from '../views/Dashboard.vue';

// Pages
import Dentists from '../views/Dentists.vue';
import Patients from '../views/Patients.vue';
import Revenue from '../views/Revenue.vue';
import PProfile from '../views/Patient/PProfile.vue';
import PAppointments from '@/components/patinet/PAppointments.vue';
import Home from '../views/Home.vue';
import Login from '@/components/Shared/LoginForm.vue';
import Register from '@/components/patinet/RegistrationForm.vue';
import Service from '../views/Service.vue';
import Contact from '../views/Contact.vue';
import About from '../views/About.vue';


// Navbar and sidebars 
import Sidebar from '../components/Sidebar.vue';
import Dsidebar from '../components/Dentist/Dashboard/Dsidebar.vue';
import PSidebar from '../components/patinet/sidebar.vue';
import Navbar from '../components/Shared/navbar/navbar.vue';
import footer from '../components/Shared/footer.vue';

import RightSidebar from '../components/Dentist/Dashboard/RightBar.vue';
const routes = [

  {
    path: '/dentist-dashboard',
    name: 'Dentist-Dashboard',
    meta: { requiresAuth: true, type: 'Dentist', isDashboard: true },
    components: {
      default: DDashboard,
      Sidebar: Dsidebar,
      Rightbar: RightSidebar
    }
  },
  {
    path: '/patient-dashboard',
    name: 'Patient-Dashboard',
    meta: { requiresAuth: true, type: 'Patient', isDashboard: true },
    components: {
      default:PDashboard,
      navbar: Navbar,
      footer: footer
    }
  },
  {
    path: '/',
    name: 'Home',
    components: {
      default: Home,
      navbar: Navbar,
      footer: footer
    },
  },
  {
    path: '/',
    name: 'Service',
    components: {
      default: Service,
      navbar: Navbar,
      footer: footer
    },
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    components: {
      default: Dashboard,
      Sidebar: Sidebar,
      Rightbar: RightSidebar,
    },
  },
  {
    path: '/register',
    name: 'Register',
    components: {
      default: Register,
      navbar: Navbar,
      footer: footer
    },
  },
  {
    path: '/login',
    name: 'Login',
    components: {
      default: Login,
      navbar: Navbar,
      footer: footer
    },
  },
  {
    path: '/Appointments',
    name: 'DAppointments',
    components: {
      default: DAppointments,
      Sidebar: Dsidebar,
      Rightbar: RightSidebar
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
    path: '/Profile',
    name: 'PProfile',
    components: {
      default: PProfile,
      Sidebar: PSidebar
    },
  },
  {
    path: '/Contact',
    name: 'Contact',
    components: {
      default: Contact,
      footer: footer,
      navbar: Navbar,
    },
  },
  {
    path: '/About',
    name: 'About',
    components: {
      default: About,
      footer: footer,
      navbar: Navbar,
    },
  },
  {
    path: '/p-appointments',
    name: 'PAppointments',
    meta: { requiresAuth: true, type: 'Patient' },
    components: {
      default: PAppointments,
      navbar: Navbar,
      footer: footer
    },
  },
  {
    path: '/',
    name: 'Services',
    components: {
      default: Service,
      navbar: Navbar,
      Sidebar: PSidebar
    },
  }
];
Contact
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach(async (to, from, next) => {
  const accessToken = store.getters.getAccessToken;

  if (to.meta.isDashboard) {
    if (accessToken) {
      try {
        const decodedToken = jwtDecode(accessToken);
        const currentTimestamp = Math.floor(Date.now() / 1000);

        if (decodedToken.exp && currentTimestamp < decodedToken.exp) {
          if (to.meta.type && to.meta.type !== decodedToken.type) {
            next('/error');
          } else {
            next();
          }
        } else {
          // Token expired
          next('/login');
        }
      } catch (error) {
        console.error('Token validation error:', error);
        next('/login');
      }
    } else {
      next('/login');
    }
  } else {
    next(); // Proceed for non-dashboard routes
  }
});
export default router;
