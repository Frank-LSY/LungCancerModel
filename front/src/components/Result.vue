<template>
  <div
    class=" w-full h-soixantedix flex flex-wrap justify-center bg-cyan-100 bg-opacity-50 relative"
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
    <div class="w-11/12 h-soixante overflow-auto" v-if="store.getters.getQuestions.length !== 0">
      <div class="m-1">
        <div class="font-bold relative">
          1. 您的身高体重
          <button
            class="absolute right-0 text-sm text-gray-200 px-1 rounded bg-sky-600 bg-opacity-70"
            @click="modify(0)"
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
        v-for="(item, i) in store.getters.getQuestions"
        :key="i"
      >
        <div class="font-bold relative" v-if="i > 0 && i < 12">
          {{ i + 1 + ". " + item.title + showInfo(i) }}
          <button
            class="absolute right-0 text-sm text-gray-200 px-1 rounded bg-sky-600 bg-opacity-70"
            @click="modify(i)"
            :disabled="disable(i)"
          >
            修改
          </button>
        </div>
        <div class="font-bold relative" v-if="i > 12">
          {{ i + ". " + item.title + showInfo(i) }}
          <button
            class="absolute right-0 text-sm text-gray-200 px-1 rounded bg-sky-600 bg-opacity-70"
            @click="modify(i)"
          >
            修改
          </button>
        </div>
        <div
          v-if="i > 0 && i < 11"
          :class="[
            'grid text-xs font-semibold',
            'grid-cols-' + item.choice.length,
          ]"
        >
          <div
            :class="[
              'border-2 border-l-0 first:border-l-2 border-gray-200',
              colorChoice(i, j),
            ]"
            v-for="(c, j) in item.choice"
            :key="j"
          >
            {{ c }}
          </div>
        </div>
        <div
          v-if="i === 11"
          :class="[
            'grid text-xs font-semibold',
            'grid-cols-' + item.choice.length,
          ]"
        >
          <div
            :class="[
              'border-2 border-l-0 first:border-l-2 border-gray-200',
              colorChoice(i, j),
            ]"
            v-for="(c, j) in store.getters.getAnswers['sex'] === 1
              ? store.getters.getQuestions[11]['choice']
              : store.getters.getQuestions[12]['choice']"
            :key="j"
          >
            {{ c }}
          </div>
        </div>
        <div
          v-if="i > 12"
          :class="[
            'grid text-xs font-semibold',
            'grid-cols-' + item.choice.length,
          ]"
        >
          <div
            :class="[
              'border-2 border-l-0 first:border-l-2 border-gray-200',
              colorChoice(i, j),
            ]"
            v-for="(c, j) in item.choice"
            :key="j"
          >
            {{ c }}
          </div>
        </div>
      </div>
    </div>
    <button
      class="my-2 w-2/3 rounded text-lg font-bold border-4 border-gray-400 bg-red-300 animatecss animatecss-infinite animatecss-fast animatecss-pulse"
      @click="showResult()"
    >
      查看预测结果
    </button>
    <res-dialog
      @click="showDialog = false"
      v-if="showDialog"
      class="animatecss animatecss-fadeIn"
    ></res-dialog>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import Avatar from "vue-boring-avatars";
import ResDialog from "@components/ResDialog.vue";

const router = useRouter();
const store = useStore();

// 问题列表
// const question_list = ref(store.getters.getQuestions);

const modify = (no) => {
  if (no > 11) {
    no -= 1;
  }
  // console.log(no);
  store.commit("changeNum", no);
  router.push("questions");
};

// 有的问题不用填，上色
const colorQuestion = (no) => {
  if (
    store.getters.getAnswers[store.getters.getQuestions[no]["questionid"]] === 0
  ) {
    return "text-gray-400";
  }
};

//有的问题不用填，标注
const showInfo = (no) => {
  if (
    store.getters.getAnswers[store.getters.getQuestions[no]["questionid"]] === 0
  ) {
    return " (无需填写)";
  } else {
    return "";
  }
};
// 有的问题不用填，不能点
const disable = (no) => {
  if (
    store.getters.getAnswers[store.getters.getQuestions[no]["questionid"]] === 0
  ) {
    return true;
  } else {
    return false;
  }
};

// 答案上色
const colorChoice = (no, choice) => {
  // console.log(no,choice)
  // console.log(store.getters.getAnswers)
  if (
    store.getters.getAnswers[store.getters.getQuestions[no]["questionid"]] ===
    choice + 1
  ) {
    return "bg-green-400";
  } else {
    return;
  }
};

const showDialog = ref(false);
const showResult = () => {
  // console.log(store.getters.getAnswers);
  showDialog.value = true;
};
</script>
