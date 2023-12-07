<template>
  <div class="Appointment-Container">
        <h1 class="text-4xl md:text-4xl leading-24 md:leading-32 font-inter font-bold tracking-tighter text-cyan-800 dark:text-cyan-600">
            Appointments
          </h1>
          <FSection />
        </div>
</template>

<script>

import FSection from '../../components/Dentist/Appointments/FSection.vue'

export default {

    components: {
        FSection,


    }

}
</script>

<style lang="scss" scoped>

.Appointment-Container{

    display: flex;
    flex-grow: 1;
    flex-direction: column;
}

</style>