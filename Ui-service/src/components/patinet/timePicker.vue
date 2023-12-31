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
                    {{ timeSlot.start_time }} - {{ timeSlot.end_time }}
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
            console.log("Selected date:", this.selectedDate)
            const selectedDateStr = `${this.selectedDate.getFullYear()}-${(this.selectedDate.getMonth() + 1).toString().padStart(2, '0')}-${this.selectedDate.getDate().toString().padStart(2, '0')}`;
            const time24h = this.convertTo24Hour(this.selectedTimeSlot.start_time);

            const appointmentDateTime = `${selectedDateStr}T${time24h}`;
            const bookingPayload = {
                patient_email: this.patient,
                dentist_email: this.selectedDentistEmail,
                appointment_datetime: appointmentDateTime
            };
            console.log("Sent date:", bookingPayload)
            axios.post('http://localhost:5002/appointments/', bookingPayload, {
                headers: {
                    'Authorization': `Bearer ${this.authToken}`,
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    console.log('Appointment booked successfully:', response.data);
                })
                .catch(error => {
                    console.error('Error booking appointment:', error);
                    if (error.response) {
                        console.error('Server response:', error.response.data);
                    }
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
        }, fetchTimeSlots() {
            const formattedDate = this.formatDateToYYYYMMDD(this.selectedDate);
            const endpoint = `http://127.0.0.1:5004/availability/get_timeslots`;

            axios.get(endpoint, {
                params: {
                    date: formattedDate,
                    booked: false
                }
            })
                .then(response => {
                    if (response.data && response.data.available_slots) {
                        const availableSlots = JSON.parse(response.data.available_slots);
                        this.availabilities = availableSlots.map(slot => ({
                            dentist_email: slot.dentist_email,
                            date: formattedDate,
                            time_slots: slot.time_slots.map(timeSlot => ({
                                start_time: this.formatTimeToLocal(timeSlot.start_time),
                                end_time: this.formatTimeToLocal(timeSlot.end_time)
                            }))
                        }));
                    } else {
                        this.availabilities = [];
                    }
                })
                .catch(error => {
                    console.error('Error fetching time slots:', error);
                });
        }, convertTo24Hour(time12h) {
            const [time, modifier] = time12h.split(' ');
            let [hours, minutes] = time.split(':');
            if (hours === '12') {
                hours = '00';
            }
            if (modifier === 'PM') {
                hours = parseInt(hours, 10) + 12;
            }
            return `${hours}:${minutes}:00`;
        },
        formatTimeToLocal(dateTime) {
            if (!dateTime) return 'Invalid time';

            const time = new Date(dateTime + 'Z');

            const hours = time.getUTCHours();
            const minutes = time.getUTCMinutes();
            const hours12 = hours % 12 || 12;
            const suffix = hours < 12 ? 'AM' : 'PM';

            return `${hours12.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')} ${suffix}`;
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
        selectTimeSlot(timeSlot, dentistEmail) {
            this.selectedTimeSlot = timeSlot;
            this.selectedDentistEmail = dentistEmail;
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
    flex-direction: column;
    align-items: center;
}

.time-slot {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 10px;
    margin-bottom: 10px;
    width: 100%;
    max-width: 250px;
    height: 50px;
    background-color: #00bcd4;
    color: white;
    border-radius: 8px;
    box-sizing: border-box;
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