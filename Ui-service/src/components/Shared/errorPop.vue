<template>
    <div v-if="showPopup" class="error-popup">
        <div class="popup-content">
            <p>{{ errorMessage }}</p>
            <button class="close-icon" @click="closePopup">×</button>
        </div>
    </div>
</template>
  
<script>
export default {
  props: {
    errorMessage: String,
    showPopup: Boolean,
  },
  methods: {
    closePopup() {
      this.$emit('closePopup');
    },
  },
};
</script>

<style scoped>
.error-popup {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  padding: 40px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  z-index: 999;
}

.popup-content {
  text-align: center;
  font-size: 18px;
}

.close-icon {
  position: absolute;
  top: 3px;
  right: 10px;
  background: none;
  border: none;
  font-size: 24px;
  color: #00000098;
  cursor: pointer;
  transition: color 0.3s;
}

.close-icon:hover {
  color: grey;
}
</style>