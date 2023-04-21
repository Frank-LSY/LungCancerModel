<template>
  <div class="flex flex-wrap justify-center">
    <div class="w-2/3 grid grid-cols-5 text-xl font-bold py-5">
      <div class="col-span-2">身高:</div>
      <input placeholder="cm" class="col-span-3 pl-2" v-model="height" />
    </div>
    <div class="w-2/3 grid grid-cols-5 text-xl font-bold py-5">
      <div class="col-span-2">体重:</div>
      <input placeholder="kg" class="col-span-3 pl-2" v-model="weight" />
    </div>
    <div
      v-if="height !== '' && weight !== ''"
      class="w-2/3 grid grid-cols-5 text-xl font-bold py-5"
    >
      <div class="col-span-2">你的BMI:</div>
      <div class="col-span-3">{{ calculateBMI() }} kg/㎡</div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const height = ref("");
const weight = ref("");

const calculateBMI = () => {
  return Math.round(weight.value / (height.value / 100) ** 2);
};
</script>
