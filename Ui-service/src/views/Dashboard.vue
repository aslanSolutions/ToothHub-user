<template>
  <main class="dashboard-page">
    <div class="dashboard-t">
      <h1 class="text-4xl md:text-4xl leading-24 md:leading-32 font-inter font-bold tracking-tighter text-cyan-800 dark:text-cyan-600">
        Dashboard
      </h1>
      <p>{{ currentDate }}</p>
      <router-view></router-view>

    </div>
    <div class="flex-container">
      <Button />
      <div class="dentist-img">
        <img src="../assets/doctor.png" alt="doctor" />
      </div>
      <cards />
      <Dlist />
    </div>
  </main>

</template>

<script>
import Button from '../components/Button.vue'
import Cards from '../components/Cards.vue'
import Dlist from '../components/Dlist.vue'

export default {
  components: { Button, Cards, Dlist},
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
  }
};
</script>

<style lang="scss">
.flex-container {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

:root {
  --primary: #BDBDBD;
  --grey: #4987A1;
  --dark: #4987A1;
  --dark-alt: #4987A1;
  --light: #f1f5f9;
  --sidebar-width: 300px;
}
* {
  font-family: 'Inter';
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
body {
  background: var(--light);
}
button {
  cursor: pointer;
  appearance: none;
  border: none;
  outline: none;
  background: none;
}


.dashboard-page {
  margin-right: 3rem;
  margin-bottom: 0;
}

.dashboard-t {
  font-family: inter;
  color: #4987A1;
  display: flex;
  flex-direction: column;
  margin-left: 0;
}


.dentist-img {
  transition: 0.2s ease-out;
  width: calc(30rem + 30rem);
  padding-bottom: 30px;

}

@media (max-width: 768px) {
  .dashboard-page {
    position: fixed;
    z-index: 99;
  }

  .dentist-img {
    overflow: hidden;
    width: 12%;
    min-height: auto;
    margin-left: auto;
    padding: 0.1rem;
    transition: 0.2s ease-out;

  }
  }



</style>
