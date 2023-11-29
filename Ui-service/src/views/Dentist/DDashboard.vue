<template>
  <div class="dentist-dashboard">
    <DSidebar />
    <div class="flex-container">
      <div class="dentist-t">
        <h1 class="text-4xl md:text-4xl leading-24 md:leading-32 font-inter font-bold tracking-tighter text-cyan-800 dark:text-cyan-600">
          Dashboard
        </h1>
        <p>{{ currentDate }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import DSidebar from '../../components/Dentist/Dashboard/Dsidebar.vue';

export default {
  components: {
    DSidebar,
  },
  data() {
    return {
      currentDate: '',
    };
  },
  mounted() {
    this.updateDate();
    setInterval(this.updateDate, 1000);
  },
  methods: {
    updateDate() {
      const now = new Date();
      this.currentDate = now.toLocaleString();
    },
  },
};
</script>

<style lang="scss" scoped>
.dentist-dashboard {
  display: flex;
}

.Dsidebar {
  display: block;
  height: 90rem;
  width: 20rem;
  background: #4987A2;
  box-shadow: 0px 1px 1px rgba(0, 0, 0, 0.1);
  padding: 0;
}

.flex-container {
  display: flex;
  flex-direction: column;
  /* Add additional styling for the flex container if needed */
}

/* Add your scoped styles for .dentist-t here */
.dentist-t {
  /* Your styles for the text container */
}

/* Adjust styles for DSidebar and its icons if needed */
.logo {
  max-width: 100%;
  height: auto;
}
</style>
