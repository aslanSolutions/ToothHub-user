<template>
  <div class="app">
    <Dsidebar />
    <router-view />
    <RightBar />
  </div>
  <div id="app" class="app">
    <router-view name="sidebar"></router-view>
    <router-view name="navbar"></router-view>
    <router-view/>
  </div>
</template>

<script setup>
import Dsidebar from './components/Dentist/Dashboard/Dsidebar.vue';
import RightBar from './components/Dentist/Dashboard/RightBar.vue';
</script>

<style lang="scss">


.app{
  display: flex;
  min-height: 100vh;
}

.content-wrapper {
  flex: 1;
}

/* Dsidebar styles */
.Dsidebar {
  flex: 0 0 300px;
  background: #4987A2;
  box-shadow: 0px 1px 1px rgba(0, 0, 0, 0.1);
  align-items: center;
  border-radius: .1rem;
  position: sticky;
  top: 0;
  overflow-y: auto;
}

.right-sidebar {
  background: rgba(28, 53, 64, 0.56);
  opacity: 0.7;
  box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.1);
  border-radius: .1rem;
  display: flex;
  flex-direction: column;

}

</style>
