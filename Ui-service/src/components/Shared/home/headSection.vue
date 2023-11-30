<!-- Header.vue -->
<template>
    <div class="header relative h-96 text-white">
      <div class="background-image absolute top-0 left-0 w-full h-full">
        <img class="w-full h-full" src="../../../assets/DentistImage.jpg" alt="Home Page Background" />
      </div>
  
      <div class="text-content absolute top-60 left-8">
        <div class="text-box p-4 rounded-md">
          <h1 class="text-5xl mb-4 text-white font-sans">
            Your Teeth <br> are in good hands
          </h1>
          <p class="text-lg text-white text-center">
            <span class="highlight">Duis aute irure dolor in reprehenderit <br> in voluptate velit</span>
          </p>
          <button class="learn-more-btn bg-learn-more text-white px-4 py-2 rounded-md">
            Learn More
          </button>
        </div>
      </div>
  
      <BookingForm class="booking-form" />
    </div>
  </template>
  
  <script>
  import BookingForm from './bookingForm.vue';
  
  export default {
    name: 'Header',
    components: {
      BookingForm,
    },
  };
  </script>
  
  <style scoped>
  .header {
    width: 100%;
    height: 100vh;
  }
  
  .background-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  
  .text-content {
    position: absolute;
    top: 60%;
    left: 8rem;
    transform: translateY(-50%);
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
  }
  
  .text-box {
  }
  
  .highlight {
    color: rgba(0, 0, 0, 0.6);
  }
  
  .learn-more-btn {
    margin-top: 2rem;
    background-color: #4987A1;
    color: white;
    cursor: pointer;
  }
  
  .booking-form {
    position: absolute;
    height: 20%;
    bottom: 0;
    right: 30%;
    width: 100%;
    background-color: white;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1rem;
    box-sizing: border-box;
  }
  </style>
  