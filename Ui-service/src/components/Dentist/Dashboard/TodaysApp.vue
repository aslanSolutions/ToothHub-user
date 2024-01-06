<template>
  <div class="dentist-t">
    <h1
      class="text-3xl md:text-3xl leading-24 md:leading-32 font-inter font-semibold tracking-tighter text-cyan-800 dark:text-cyan-600">
      Today’s Appointments
    </h1>

    <div class="group">
      <div class="square-container">
        <div class="square" v-for="(appointment, index) in appointments" :key="index">
          <div class="flex-container">
            <div class="ellipse" :style="{ backgroundImage: 'url(' + appointment.patient_image + ')' }"></div>

            <div class="flex-item text-info-container">
              <div class="text-info">
                <!-- Bind appointment details dynamically -->
                <div class="name">{{ appointment.patient_name }}</div>
                <div class="email">{{ appointment.patient_email }}</div>
                <div class="time">{{ appointment.appointment_time }}</div>
                <div class="dental-implant">{{ appointment.treatment_type }}</div>
              </div>
            </div>
          </div>

          <div class="button-container">
            <button class="view-details-btn">View Details</button>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>


<script>
import { mapGetters } from 'vuex';
import axios from 'axios';

export default {
  computed: {
    ...mapGetters(['getEmail'])
  },
  data() {
    return {
      dentist: '',
      appointments: []
    };
  },
  async mounted() {
    this.dentist = this.getEmail;

    try {
      const response = await axios.get('http://127.0.0.1:5002/appointments/get_by_date/', {
        params: { dentist_email: this.dentist, date: new Date().toISOString().split('T')[0] }
      });
      this.appointments = response.data;
      console.log("Data sent: ", response.data)
    } catch (error) {
      console.error('Error fetching appointments:', error);
    }
  }
}
</script>

<style lang="scss">
.square-container {
  display: flex;
  flex-direction: row;
  margin: 1rem;
  gap: 10rem;
}

.flex-container {
  display: flex;
  flex-direction: row;
}

.appointments {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 600;
  font-size: 20px;
  line-height: 61px;
  color: #4987A1;
  width: 100%;
  text-align: end;
  margin-right: 30rem;
}

.view-details-btn {
  width: 18rem;
  background-color: #4987a1;
  border-radius: 1.5rem;
  color: #fff;
  margin-top: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.view-details-btn:hover {
  background-color: #346e8a;
}

.square {
  width: 18rem;
  height: auto;
  border: 0.5px solid rgba(163, 163, 163, 0.05);
  border-radius: 1.5rem;
  margin-right: 1rem;
}

.ellipse {
  width: 100px;
  height: 100px;
  border-radius: 78px;
  background: url('~@/assets/Guy.png') center/cover;
}

.flex-item {
  margin-top: 0.5rem;
}

.name,
.email,
.time,
.view-details-btn,
.dental-implant {
  font-family: 'Inter';
  font-style: normal;
}

.view-details-btn {
  font-weight: 700;
}

.name {
  font-weight: 600;
  font-size: 15px;
  line-height: 24px;
  color: #000000;
}

.email {
  font-weight: 400;
  font-size: 10px;
  line-height: 14px;
  color: #B7B7B7;
}

.time {
  font-weight: 400;
  font-size: 15px;
  line-height: 24px;
  color: #B7B7B7;
}

.dental-implant {
  font-weight: 600;
  font-size: 15px;
  line-height: 24px;
  color: #B7B7B7;
}
</style>
