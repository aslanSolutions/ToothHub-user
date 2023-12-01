<template>
    <div class="dentist-t">
      <h1 class="text-3xl md:text-3xl leading-24 md:leading-32 font-inter font-semibold tracking-tighter text-cyan-800 dark:text-cyan-600">
        Availability
      </h1>
  <div class="calendar-wrapper is-light-mode" :style="{ height: qalendarHeight, maxWidth: qalendarMaxWidth, padding: qalendarPadding}">
    <Qalendar
      :events="events"
      :config="qalendarConfig"
    />
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
        {
          title: 'Beep',
          time: { start: '2022-05-16 08:00', end: '2022-05-16 09:00' },
          colorScheme: 'meetings',
          id: '1',
        },
        {
          title: 'Boop',
          time: { start: '2022-05-16 08:00', end: '2022-05-16 09:00' },
          colorScheme: 'sports',
          id: '2',
        },
      ],
      qalendarHeight: '35rem',
      qalendarWidth: '100%',
      qalendarPadding: '10px',
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

<style lang="scss" scoped>


</style>
