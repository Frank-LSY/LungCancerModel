<template>
  <div class="flex flex-wrap justify-center bg-gray-300">
    <router-view class="w-full md:w-full lg:w-1/2 xl:w-1/3 shadow-lg"></router-view>
  </div>
</template>

<script>
import questionAPI from "@/api/question";
import { onBeforeMount } from "vue";
import { useStore } from "vuex";
import { errorMessage } from "@/assets/js/common";

export default {
  name: "App",
  setup() {
    const store = useStore();
    const getQuestion = () => {
      questionAPI
        .getAllQuestions()
        .then((res) => {
          store.commit("changeQuestions", res.data);
          console.log(res.data);
        })
        .catch((err) => {
          errorMessage(err);
        });
    };

    onBeforeMount(() => {
      getQuestion();
    });
    // return { getQuestion };
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
