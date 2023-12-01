<template>
  <div class="Dsidebar">
    <div class="text-container">
      <h1 class="custom-h1">
        <img src="../../../assets/Logo.png" alt="logo" class="logo" />
        TOOTHTALES
      </h1>
      <p class="custom-p">Where Every Smile Has a Story.</p>
    </div>

    <div class="icon-container">
      <div class="icon">
        <img src="../../../assets/DashIcon.png" alt="Dashboard Icon" class="icon-img" />
        <h1 class="icon-text">Dashboard</h1>
      </div>

      <div class="icon">
        <img src="../../../assets/AppIcon.png" alt="Appointments Icon" class="icon-img" />
        <h1 class="icon-text">Appointments</h1>
      </div>

      <div class="icon">
        <img src="../../../assets/SetIcon.png" alt="Settings Icon" class="icon-img" />
        <h1 class="icon-text">Settings</h1>
      </div>
    </div>
  </div>
</template>

<script>
export default {
};
</script>

<style lang="scss">
.Dsidebar {
  width: 300px;  // Set a fixed width
  background: #4987A2;
  box-shadow: 0px 1px 1px rgba(0, 0, 0, 0.1);
  align-items: center;
  position: sticky;
  top: 0;
  overflow-y: auto;
}

.text-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 4rem;
  margin-left: 1%;
}

.custom-h1 {
  display: flex;
  align-items: center;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 34px;
  line-height: 102px;
  color: #FFFFFF;
  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  margin-bottom: -2rem;
}

.logo {
  max-width: 15%;
  height: auto;
  margin-right: 1rem;
}

.custom-p {
  font-family: 'Inter';
  font-style: light;
  font-weight: 100;
  font-size: 15px;
  text-align: center;
  color: #000000;
  text-shadow: 0px 1px 1px rgba(0, 0, 0, 0.25);
  margin-left: 2.5rem;
}

.icon-container {
  display: flex;
  flex-direction: column;
  margin-top: 5rem;
  gap: 5rem;
}

.icon {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-bottom: 1rem;
  margin-left: 1rem;
  gap: 1.5rem;
  transition: background-color 0.3s ease;
}

.icon-img {
  max-width: 30px;
  height: auto;
}

.icon-text {
  font-family: 'Inter';
  font-style: medium;
  font-weight: 500;
  font-size: 20px;
  color: #FFFFFF;
}

@media screen and (max-width: 768px) {
  .Dsidebar {
    width: 100%;  // Make it full width in responsive mode
  }
}
</style>
