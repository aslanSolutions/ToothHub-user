<template>
  <div id="app">
    <!-- router-view will render the component based on the current route -->
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
html, body {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  height: 100%;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #f0f0f0; /* Set your desired background color here /
  min-height: 100vh; / Ensure it covers the full height of the viewport */
  box-sizing: border-box;
}
</style>