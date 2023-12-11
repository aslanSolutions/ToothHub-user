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
        // Fetch availability
        const availabilityResponse = await axios.get('http://127.0.0.1:5004/availability/get_availability', {
          params: { dentist_email: this.dentist }
        });
        console.log('Availability Response:', availabilityResponse.data);

        // Fetch appointments
        const appointmentsResponse = await axios.get('http://127.0.0.1:5002/appointments/all_appointments', {
          params: { dentist_email: this.dentist }
        });
        console.log('Appointments Response:', appointmentsResponse.data);

        // Pass the correct structure to combineEvents
        // The availability data is nested under 'availability', so we access that key.
        // The appointments data is an array, so we can pass it directly.
        this.events = this.combineEvents(availabilityResponse.data.availability, appointmentsResponse.data);
      } catch (error) {
        console.error('Error fetching events:', error);
        this.showErrorToUser('Failed to fetch events.');
      }
    },
    combineEvents(availability, appointments) {
      let events = [];

      // Convert availability and appointments to a comparable format (e.g., timestamps)
      let availableSlots = availability.map(slot => ({
        start: new Date(slot.start_time).getTime(),
        end: new Date(slot.end_time).getTime(),
        type: 'available'
      }));

      let bookedSlots = appointments.map(appointment => ({
        start: new Date(appointment.appointment_datetime).getTime(),
        end: new Date(appointment.appointment_datetime).getTime() + 30 * 60000, // assuming a 30-minute appointment
        type: 'booked'
      }));

      // Remove booked slots from available slots
      bookedSlots.forEach(booked => {
        availableSlots = availableSlots.reduce((slots, available) => {
          // If the booked slot is within the available slot
          if (booked.start >= available.start && booked.end <= available.end) {
            // Split the available slot into two parts, before and after the booked slot
            if (booked.start > available.start) {
              slots.push({ start: available.start, end: booked.start, type: 'available' });
            }
            if (booked.end < available.end) {
              slots.push({ start: booked.end, end: available.end, type: 'available' });
            }
          } else {
            slots.push(available); // No overlap, keep the available slot as is
          }
          return slots;
        }, []);
      });

      // Combine the remaining available slots and booked slots into events
      events = [...availableSlots, ...bookedSlots].map(slot => ({
        start: new Date(slot.start),
        end: new Date(slot.end),
        title: slot.type === 'available' ? 'Available' : 'Booked',
        class: slot.type
      }));

      return events;
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
/* Example styles *//* Ensure these styles are scoped or correctly targeted to the vue-cal component */
.vuecal__event.available {
  background-color: #2df29dd4;
}

.vuecal__event.booked {
  background-color: #ff6961;
}


.vuecal--event.done {
  background-color: #cfcfcf;
}
</style>