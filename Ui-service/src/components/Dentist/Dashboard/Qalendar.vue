<template>
  <vue-cal ref="calendar" id="cal" hide-view-selector hide-title-bar hide-weekends :time-from="8 * 60" :time-to="18 * 60"
    :time-step="30" :disable-views="['years', 'year']"
    :editable-events="{ title: false, drag: true, resize: true, delete: true, create: true }"
    :drag-to-create-threshold="0" @event-drop="handleEventDrop" @event-resize="handleEventResize" @event-drag="handleCellClick">
    ></vue-cal>
</template>

<script>
import VueCal from 'vue-cal';
import 'vue-cal/dist/vuecal.css';
import axios from 'axios';

export default {
  name: 'Calendar',
  components: {
    VueCal
  },
  props: {
  },
  data() {
    return {
      events: [],
      selectedTimeSlots: []
    };
  },
  methods: {
    showErrorToUser(message) {
      // Display the error message to the user using an alert or another UI element
      alert(message);
    },
    // Called when an existing event is dropped after dragging
    handleEventDrop({ event, newStart, newEnd }) {
      // Prompt for confirmation before updating the event
      if (confirm('Are you sure you want to move this appointment?')) {
        // Here you would call the backend to update the event's times
        this.updateAvailability(event._id, newStart, newEnd);
      } else {
        // If the user cancels, revert the event back to its original position
        this.fetchEvents(); // Assuming fetchEvents refreshes the events from the backend
      }
    },
    // Called when an event is resized
    handleEventResize({ event, newStart, newEnd }) {
      // Prompt for confirmation before updating the event
      if (confirm('Confirm the new time slot?')) {
        // Call the backend to update the event's duration
        this.updateAvailability(event._id, newStart, newEnd);
      } else {
        // Revert the changes if the user cancels
        this.fetchEvents();
      }
    },
    handleEventClick() {
      // Event click logic
    },
    async setAvailability(dentistEmail, date, timeSlots) {
      if (!date) {
        console.error('Date is undefined');
        this.showErrorToUser('Date is required to set availability.');
        return;
      }

      const formattedDate = new Date(date).toISOString().split('T')[0];
      const formattedTimeSlots = timeSlots.map((slot, index) => ({
        time_slot_id: `slot_${index}`,
        start_time: new Date(slot.start_time).toISOString(),
        end_time: new Date(slot.end_time).toISOString(),
      }));

      // Log the payload for debugging
      console.log('Sending availability data:', { dentist_email: dentistEmail, date: formattedDate, time_slots: formattedTimeSlots });

      try {
        const response = await axios.post('http://127.0.0.1:5004/availability/set_availability', {
          dentist_email: dentistEmail,
          date: date,
          time_slots: timeSlots
        });

        console.log(response)

        // Rest of the success handling...
      } catch (error) {
        console.error('Error setting availability:', error.response ? error.response.data : error);
        if (error.response && error.response.data) {
          // If the backend provides error details, log them or display them to the user
          this.showErrorToUser(`Failed to set availability: ${error.response.data.detail || 'Unknown error'}`);
        } else {
          this.showErrorToUser('Failed to set availability. Please try again.');
        }
      }
    },
    async updateAvailability(eventId, newStart, newEnd) {
      try {
        const response = await axios.put(`/availability/update_timeslot/${eventId}`, {
          start_time: newStart,
          end_time: newEnd
        });
        if (response.data.success) {
          // Optionally, refresh the events here or handle the UI update
          this.fetchEvents();
        }
      } catch (error) {
        console.error('Error updating availability:', error.response ? error.response.data.message : error);
        // Optionally, revert the changes in the UI or inform the user of the error
        this.fetchEvents();
      }
    },
    handleCellClick(eventDetails) {
      // Check if eventDetails contains valid properties
      if (!eventDetails || !eventDetails.start || !eventDetails.end) {
        console.error('Invalid event data:', eventDetails);
        // Handle the invalid data appropriately, e.g., show an error message
        return;
      }
      console.log("Test")
      // Convert the start and end to ISO strings
      const startTime = eventDetails.start.toISOString();
      const endTime = eventDetails.end.toISOString();

      // Create the time slot data
      const timeSlot = {
        time_slot_id: `slot_${Date.now()}`, // You can generate a unique ID here
        start_time: startTime,
        end_time: endTime,
      };

      // Now, call setAvailability with the necessary data
      this.setAvailability('dentistEmail', startTime.split('T')[0], [timeSlot]);
    },
    fetchEvents() {
      // Fetching logic
    }
  },
  mounted() {
    this.fetchEvents();
  }
};
</script>

<style scoped>
/* Example styles */
.vuecal--event.available {
  background-color: #9fcd9f;
}

.vuecal--event.booked {
  background-color: #9fcdff;
}

.vuecal--event.done {
  background-color: #cfcfcf;
}
</style>