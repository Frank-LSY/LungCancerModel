<template>
  <div class="w-full h-soixantedix bg-sky-100">
    <div class="grid grid-cols-12 w-full h-cinq">
      <div class="text-xl font-bold col-span-2" @click="goBack()">返回</div>
      <Avatar
        class="col-start-6"
        :size="30"
        :name="store.getters.getName"
        variant="sunset"
        :colors="['#004EA2', '#A30300', '#00A0A3', '#1F8BFF', '#00A354']"
      />
      <div class="text-xl font-bold mx-4 col-span-6 text-left">
        <span style="color: rgba(0, 78, 162, 1)">{{
          store.getters.getName
        }}</span
        >，您好!
      </div>
    </div>

    <div class="h-dix" v-if="num > -2">
      <div class="w-full grid grid-cols-8" v-for="i in 2" :key="i">
        <div
          v-for="j in 8"
          :key="j"
          style="color: rgba(0, 78, 162, 1)"
          class="font-bold bg-gray-300 py-1 border-2 border-gray-600 cursor-pointer"
          @click="num = (i - 1) * 8 + j - 2"
        >
          {{ (i - 1) * 8 + j }}
        </div>
      </div>
    </div>
    <div
      v-if="num === -2"
      class="text-xl font-bold pt-32 h-quarantecinq flex flex-wrap justify-center content-start"
    >
      <div class="w-full">问卷分为3部分，共16题。</div>
      <div @click="num = -1" class="w-2/3 border-4 border-gray-400 rounded">
        开始填写
      </div>
    </div>
    <div class="h-quarantecinq overflow-y-auto" v-if="num > -2">
      <question-choose
        v-if="num >= 0"
        class="animatecss animatecss-fadeInUp"
        :title="q.question[num]['title']"
        :size="q.question[num]['choices'].length"
        :choices="q.question[num]['choices']"
      ></question-choose>
      <question-fill
        class="animatecss animatecss-fadeInUp"
        v-if="num == -1"
      ></question-fill>
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
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import Avatar from "vue-boring-avatars";
import QuestionIntro from "@questions/QuestionIntro.vue";
import QuestionChoose from "@/questions/QuestionChoose.vue";
import QuestionFill from "@/questions/QuestionFill.vue";
import q from "@assets/json/questions.json";

const store = useStore();
const router = useRouter();

const num = ref(-2);

const goBack = () => {
  router.push("check");
};

const prevQuestion = () => {
  num.value -= 1;
};
const nextQuestion = () => {
  num.value += 1;
};

console.log(q);
</script>
