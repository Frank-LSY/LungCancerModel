<template>
  <div class="absolute h-soixantedix w-full bg-black bg-opacity-30">
    <div
      class="absolute w-2/3 left-1/6 top-32 h-trente bg-cyan-100 bg-opacity-90 rounded-xl"
    >
      <div class="w-full h-dix flex flex-wrap content-center">
        <div class="w-full flex flex-wrap justify-center">
          <Avatar
            :size="25"
            :name="store.getters.getName"
            variant="sunset"
            :colors="['#004EA2', '#A30300', '#00A0A3', '#1F8BFF', '#00A354']"
          />
          <div class="font-bold mx-2 text-left">
            <div style="color: rgba(0, 78, 162, 1)">
              {{ store.getters.getName }}
            </div>
            您的5年期肺癌风险为：
          </div>
        </div>
      </div>
      <div :class="[color, 'text-6xl font-extrabold h-dix']">
        {{ prob }}
      </div>
      <div class="font-bold h-dix">
        <div>您是 {{ smokeC }}</div>
        <div>
          您的肺癌风险 <span :class="color">{{ risk }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useStore } from "vuex";
import Avatar from "vue-boring-avatars";
import resultsAPI from "@/api/results";
import { errorMessage } from "@/assets/js/common";

const store = useStore();

// 分数
const score = ref(0);
// 概率
const prob = ref("");
const risk = ref("很低");
const color = ref("text-green-500");
const smoke = ref("");
const smokeC = ref("");

// 算分
const calScore = () => {
  resultsAPI
    .calcProbability({
      answers: store.getters.getAnswers,
      year: "five",
    })
    .then((res) => {
      prob.value = res.data.probability;
      smoke.value = res.data.smoking;
      switch (smoke.value) {
        case "LIGHT":
          smokeC.value = "轻度吸烟者";
          break;
        case "NEVER":
          smokeC.value = "不吸烟者";
          break;
        case "HEAVY":
          smokeC.value = "重度吸烟者";
          break;
      }
      colorPercent();
    })
    .catch((err) => {
      errorMessage(err);
    });
};

// 上色
const colorPercent = () => {
  // console.log(prob.value.split("%"));
  if (prob.value.split("%")[0] < 5) {
    risk.value = "低";
    color.value = "text-green-500";
  } else {
    risk.value = "高";
    color.value = "text-red-500";
  }
  // console.log(parseInt(prob.split("%")))
};

onMounted(() => {
  calScore();
});
</script>
