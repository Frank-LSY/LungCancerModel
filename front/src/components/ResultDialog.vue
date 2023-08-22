<template>
  <div
    class="absolute left-0 top-0 h-soixantedix w-full bg-gray-400 bg-opacity-95"
  >
    <div
      class="absolute w-11/12 top-8 left-1/24 h-soixante bg-teal-500 bg-opacity-50 border-4 border-gray-400 rounded-sm shadow shadow-gray-500"
    >
      <div class="flex flex-wrap justify-evenly">
        <div v-for="num in [1, 2]" :key="num">
          <div>
            {{ store.getters.getQuestions[num]["title"] }}:
            {{
              store.getters.getQuestions[num]["choice"][
                store.getters.getAnswers[
                  store.getters.getQuestions[num]["questionid"]
                ] - 1
              ]
            }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
import { useStore } from "vuex";

const store = useStore();
const router = useRouter();
</script>
