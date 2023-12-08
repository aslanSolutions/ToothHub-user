<template>
    <main class="home-page">>
        <headSec />
        <servicePhoto />
        <whoAreWeSec />
    </main>
</template>

<script>
    import headSec from '@/components/Shared/home/headSection.vue'
    import servicePhoto from '@/components/Shared/home/servicePhoto.vue'
    import whoAreWeSec from '@/components/Shared/home/whoAreWeSec.vue'

    export default {
        components: {
            headSec,
            servicePhoto,
            whoAreWeSec
        }
    }
</script>

<style scoped>
.home-page {
    padding: 1%;
    background-color: rgb(255, 255, 255);
}

</style>