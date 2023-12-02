<template>
  <div class="dentist-t">
    <h1 class="text-3xl md:text-3xl leading-24 md:leading-32 font-inter font-semibold tracking-tighter text-cyan-800 dark:text-cyan-600">
      Availability
    </h1>
    <div class="calendar-container">
      <div class="calendar-wrapper is-light-mode" :style="{ maxWidth: qalendarMaxWidth, padding: qalendarPadding}">
        <Qalendar
          :events="events"
          :config="qalendarConfig"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { Qalendar } from "qalendar";
import "qalendar/dist/style.css";

export default {
  components: {
    Qalendar,
  },
  data() {
    return {
      events: [
      ],
      qalendarHeight: '50rem',
      qalendarWidth: '100%',
      qalendarPadding: '10px',
      qalendarMaxWidth: '100%',
      qalendarConfig: {
        showHeader: true,
        showWeekNumbers: true,
        style: {
          colorSchemes: {
            backgroundColor: '#4987A1',
            meetings: {
              color: '#fff',
              backgroundColor: '#131313',
            },
            sports: {
              color: '#fff',
              backgroundColor: '#ff4081',
            },
          },
        },
      },
    };
  },
};
</script>

<style lang="scss">
  .calendar-container {
    height: 30rem;
    overflow-y: auto;
  }

  .calendar-wrapper {
    height: 100%;
  }
</style>
