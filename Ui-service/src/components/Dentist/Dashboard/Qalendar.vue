<template>
  <vue-cal id="cal" hide-view-selector hide-title-bar hide-weekends :time-from="8 * 60" :time-to="18 * 60" :time-step="30"
    :disable-views="['years', 'year']"
    :editable-events="{ title: false, drag: true, resize: true, delete: true, create: true }"
    :drag-to-create-threshold="0" @event-create="handleEventCreate" @event-drop="handleEventDrop"
    @event-resize="handleEventResize">
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
    timeFrom: {
      type: Number,
      default: 480 // Default start time (e.g., 8 AM if using minutes from midnight)
    },
    timeTo: {
      type: Number,
      default: 1020 // Default end time (e.g., 5 PM if using minutes from midnight)
    }
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
    handleEventCreate(event) {
      // Initial start and end times
      let startTime = event.start;
      let endTime = event.end;

      // Variables to store initial drag positions
      let startX;
      let startY;


      // Listen for drag events on the calendar
      const calendar = document.querySelector('#cal'); // Ensure correct selector
      this.dragging = false;
      calendar.addEventListener('mousedown', (e) => {
        startX = e.offsetX;
        startY = e.offsetY;
        this.dragging = true;
      });
      // Listen for mouse move events during dragging
      document.addEventListener('mousemove', (e) => {
        if (!this.dragging) return;

        const x = e.offsetX;
        const y = e.offsetY;

        // Update the event's start and end times based on drag positioning
        const currentTime = new Date();
        let newStartTime = new Date(startTime);
        let newEndTime = new Date(endTime);

        if (x < startX) {
          newStartTime.setHours(currentTime.getHours() - 1);
        } else if (x > startX + event.width) {
          newStartTime.setHours(currentTime.getHours() + 1);
        }

        if (y < startY) {
          newStartTime.setMinutes(currentTime.getMinutes() - 15);
          newStartTime.setSeconds(0);
        } else if (y > startY + event.height) {
          newStartTime.setMinutes(currentTime.getMinutes() + 15);
          newStartTime.setSeconds(0);
        }

        newEndTime.setMinutes(newStartTime.getMinutes() + event.duration);

        // Update the event object with the new times
        event.start = newStartTime.toISOString();
        event.end = newEndTime.toISOString();
      });

      // Listen for mouse up events to stop dragging
      document.addEventListener('mouseup', () => {
        this.dragging = false;

        // Convert the start and end times to ISO string
        const startDate = event.start.toISOString().split('T')[0];
        const startTime = event.start.toISOString();
        const endTime = event.end.toISOString();

        // Prepare the new time slot object
        const newTimeSlot = {
          time_slot_id: `slot_${Date.now()}`,
          start_time: startTime,
          end_time: endTime,
        };

        // Once dragging ends, send the updated event to backend
        this.setAvailability("dentistEmail",startDate, [newTimeSlot]);
      });
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

      // Convert the start and end to ISO strings
      const startTime = eventDetails.start.toISOString();
      const endTime = eventDetails.end.toISOString();

      // Create the time slot data
      const timeSlots = [
        {
          time_slot_id: '1', // You can generate a unique ID here
          start_time: startTime,
          end_time: endTime,
        },
      ];

      // Now, call setAvailability with the necessary data
      this.setAvailability('john@example.com', startTime.split('T')[0], timeSlots);
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