<template>
  <div>
    <div style="color: rgba(0, 78, 162, 1)" class="my-2 py-1 text-xl font-bold">
      {{ props.no + 1 + ". " + props.title }}
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
// import { watch } from "vue";

const store = useStore();

const props = defineProps({
  size: Number, //问题有几个选项
  title: String, //题目
  choices: Array, //选项
  id: String, //问题id
  no: Number, //第几题
});

const changeAnswers = (choice) => {
  // console.log('改！')
  store.commit("changeAnswers", { name: props.id, val: choice });
  if (props.no === 5) {
    if (choice === 1) {
      store.commit("changeAnswers", { name: "packYear", val: 0 });
      store.commit("changeAnswers", { name: "smokingIntensity", val: 0 });
    } else {
      store.commit("deleteAnswers", "packYear");
      store.commit("deleteAnswers", "smokingIntensity");
    }
  }
  if (props.no === 6) {
    if (choice === 1 || choice === 2) {
      store.commit("changeAnswers", { name: "smokingIntensity", val: 0 });
    } else {
      store.commit("deleteAnswers", "smokingIntensity");
    }
  }
  console.log(store.getters.getAnswers);
};

const setAnswer = (choice) => {
  if (store.getters.getAnswers[props.id] === choice) {
    return "bg-green-400";
  }
};

// watch(
//   () => props.no,
//   () => {
//     console.log(store.getters.getAnswers[1] === 1);
//     console.log(props.choices)
//   }
// );
</script>
