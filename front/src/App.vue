<template>
  <router-view></router-view>
</template>

<script>
import questionAPI from "@/api/question";
import { onBeforeMount } from "vue";
import { useStore } from "vuex";
import { errorMessage } from "@/assets/js/common";

export default {
  name: "App",
  setup() {
    const store = useStore()
    const getQuestion = () => {
      questionAPI
        .getAllQuestions()
        .then((res) => {
          store.commit("changeQuestions",res.data)
          console.log(res.data);
        })
        .catch((err) => {
          errorMessage(err);
        });
    };

    onBeforeMount(()=> {
      getQuestion()
    })
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
