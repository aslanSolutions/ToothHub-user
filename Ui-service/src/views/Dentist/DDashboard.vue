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
      <DentistImg />
      <VueDatePicker v-model="date" position= "left"></VueDatePicker>
      <TodaysApp />
    </div>
  </div>
</template>

<script>
import DSidebar from '../../components/Dentist/Dashboard/Dsidebar.vue';
import DentistImg from '../../components/Dentist/Dashboard/DentistImg.vue'
import VueDatePicker from '@vuepic/vue-datepicker'
import '@vuepic/vue-datepicker/dist/main.css'
import TodaysApp from '../../components/Dentist/Dashboard/TodaysApp.vue'

export default {
  components: {
    DSidebar,DentistImg,VueDatePicker,TodaysApp,
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

.Dsidebar {
  display: block;
  height: 100%;
  width: 20rem;
  background: #4987A2;
  box-shadow: 0px 1px 1px rgba(0, 0, 0, 0.1);
  padding: 0;
}

.flex-container {
  display: flex;
  flex-grow: 1;
  flex-direction: column;
}


</style>
