<template>
  <div class="flex flex-wrap justify-center">
    <div
      style="color: rgba(0, 78, 162, 1)"
      class="w-2/3 my-2 py-1 text-xl font-bold"
    >
      1. {{ props.title }}
    </div>
    <div class="w-2/3 grid grid-cols-5 text-xl font-bold pt-16 pb-5">
      <div class="col-span-2">{{ props.height }}:</div>
      <input
        placeholder="cm"
        type="number"
        class="col-span-3 pl-2"
        v-model="height"
      />
    </div>
    <div class="w-2/3 grid grid-cols-5 text-xl font-bold py-5">
      <div class="col-span-2">{{ props.weight }}:</div>
      <input
        placeholder="kg"
        type="number"
        class="col-span-3 pl-2"
        v-model="weight"
      />
    </div>
    <div
      v-if="height !== '' && weight !== ''"
      class="w-2/3 grid grid-cols-5 text-xl font-bold py-5"
    >
      <div class="col-span-2">您的BMI:</div>
      <div class="col-span-3">{{ calculateBMI() }} kg/㎡</div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from "vue";
import { useStore } from "vuex";

const props = defineProps({
  title: String,
  height: String,
  weight: String
});

const store = useStore();
const height = ref(store.state.height);
const weight = ref(store.state.weight);

const calculateBMI = () => {
  var bmi = Math.round((weight.value / (height.value / 100) ** 2) * 100) / 100;
  store.commit("changeBmi", bmi);
  return bmi;
};

watch(
  () => height.value,
  () => {
    store.commit("changeHeight", height.value);
  }
);

watch(
  () => weight.value,
  () => {
    store.commit("changeWeight", weight.value);
    var bmi = calculateBMI();
    // console.log(bmi);
    var choice;
    if (bmi < 25) {
      choice = 1;
    } else if (bmi <= 29.9) {
      choice = 2;
    } else {
      choice = 3;
    }
    store.commit("changeAnswers", { name: "BMI", val: choice });
  }
);
watch(
  () => height.value,
  () => {
    store.commit("changeHeight", weight.value);
    var bmi = calculateBMI();
    // console.log(bmi);
    var choice;
    if (bmi < 25) {
      choice = 1;
    } else if (bmi <= 29.9) {
      choice = 2;
    } else {
      choice = 3;
    }
    store.commit("changeAnswers", { name: "BMI", val: choice });
  }
);
</script>
