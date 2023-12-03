<template>
    <div>
      <div class="button-container">
        <button @click="goToBook"><i class="fa fa-calendar"></i>Book</button>
      </div>
    </div>
  </template>
  <script>
  export default {
    name: 'BookingButton',
    methods: {
    }
  }
  </script>
  <style lang="scss" scoped>
  .button-container {
    display: flex;
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
  