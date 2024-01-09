<template>
  <div class="Dsidebar">
    <div class="text-container">
      <h1 class="custom-h1">
        <img src="../../../assets/Logo.png" alt="logo" class="logo" />
        <router-link class="link" active-class="active-class" :to="{ name: 'Home' }">TOOTHTALES</router-link>
      </h1>
      <p class="custom-p">Where Every Smile Has a Story.</p>
    </div>

    <div class="icon-container">
      <div class="icon">
        <img src="../../../assets/DashIcon.png" alt="Dashboard Icon" class="icon-img" />
        <router-link class="link" active-class="active-class" exact :to="{ name: 'Dentist-Dashboard' }">Dashboard</router-link>
      </div>

      <div class="icon">
        <img src="../../../assets/AppIcon1.png" alt="Appointments Icon" class="icon-img" />
        <router-link class="link" active-class="active-class" exact :to="{ name: 'DAppointments' }">Appointments</router-link>
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
  width: 300px;
  background: #4987A2;
  box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.3);
  align-items: center;
  position: sticky;
  top: 0;
  overflow-y: auto;
}

.text-container {
  display: flex;
  flex-direction: column;
  margin-left: .2rem;
}

.custom-h1 {
  display: flex;
  align-items: center;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 30px;
  line-height: 100px;
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
  font-weight: 300;
  font-size: 13px;
  text-align: center;
  color: #1e1e1e;
  text-shadow: 0px 1px 1px rgba(0, 0, 0, 0.15);
  margin-left: 1.5rem;
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
.icon:hover {
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 30px;
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
    width: 100%;
  }
}
</style>
