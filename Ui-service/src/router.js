import Vue from 'vue';
import Router from 'vue-router';
import UserLogin from './components/LoginForm.vue'; 
import UserRegister from './components/RegistrationForm.vue'; 
 
Vue.use(Router);
 
export default new Router({
  mode: 'history', 
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: UserLogin
    },
    {
      path: '/register',
      name: 'Register',
      component: UserRegister
    },
    {
      path: '*', 
      redirect: '/login'
    }
  ]
});