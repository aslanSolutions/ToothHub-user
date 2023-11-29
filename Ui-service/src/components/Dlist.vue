<template>
    <div>
        <div class="dentist-h1">
        <h1 class="font-inter font-semibold text-3xl md:text-3xl leading-none md:leading-none tracking-tighter mt-5 text-cyan-800 dark:text-cyan-600 overflow-hidden">
              Dentist
            </h1>
        </div>
        <div class="cylinder-like-square-container">
            <div class="cylinder-like-square"></div>
          </div>
    </div>
</template>

<script>

</script>

<style lang="scss">

.cylinder-like-square-container {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }

  .cylinder-like-square {
    box-sizing: border-box;
    width: 65rem;
    height: 5rem;
    background: rgba(191, 188, 188, 0.2);
    border: 1px solid #F2F2F2;
    box-shadow: 0px 3px 2px rgba(0, 0, 0, 0.1);
    border-radius: 30px;

    transform: rotateX(45deg);
    transform-origin: bottom;
    perspective: 1000px;
  }
</style>