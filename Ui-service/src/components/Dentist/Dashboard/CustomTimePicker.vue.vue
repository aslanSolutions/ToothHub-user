<template>
    <div class="time-picker">
        <VueTimepicker v-model="selectedTime" />
        <button @click="confirmTime">Set Availability</button>
    </div>
</template>
  
<script>
import VueTimepicker from 'vue-timepicker';

export default {
    components: {
        VueTimepicker,
    },
    data() {
        return {
            selectedTime: '',
        };
    },
    methods: {
        confirmTime() {
            this.$emit('time-selected', this.selectedTime);
        },
    },
};
</script>
  