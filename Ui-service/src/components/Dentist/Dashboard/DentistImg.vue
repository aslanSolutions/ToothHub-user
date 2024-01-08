<template>
  <div class="dentist-img">
    <div class="overlay-container">
      <img src="../../../assets/doctor.png" alt="doctor">
      <div class="text-container">
        <h1
          class="text-4xl md:text-4xl leading-24 md:leading-35 font-inter font-semibold tracking-tighter text-stone-50	">
          Welcome, {{ dentistName }}
        </h1>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters } from 'vuex';
export default {
  data() {
    return {
      dentisEmail: '',
      dentistName: ''
    }
  },
  computed: {
    ...mapGetters(['getEmail'])
  },
  mounted() {
    this.getDentistDetails();
  },

  methods: {
    async getDentistDetails() {
      this.dentistEmail = this.getEmail;

      try {
        const response = await axios.get(`http://127.0.0.1:5000/dentist/${this.dentistEmail}`);

        if ('name' in response.data) {
          this.dentistName = response.data.name;
        } else {
          console.error('Error: Name property not found in the response data');
        }
      } catch (error) {
        console.error('Error getting dentist name:', error);
      }
    }
  }
}
</script>
<style lang="scss" scoped>
.text-container {
  position: relative;
  transform: translate(5%, -350%);
  text-align: center;
  width: 100%;
}
</style>