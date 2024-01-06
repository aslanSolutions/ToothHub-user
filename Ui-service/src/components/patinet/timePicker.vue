<template>
    <div class="time-picker">
        <div class="date-header">{{ selectedDateFormatted }}</div>
        <div v-if="availabilities.length > 0" class="dentists-container">
            <div v-for="(availability, index) in availabilities" :key="index" class="dentist-row">
                <div class="dentist-email">{{ availability.dentist_email }}</div>
                <div
  v-for="(timeSlot, timeIndex) in availability.time_slots"
  :key="`${availability.dentist_email}-${timeIndex}`"
  class="time-slot"
  :class="{ 
    'selected-locally': locallySelectedTimeSlot === timeSlot.id, 
    'selected-remotely': timeSlot.selected && locallySelectedTimeSlot !== timeSlot.id, 
    'booked': timeSlot.booked 
}"
  @click="!timeSlot.booked && selectTimeSlot(timeSlot, availability.dentist_email)"
>
  {{ formatTime(timeSlot.start_time) }}
</div>

            </div>
        </div>
        <div v-else class="no-availability-message">
            There are no available times, would you like to make a wishlist for an appointment?
            <div class="wishlist-buttons">
                <button class="add-wishlist-btn" @click="addToWishlist">Add to Wishlist</button>
                <button class="cancel-btn" @click="cancelWishlist">Cancel</button>
            </div>
        </div>
        <div v-if="selectedTimeSlot" class="buttons-container">
            <button class="cancel-btn" @click="cancelSelection">Cancel</button>
            <button class="apply-btn" @click="applySelection">Apply</button>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { mapGetters } from 'vuex';
import { DateTime } from 'luxon';
import io from 'socket.io-client';



