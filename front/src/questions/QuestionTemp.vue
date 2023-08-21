<template>
  <div>
    <div class="py-1.5 font-bold text-gray-700 text-left pl-4">
      > {{ props.title }}
    </div>
    <div :class="['grid', 'grid-cols-' + props.size]">
      <div
        :class="['text-sm font-semibold flex flex-wrap justify-center']"
        v-for="i in props.size"
        :key="i"
        @click="changeAnswers(i)"
      >
        <div
          :class="[
            'md:w-3/4 w-5/6 cursor-pointer ring-2 ring-gray-400 rounded-xs shadow hover:bg-sky-200 select-none',
            setAnswer(i),
          ]"
        >
          {{ props.choices[i - 1] }}
        </div>
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
  id: String, //问题id
  no: Number, //第几题
});

const changeAnswers = (choice) => {
  // console.log('改！')
  store.commit("changeAnswers", { name: props.id, val: choice });
  console.log(store.getters.getAnswers);
};

const setAnswer = (choice) => {
  if (store.getters.getAnswers[props.id] === choice) {
    return "bg-teal-400";
  }
};
</script>
