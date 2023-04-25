<template>
  <div
    class="w-full h-soixantedix flex flex-wrap justify-center bg-cyan-100 bg-opacity-50"
  >
    <div class="w-full h-cinq flex flex-wrap content-center">
      <div class="w-full flex flex-wrap justify-center">
        <Avatar
          :size="25"
          :name="store.getters.getName"
          variant="sunset"
          :colors="['#004EA2', '#A30300', '#00A0A3', '#1F8BFF', '#00A354']"
        />
        <div class="text-lg font-bold mx-2 text-left">
          <span style="color: rgba(0, 78, 162, 1)">{{
            store.getters.getName
          }}</span
          >，以下是您的选择：
        </div>
      </div>
    </div>
    <div class="w-11/12">
      <div>
        <div class="font-bold relative">
          1. 您的身高体重
          <button
            class="absolute right-0 text-sm text-gray-200 px-1 rounded bg-sky-600"
            @click="modify(-1)"
          >
            修改
          </button>
        </div>
        <div
          class="border-t-2 border-gray-200 text-xs font-semibold grid grid-cols-3"
        >
          <div class="border-l-2 border-gray-200">身高 (cm)</div>
          <div class="border-l-2 border-gray-200">体重 (kg)</div>
          <div class="border-x-2 border-gray-200">BMI (kg/㎡)</div>
        </div>
        <div
          class="border-b-2 border-gray-200 text-xs font-semibold grid grid-cols-3"
        >
          <div class="border-l-2 border-gray-200">
            {{ store.getters.getHeight }}
          </div>
          <div class="border-l-2 border-gray-200">
            {{ store.getters.getWeight }}
          </div>
          <div class="border-x-2 border-gray-200">
            {{ store.getters.getBmi }}
          </div>
        </div>
      </div>
      <div
        :class="['m-1', colorQuestion(i)]"
        v-for="(item, i) in q.question"
        :key="i"
      >
        <div class="font-bold relative">
          {{ i + 2 + ". " + item.title + showInfo(i) }}
          <button
            class="absolute right-0 text-sm text-gray-200 px-1 rounded bg-sky-600"
            @click="modify(i)" :disabled="disable(i)"
          >
            修改
          </button>
        </div>
        <div
          v-if="i !== 10"
          :class="[
            'grid text-xs font-semibold',
            'grid-cols-' + item.choices.length,
          ]"
        >
          <div
            :class="[
              'border-2 border-l-0 first:border-l-2 border-gray-200',
              colorChoice(i, j),
            ]"
            v-for="(c, j) in item.choices"
            :key="j"
          >
            {{ c }}
          </div>
        </div>
        <div
          v-else
          :class="[
            'grid text-xs font-semibold',
            'grid-cols-' + item.choices.male.length,
          ]"
        >
          <div
            :class="[
              'border-2 border-l-0 first:border-l-2 border-gray-200',
              colorChoice(i, j),
            ]"
            v-for="(c, j) in store.getters.getAnswers[1] === 1
              ? item.choices.male
              : item.choices.female"
            :key="j"
          >
            {{ c }}
          </div>
        </div>
      </div>
    </div>
    <button
      class="my-2 w-2/3 rounded text-lg font-bold border-4 border-gray-400 bg-red-300 animatecss animatecss-infinite animatecss-fast animatecss-pulse"
    >
      查看预测结果
    </button>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import Avatar from "vue-boring-avatars";
import q from "@assets/json/questions14.json";

const router = useRouter();
const store = useStore();

const modify = (no) => {
  store.commit("changeNum", no);
  router.push("questions");
};

// 有的问题不用填，上色
const colorQuestion = (no) => {
  if (store.getters.getAnswers[no] === 0) {
    return "text-gray-400";
  }
};

//有的问题不用填，标注
const showInfo = (no) => {
  if (store.getters.getAnswers[no] === 0) {
    return " (无需填写)";
  } else {
    return "";
  }
};
// 有的问题不用填，不能点
const disable = (no) => {
  if (store.getters.getAnswers[no] === 0) {
    return true;
  } else {
    return false;
  }
};

// 答案上色
const colorChoice = (no, choice) => {
  // console.log(no,choice)
  // console.log(store.getters.getAnswers)
  if (store.getters.getAnswers[no] === choice + 1) {
    return "bg-green-400";
  } else {
    return;
  }
};
</script>
