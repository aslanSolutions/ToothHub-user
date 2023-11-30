<template>
    <main class="home-page">
    <div class="container">
        <headSec />
    </div>
    </main>
</template>

<script>
    import headSec from '@/components/Shared/home/headSection.vue'

    export default {
        components: {headSec}
    }
</script>

<style scoped>
.home-page {
    padding: 0%;
}

.container {
    padding-top: 20px;
}
</style>