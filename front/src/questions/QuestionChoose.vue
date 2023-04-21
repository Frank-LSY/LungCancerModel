<template>
  <div>
    <div style="color: rgba(0, 78, 162, 1)" class="my-2 py-1 text-xl font-bold">
      {{ props.title }}
    </div>
    <div class="flex flex-wrap justify-center">
      <div
        v-for="i in props.size"
        :key="i"
        :class="[
          'w-2/3 text-lg font-bold ring-2 ring-gray-400 rounded my-1 py-1 cursor-pointer hover:bg-sky-200',
          setAnswer(i),
        ]"
        @click="changeAnswers(i)"
      >
        {{ props.choices[i - 1] }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from "vue";
import { useStore } from "vuex";

const store = useStore();

const props = defineProps({
  size: Number, //问题有几个选项
  title: String, //题目
  choices: Array, //选项
  no: Number, //第几题
});

const changeAnswers = (choice) => {
  // console.log('改！')
  store.commit("changeAnswers", { name: props.no, val: choice });
  console.log(store.getters.getAnswers);
};

const setAnswer = (choice) => {
  if (store.getters.getAnswers[props.no]===choice ) {
    return "bg-green-400";
  }
};
</script>
