<template>
  <div class="container">
  <div class="registration-form">
    <div class="headline"><h1>TOOTHTALES</h1>
    <p>Where Every Smile Has A Story.</p>
   </div>
    <form @submit.prevent="submitForm">
      <div class="reg-form">
        <div class="input-group">
          <label for="fname">First Name</label>
          <input type="text" id="fname" name="fname" v-model="firstName">
        </div>
        <div class="input-group">
          <label for="lname">Last Name</label>
          <input type="text" id="lname" name="lname" v-model="lastName">
        </div>
        <div class="input-group">
          <label for="email">Email</label>
          <input type="text" id="email" name="email" v-model="email">
        </div>
        <div class="input-group">
          <label for="password">Password</label>
          <input type="password" id="password" name="password" v-model="password">
        </div>
        <div class="input-group">
          <label for="ConfirmPassword">Confirm Password</label>
          <input type="password" id="ConfirmPassword" name="ConfirmPassword" v-model="confirmPassword">
        </div>
 
      <div class="account-info">
        <p class="already">Already have an account?</p>
        <a href="/login" class="login">Login!</a>
      </div>
      <div class="create">
        <input type="submit" value="Create Account">
      </div></div>
    </form>
  </div></div>
</template>
<script>
import axios from 'axios';
 
export default {
  name: 'UserRegister',
  data() {
    return {
      firstName: '',
      lastName: '',
      email: '',
      password: '',
      confirmPassword: ''
    };
  },
  methods: {
    
  async submitForm() {
    try {
      const response = await axios.post('http://127.0.0.1:5000/auth/register', {
        first_name: this.firstName,
        last_name: this.lastName,
        email: this.email,
        password: this.password
      });
      console.log(response.data);
      // Handle success
      alert('Registration successful!'); // Replace with a more suitable success message or action
      // Example: Redirect to a login page or a success page
      // this.$router.push('/login');
    } catch (error) {
      console.error(error);

      if (!error.response) {
        // Network error or server unreachable
        alert('Unable to connect to the server. Please try again later.');
      } else {
        // Handle common HTTP errors
        switch (error.response.status) {
          case 400:
            alert('Invalid input. Please check your data and try again.');
            break;
          case 409:
            alert('This email is already in use. Please use a different email.');
            break;
          default:
            alert('An error occurred. Please try again.');
            break;
        }
      }
    }
  }
}

  }

</script>
<style scoped>
.container {
  display: flex;
  justify-content: flex-start; /* Adjust as needed */
  padding: 20px;
  height: 100vh; /* Adjust as needed */
  transform: translateX(35%);
}
 
.headline {
padding-bottom: 5%;
}
 
.headline p{
  padding-right: 5vh;
  padding-left: 5px;
}
 
h1{
  color:#4987A1 ;
  margin-bottom: 0; /* Removes the bottom margin from the h1 tag */
  padding-bottom: 0; /* Optional: Adjusts the bottom padding */
 
}
 
p{
  font-size: 11px;
  color: grey;
  margin-top: 0; /* Removes the top margin from the p tag */
  padding-top: 0; /* Optional: Adjusts the top padding */
}
.registration-form {
  padding-top: 5%;
}
 
.account-info {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  gap: 5px;
  margin-top: 5%;
}
 
.already {
  font-size: 12px;
  margin: 0;
}
 
.login {
  font-size: 12px;
  text-decoration: none;
  color: #4987A1;
  font-weight: bold;
}
 
.reg-form {
  margin: auto;
  width: 200%;/* Adjust this to control the width of the form */
}
 
.input-group {
  margin-bottom: 2vh;
}
 
.input-group label {
  display: block;
  text-align: left;
  margin-bottom: 0.5vh;
  font-size: 11px;
  color: grey;
}
 
.input-group input {
  width: 100%;
  height: 3.0vh;
  border: none;
  outline: none;
 
}
 
.create {
  text-align: center; /* Center the submit button */
  margin-top: 2vh; /* Space above the submit button */
  height: 2.5vh;
 
}
.create input{
  height: 3vh;
}
 
.create input[type="submit"] {
  width: 100%; /* Full width of its container */
  height: 3.3vh; 
  padding: 0; 
  background-color: #4987A1;
  color: white;
  border: none; /* Optional: Removes the border */
  cursor: pointer; /* Changes cursor to pointer on hover */
  border-radius: 5px;
}
 
.create input[type="submit"]:hover {
  background-color: #3b6d85; 
}
</style>
 
 
 
