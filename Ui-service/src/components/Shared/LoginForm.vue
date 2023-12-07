<template>
    <div class="container">
        <div class="login-form">
            <div class="headline">
                <h1>TOOTHTALES</h1>
                <p>Where Every Smile Has A Story.</p>
                <p class="your-acc">Login to Your Account</p>
            </div>

            <div class="account-info">

                <p class="already">Don't have an account yet?</p>
                <a href="/register" class="signup">Sign up now!</a>
            </div>
            <div class="l-form">
                <form @submit.prevent="submitForm">
                    <div class="input-group">
                        <label for="email">Email</label>
                        <input type="email" id="email" name="email" v-model="email" required>
                    </div>
                    <div class="input-group">
                        <label for="password">Password</label>
                        <input type="password" id="password" name="password" v-model="password" required>
                    </div>
                    <div class="remember-me">
                        <input type="checkbox" id="rememberMe" name="rememberMe">
                        <label for="rememberMe">Remember Me</label>
                    </div>
                    <div class="create">
                        <input type="submit" value="Login">
                    </div>

                </form>
            </div>
        </div>
    </div>
</template>
   
<script>
import axios from 'axios';

export default {
    name: 'UserLogin',
    data() {
        return {
            email: '',
            password: ''
        };
    },
    methods: {
        async submitForm() {
            try {
                const response = await axios.post('http://127.0.0.1:5005/auth/login', {
                    email: this.email,
                    password: this.password
                });
                console.log(response.data);
                // Handle success (e.g., redirect or show a success message)
            } catch (error) {
                console.error(error);
                // Handle error (e.g., show error message)
            }
        }
    }
}
</script>
<style scoped>
.container {
    display: flex;
    justify-content: flex-start;
    /* Adjust as needed */
    padding: 20px;
    height: 100vh;
    /* Adjust as needed */
    margin-top: 5rem;
    transform: translateX(35%);

}

.headline {
    padding-bottom: 5%;
}

.headline p {
    padding-right: 5vh;
    padding-left: 5px;
}

.login-form {
    padding-top: 5%;
}

h1 {
    color: #4987A1;
    margin-bottom: 0;
    /* Removes the bottom margin from the h1 tag */
    padding-bottom: 0;
    /* Optional: Adjusts the bottom padding */

}

p {
    font-size: 11px;
    color: grey;
    margin-top: 0;
    /* Removes the top margin from the p tag */
    padding-top: 0;
    /* Optional: Adjusts the top padding */
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

.l-form {

    margin: auto;
    width: 185%;
}

.signup {
    font-size: 12px;
    text-decoration: none;
    color: #4987A1;
    font-weight: bold;
}



.already,
.signup {
    font-size: 12px;
    text-decoration: none;
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
    margin-bottom: 2vh;

}

.create {
    text-align: center;
    /* Center the submit button */
    margin-top: 2vh;
    /* Space above the submit button */
    height: 2.5vh;

}

.create input {
    height: 3vh;
}

.create input[type="submit"] {
    width: 100%;
    /* Full width of its container */
    height: 3.3vh;
    padding: 0;
    background-color: #4987A1;
    color: white;
    border: none;
    /* Optional: Removes the border */
    cursor: pointer;
    /* Changes cursor to pointer on hover */
    border-radius: 5px;
}

.create input[type="submit"]:hover {
    background-color: #3b6d85;
}

.your-acc {
    padding-bottom: 10px;
    color: #4987A1;
    font-size: 16px;
    margin-bottom: 0;
    font-weight: bold;
}

.remember-me {
    display: flex;
    align-items: center;
    /* Vertically centers the checkbox and label */
    margin-bottom: 2vh;
    /* Adjust as needed */
    color: grey;
    font-size: 10px;
}

.remember-me input[type="checkbox"] {
    margin-right: 5px;
    /* Space between checkbox and label */
    outline: none;
    border: none;
}</style>