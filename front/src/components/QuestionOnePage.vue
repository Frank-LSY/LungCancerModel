<template>
  <div class="w-full h-soixantedix bg-sky-100 bg-opacity-70">
    <div class="flex flex-wrap justify-between w-full h-cinq text-right">
      <div class="text-lg font-bold ml-2 cursor-pointer" @click="goBack()">
        返回
      </div>
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
      class="w-full h-soixantecinq overflow-auto flex flex-wrap justify-center content-center"
      v-if="store.getters.getQuestions.length !== 0"
    >
      <div
        class="w-11/12 ring-2 ring-orange-200 rounded m-5 p-1.5 shadow-lg hover:shadow-xl hover:shadow-orange-300"
      >
        <div style="color: rgba(0, 78, 162, 1)" class="text-lg font-bold">
          人体测量变量
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
        class="w-11/12 ring-2 ring-orange-200 rounded m-5 p-1.5 shadow-lg hover:shadow-xl hover:shadow-orange-300"
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
        class="w-11/12 ring-2 ring-orange-200 rounded m-5 p-1.5 shadow-lg hover:shadow-xl hover:shadow-orange-300"
      >
        <div style="color: rgba(0, 78, 162, 1)" class="text-lg font-bold">
          家族史
        </div>
        <div v-for="num in [3,4]" :key="num">
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
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import Avatar from "vue-boring-avatars";
import QuestionTemp from "@questions/QuestionTemp.vue";

const store = useStore();
const router = useRouter();

const goBack = () => {
  router.push("history");
};

const questionid = ref("");
</script>
