<template>
    <div class="time-picker">
        <div class="date-header">{{ selectedDateFormatted }}</div>
        <div v-if="availabilities.length > 0" class="dentists-container">
            <div v-for="availability in availabilities" :key="availability.dentist_email" class="dentist-row">
                <div class="dentist-email">{{ availability.dentist_email }}</div>
                <ul class="time-slots">
                    <li v-for="timeSlot in availability.time_slots" :key="timeSlot.time_slot_id" class="time-slot"
                        :class="{ 'selected': selectedTimeSlot === timeSlot }" @click="selectTimeSlot(timeSlot)">
                        <span class="dot"></span>
                        {{ formatTime(timeSlot.start_time) }}
                    </li>
                </ul>
            </div>
        </div>
        <div v-else class="no-availability-message">
            There are no available times, would you like to make a wishlist for an appointment?
        </div>
        <div v-if="selectedTimeSlot" class="buttons-container">
            <button class="cancel-btn" @click="cancelSelection">Cancel</button>
            <button class="apply-btn" @click="applySelection">Apply</button>
        </div>
    </div>
</template>
  
<script>
import axios from 'axios';

export default {
    props: {
        selectedDate: Date
    },
    data() {
        return {
            availabilities: [],
            selectedTimeSlot: null,
            selectedDentistEmail: '',
        };
    },
    watch: {
        selectedDate(newDate) {
            if (newDate) {
                console.log('Received new selected date:', newDate);
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
    },
    methods: {
        fetchTimeSlots(date) {
            const formattedDate = this.formatDateToYYYYMMDD(date);
            axios.get(`http://localhost:5004/availability/get_timeslots?date=${formattedDate}`)
                .then(response => {
                    if (response.data && response.data.available_slots) {
                        this.availabilities = JSON.parse(response.data.available_slots);
                    } else {
                        console.log('No time slots available for this date.');
                        this.availabilities = [];
                    }
                })
                .catch(error => {
                    console.error('Error fetching time slots:', error);
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
            return time.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        },
        selectTimeSlot(timeSlot, dentistEmail) {
            this.selectedTimeSlot = timeSlot;
            this.selectedDentistEmail = dentistEmail;
        },
        applySelection() {
            console.log('Time slot selected:', this.selectedTimeSlot);
            console.log(this.selectedDentistEmail)
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
    width: auto;
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
    flex-direction: row;
}

.dentist-row {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-right: 1rem;
}

.dentist-email {
    font-weight: bold;
    margin-bottom: 0.5rem;
}

.time-slots {
    list-style-type: none;
    padding: 0;
    margin: 0;
}

.time-slot {
    background: #00bcd4;
    color: #ffffff;
    margin-bottom: 0.5rem;
    padding: 0.5rem;
    border-radius: 6px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
}

.dot {
    height: 10px;
    width: 10px;
    background-color: #00e676;
    border-radius: 50%;
    display: inline-block;
    margin-right: 8px;
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