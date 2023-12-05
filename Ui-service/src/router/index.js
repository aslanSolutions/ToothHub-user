import { createRouter, createWebHistory } from 'vue-router';
//import jwt_decode from 'jwt-decode';
//import store from '../store/auth.js';

// Dashboard of users
import DDashboard from '../views/Dentist/DDashboard.vue';
import PDashboard from '../views/Patient/Dashboard.vue';
import Dashboard from '../views/Dashboard.vue';
// Pages
import Appointments from '../views/Appointments.vue';
import Dentists from '../views/Dentists.vue';
import Patients from '../views/Patients.vue';
import Revenue from '../views/Revenue.vue';
import Settings from '../views/Settings.vue';
import Home from '../views/Home.vue';
import Login from '@/components/Shared/LoginForm.vue';
import Register from '@/components/patinet/RegistrationForm.vue';

// Navbar and sidebars 
import Sidebar from '../components/Sidebar.vue';
import Dsidebar from '../components/Dentist/Dashboard/Dsidebar.vue';
import PSidebar from '../components/patinet/sidebar.vue';
import Navbar from '../components/Shared/navbar/navbar.vue';
import RightSidebar from '../components/Dentist/Dashboard/RightBar.vue';

const routes = [

  {
    path: '/dentist-dashboard',
    name: 'Dentist-Dashboard',
    components: {
      default: DDashboard,
      Sidebar: Dsidebar,
      Rightbar: RightSidebar
    }
  },
  {
    path: '/patient-dashboard',
    name: 'Patient-Dashboard',
    components: {
      default: PDashboard,
      Sidebar: PSidebar,
      Rightbar: RightSidebar,
    }
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
      navbar: Navbar
    },
  },
  {
    path: '/login',
    name: 'Login',
    components: {
      default: Login,
      navbar: Navbar
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

/*router.beforeEach(async (to, from, next) => {
  const accessToken = store.state.accessToken;

  if (accessToken && isTokenValid(accessToken)) {
    if (to.meta.userType === 'dentist' && accessToken.userType === 'Dentist') {
      next();
    } else if (to.meta.userType === 'patient' && accessToken.userType === 'Patient') {
      next();
    } else {
      next('/error');
    }
  } else {
    next('/login');
  }
});

function isTokenValid(token) {
  if (!token) {
    return false;
  }

  try {
    const decodedToken = jwt_decode(token);

    if (decodedToken && decodedToken.exp) {
      const currentTimestamp = Math.floor(Date.now() / 10000);

      if (currentTimestamp < decodedToken.exp) {
        return true;
      }
    }
  } catch (error) {
    console.error('Token validation error:', error);
  }

  return false;
}*/

export default router;
