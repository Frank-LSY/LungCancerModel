<template>
  <div
    class="absolute w-full h-soixantedix left-0 top-0 bg-black bg-opacity-30"
  >
    <div
      class="absolute w-11/12 bottom-1 left-1/24 bg-red-500 bg-opacity-70 cursor-pointer text-gray-200 font-bold px-2 rounded z-20 animatecss animatecss-infinite animatecss-fast animatecss-pulse"
      @click="closeDialog()"
    >
      关闭
    </div>
    <div
      class="overflow-auto absolute top-4 left-1/24 flex flex-wrap justify-center w-11/12 h-soixantecinq bg-cyan-100 bg-opacity-95 rounded z-10"
    >
      <div class="w-11/12">
        <div v-for="(item, i) in questions" :key="i">
          <div v-if="i === 0">
            <div class="font-bold">{{ item.title }}</div>
            <div
              :class="[
                'grid text-xs font-semibold',
                'grid-cols-' + (item.choice.length - 2),
              ]"
            >
              <div
                :class="[
                  'border-2 border-l-0 first:border-l-2 border-gray-200',
                  colorChoice(i, j),
                ]"
                v-for="(c, j) in item.choice.slice(2)"
                :key="j"
              >
                {{ c }}
              </div>
            </div>
          </div>
          <div
            v-if="
              i > 0 &&
              i < 11 &&
              store.getters.getDetail.details[i]['choice'] !== 0
            "
          >
            <div class="font-bold">{{ item.title }}</div>
            <div
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
          <div v-if="i === 11">
            <div class="font-bold">{{ item.title }}</div>
            <div
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
                v-for="(c, j) in store.getters.getDetail.details[2][
                  'choice'
                ] === 1
                  ? questions[11]['choice']
                  : questions[12]['choice']"
                :key="j"
              >
                {{ c }}
              </div>
            </div>
          </div>
          <div v-if="i > 12">
            <div class="font-bold">{{ item.title }}</div>
            <div
              :class="[
                'grid text-xs font-semibold',
                'grid-cols-' + item.choice.length,
              ]"
            >
              <div
                :class="[
                  'border-2 border-l-0 first:border-l-2 border-gray-200',
                  colorChoice(i - 1, j),
                ]"
                v-for="(c, j) in item.choice"
                :key="j"
              >
                {{ c }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import questionAPI from "@/api/question";
import historyAPI from "@/api/history";
import { ref, onMounted } from "vue";

import { useStore } from "vuex";
import { errorMessage } from "@/assets/js/common";

const store = useStore();

const questions = ref();

const getQuestions = () => {
  questionAPI
    .getAllQuestions()
    .then((res) => {
      questions.value = res.data;
    })
    .catch((err) => {
      errorMessage(err);
    });
};

onMounted(() => {
  getQuestions();
});

const colorChoice = (no, choice) => {
  // console.log(no,choice)
  console.log(store.getters.getDetail.details)
  if (store.getters.getDetail.details[no]["choice"] === choice + 1) {
    return "bg-green-400";
  } else {
    return;
  }
};
const closeDialog = () => {
  store.commit("changeDetail", {
    showDialog: false,
    details: [],
  });
};
</script>
