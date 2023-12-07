<template>
    <div class="branding">
        <img src="../../../assets/Logo1.png" alt="logo">
    </div>
</template>

<script>
export default {
  name: 'Logo'
}
</script>

<style lang="scss" scoped>
.branding {
    position: relative;
    max-width: 300px;
    height: 100px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 5px 10px;
    margin-right: 20px;

    @media (max-width: 600px) {
        width: 100%;
    }

    img {
        width: 70%;
        transition: .5s ease all;
    }
}
</style>
