<!-- BookingForm.vue -->
<template>
  <div class="booking-form">
    <div class="form-box p-4 rounded-md">
      <h2 class="text-2xl mb-4">Book an Appointment</h2>
      <form @submit.prevent="submitForm">
        <div class="flex mb-4">
          <label for="name" class="flex-none pr-2">Name:</label>
          <input type="text" id="name" v-model="name" class="input-field flex-grow" />
        </div>
        <div class="flex mb-4">
          <label for="email" class="flex-none pr-2">Email:</label>
          <input type="email" id="email" v-model="email" class="input-field flex-grow" />
        </div>
        <div class="flex mb-4">
          <label for="message" class="flex-none pr-2">Message:</label>
          <textarea id="message" v-model="message" class="input-field flex-grow"></textarea>
        </div>
        <button type="submit" class="bg-learn-more text-white px-4 py-2 rounded-md">
          Book
        </button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      email: '',
      message: '',
    };
  },
  methods: {
    submitForm() {
      console.log('Form submitted:', this.name, this.email, this.message);
    },
  },
};
</script>

<style scoped>
.booking-form {
  background-color: rgba(255, 255, 255, 0.9);
  width: 100%;
  max-width: 30rem;
  margin: 0 auto;
}

.input-field {
  width: 100%;
  padding: 0.5rem;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 0.25rem;
}

/* Flex utility classes for horizontal layout */
.flex {
  display: flex;
  align-items: center;
}

.flex-none {
  flex: none;
}
.flex-grow {
  flex-grow: 1;
}
</style>
