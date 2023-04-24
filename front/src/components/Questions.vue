<template>
  <div class="w-full h-soixantedix bg-sky-100">
    <div class="flex flex-wrap justify-between w-full h-cinq text-right">
      <div class="text-lg font-bold ml-2" @click="goBack()">返回</div>
      <div class="flex flex-wrap justify-center">
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
          >，您好!
        </div>
      </div>
    </div>

    <div class="h-dix grid grid-cols-4" v-if="num > -2">
      <div class="col-span-3">
        <div class="w-full grid grid-cols-8" v-for="i in 2" :key="i">
          <button
            v-for="j in 8"
            :key="j"
            style="color: rgba(0, 78, 162, 1)"
            :class="[
              'font-bold py-1 border-2 border-gray-600',
              questionColor((i - 1) * 8 + j - 2),
            ]"
            @click="num = (i - 1) * 8 + j - 2"
            :disabled="condition((i - 1) * 8 + j - 2)"
          >
            {{ (i - 1) * 8 + j }}
          </button>
        </div>
      </div>
      <div class="font-bold">
        <div class="flex flex-wrap justify-evenly">
          <div class="px-2 m-1 bg-gray-300"></div>
          <div>未填写</div>
        </div>
        <div class="flex flex-wrap justify-evenly">
          <div class="px-2 m-1 bg-green-500"></div>
          <div>已填写</div>
        </div>
        <div class="flex flex-wrap justify-evenly">
          <div class="px-2 m-1 bg-sky-500"></div>
          <div>无需填</div>
        </div>
      </div>
    </div>
    <div
      v-if="num === -2"
      class="text-xl font-bold pt-32 h-quarantecinq flex flex-wrap justify-center content-start"
    >
      <div class="w-3/4 text-justify text-gray-500">
        问卷分为3部分，共16题。涉及您的基本情况、吸烟情况及检查指标。
      </div>
      <div
        @click="num = -1"
        class="w-2/3 mt-10 py-1 border-4 border-gray-400 rounded cursor-pointer hover:bg-sky-200"
      >
        开始填写
      </div>
    </div>
    <div class="h-quarantecinq overflow-y-auto" v-if="num > -2">
      <question-choose
        v-if="num >= 0 && num != 12"
        :title="q.question[num]['title']"
        :size="q.question[num]['choices'].length"
        :choices="q.question[num]['choices']"
        :no="num"
      ></question-choose>
      <question-choose
        v-if="num === 12"
        :title="q.question[num]['title']"
        :size="
          store.getters.getAnswers[1] === 1
            ? q.question[num]['choices']['male'].length
            : q.question[num]['choices']['female'].length
        "
        :choices="
          store.getters.getAnswers[1] === 1
            ? q.question[num]['choices']['male']
            : q.question[num]['choices']['female']
        "
        :no="num"
      ></question-choose>
      <question-fill v-if="num == -1"></question-fill>
    </div>
    <div
      v-if="num > -2"
      class="h-cinq flex flex-wrap content-start justify-evenly text-xl font-bold pt-3"
    >
      <div
        v-if="num !== -1"
        class="border-4 border-gray-500 rounded px-3 py-2 cursor-pointer"
        @click="prevQuestion"
      >
        上一题
      </div>
      <div
        v-if="num !== 14"
        class="border-4 border-gray-500 rounded px-3 py-2 cursor-pointer"
        @click="nextQuestion"
      >
        下一题
      </div>
      <div
        v-if="num === 14"
        class="border-4 border-gray-500 rounded px-3 py-2 cursor-pointer"
        @click="submit"
      >
        完成
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import Avatar from "vue-boring-avatars";
import QuestionChoose from "@/questions/QuestionChoose.vue";
import QuestionFill from "@/questions/QuestionFill.vue";
import q from "@assets/json/questions.json";

const store = useStore();
const router = useRouter();

const goBack = () => {
  router.push("check");
};

// 方块染色
const questionColor = (no) => {
  if ((no === 7 || no === 8) && store.getters.getAnswers[6] === 1) {
    return "bg-sky-500";
  } else if (
    no === 8 &&
    (store.getters.getAnswers[7] === 2 || store.getters.getAnswers[7] === 3)
  ) {
    return "bg-sky-500";
  } else if (store.getters.getAnswers.hasOwnProperty(no)) {
    return "bg-green-400";
  } else {
    return "bg-gray-300";
  }
};

// 上一题下一题
const num = ref(-1);
const prevQuestion = () => {
  num.value -= 1;
};
const nextQuestion = () => {
  num.value += 1;
};

//判断有的题填不填
const condition = (no) => {
  if (no === 7) {
    if (
      store.getters.getAnswers[6] !== 2 ||
      store.getters.getAnswers[6] !== 3
    ) {
      return true;
    } else {
      return false;
    }
  } else if (no === 8) {
    if (
      store.getters.getAnswers[6] !== 2 ||
      store.getters.getAnswers[6] !== 3
    ) {
      return true;
    } else {
      return false;
    }
  } else {
    return false;
  }
  // if (no === 7) {
  //   // 判断第9题
  //   if (
  //     store.getters.getAnswers[6] !== 2 ||
  //     store.getters.getAnswers[6] !== 3
  //   ) {
  //     //如果第8题抽烟
  //     return true;
  //   } else {
  //     return false;
  //   }
  // } else if (no === 8) {
  //   //判断第10题
  //   if (
  //     store.getters.getAnswers[6] !== 2 ||
  //     store.getters.getAnswers[6] !== 3
  //   ) {
  //     return true;
  //   } else {
  //     //如果第8题抽烟
  //     if (
  //       store.getters.getAnswers[7] !== 2 ||
  //       store.getters.getAnswers[7] !== 3
  //     ) {
  //       // 如果第七题抽的多
  //       return false;
  //     } else {
  //       return true;
  //     }
  //   }
  // }
};
</script>
