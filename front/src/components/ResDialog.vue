<template>
  <div class="absolute h-soixantedix w-full bg-black bg-opacity-30">
    <div
      class="absolute w-2/3 left-1/6 top-32 h-trente bg-cyan-100 bg-opacity-90 rounded-xl"
    >
      <div class="w-full mt-5 flex flex-wrap content-center">
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
      <div :class="[color, 'text-6xl font-extrabold mt-4']">
        {{ prob }}
      </div>
      <div class="font-bold mt-4">
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
import c2s from "@assets/json/choice2score.json";
import s2p from "@assets/json/score2Prob5.json";

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
  console.log(store.getters.getAnswers);
  //   答案拿过来
  var answers = store.getters.getAnswers;

  //   判断吸烟状况
  if (answers["smoking"] === 1) {
    smoke.value = "never";
    smokeC.value = "不吸烟者";
  } else {
    if (answers["packYear"] === 3) {
      smoke.value = "heavy";
      smokeC.value = "重度吸烟者";
    } else {
      smoke.value = "light";
      smokeC.value = "轻度吸烟者";
    }
  }

  for (var id in answers) {
    // console.log(id, answers[id]);
    score.value += c2s[smoke.value][id][answers[id]];
  }
  console.log(score.value);
  prob.value = s2p[smoke.value][score.value];
};

// 上色
const colorPercent = () => {
  console.log(prob.value.split("%"));
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
  colorPercent();
});
</script>
