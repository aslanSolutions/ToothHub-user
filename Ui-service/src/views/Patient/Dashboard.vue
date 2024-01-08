<template>
  <div class="flex-container">
    <div class="dentist-t">
      <h1
        class="text-4xl md:text-4xl leading-24 md:leading-32 font-inter font-bold tracking-tighter text-cyan-800 dark:text-cyan-600">
        Dashboard
      </h1>
      <p>{{ currentDate }}</p>
    </div>
    <div class="map-and-picker-container">
      <div class="map-container">
        <mapComponent @clinic-selected="onClinicSelected" />
      </div>
      <div class="DataPicker">
        <DataPicker @date-selected="updateSelectedDate"/>
      </div>
    </div>
    <TimePicker :selectedDate="selectedDate" :selectedClinic="selectedClinic" />
  </div>
</template>

<script>
import DataPicker from '../../components/patinet/dataPicker.vue'
import TimePicker from '../../components/patinet/timePicker.vue'
import mapComponent from '@/components/Shared/map.vue'

export default {
  components: {
    DataPicker,
    TimePicker,
    mapComponent
  },
  data() {
    return {
      currentDate: '',
      selectedDate: new Date(),
      selectedClinic: null,
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
      this.selectedDate = date;
    },
    onClinicSelected(clinicName) {
      console.log("Provided clinic:", clinicName)
      this.selectedClinic = clinicName;
    },
  },
};
</script>

<style lang="scss" scoped>
.flex-container {
  display: flex;
  flex-grow: 1;
  flex-direction: column;
  padding: .5rem;
  margin-top: 8rem;
  margin-bottom: 8rem;
}

.map-and-picker-container {
  display: flex;
  margin-left: 15px;
  flex: 1;
  max-width: 95rem;
}

.map-container {
  flex: 1;
}

.DataPicker {
  flex: 1;
  margin: 35px 20px;
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
