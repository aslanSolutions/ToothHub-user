<template>
  <div class="dentist-dashboard">
    <div class="Dsidebar">
    </div>

    <div class="flex-container">
      <div class="dentist-t">
        <h1
          class="text-4xl md:text-4xl leading-24 md:leading-32 font-inter font-bold tracking-tighter text-cyan-800 dark:text-cyan-600">
          Appointments
        </h1>
        <p>{{ currentDate }}</p>
      </div>

      <!-- Categorized Appointments Section -->
      <div class="categorized-appointments">
        <h2>Categorized Appointments</h2>
        <p>-----------------------------------------------------</p>
        <div class="upcoming-appointments">
          <h3 class="appointment-heading">Upcoming Appointments</h3>
          <div class="appointment-card" v-for="appointment in upcomingAppointments" :key="appointment._id">
            <p> Date: {{ appointment.appointment_datetime }}</p>
            <p> Clinic: {{ appointment.clinic }}</p>
            <p> Dentist: Dr. {{ appointment.dentistName }}</p>
            <p> Status: Upcoming</p>
            <button class="delete-button" @click="deleteAppointment(appointment._id)">🗑️</button>
          </div>

        </div>

        <div class="done-appointments">
          <h3 class="appointment-heading">Done Appointments</h3>
          <div class="appointment-card" v-for="appointment in doneAppointments" :key="appointment._id">
            <p> Date: {{ appointment.appointment_datetime }}</p>
            <p> Clinic: {{ appointment.clinic }}</p>
            <p> Dentist: Dr. {{ appointment.dentistName }}</p>
            <p> Status: Done</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script>
import axios from 'axios';
import { mapGetters } from 'vuex';

export default {
  data() {
    return {
      patientEmail: '',
      currentDate: '',
      upcomingAppointments: [],
      doneAppointments: [],
    };
  },
  computed: {
    ...mapGetters(['getEmail'])
  },
  mounted() {
    this.patientEmail = this.getEmail;
    this.updateDate();
    setInterval(this.updateDate, 1000);

    this.fetchAppointments();
  },
  methods: {
    updateDate() {
      const now = new Date();
      this.currentDate = now.toLocaleString();
    },
    async deleteAppointment(appointmentId) {
      try {
        const response = await axios.delete(`http://127.0.0.1:5002/appointments/${appointmentId}`);
        console.log('Delete Response:', response);
        if (response.status === 200) {
          this.upcomingAppointments = this.upcomingAppointments.filter(appointment => appointment._id !== appointmentId);
        } else {
          console.error('Error deleting appointment:', response.data.message);
        }
      } catch (error) {
        console.error('Error deleting appointment:', error);
      }
    },
    async fetchAppointments() {
      try {
        const response = await axios.get(`http://127.0.0.1:5002/appointments/get_by_email?patient_email=${this.patientEmail}`);
        const data = response.data;

        const currentDate = new Date();

        this.upcomingAppointments = await this.enhanceAppointments(data.filter(appointment =>
          new Date(appointment.appointment_datetime) >= currentDate
        ));

        this.doneAppointments = await this.enhanceAppointments(data.filter(appointment =>
          new Date(appointment.appointment_datetime) < currentDate
        ));
      } catch (error) {
        console.error('Error fetching appointments:', error);
      }
    },
    async enhanceAppointments(appointments) {
      const enhancedAppointments = [];
      for (const appointment of appointments) {
        const dentistEmail = appointment.dentist_email;
        const dentistName = await this.getDentistDetails(dentistEmail);
        enhancedAppointments.push({ ...appointment, dentistName });
      }
      return enhancedAppointments;
    },
    async getDentistDetails(dentistEmail) {
      try {
        const response = await axios.get(`http://127.0.0.1:5000/dentist/${dentistEmail}`);

        if ('name' in response.data) {
          const dentist = response.data.name;
          return dentist;
        } else {
          console.error('Error: Name property not found in the response data');
        }
      } catch (error) {
        console.error(`Error fetching dentist name for email ${dentistEmail}:`, error);
        return 'Unknown Dentist';
      }
    }
  },
};
</script>
  
<style lang="scss" scoped>
.flex-container {
  display: flex;
  flex-grow: 1;
  flex-direction: column;
  padding: 1rem;
}

.upcoming-appointments,
.history {
  margin-top: 20px;
}

.appointment-card {
  background-color: #fff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 16px;
  transition: transform 0.2s ease-in-out;
}

.appointment-card:hover {
  transform: translateY(-4px);
}

h2,
h3 {
  font-size: 24px;
  margin-bottom: 12px;
  color: #333;
}

.upcoming-appointments,
.done-appointments {
  margin-top: 20px;
}

p {
  margin: 8px 0;
}

.delete-button {
  background-color: transparent;
  border: none;
  cursor: pointer;
  font-size: 1.5rem;
  color: red;
}

.delete-button:hover {
  color: darkred;
}
</style>
  
  