<template>
    <div class="flex-container">
      <div class="dentist-t">
        <h1 class="text-4xl md:text-4xl leading-24 md:leading-32 font-inter font-bold tracking-tighter text-cyan-800 dark:text-cyan-600">
          Edit Profile
        </h1>
        <p>{{ currentDate }}</p>
  
        <form @submit.prevent="submitForm" class="profile-form">
          <div class="form-group">
            <label for="name">Name:</label>
            <input type="text" id="name" v-model="formData.name" />
          </div>
  
          <div class="form-group">
            <label for="phoneNumber">Phone Number:</label>
            <input type="tel" id="phoneNumber" v-model="formData.phoneNumber" />
          </div>
  
          <div class="form-group">
            <label for="password">Password:</label>
            <input type="password" id="password" v-model="formData.password" />
          </div>
  
          <button type="submit">Save Changes</button>
        </form>
  
        <div v-if="message" :class="{ 'success-message': isSuccess, 'error-message': !isSuccess }">
          {{ message }}
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        currentDate: '',
        selectedDate: new Date(),
        formData: {
          name: '',
          phoneNumber: '',
          password: '',
        },
        message: null,
        isSuccess: false,
      };
    },
    mounted() {
      this.updateDate();
      setInterval(this.updateDate, 1000);
    },
    methods: {
      updateDate() {
        const now = new Date();
        this.currentDate = now.toLocaleString();
      },
      submitForm() {
        
        axios
          .patch('http://127.0.0.1:5001/patient', {
            id: 'user-id', // I need help getting the user ID
            data: this.formData,
          })
          .then(response => {
            this.isSuccess = true;
            this.message = 'Your information has been updated.';
            this.hideMessageAfterDelay();
            console.log(response)
          })
          .catch(error => {
            this.isSuccess = false;
            this.message = 'Could not update your information. Please try again later.';
            this.hideMessageAfterDelay();
            console.log(error)
          });
      },
      hideMessageAfterDelay() {
        setTimeout(() => {
          this.message = null;
        }, 2000);
      },
    },
  };
  </script>
  
  <style lang="scss" scoped>
  .dentist-t {
    max-width: 400px;
    margin: auto;
  }
  
  .profile-form {
    width: 100%;
    max-width: 400px;
    margin: auto;
  }
  
  .form-group {
    margin-bottom: 1rem;
  }
  
  label {
    display: block;
    margin-bottom: 0.5rem;
  }
  
  input {
    width: 100%;
    padding: 0.5rem;
    font-size: 1rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    margin-bottom: 0.5rem;
  }
  
  button {
    background-color: #3490dc;
    color: #fff;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
  }
  
  .success-message {
    background-color: #4caf50;
    color: white;
  }
  
  .error-message {
    background-color: #f44336;
    color: white;
  }
  
  div {
    padding: 1rem;
    margin-top: 1rem;
    border-radius: 4px;
    display: inline-block;
    width: 100%;
    box-sizing: border-box;
  }
  </style>
  