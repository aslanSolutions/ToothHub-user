<template>
  <header :class="{ 'scrolled-nav': scrollNav }">
    <div class="navbar-container">
      <router-link class="branding" active-class="active-link" :to="{ name: 'Home' }">
        <div class="branding">
          <Logo />
        </div>
      </router-link>

      <nav>
        <ul v-if="!getIsLoggedIn" class="navigation">
          <li><router-link class="link" active-class="active-class" :to="{ name: 'Home' }">Home</router-link></li>
          <li><router-link class="link" active-class="active-class" :to="{ name: 'About' }">About Us</router-link></li>
          <li><router-link class="link" active-class="active-class" :to="{ name: 'Service' }">Services</router-link></li>
          <li><router-link class="link" active-class="active-class" :to="{ name: 'Contact' }">Contact</router-link></li>
        </ul>

        <ul v-if="getIsLoggedIn" class="navigation">
          <li><router-link class="link" active-class="active-class" :to="{ name: 'Home' }">Home</router-link></li>
          <li><router-link class="link" active-class="active-class" :to="{ name: 'About' }">About Us</router-link></li>
          <li><router-link class="link" active-class="active-class" :to="{ name: 'Service' }">Services</router-link></li>
          <li><router-link class="link" active-class="active-class" :to="{ name: 'Contact' }">Contact</router-link></li>
          <li><router-link class="link" active-class="active-class" :to="{ name: 'PAppointments' }">Appointment</router-link></li>
        </ul>
      </nav>

      <bookbtn />
    </div>
  </header>
</template>

<script>
import Logo from './logoSec.vue'
import Bookbtn from './btnSec'
import { mapGetters } from 'vuex'
export default {
  components: {
    Logo,
    Bookbtn
  },
  name: 'Navbar',

  computed: {
    ...mapGetters(['getIsLoggedIn'])
  },
  data() {
    return {
      scrollNav: null,
      lastScrollPosition: 0,
      windowWidth: null,
      routes: [
        { name: 'Home', label: 'Home' }
      ],
    }
  },
  methods: {
    checkScreen() {
      this.windowWidth = window.innerWidth
    },
    updateScroll() {
      const currentScrollPosition = window.scrollY;

      if (currentScrollPosition > this.lastScrollPosition) {
        this.scrollNav = true;
      } else {
        this.scrollNav = false;
      }

      this.lastScrollPosition = currentScrollPosition;
    }
  },
  mounted() {
    window.addEventListener('scroll', this.updateScroll)
    this.updateScroll()
  }
}
</script>
<style lang="scss" scoped>
header {
  background-color: #ffffff;
  z-index: 3;
  width: 100%;
  position: fixed;
  transition: .1s ease all;
  color: rgba($color: #000000, $alpha: 1.0);

  .navbar-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    padding-right: 5%;
  }

  nav {
    display: flex;
    flex-direction: row;
    padding: 0;
    justify-content: space-between;
    align-items: center;
    transition: .5s ease all;
    width: 90%;
    margin: 0;

    @media(min-width: 1140px) {
      max-width: 1140px;
    }

    ul,
    .link {
      font-weight: 500;
      color: #4987A1;
      list-style: none;
      text-decoration: none;
    }

    li {
      text-transform: uppercase;
      padding: 14px;
      margin-left: 16px;
    }

    .link {
      font-size: 14px;
      transition: .5s ease all;
      padding-bottom: 4px;
      border-bottom: 1px solid transparent;

      &:hover {
        color: #014a69;
        border-color: reds;
      }

    }

    .navigation {
      display: flex;
      align-items: center;
      justify-content: center;
      flex: 1;
      padding-right: 5%;

    }

    li {
      margin-left: 0;

      .link {
        color: #000000;
      }
    }
  }
}

.link.active-link {
  color: #014a69;
}

@media (max-width: 750px) {
  header {
    .navbar-container {
      padding-right: 2%;
    }

    .branding img {
      width: 60%;
    }

    nav .navigation {
      display: none;
    }
  }
}

.scrolled-nav {
  background-color: #d0caca;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px, -1px rgba(0, 0, 0, 0.06);

  nav {
    padding: 4px 0;
  }

  .branding {
    img {
      width: 25%;
    }
  }
}
</style>
  