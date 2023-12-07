<template>
    <div class="time-picker">
        <div class="date-header">{{ selectedDateFormatted }}</div>
        <ul class="time-slots">
            <li v-for="timeSlot in timeSlots" :key="timeSlot.id" class="time-slot"
                :class="{ 'selected': selectedTimeSlot === timeSlot }" @click="selectTimeSlot(timeSlot)">
                <span class="dot"></span>
                {{ timeSlot.startTime }} - {{ timeSlot.endTime }}
            </li>
        </ul>
        <button class="cancel-btn">Cancel</button>
        <button class="apply-btn" @click="applySelection">Apply</button>
    </div>
</template>
  
<script>
export default {
    props: {
        selectedDate: Date
    },
    data() {
        return {
            timeSlots: [],
            selectedTimeSlot: null,
        };
    },
    watch: {
        selectedDate(newDate) {
            console.log('Received new selected date:', newDate);
            // Fetch and update timeSlots based on the selected date
            this.fetchTimeSlots(newDate);
        }
    },
    computed: {
        selectedDateFormatted() {
            // Format the selected date
            return this.selectedDate.toLocaleDateString(undefined, { year: 'numeric', month: 'long', day: 'numeric' });
        },
    },
    methods: {
        selectTimeSlot(timeSlot) {
            this.selectedTimeSlot = timeSlot;
        },
        applySelection() {
            console.log('Time slot selected:', this.selectedTimeSlot);
        },
    },
};
</script>
  
<style scoped>
.time-picker {
    background: #ffffff;
    border-radius: 8px;
    padding: 1rem;
    width: 200px;
}

.date-header {
    background: #00bcd4;
    color: #ffffff;
    text-align: center;
    padding: 0.5rem;
    border-radius: 6px;
    margin-bottom: 1rem;
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

.cancel-btn,
.apply-btn {
    width: calc(50% - 0.5rem);
    padding: 0.5rem;
    border: none;
    border-radius: 6px;
    margin-top: 1rem;
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
  