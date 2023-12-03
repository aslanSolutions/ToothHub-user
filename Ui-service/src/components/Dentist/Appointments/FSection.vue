<template>
    <div class="main-container">
      <div class="ellipse-container">
        <div v-for="index in 3" :key="index" class="ellipse">
          <div class="appointment-container">
            <img
              src="../../../assets/AppIcon.png"
              alt="AppIcon Image"
              class="app-icon-img"
            />
          </div>
        </div>
      </div>

    </div>
  </template>
  
  <script>


  </script>
  
  <style lang="scss" scoped>
  .main-container {
    width: 98%;
    max-width: 100%;
    height: 12em;
    display: flex;
    align-items: center;
    margin: 3em auto 0;
    background: #ffffff;
    box-shadow: 0px 5px 2px rgba(0, 0, 0, 0.01);
    border-radius: 5px;
  }
  
  .ellipse-container {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 18.8rem;
    margin-left: .5rem;
  }
  
  .ellipse {
    width: 10rem;
    height: 10rem;
    background: #4987a1;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.05);
    border-radius: 50%;
    margin-right: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .app-icon-img {
    width: 50px;
  }
  
  .appointment-text-container {

  }
  
  .appointments-text {
    font-family: 'Inter';
    font-size: 10px;
    color: rgb(0, 0, 0);
    font-weight: 600;
  }
  </style>
  