export default {
    props: {
        selectedDate: Date
    },
    data() {
        return {
            availabilities: [],
            selectedTimeSlot: null,
            selectedDentistEmail: '',
            patient: '',
            authToken: '',
            pendingConfirmation: false,
            countdownTimer: null,
            socket: null,
        };
    },
    watch: {
        selectedDate(newDate) {
            if (newDate) {
                this.fetchTimeSlots(newDate);
            }
        }
    },
    created() {
        this.fetchTimeSlots(this.selectedDate);
    },
    computed: {
        selectedDateFormatted() {
            if (this.selectedDate) {
                return this.selectedDate.toLocaleDateString(undefined, { year: 'numeric', month: 'long', day: 'numeric' });
            }
            return '';
        },
        ...mapGetters(['getEmail', 'getAccessToken'])
    },
    mounted() {
        this.patient = this.getEmail;
        this.authToken = this.getAccessToken
        this.socket = io('http://localhost:5002');
         // Listen for real-time updates
         this.socket.on('appointment_created', (data) => {
            console.log('Appointment update received:', data);
            this.fetchTimeSlots(this.selectedDate);
        });

        this.socket.on('time_slot_selected', (data) => {
    this.updateSelectedState(data.timeSlotId, true);
});


    },
    methods: {

     updateSelectedState(timeSlotId, isSelected) {
    console.log(`Updating time slot with ID ${timeSlotId} to selected state: ${isSelected}`);
    this.availabilities.forEach(availability => {
        availability.time_slots.forEach(slot => {
            console.log(`Checking slot with ID ${slot.id}`);
            if (slot.id === timeSlotId) {
                console.log(`Found matching slot. Updating selected state.`);
                slot.selected = isSelected;
            }
        });
    });
}

,
        applySelection() {
    if (!this.selectedTimeSlot || !this.selectedDentistEmail || !this.pendingConfirmation) {
        alert("Please select a time slot.");
        return;
    }
    this.verifyAndBookAppointment();
},

// New method to verify and book the appointment
verifyAndBookAppointment() {
    // Convert the selected time slot start time to UTC
    const startTimeUTC = DateTime.fromISO(this.selectedTimeSlot.start_time, { zone: 'utc' }).toISO();

    // API call to verify if the selected time slot is still available
    axios.get(`http://localhost:5004/availability/verify_slot`, {
        params: {
            dentist_email: this.selectedDentistEmail,
            start_time: startTimeUTC
        }
    }).then(response => {
        if (response.data.isAvailable) {
            this.finalizeBooking();
        } else {
            alert("Sorry, this time slot is no longer available.");
            // Reset UI state as necessary
            this.selectedTimeSlot = null;
            this.pendingConfirmation = false;
        }
    }).catch(error => {
        console.error('Error verifying time slot:', error);
        // Handle error
        this.selectedTimeSlot = null;
        this.pendingConfirmation = false;
    });
},


// Finalize the booking process after successful verification
finalizeBooking() {
  // Ensure a time slot is actually selected
  if (!this.selectedTimeSlot || !this.selectedDentistEmail) {
    alert("No time slot selected for booking.");
    return;
  }

  // Convert the selected time slot start time to UTC
  const startTimeUTC = DateTime.fromISO(this.selectedTimeSlot.start_time, { zone: 'utc' }).toISO();

  // Construct the payload for the booking
  const bookingPayload = {
    patient_email: this.patient,
    dentist_email: this.selectedDentistEmail,
    appointment_datetime: startTimeUTC
  };

  // Send the booking request to the server
  axios.post('http://localhost:5002/appointments/', bookingPayload, {
    headers: {
      'Authorization': `Bearer ${this.authToken}`,
      'Content-Type': 'application/json'
    }
  }).then(response => {
    // Handle successful booking
    console.log('Appointment booked successfully:', response.data);

    // Emit a socket event to notify about the booking confirmation
    this.socket.emit('confirm_booking', {
      timeSlotId: this.selectedTimeSlot.id, 
      dentistEmail: this.selectedDentistEmail
    });

    // Fetch the updated time slots to reflect the change in the UI
    this.fetchTimeSlots(this.selectedDate);

    // Reset the selected time slot and pending confirmation state
    this.selectedTimeSlot = null;
    this.pendingConfirmation = false;

  }).catch(error => {
    // Handle errors in booking
    console.error('Error booking appointment:', error);
    if (error.response) {
      console.error('Server response:', error.response.data);
    }
  });
}
,

fetchTimeSlots(date) {
    const formattedDate = this.formatDateToYYYYMMDD(date);
    axios.get(`http://localhost:5004/availability/get_timeslots?date=${formattedDate}`)
        .then(response => {
            console.log("Fetched time slots:", response.data);
            if (response.data && response.data.available_slots) {
                // Parse the stringified JSON to convert it into JavaScript objects
                const rawSlots = JSON.parse(response.data.available_slots);
                this.availabilities = this.create30MinIntervals(rawSlots);
            } else {
                this.availabilities = [];
            }
        })
        .catch(error => {
            console.error('Error fetching time slots:', error);
        });
},


        addToWishlist() {
            const payload = {
                patient_email: this.patient,
                date: this.formatDateToYYYYMMDD(this.selectedDate)
            };


            axios.post('http://localhost:5006/wishlist/create', payload, {
                headers: {
                    'Authorization': `Bearer ${this.authToken}`
                }
            })
                .then(response => {
                    console.log('Wishlist entry created:', response);
                })
                .catch(error => {
                    console.error('Error creating wishlist entry:', error);
                    if (error.response) {
                        console.error('Server response:', error.response.data);
                    }
                });
        },create30MinIntervals(rawSlots) {
    let intervalsByDentist = {};
    rawSlots.forEach((slot, slotIndex) => {
        const dentistEmail = slot.dentist_email;
        if (!intervalsByDentist[dentistEmail]) {
            intervalsByDentist[dentistEmail] = [];
        }

        slot.time_slots.forEach((timeSlot, timeSlotIndex) => {
            let startTime = DateTime.fromISO(timeSlot.start_time, { zone: 'utc' });
            const endTime = DateTime.fromISO(timeSlot.end_time, { zone: 'utc' });

            while (startTime < endTime) {
                let endTimeInterval = startTime.plus({ minutes: 30 });
                if (endTimeInterval > endTime) {
                    endTimeInterval = endTime;
                }

                // Generate a unique ID for each time slot
                const uniqueId = `${dentistEmail}-${slotIndex}-${timeSlotIndex}-${startTime.toISO()}`;

                intervalsByDentist[dentistEmail].push({
                    id: uniqueId,
                    start_time: startTime.toISO(),
                    end_time: endTimeInterval.toISO(),
                    booked: timeSlot.booked
                });

                startTime = endTimeInterval;
            }
        });
    });

    return Object.keys(intervalsByDentist).map(dentistEmail => {
        return {
            dentist_email: dentistEmail,
            time_slots: intervalsByDentist[dentistEmail]
        };
    });
},



        formatDateToYYYYMMDD(date) {
            const d = new Date(date);
            let month = '' + (d.getMonth() + 1);
            let day = '' + d.getDate();
            const year = d.getFullYear();

            if (month.length < 2)
                month = '0' + month;
            if (day.length < 2)
                day = '0' + day;

            return [year, month, day].join('-');
        },
        formatTime(dateTime) {
    const time = DateTime.fromISO(dateTime, { zone: 'utc' }).toLocal();
    return time.toLocaleString(DateTime.TIME_SIMPLE);
  },
  selectTimeSlot(timeSlot, dentistEmail) {
    // If the same time slot is clicked again, toggle the selection
    if (this.selectedTimeSlot === timeSlot.id) {
        this.resetLocalSelection();
        this.socket.emit('deselect_time_slot', {
            timeSlotId: timeSlot.id,
            dentistEmail: dentistEmail
        });
    } else {
        this.resetLocalSelection();
        this.locallySelectedTimeSlot = timeSlot.id; // Locally select the new time slot
        this.selectedTimeSlot = timeSlot.id; // This is for comparison in class binding
        this.socket.emit('select_time_slot', {
            timeSlotId: timeSlot.id,
            dentistEmail: dentistEmail
        });
    }
    this.pendingConfirmation = true;
    clearTimeout(this.countdownTimer);
    this.countdownTimer = setTimeout(() => {
        this.pendingConfirmation = false;
        this.selectedTimeSlot = null;
    }, 120000);
},

resetLocalSelection() {
    if (this.locallySelectedTimeSlot) {
        const localSlot = this.availabilities.flatMap(a => a.time_slots)
                             .find(slot => slot.id === this.locallySelectedTimeSlot);
        if (localSlot) {
            localSlot.selected = false; // Reset the local selection
        }
        this.locallySelectedTimeSlot = null; // Clear the local selection ID
    }
},



    cancelSelection() {
            console.log('Selection cancelled');
            this.selectedTimeSlot = null;
        }
    },
    beforeDestroy() {
        if (this.socket) {
            this.socket.disconnect();
        }
    }
};
</script>
  
