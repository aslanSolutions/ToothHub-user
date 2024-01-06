<!-- headSec.vue -->
<template>
  <div class="header-section">
    <!-- Background image -->
    <div class="background-overlay"></div>
    <img class="header-background" src="@/assets/DentistImage.jpg" alt="Dentist Background">

    <!-- Text Content -->
    <div class="header-content">
      <h1 class="header-title">Your teeth <br> are in good hands</h1>
      <p class="text-lg text-white text-center">
            <span class="highlight">Duis aute irure dolor in reprehenderit <br> in voluptate velit</span>
      </p>
      <button class="learn-more-button"><router-link class="link" active-class="active-class" :to="{ name: 'About' }">Learn more</router-link></button>
      
    </div>
  </div>
</template>

<style scoped>
.header-section {
  position: relative;
  width: 100%;
  height: 100vh;
}

.background-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.3); /* Dark overlay for better text readability */
  z-index: 1;
}

.header-background {
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 0;
}

.header-content {
  position: absolute;
  top: 50%;
  left: 10%;
  transform: translateY(-50%);
  z-index: 2;
  color: aliceblue;
}

.header-title {
  font-size: 3rem;
}

.highlight {
    color: rgba(0, 0, 0, 0.6);
  }

.learn-more-button {
  margin-top: 2rem;
  background-color: #4987A1; /* Or any other color you prefer */
  color: white;
  padding: 1rem 2rem;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
  font-size: 1rem;
}
</style>
