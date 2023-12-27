<template>
    <div class="dentist-dashboard">
      <div class="Dsidebar">
      </div>
  
      <div class="flex-container">
        <div class="dentist-t">
          <h1 class="text-4xl md:text-4xl leading-24 md:leading-32 font-inter font-bold tracking-tighter text-cyan-800 dark:text-cyan-600">
            Appointments
          </h1>
          <p>{{ currentDate }}</p>
        </div>
  
        <div class="upcoming-appointments">
          <h2>Upcoming Appointments</h2>
          <div class="appointment-card" v-for="appointment in upcomingAppointments" :key="appointment._id">
            <p>{{ appointment.service }}</p>
            <p>{{ appointment.appointment_datetime }}</p>
            <p>{{ appointment.clinic }}</p>
            <p>{{ appointment.dentist_email }}</p>
            <p>Status: {{ appointment.status }}</p>
          </div>
        </div>
  
        <div class="history">
          <h2>Appointment History</h2>
          <div class="appointment-card" v-for="appointment in historyAppointments" :key="appointment._id">
            <p>{{ appointment.service }}</p>
            <p>{{ appointment.appointment_datetime }}</p>
            <p>{{ appointment.clinic }}</p>
            <p>{{ appointment.dentist_email }}</p>
            <p>Status: {{ appointment.status }}</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        currentDate: '',
        selectedDate: new Date(),
        upcomingAppointments: [],
        historyAppointments: [],
      };
    },
    mounted() {
      this.updateDate();
      setInterval(this.updateDate, 1000);
  
      // Mock data for testing
      this.upcomingAppointments = this.generateMockAppointments(5, 'pending');
      this.historyAppointments = this.generateMockAppointments(3, 'done');
    },
    methods: {
      updateDate() {
        const now = new Date();
        this.currentDate = now.toLocaleString();
      },
      updateSelectedDate(date) {
        this.selectedDate = date;
      },
      generateMockAppointments(count, status) {
        const mockAppointments = [];
        const currentDate = new Date();
  
        for (let i = 0; i < count; i++) {
          const appointment = {
            _id: i + 1,
            service: `Mock Service ${i + 1}`,
            appointment_datetime: new Date(currentDate.getTime() + i * 3600000).toLocaleString(),
            clinic: `Mock Clinic ${i + 1}`,
            dentist_email: `mock_dentist${i + 1}@example.com`,
            status,
          };
          mockAppointments.push(appointment);
        }
  
        return mockAppointments;
      },
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
  
  h2 {
    font-size: 24px;
    margin-bottom: 12px;
    color: #333;
  }
  
  p {
    margin: 8px 0;
  }
  
</style>
  
  