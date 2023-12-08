<template>
    <div class="flex-container">
      <div class="dentist-t">
        <h1 class="text-4xl md:text-4xl leading-24 md:leading-32 font-inter font-bold tracking-tighter text-cyan-800 dark:text-cyan-600">
          Dashboard
        </h1>
        <p>{{ currentDate }}</p>
      </div>
      <DentistImg />
      <DataPicker @date-selected="updateSelectedDate"/>
      <TimePicker :selectedDate="selectedDate" />
    </div>
</template>

<script>
import DentistImg from '../../components/Dentist/Dashboard/DentistImg.vue'
import DataPicker from '../../components/patinet/dataPicker.vue'
import TimePicker from '../../components/patinet/timePicker.vue'

export default {
  components: {
    DentistImg,
    DataPicker,
    TimePicker
  },
  data() {
    return {
      currentDate: '',
      selectedDate: new Date()
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
    updateSelectedDate(date) {
      console.log('Date selected:', date);
      this.selectedDate = date;
    }
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

.DentistImg, .DataPicker {
  flex: none;
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
