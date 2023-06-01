<template>
  <div class="absolute left-0 top-0 h-soixantedix w-full bg-black bg-opacity-30">
    <div
      class="absolute w-2/3 left-1/6 top-32 h-trente bg-cyan-100 bg-opacity-90 rounded-xl shadow-lg"
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
      <div class="font-bold h-dix text-left ml-4">
        <div>您是 {{ smokeC }}</div>
        <div>
          您的肺癌风险 <span :class="color">{{ risk }}</span>
        </div>
      </div>
      <div
        class="absolute right-2 bottom-2 cursor-pointer px-2 rounded text-gray-200 bg-sky-500"
        @click="router.push('history')"
      >
        返回主页
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useStore } from "vuex";
import Avatar from "vue-boring-avatars";
import resultsAPI from "@/api/results";
import { errorMessage, infoMessage } from "@/assets/js/common";
import { useRouter } from "vue-router";

const store = useStore();
const router = useRouter();

// 分数
const score = ref(0);
// 概率
const prob = ref("");
const risk = ref("很低");
const color = ref("text-green-500");
const smoke = ref("");
const smokeC = ref("");

// 算分，并保存
const calScore = () => {
  if (store.getters.getPollid) {
    infoMessage("已保存");
    prob.value = store.getters.getProb;
    smokeC.value = store.getters.getSmoke;
    colorPercent();
  } else {
    resultsAPI
      .calcProbability({
        userid: store.getters.getUserid,
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
        store.commit("changePollid", res.data.pollid);
        store.commit("changeProb", prob.value);
        store.commit("changeSmoke", smokeC.value);
      })
      .catch((err) => {
        errorMessage(err);
      });
  }
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
