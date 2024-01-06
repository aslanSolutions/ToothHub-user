<template>
  <div class="message-box">
    <label for="name">Name:</label>
    <input type="text" required class="input-field" placeholder="Your Name" title="Name is required"/>
    <label for="name">Email:</label>
    <input type="email" required class="input-field" placeholder="Your Email" />
    <textarea required class="textarea" name="message" id="message" cols="30" rows="20"
      placeholder="Write your message..."></textarea>
    <button @click="submitForm">Send</button>
  </div>
</template>


<script>
export default {
  data() {
    return {
      name: '',
      email: '',
      message: ''
    };
  },
  methods: {
    submitForm() {
      if (!this.name || !this.email || !this.message) {
        alert('All fields are required');
        return;
      }
      console.log("Button pressed")
    }
  }
}
</script>

<style lang="scss" scoped>
.message-box {
  font-size: 14px;
  line-height: 20px;
  color: rgba(136, 135, 143, 1);
  margin-bottom: 100px;
  width:70%;
}

button {
  padding: 10px 20px;
  background: rgba(73, 135, 161, 1);
  border-radius: 10px;
  color: rgba(255, 255, 255, 1);
  border: none;
  cursor: pointer;
  width: 200px;
  height: 59px;
  margin-top: 30px;
}

button:hover {
  background: rgb(255, 162, 0);
}

.textarea {
  width: 90%;
  height: 70%;
  border-radius: 10px;
  font-size: inherit;
  outline-color: rgba(73, 135, 161, 1);
  padding: 10px;
  min-height: 100px;
  resize: vertical;
  max-height: 290px;
  min-height: 200px;
}

@media (max-width: 768px) {
  .message-box {
    font-size: 13px;
    line-height: 17px;
  }
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.input-field {
  width: 90%;
  padding: 10px;
  margin-bottom: 20px;
  border-radius: 10px;
  font-size: inherit;
  outline-color: rgba(73, 135, 161, 1);
  border: 1px solid rgb(118, 113, 113);
}
</style>
