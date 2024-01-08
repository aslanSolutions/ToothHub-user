<template>
  <div class="right-sidebar">
    <div class="rightIcons-container">
      <div class="logOut" @click="logout">
        <div class="logout-container">
          <img src="../../../assets/Logout.png" alt="Logout Icon" class="icon-img" />
          <button class="logout-btn">Log Out</button>
        </div>
      </div>
    </div>
    <div class="Latest-Patient">
      <div class="latest-patient-heading">
        <h2>Latest Patient</h2>
      </div>
      <div class="view-patient-heading">
        <button class="view-all-btn" @click="viewAllPatients">View All</button>
      </div>
    </div>
    <div class="man-ellipse-container">
      <div class="man-ellipse">
        <div class="patient-info">
          <img src="../../../assets/man-image.png" alt="man Image" class="person-img" />
          <p class="person-text">Ian Conley</p>
        </div>
        <div class="patient-info">
          <img src="../../../assets/chelsea.png" alt="Chelsea Image" class="person-img" />
          <p class="person-text">Chelsea Bishop</p>
        </div>
        <div class="patient-info">
          <img src="../../../assets/Philip.png" alt="Philip Image" class="person-img" />
          <p class="person-text">Philip Griffin</p>
        </div>
      </div>
    </div>

    <div class="Patient-Information">
    </div>
  </div>
</template>


<script>
import { mapActions } from 'vuex';

export default {
  methods: {
    ...mapActions(['resetVuexState']),
    logout() {
      this.resetVuexState();
      this.$router.push('/');
    },
    viewAllPatients() {
      console.log("Viewing all patients...");
    },
  }
};
</script>

<style lang="scss" scoped>
.girl-img {
  width: 10rem;
}

.person-text {
  display: flex;
  flex-direction: row;
  color: white;
}

.right-sidebar {
  width: 30rem;
  background: rgba(28, 53, 64, 0.56);
  opacity: 0.7;
  box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.1);
  padding: 20px;
  box-sizing: border-box;
}

.logOut {
  display: flex;
  justify-content: space-between;
}

.logout-btn {
  font-family: 'Inter';
  font-weight: 500;
  color: #ffffff;
  background: none;
  border: none;
  cursor: pointer;
  transition: color 0.3s;
}

.logout-btn:hover {
  color: rgb(29, 107, 115);
}

.view-all-btn {
  font-family: 'Inter';
  font-weight: 500;
  color: #ffffff;
  background: none;
  border: none;
  cursor: pointer;
  transition: color 0.3s;
}

.view-all-btn:hover {
  color: rgb(29, 107, 115);
}

.icon-img {
  width: 24px;
  height: auto;
}

.girl-ellipse-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 8rem;
}

.girl-ellipse {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.person-img {
  width: 4rem;
  height: auto;
  border-radius: 70px;
}

.person-name {
  font-family: 'Inter';
  font-weight: 500;
  color: #ffffff;
  margin-top: 10px;
}

.Latest-Patient {
  font-family: 'Inter';
  font-weight: 500;
  font-size: 15px;
  color: #ffffff;
  display: flex;
  margin-top: 3rem;
  flex-direction: row;
  gap: 4rem;
}

.latest-patient-heading {
  display: flex;
  flex: 1;
}

.view-patient-heading {
  display: flex;
  flex: 1;
  justify-content: flex-end;
}

.man-ellipse-container {
  display: flex;
  flex-direction: column;
  margin-top: 1rem;
}

.man-ellipse {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  align-items: start;
}

@media screen and (max-width: 768px) {
  .right-sidebar {
    width: 80%;
  }

  .Latest-Patient {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .man-ellipse-container {
    margin-top: 2rem;
  }
}
</style>
