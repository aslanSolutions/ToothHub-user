<template>
  <div id="app" class="app">
    <!-- Navbar always on top -->
    <router-view name="navbar" class="navbar"></router-view>
    
    <!-- Main content area with sidebar and the page content -->
    <div class="content-area">
      <!-- Sidebars -->
      <router-view name="Sidebar" class="sidebar"></router-view>

      <!-- Page content -->
      <div class="content-wrapper">
        <router-view></router-view>
      </div>
      <router-view name="Rightbar" class="right-sidebar"></router-view>
    </div>
    <router-view name="footer" class="footer"></router-view>
  </div>
</template>

<script setup>
</script>

<style lang="scss">
.app {
  display: flex;
  flex-direction: column;
  height: 110vh;
}

.content-area {
  display: flex;
  flex: 1;
}

.sidebar{
  flex: 0 0 300px;
  background: #4987A2;
  box-shadow: 0px 1px 1px rgba(0, 0, 0, 0.1);
  align-items: center;
  border-radius: .1rem;
  position: sticky;
  top: 0;
  overflow-y: auto;

}

.content-wrapper {
  flex: 1;
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