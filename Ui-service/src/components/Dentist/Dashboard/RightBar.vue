<template>
  <div class="right-sidebar">
    <div class="user-info">
      <p>User: John Doe</p>
      <p>Email: john.doe@example.com</p>
    </div>
    <button @click="logout" class="logout-button">Logout</button>
    <div class="latest-activity">
      <h2>Latest Activity</h2>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    logout() {
    },
  },
};
</script>

<style lang="scss">
.right-sidebar {
  width: 20rem;
  background: rgba(28, 53, 64, 0.56);
  opacity: 0.7;
  box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.1);
  padding: 20px;
  box-sizing: border-box;
}

.user-info {
  margin-bottom: 20px;
  p {
    margin: 0;
    color: #ffffff;
  }
}

.logout-button {
  background-color: #ffffff;
  color: #000000;
  border: none;
  padding: 10px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  margin-bottom: 20px;
}

.latest-activity {
  h2 {
    color: #ffffff;
    font-size: 18px;
  }
}

@media screen and (max-width: 768px) {
  .right-sidebar {
    width: 80%;
  }
}
</style>
