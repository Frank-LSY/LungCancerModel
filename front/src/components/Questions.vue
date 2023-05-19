<template>
  <div class="w-full h-soixantedix bg-sky-100 bg-opacity-70">
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
    <div
      v-if="num === -1"
      class="text-xl font-bold pt-32 h-quarantecinq flex flex-wrap justify-center content-start"
    >
      <div class="w-3/4 text-justify text-gray-500">
        问卷共14题。涉及您的基本情况、吸烟情况及一些检查指标。
      </div>
      <div
        @click="num += 1"
        class="w-2/3 mt-10 py-1 border-4 border-gray-400 rounded cursor-pointer hover:bg-sky-200"
      >
        开始填写
      </div>
    </div>
    <div v-if="store.getters.getQuestions.length !== 0">
      <div class="h-dix grid grid-cols-4" v-if="num > -1">
        <div class="col-span-3">
          <div class="w-full grid grid-cols-8" v-for="i in 2" :key="i">
            <button
              v-for="j in 7"
              :key="j"
              style="color: rgba(0, 78, 162, 1)"
              :class="[
                'font-bold py-1 border-2 border-gray-600',
                questionColor((i - 1) * 7 + j - 1),
              ]"
              @click="num = (i - 1) * 7 + j - 1"
              :disabled="condition((i - 1) * 7 + j - 1)"
            >
              {{ (i - 1) * 7 + j }}
            </button>
          </div>
        </div>
        <div class="font-bold col-span-1">
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
      <div class="h-quarantecinq overflow-y-auto" v-if="num > -2">
        <question-choose
          v-if="num > 0 && num < 11"
          :title="store.getters.getQuestions[num]['title']"
          :size="store.getters.getQuestions[num]['choice'].length"
          :choices="store.getters.getQuestions[num]['choice']"
          :no="num"
          :id="store.getters.getQuestions[num]['questionid']"
        ></question-choose>
        <question-choose
          v-if="num === 11"
          :title="store.getters.getQuestions[num]['title']"
          :size="store.getters.getQuestions[num]['choice'].length"
          :choices="
            store.getters.getAnswers['sex'] === 1
              ? store.getters.getQuestions[num]['choice']
              : store.getters.getQuestions[num + 1]['choice']
          "
          :no="num"
          :id="store.getters.getQuestions[num]['questionid']"
        ></question-choose>
        <question-choose
          v-if="num > 11"
          :title="store.getters.getQuestions[num + 1]['title']"
          :size="store.getters.getQuestions[num + 1]['choice'].length"
          :choices="store.getters.getQuestions[num + 1]['choice']"
          :no="num"
          :id="store.getters.getQuestions[num + 1]['questionid']"
        ></question-choose>
        <question-fill
          v-if="num == 0"
          :title="store.getters.getQuestions[num]['title']"
          :height="store.getters.getQuestions[num]['choice'][0]"
          :weight="store.getters.getQuestions[num]['choice'][1]"
        ></question-fill>
      </div>
      <div
        v-if="num > -1"
        class="h-cinq flex flex-wrap content-start justify-evenly text-xl font-bold pt-3"
      >
        <div
          v-if="num !== 0"
          class="border-4 border-gray-500 rounded px-3 py-2 cursor-pointer"
          @click="prevQuestion"
        >
          上一题
        </div>
        <div
          v-if="num !== store.getters.getQuestions.length - 2"
          class="border-4 border-gray-500 rounded px-3 py-2 cursor-pointer"
          @click="nextQuestion"
        >
          下一题
        </div>
        <div
          v-if="
            Object.keys(store.getters.getAnswers).length ===
            store.getters.getQuestions.length - 1
          "
          class="border-4 border-gray-500 rounded px-3 py-2 bg-green-300 cursor-pointer"
          @click="submit"
        >
          完成
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import Avatar from "vue-boring-avatars";
import QuestionChoose from "@/questions/QuestionChoose.vue";
import QuestionFill from "@/questions/QuestionFill.vue";

import { errorMessage, warningMessage } from "@/assets/js/common";

const store = useStore();
const router = useRouter();

const goBack = () => {
  router.push("history");
};

// 方块染色
const questionColor = (no) => {
  // console.log(no);
  // console.log(question_list.value)
  if (no < 12) {
    if ((no === 6 || no === 7) && store.getters.getAnswers["smoking"] === 1) {
      return "bg-sky-500";
    } else if (
      no === 7 &&
      (store.getters.getAnswers["packYear"] === 1 ||
        store.getters.getAnswers["packYear"] === 2)
    ) {
      return "bg-sky-500";
    } else if (
      store.getters.getAnswers.hasOwnProperty(
        store.getters.getQuestions[no]["questionid"]
      )
    ) {
      return "bg-green-400";
    } else {
      return "bg-gray-300";
    }
  } else {
    if (
      store.getters.getAnswers.hasOwnProperty(
        store.getters.getQuestions[no + 1]["questionid"]
      )
    ) {
      return "bg-green-400";
    } else {
      return "bg-gray-300";
    }
  }
};

// 上一题下一题
const num = ref(store.getters.getNum);
const prevQuestion = () => {
  // console.log(num.value);
  // console.log(store.getters.getQuestions[num.value]);
  if (num.value === 8) {
    if (store.getters.getAnswers["smoking"] === 1) {
      num.value -= 3;
    } else if (
      store.getters.getAnswers["packYear"] === 1 ||
      store.getters.getAnswers["packYear"] === 2
    ) {
      num.value -= 2;
    }
  } else {
    num.value -= 1;
  }
};
const nextQuestion = () => {
  // console.log(store.getters.getQuestions[num.value]);
  if (num.value === 5 && store.getters.getAnswers["smoking"] === 1) {
    num.value += 3;
  } else if (
    num.value === 6 &&
    (store.getters.getAnswers["packYear"] === 1 ||
      store.getters.getAnswers["packYear"] === 2)
  ) {
    num.value += 2;
  } else {
    num.value += 1;
  }
};

//判断有的题填不填
const condition = (no) => {
  if (no === 6) {
    // 如果第六题选不吸烟
    if (
      store.getters.getAnswers["smoking"] !== 2 &&
      store.getters.getAnswers["smoking"] !== 3
    ) {
      return true;
    }
    // 如果第六题吸烟，则第七题权限放开
    else {
      return false;
    }
  } else if (no === 7) {
    // 如果第六题选不吸烟
    if (
      store.getters.getAnswers["smoking"] !== 2 &&
      store.getters.getAnswers["smoking"] !== 3
    ) {
      return true;
    }
    // 如果第六题吸烟
    else {
      // 如果第七题吸烟多
      if (store.getters.getAnswers["packYear"] === 3) {
        return false;
      } else {
        return true;
      }
    }
  } else {
    return false;
  }
};

const submit = () => {
  // console.log(Object.keys(store.getters.getAnswers).length)
  if (
    Object.keys(store.getters.getAnswers).length ===
    store.getters.getQuestions.length - 1
  ) {
    router.push("result");
  } else {
    warningMessage("请完成全部问题！");
  }
};
</script>
