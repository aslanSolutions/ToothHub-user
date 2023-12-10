<template>
    <div>
        <Calendar expanded show-weeknumbers="right" @dayclick="handleDayClick" />
    </div>
</template>
  
<script>
import { Calendar} from 'v-calendar';
import 'v-calendar/style.css';



export default {
    components: {
        Calendar
    },
    data() {
        return {
            date: new Date(),
        };
    },
    methods: {
        handleDayClick(day) {
            console.log('Day clicked:', day);
            this.$emit('date-selected', day.date);  // Emit JavaScript Date object
        }
    }
}
</script>