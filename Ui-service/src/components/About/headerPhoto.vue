<template>
    <div class="header-photo">
      <img src="@/assets/about.png" alt="Image of a man cutting a client hair" />
    </div>
</template>

<script>
const screenWidth = window.innerWidth
document.documentElement.style.setProperty('--screen-width', `${screenWidth}px`)

</script>

<style scoped>
.header-photo img {
    max-width: 100%;
    min-width: 400px;
    height: auto;
    width: auto\9;
}
</style>
