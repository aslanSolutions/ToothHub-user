<template>
  <div class="booking-form">
    <div class="form-container">
      <!-- Title container -->
      <div class="title-container">
        <h2 class="form-title">Book <br> an Appointment</h2>
      </div>
      <!-- Form container -->
      <div class="form-box">
        <form @submit.prevent="submitForm" class="form-fields">
          <div class="field-container">
            <label for="appointment-date" class="form-label">Appointment Date:</label>
            <input type="date" id="appointment-date" v-model="appointmentDate" class="input-field" />
          </div>
          <div class="field-container">
            <label for="persons" class="form-label">Persons:</label>
            <input type="number" id="persons" v-model="persons" class="input-field" min="1" />
          </div>
          <div class="field-container">
            <label for="location" class="form-label">Location:</label>
            <select id="location" v-model="location" class="input-field">
              <!-- Options should be populated dynamically -->
              <option value="">Select your location</option>
            </select>
          </div>
          <button type="submit" class="submit-button">Book Now</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      appointmentDate: '',
      persons: 1,
      location: '',
    };
  },
  methods: {
    submitForm() {
      console.log('Form submitted:', this.appointmentDate, this.persons, this.location);
    },
  },
};
</script>

<style scoped>
.booking-form {
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 40px;
  border-color: #000000;
  padding: 2rem;
  margin: 2rem;
  background-image: url('../../../assets/iconsBackground.svg');
  background-repeat: repeat;
}

.form-container {
  display: flex;
  width: 100%;
}

.title-container {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: flex-start;
}

.form-title {
  margin: 0;
  color: #4987A1;
  font-size: 2rem;
  font-weight: bold;
}

.form-box {
  flex: 2;
  margin-left: 2rem;
}

.form-fields {
  display: flex;
  flex-direction: column;
}

.field-container {
  display: flex;
  flex-direction: column;
  margin-bottom: 1rem;
}

.form-label {
  margin-bottom: 0.5rem;
  color: #333;
  font-size: 1rem;
}

.input-field {
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
}

.submit-button {
  background-color: #007bff;
  color: white;
  padding: 1rem;
  border: none;
  border-radius: 4px;
  margin-top: 1rem;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s ease;
}

.submit-button:hover {
  background-color: #0056b3;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .form-container {
    flex-direction: column;
  }

  .title-container,
  .form-box {
    width: 100%;
    margin: 0;
  }

  .form-title {
    text-align: center;
  }

  .submit-button {
    width: 100%;
  }
}
</style>