<style scoped>
.time-picker {
    background: #ffffff;
    border-radius: 8px;
    padding: 1rem;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.date-header {
    background: #00bcd4;
    color: #ffffff;
    text-align: center;
    padding: 0.5rem;
    border-radius: 6px;
    margin-bottom: 1rem;
    align-self: stretch;
}

.time-slot.booked {
    background: #e0e0e0;
    cursor: not-allowed;
    display: none;
}

.time-slot.selected-remotely {
    background-color: grey; /* or any other styling you prefer */
    pointer-events: none;
}
.time-slot.selected-locally{
    background-color: rgb(3, 95, 120); /* or any other styling you prefer */
}
.no-availability-message {
    margin-top: 1rem;
    padding: 1rem;
    text-align: center;
    color: #757575;
}

.dentists-container {
    display: flex;
    flex-direction: column;
    width: 100%;
}

.dentist-row {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    margin-bottom: 1rem;
    width: 100%;
}

.dentist-email {
    font-weight: bold;
    margin-bottom: 0.5rem;
}

.time-slots-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;
}

.time-slot {
    background: #00bcd4;
    color: #ffffff;
    margin-bottom: 0.5rem;
    margin-right: 0.5rem;
    padding: 0.5rem;
    border-radius: 6px;
    cursor: pointer;
    flex: 1 1 auto;
    min-width: 100px;
    text-align: center;
}

.time-slot:nth-child(2n) {
    margin-right: 0;
}

.buttons-container {
    margin-top: auto;
    align-self: flex-end;
    display: flex;
    gap: 0.5rem;
}

.cancel-btn,
.apply-btn {
    padding: 0.5rem;
    border: none;
    border-radius: 6px;
}

.wishlist-buttons {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-top: 1rem;
}

.add-wishlist-btn {
    background: #4CAF50;
    color: #ffffff;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 6px;
    cursor: pointer;
}

.cancel-btn {
    background: #e0e0e0;
}

.apply-btn {
    background: #00bcd4;
    color: #ffffff;
}

.selected {
    background: #009688;
}
</style>  