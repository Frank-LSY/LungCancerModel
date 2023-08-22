<template>
  <div class="relative w-full h-soixantedix bg-sky-100 bg-opacity-70">
    <div class="flex flex-wrap justify-between w-full h-cinq text-right">
      <div class="text-lg font-bold ml-2 pt-1 cursor-pointer" @click="goBack()">
        返回
      </div>
      <div class="flex flex-wrap justify-center pt-1">
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
      class="w-full h-soixantecinq overflow-auto flex flex-wrap justify-center"
      v-if="store.getters.getQuestions.length !== 0"
    >
      <div
        class="w-11/12 ring-2 ring-orange-200 rounded m-5 p-1.5 shadow-xl hover:shadow-xl hover:shadow-orange-300"
      >
        <div style="color: rgba(0, 78, 162, 1)" class="text-lg font-bold">
          人体测量变量
        </div>
        <div class="grid grid-cols-2">
          <div>
            <div class="py-1.5 font-bold text-gray-700 text-left pl-4">
              > {{ store.getters.getQuestions[0]["choice"][0] }}
            </div>
            <input
              type="number"
              :class="[
                'rounded-sm w-5/6 pl-2 text-sm font-semibold border-2 border-gray-400',
                height ? ' bg-teal-400' : '',
              ]"
              placeholder="身高（cm）"
              v-model="height"
            />
          </div>
          <div>
            <div class="py-1.5 font-bold text-gray-700 text-left pl-4">
              > {{ store.getters.getQuestions[0]["choice"][1] }}
            </div>
            <input
              type="number"
              :class="[
                'rounded-sm w-5/6 pl-2 text-sm font-semibold border-2 border-gray-400',
                weight ? ' bg-teal-400' : '',
              ]"
              placeholder="体重（kg）"
              v-model="weight"
            />
          </div>
        </div>
        <div v-for="num in [1, 2]" :key="num">
          <question-temp
            :title="store.getters.getQuestions[num]['title']"
            :size="store.getters.getQuestions[num]['choice'].length"
            :choices="store.getters.getQuestions[num]['choice']"
            :no="num"
            :id="store.getters.getQuestions[num]['questionid']"
          ></question-temp>
        </div>
      </div>
      <div
        class="w-11/12 ring-2 ring-orange-200 rounded m-5 p-1.5 shadow-xl hover:shadow-xl hover:shadow-orange-300"
      >
        <div style="color: rgba(0, 78, 162, 1)" class="text-lg font-bold">
          吸烟史
        </div>
        <div v-for="num in [5, 6, 7]" :key="num">
          <question-temp
            :title="store.getters.getQuestions[num]['title']"
            :size="store.getters.getQuestions[num]['choice'].length"
            :choices="store.getters.getQuestions[num]['choice']"
            :no="num"
            :id="store.getters.getQuestions[num]['questionid']"
          ></question-temp>
        </div>
      </div>
      <div
        class="w-11/12 ring-2 ring-orange-200 rounded m-5 p-1.5 shadow-xl hover:shadow-xl hover:shadow-orange-300"
      >
        <div style="color: rgba(0, 78, 162, 1)" class="text-lg font-bold">
          癌症史/家族史
        </div>
        <div v-for="num in [3, 4]" :key="num">
          <question-temp
            :title="store.getters.getQuestions[num]['title']"
            :size="store.getters.getQuestions[num]['choice'].length"
            :choices="store.getters.getQuestions[num]['choice']"
            :no="num"
            :id="store.getters.getQuestions[num]['questionid']"
          ></question-temp>
        </div>
      </div>
      <div
        class="w-11/12 ring-2 ring-orange-200 rounded m-5 p-1.5 shadow-xl hover:shadow-xl hover:shadow-orange-300"
      >
        <div style="color: rgba(0, 78, 162, 1)" class="text-lg font-bold">
          肺功能指标
        </div>
        <div v-for="num in [8, 9]" :key="num">
          <question-temp
            :title="store.getters.getQuestions[num]['title']"
            :size="store.getters.getQuestions[num]['choice'].length"
            :choices="store.getters.getQuestions[num]['choice']"
            :no="num"
            :id="store.getters.getQuestions[num]['questionid']"
          ></question-temp>
        </div>
      </div>
      <div
        class="w-11/12 ring-2 ring-orange-200 rounded m-5 p-1.5 shadow-xl hover:shadow-xl hover:shadow-orange-300"
      >
        <div style="color: rgba(0, 78, 162, 1)" class="text-lg font-bold">
          血检指标
        </div>
        <div v-for="num in [10, 13, 14]" :key="num">
          <question-temp
            :title="store.getters.getQuestions[num]['title']"
            :size="store.getters.getQuestions[num]['choice'].length"
            :choices="store.getters.getQuestions[num]['choice']"
            :no="num"
            :id="store.getters.getQuestions[num]['questionid']"
          ></question-temp>
        </div>
      </div>
    </div>
    <div
      class="absolute h-cinq top-0 left-1/6 flex flex-wrap justify-evenly content-center border-2 border-t-0 border-orange-200 rounded-sm shadow-lg bg-gray-400 bg-opacity-25 hover:shadow-xl"
    >
      <button
        :disabled="Object.keys(store.getters.getAnswers).length === 0"
        class="rounded text-sm font-semibold px-2 py-0.5 mx-2 border-2 border-red-500 cursor-pointer hover:bg-red-200 hover:bg-opacity-70"
        @click="clear"
      >
        清空
      </button>
      <button
        :disabled="
          Object.keys(store.getters.getAnswers).length !==
          store.getters.getQuestions.length - 2
        "
        class="rounded text-sm font-semibold px-2 py-0.5 mx-2 border-2 border-sky-700 cursor-pointer hover:bg-sky-200 hover:bg-opacity-70"
        @click="submit"
      >
        查看结果
      </button>
    </div>
    <result-dialog v-if="showDialog"> </result-dialog>
    <div
      class="absolute bottom-2 w-2/3 left-1/6 rounded border-2 font-semibold border-orange-300 bg-red-50 cursor-pointer select-none animatecss animatecss-infinite animatecss-pulse"
      v-if="showDialog"
      @click="showDialog = false"
    >
      关闭
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import Avatar from "vue-boring-avatars";
import QuestionTemp from "@questions/QuestionTemp.vue";
import ResultDialog from "./ResultDialog.vue";
const store = useStore();
const router = useRouter();

const goBack = () => {
  router.push("history");
};

// 清空
const clear = () => {
  weight.value = "";
  height.value = "";
  store.commit("changeAnswer", {});
  console.log(store.getters.getAnswers);
};
// 提交
const submit = () => {
  console.log(store.getters.getAnswers);
  showDialog.value = true;
};

// 身高体重相关
const height = ref(store.state.height);
const weight = ref(store.state.weight);

const calculateBMI = () => {
  var bmi = Math.round((weight.value / (height.value / 100) ** 2) * 100) / 100;
  store.commit("changeBmi", bmi);
  return bmi;
};

watch(
  () => weight.value,
  () => {
    store.commit("changeWeight", weight.value);
    var bmi = calculateBMI();
    console.log(bmi);
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
    console.log(bmi);
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

// 是否显示结果
const showDialog = ref(false);
</script>
