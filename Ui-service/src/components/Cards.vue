<template>
  <div class="cards-h1">
    <h1 class="font-inter font-semibold text-3xl md:text-3xl leading-none md:leading-none tracking-tighter mb-5 text-cyan-800 dark:text-cyan-600 overflow-hidden">
          Report
        </h1>
  <div class="box-container">
    <div v-for="(square, index) in squares" :key="index" class="square" :style="{ ...(index === squares.length - 1 ? rectangle182Styles : {}) }">
      <div v-if="index === squares.length - 1" @click="addNewSquare" class="plus-sign">+</div>
    </div>
  </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      squares: JSON.parse(localStorage.getItem('squares')) || [0, 1, 2, 3],
    };
  },
  methods: {
    addNewSquare() {
      if (this.squares.length < 5) {
        this.squares.push(this.squares.length);

        localStorage.setItem('squares', JSON.stringify(this.squares));
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.box-container {
  display: flex;
  flex-direction: row;
  gap: 4rem;
}

.square {
  width: 10rem;
  height: 13rem;
  border-radius: 10px;
  background-color: #4987A1;
  position: relative;
}

.plus-sign {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 2rem;
  color: #46819A;
  cursor: pointer;
}

.square:last-child {
  box-sizing: border-box;
  background: #FFFFFF;
  border: 2px dashed #46819A;
  border-radius: 10px;
}
</style>
