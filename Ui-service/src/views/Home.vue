<template>
    <main class="home-page">
        <headSec />
        <servicePhoto />
        <dentistMap />
        <whoAreWeSec />
    </main>
</template>

<script>
    import headSec from '@/components/Shared/home/headSection.vue'
    import servicePhoto from '@/components/Shared/home/servicePhoto.vue'
    import whoAreWeSec from '@/components/Shared/home/whoAreWeSec.vue'
    import dentistMap from '@/components/Shared/map.vue'

    export default {
        components: {
            headSec,
            servicePhoto,
            dentistMap,
            whoAreWeSec
        }
    }
</script>

<style>
.home-page {
    background-color: rgb(255, 255, 255);
}

</style>