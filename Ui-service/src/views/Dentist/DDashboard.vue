<template>
    <div class="flex-container">
      <div class="dentist-t">
        <h1 class="text-4xl md:text-4xl leading-24 md:leading-32 font-inter font-bold tracking-tighter text-cyan-800 dark:text-cyan-600">
          Dashboard
        </h1>
        <p>{{ currentDate }}</p>
      </div>
      <DentistImg />
      <Qalendar />
      <TodaysApp />
    </div>
</template>

<script>
import DentistImg from '../../components/Dentist/Dashboard/DentistImg.vue'
import Qalendar from '../../components/Dentist/Dashboard/Qalendar.vue'
import TodaysApp from '../../components/Dentist/Dashboard/TodaysApp.vue'

export default {
  components: {
    DentistImg, Qalendar, TodaysApp,
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
  min-height: 100vh;
}

.flex-container {
  display: flex;
  flex-grow: 1;
  flex-direction: column;
  padding: .5rem;
}

.DentistImg {
  flex-shrink: 0;
  max-width: 80%;
}

@media screen and (max-width: 768px) {
  .dentist-dashboard {
    flex-direction: column;
  }

  .Dsidebar {
    width: 100%;
  }

  .DentistImg {
    order: -1;
  }
}
</style>
