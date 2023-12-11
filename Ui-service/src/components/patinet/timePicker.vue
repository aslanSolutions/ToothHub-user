<template>
    <div class="time-picker">
        <div class="date-header">{{ selectedDateFormatted }}</div>
        <div v-if="availabilities.length > 0" class="dentists-container">
            <div v-for="(availability, index) in availabilities" :key="index" class="dentist-row">
                <div class="dentist-email">{{ availability.dentist_email }}</div>
                <div v-for="(timeSlot, timeIndex) in availability.time_slots"
                    :key="`${availability.dentist_email}-${timeIndex}`" class="time-slot"
                    :class="{ 'selected': selectedTimeSlot === timeSlot }"
                    @click="selectTimeSlot(timeSlot, availability.dentist_email)">
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
            authToken: ''
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
    },
    methods: {
        applySelection() {
            if (!this.selectedTimeSlot || !this.selectedDentistEmail) {
                alert("Please select a time slot.");
                return;
            }

            const bookingPayload = {
                patient_email: this.patient,
                dentist_email: this.selectedDentistEmail,
                appointment_datetime: this.selectedTimeSlot.start_time
            };

            axios.post('http://localhost:5002/appointments/', bookingPayload, {
                headers: {
                    'Authorization': `Bearer ${this.authToken}`,
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    console.log('Appointment booked successfully:', response.data);
                    // You can also handle UI updates here
                })
                .catch(error => {
                    console.error('Error booking appointment:', error);
                    if (error.response) {
                        console.error('Server response:', error.response.data);
                    }
                });
        },
        fetchTimeSlots(date) {
            const formattedDate = this.formatDateToYYYYMMDD(date);
            axios.get(`http://localhost:5004/availability/get_timeslots?date=${formattedDate}`)
                .then(response => {
                    if (response.data && response.data.available_slots) {
                        const rawSlots = JSON.parse(response.data.available_slots);
                        // Process the raw slots into 30-minute intervals
                        this.availabilities = this.create30MinIntervals(rawSlots);
                    } else {
                        console.log('No time slots available for this date.');
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
        },
        create30MinIntervals(rawSlots) {
            let intervalsByDentist = {};
            rawSlots.forEach(slot => {
                const dentistEmail = slot.dentist_email;
                if (!intervalsByDentist[dentistEmail]) {
                    intervalsByDentist[dentistEmail] = [];
                }

                slot.time_slots.forEach(timeSlot => {
                    let startTime = new Date(timeSlot.start_time);
                    const endTime = new Date(timeSlot.end_time);

                    while (startTime < endTime) {
                        let endTimeInterval = new Date(startTime.getTime() + 30 * 60000); // Add 30 minutes

                        if (endTimeInterval > endTime) {
                            endTimeInterval = endTime;
                        }

                        intervalsByDentist[dentistEmail].push({
                            start_time: startTime.toISOString(),
                            end_time: endTimeInterval.toISOString()
                        });

                        startTime = endTimeInterval;
                    }
                });
            });

            // Convert the intervalsByDentist object into an array of objects with dentist_email and time_slots array
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
            const time = new Date(dateTime);
            return time.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', timeZone: 'UTC' });
        },
        selectTimeSlot(timeSlot, dentistEmail) {
            this.selectedTimeSlot = timeSlot;
            this.selectedDentistEmail = dentistEmail;
            // ... rest of the method ...
        },
        cancelSelection() {
            console.log('Selection cancelled');
            this.selectedTimeSlot = null;
        }
    },
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