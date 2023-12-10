<template>
  <vue-cal :events="events" ref="calendar" id="cal" :time-from="8 * 60" :time-to="18 * 60" :time-step="30"
    :disable-views="['years', 'year']" hide-weekends @event-drag-create="onDragCreate"
    :editable-events="{ title: false, drag: true, resize: true, delete: true, create: true }"
    :drag-to-create-threshold="0" @event-drop="handleEventDrop" @event-resize="handleEventResize"></vue-cal>
</template>

<script>
import VueCal from 'vue-cal';
import 'vue-cal/dist/vuecal.css';
import axios from 'axios';
import { mapGetters } from 'vuex';

export default {
  name: 'Calendar',
  components: {
    VueCal
  }, computed: {
    ...mapGetters(['getEmail'])
  },
  data() {
    return {
      events: [],
      selectedTimeSlots: [],
      selectedDate: null,
      dentist: ''
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
    },
    handleEventClick() {
    },
    async setAvailability(dentistEmail, date, timeSlots) {

      console.log("email", dentistEmail)

      if (!date) {
        console.error('Date is undefined');
        this.showErrorToUser('Date is required to set availability.');
        return;
      }

      const formattedDate = new Date(date).toISOString().split('T')[0];

      const roundToNearest = (date) => {
        const minutes = date.getMinutes();
        if (minutes < 15) {
          date.setMinutes(0); // Round down to 00
        } else if (minutes < 45) {
          date.setMinutes(30);
        } else {
          date.setHours(date.getHours() + 1);
          date.setMinutes(0);
        }
        return date;
      };

      const formattedNewTimeSlots = timeSlots.map((slot) => {
        let startDateTime = new Date(slot.start_time);
        let endDateTime = new Date(slot.end_time);

        startDateTime = roundToNearest(startDateTime);
        endDateTime = roundToNearest(endDateTime);

        const startUtc = new Date(startDateTime.getTime() - (startDateTime.getTimezoneOffset() * 60000)).toISOString();
        const endUtc = new Date(endDateTime.getTime() - (endDateTime.getTimezoneOffset() * 60000)).toISOString();

        return {
          start_time: startUtc,
          end_time: endUtc,
        };
      });

      try {
        let response = await axios.get('http://127.0.0.1:5004/availability/get_availability', {
          params: { dentist_email: dentistEmail, date: formattedDate }
        });

        let existingTimeSlots = [];
        if (response.data && response.data.availability && response.data.availability.length > 0) {
          existingTimeSlots = response.data.availability[0].time_slots;
        }

        const combinedTimeSlots = [...existingTimeSlots, ...formattedNewTimeSlots];

        response = await axios.post('http://127.0.0.1:5004/availability/set_availability', {
          dentist_email: dentistEmail,
          date: formattedDate,
          time_slots: combinedTimeSlots
        });

        console.log(response);

      } catch (error) {
        console.error('Error setting availability:', error.response ? error.response.data : error);
        this.showErrorToUser(`Failed to set availability: ${error.response.data.detail || 'Unknown error'}`);
      }
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

      const timeSlot = {
        start_time: event.start,
        end_time: event.end,
      };

      this.setAvailability(this.dentist, date, [timeSlot]);
    },
    async fetchEvents() {
      try {
        // Replace with the correct endpoint URL
        const response = await axios.get('http://127.0.0.1:5004/availability/get_availability', {
          params: { dentist_email: this.dentist }
        });

        if (response.data && response.data.availability) {
          // Assuming each item in 'availability' has 'date' and 'time_slots'
          const events = [];
          response.data.availability.forEach(availabilityItem => {
            availabilityItem.time_slots.forEach(slot => {
              const start = new Date(slot.start_time);
              const end = new Date(slot.end_time);

              start.setHours(start.getHours() - 1);
              end.setHours(end.getHours() - 1);

              events.push({
                start: start,
                end: end,
                title: 'Available',
                class: 'available'
              });
            });

          });
          this.events = events;
        }
      } catch (error) {
        console.error('Error fetching events:', error);
        this.showErrorToUser('Failed to fetch available time slots.');
      }
    },
  },
  mounted() {
    this.dentist = this.getEmail;

    this.$nextTick(() => {
      this.fetchEvents();
    });
  }
};
</script>

<style scoped>
/* Example styles */
.vuecal__event.available {
  background-color: #2df29dd4;
}

.vuecal--event.booked {
  background-color: #9fcdff;
}

.vuecal--event.done {
  background-color: #cfcfcf;
}
</style>