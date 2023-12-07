<template>
  <div>
    <div class="button-container">
      <button @click="goToBook"><i class="fa fa-calendar"></i> Book</button>
      <button @click="goToLogin"><i class="fa fa-sign-in"></i> Login</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BookingButton',
  methods: {
    goToBook() {
      // Implement the logic to navigate to the booking page
      // For example, using Vue Router:
      this.$router.push('/book');
    },
    goToLogin() {
      // Implement the logic to navigate to the login page
      // For example, using Vue Router:
      this.$router.push('/login');
    },
  },
};
</script>

<style lang="scss" scoped>
.button-container {
  display: flex; /* Make the buttons appear next to each other */
  gap: 2rem;
}

button {
  display: flex;
  align-items: center;
  padding: 8px 16px;
  background-color: #4987A1;
  color: white;
  font-weight: 500;
  border: rgba(0, 0, 0, 0);
  border-radius: 5px;
  font-weight: 500;
  cursor: pointer;
  transition: 0.3s ease-in-out;

  i {
    margin-right: 8px;
    font-size: 16px;
  }

  &:hover {
    background-color: darken(#cad6db, 10%);
    color: #4987A1;
  }

  @media (max-width: 758px) {
    display: none;
  }
}
</style>
