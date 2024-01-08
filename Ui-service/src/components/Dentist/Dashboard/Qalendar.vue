<template>
  <div>
    <vue-cal :events="events" ref="calendar" id="cal" :time-from="8 * 60" :time-to="18 * 60" :time-step="30"
      :disable-views="['years', 'year']" hide-weekends @event-drag-create="onDragCreate"
      :editable-events="{ title: false, drag: true, resize: true, delete: true, create: true }"
      :drag-to-create-threshold="0" @event-drop="handleEventDrop" @event-resize="handleEventResize"></vue-cal>

    <error-popup :errorMessage="popupMessage" :showPopup="showPopup" @closePopup="closePopup" />
  </div>
</template>

<script>
import VueCal from 'vue-cal';
import 'vue-cal/dist/vuecal.css';
import axios from 'axios';
import { mapGetters } from 'vuex';
import ErrorPopup from '../../Shared/errorPop.vue';

export default {
  name: 'Calendar',
  components: {
    VueCal,
    ErrorPopup
  },
  computed: {
    ...mapGetters(['getEmail'])
  },
  data() {
    return {
      events: [],
      selectedTimeSlots: [],
      selectedDate: null,
      dentist: '',
      popupMessage: '',
      showPopup: false,
    };
  },
  methods: {
    showErrorToUser(message) {
      alert(message);
    },

    handleEventDrop({ event, newStart, newEnd }) {

      if (confirm('Are you sure you want to move this appointment?')) {

        this.updateAvailability(event._id, newStart, newEnd);
      } else {

        this.fetchEvents();
      }
    },
    handleEventResize({ event, newStart, newEnd }) {
      if (confirm('Confirm the new time slot?')) {
        this.updateAvailability(event._id, newStart, newEnd);
      } else {
        this.fetchEvents();
      }
    }, roundToNearestHalfHour(date) {
      let minutes = date.getMinutes();
      let roundedMinutes;

      if (minutes < 15) {
        roundedMinutes = 0;
      } else if (minutes < 45) {
        roundedMinutes = 30;
      } else {
        date.setHours(date.getHours() + 1);
        roundedMinutes = 0;
      }

      date.setMinutes(roundedMinutes);
      date.setSeconds(0);
      date.setMilliseconds(0);

      return date;
    },
    async setAvailability(dentistEmail, date, start, end) {
      if (!date) {
        console.error('Date is undefined');
        this.showErrorToUser('Date is required to set availability.');
        return;
      }

      const formattedDate = new Date(date).toISOString().split('T')[0];

      let startTime = this.roundToNearestHalfHour(new Date(start));
      let endTime = this.roundToNearestHalfHour(new Date(end));
      let timeSlots = [];
      while (startTime < endTime) {
        let slotEnd = new Date(startTime.getTime() + 30 * 60000);
        timeSlots.push({
          start_time: this.formatDateTimeForBackend(startTime, formattedDate),
          end_time: this.formatDateTimeForBackend(slotEnd, formattedDate),
        });

        startTime = slotEnd;
      }

      console.log("Generated Time Slots:", timeSlots);

      try {
          await axios.post('http://127.0.0.1:5004/availability/', {
          dentist_email: dentistEmail,
          date: formattedDate,
          time_slots: timeSlots
        });

        this.popupMessage = 'You sat new timeslots successfully!';
        this.showPopup = true;  

      } catch (error) {
        this.popupMessage = 'Failed to set availability';
        this.showPopup = true;
      }
    },
    closePopup() {
      this.showPopup = false;
      this.popupMessage = '';
      this.fetchEvents();
    },
    formatDateTimeForBackend(dateTime, dateStr) {
      return `${dateStr}T${dateTime.getHours().toString().padStart(2, '0')}:${dateTime.getMinutes().toString().padStart(2, '0')}:00`;
    },
    async updateAvailability(eventId, newStart, newEnd) {
      try {
        const response = await axios.put(`/availability/update_timeslot/${eventId}`, {
          start_time: newStart,
          end_time: newEnd
        });
        if (response.data.success) {
          this.fetchEvents();
        }
      } catch (error) {
        console.error('Error updating availability:', error.response ? error.response.data.message : error);
        this.fetchEvents();
      }
    },
    onDragCreate(event) {
      console.log(event);
      const date = event.start.toISOString().split('T')[0]
      if (!date) {
        console.error('Selected date is undefined');
        this.showErrorToUser('A date must be selected to set availability.');
        return;
      }
      const start = new Date(event.start);
      const end = new Date(event.end);

      this.setAvailability(this.dentist, date, start, end);
    },
    async fetchEvents() {
      try {
        const availabilityResponse = await axios.get('http://127.0.0.1:5004/availability/get_availability', {
          params: {
            dentist_email: this.dentist,
            booked: false
          }
        });

        const appointmentsResponse = await axios.get('http://127.0.0.1:5002/appointments/', {
          params: { dentist_email: this.dentist }
        });

        this.events = this.createEventsFromData(
          availabilityResponse.data.availability,
          appointmentsResponse.data
        );

      } catch (error) {
        console.error('Error fetching events:', error);
        this.showErrorToUser('Failed to fetch events.');
      }
    },
    createEventsFromData(availability, appointments) {
      const parseDate = (dateStr) => {
        const parsedDate = new Date(dateStr);
        return isNaN(parsedDate.getTime()) ? null : parsedDate;
      };
      const availabilityEvents = availability.flatMap(availabilityDay =>
        availabilityDay.time_slots.map(slot => ({
          start: parseDate(slot.start_time),
          end: parseDate(slot.end_time),
          title: 'Available',
          class: 'availability',
          booked: slot.booked
        }))
      );

      const appointmentEvents = appointments.map(appointment => {
        const startTime = parseDate(appointment.appointment_datetime);
        const endTime = new Date(startTime.getTime());
        endTime.setMinutes(startTime.getMinutes() + 30);

        return {
          start: startTime,
          end: endTime,
          title: `Booked`,
          class: 'appointment'
        };
      }).filter(event => event.start && event.end);

      return [...availabilityEvents, ...appointmentEvents];
    }
  },
  mounted() {
    this.dentist = this.getEmail;

    this.fetchEvents();

    setInterval(() => {
      this.fetchEvents();
    }, 10000);
  }
};
</script>

<style scoped>
.vuecal .vuecal__event.availability {
  background-color: #2df29dd4;
}

.vuecal .vuecal__event.appointment {
  background-color: #ff6961;
}



.vuecal--event.done {
  background-color: #cfcfcf;
}
</style>