<template>
    <div class="text">
      <p>{{ text }}</p>
    </div>
</template>

<script>
export default {
  props: {
    text: {
      type: String,
      required: true
    }
  }
}
</script>

<style>
.text {
    font-family: 'Roboto';
    font-weight: 400;
    font-size: max(1.0vw, 17px);
    line-height: max(1.7vw, 23);
    color: rgb(90, 90, 90);
    width: 75%;
}

@media (max-width: 768px) {
  .text {
    font-size: min(7vw, 13);
    line-height: min(5vw, 17);
  }
}
</style>
