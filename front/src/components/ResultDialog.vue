<template>
  <div
    class="absolute left-0 top-0 h-soixantedix w-full bg-gray-400 bg-opacity-95"
  >
    <div
      class="absolute w-11/12 top-8 left-1/24 h-soixante bg-teal-500 bg-opacity-50 border-4 border-gray-400 rounded-sm shadow shadow-gray-500"
    >
      <div class="flex flex-wrap justify-evenly font-bold">
        <div class="w-1/2 sm:w-1/4 text-left pl-2 my-0.5">
          <span class="text-gray-100"
            >{{ store.getters.getQuestions[0]["title"] }}:
          </span>
          <span class="text-amber-400">{{
            store.getters.getQuestions[0]["choice"][
              store.getters.getAnswers[
                store.getters.getQuestions[0]["questionid"]
              ] + 1
            ]
          }}</span>
        </div>
        <div
          v-for="num in [1, 2]"
          :key="num"
          class="w-1/2 sm:w-1/4 text-left pl-2 my-0.5"
        >
          <span class="text-gray-100"
            >{{ store.getters.getQuestions[num]["title"] }}:
          </span>
          <span class="text-amber-400">{{
            store.getters.getQuestions[num]["choice"][
              store.getters.getAnswers[
                store.getters.getQuestions[num]["questionid"]
              ] - 1
            ]
          }}</span>
        </div>
        <div class="w-1/2 sm:w-1/4 text-left pl-2 my-0.5">
          <span class="text-gray-100">吸烟情况: </span>
          <span class="text-amber-400">{{ smokeC }}</span>
        </div>
        <div class="w-1/2 sm:w-1/4 text-left pl-2 my-0.5">
          <span class="text-gray-100">癌症史: </span>
          <span class="text-amber-400">{{
            store.getters.getQuestions[3]["choice"][
              store.getters.getAnswers[
                store.getters.getQuestions[3]["questionid"]
              ] - 1
            ]
          }}</span>
        </div>
        <div class="w-1/2 sm:w-1/4 text-left pl-2 my-0.5">
          <span class="text-gray-100">家族史: </span>
          <span class="text-amber-400">{{
            store.getters.getQuestions[4]["choice"][
              store.getters.getAnswers[
                store.getters.getQuestions[4]["questionid"]
              ] - 1
            ]
          }}</span>
        </div>
        <div
          v-for="num in [8, 9, 10, 13, 14]"
          :key="num"
          class="w-1/2 sm:w-1/4 text-left pl-2 my-0.5 last:w-full last:sm:w-1/2"
        >
          <span class="text-gray-100"
            >{{ ceDict[store.getters.getQuestions[num]["questionid"]] }}:
          </span>
          <span class="text-amber-400">{{
            store.getters.getQuestions[num]["choice"][
              store.getters.getAnswers[
                store.getters.getQuestions[num]["questionid"]
              ] - 1
            ]
          }}</span>
        </div>
      </div>
      <div>
        {{ prob_dict }}
      </div>
      <div id="riskChart" class="absolute bottom-2 w-full h-trentecinq"></div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import resultsAPI from "@/api/results";
import { errorMessage, infoMessage } from "@/assets/js/common";
import * as echarts from "echarts";

const store = useStore();
const router = useRouter();

// 概率

const risk = ref("很低");
const color = ref("text-green-500");
const smoke = ref("");
const smokeC = ref("");

// 作图需要
var chartDom;
var myChart;
const qid = ref([]);
const prob = ref([]);
const prob_dict = ref({});
var option = {
  title: {
    text: "各因素概率",
  },
  tooltip: {
    trigger: "axis",
    axisPointer: {
      type: "shadow",
    },
    formatter: function (params) {
      var tar = params[1];
      return tar.name + " : " + tar.value;
    },
  },
  grid: {
    left: "3%",
    right: "4%",
    bottom: "3%",
    containLabel: true,
  },
  xAxis: {
    type: "category",
    splitLine: { show: false },
  },
  yAxis: {
    type: "value",
  },
  series: [
    {
      name: "Placeholder",
      type: "bar",
      stack: "Total",
      itemStyle: {
        borderColor: "transparent",
        color: "transparent",
      },
      emphasis: {
        itemStyle: {
          borderColor: "transparent",
          color: "transparent",
        },
      },
    },
    {
      name: "Life Cost",
      type: "bar",
      stack: "Total",
      label: {
        show: true,
        position: "inside",
      },
    },
  ],
};

// 算分，并保存
const calScore = () => {
  if (store.getters.getPollid) {
    infoMessage("已保存");
    prob_dict.value = store.getters.getProb;
    smokeC.value = store.getters.getSmoke;

    option.xAxis.data = Object.keys(prob_dict.value);
    prob.value = Object.values(prob_dict.value);
    prob.value.pop();
    prob.value.unshift(0);
    option.series[0].data = prob.value;
    option.series[1].data = [];
    for (let i = 0; i < prob.value.length; i++) {
      option.series[1].data.push(
        (Object.values(prob_dict.value)[i] - prob.value[i]).toFixed(2)
      );
    }

    chartDom = document.getElementById("riskChart");
    myChart = echarts.init(chartDom);
    option && myChart.setOption(option);

  } else {
    resultsAPI
      .calcProbability({
        userid: store.getters.getUserid,
        answers: store.getters.getAnswers,
      })
      .then((res) => {
        console.log(res.data.probability);
        qid.value = Object.keys(res.data.probability);
        prob_dict.value = res.data.probability;
        option.xAxis.data = Object.keys(res.data.probability);
        prob.value = Object.values(prob_dict.value);
        prob.value.pop();
        prob.value.unshift(0);
        option.series[0].data = prob.value;
        option.series[1].data = [];
        for (let i = 0; i < prob.value.length; i++) {
        option.series[1].data.push(
            (Object.values(prob_dict.value)[i] - prob.value[i]).toFixed(2)
        );
        }

        chartDom = document.getElementById("riskChart");
        myChart = echarts.init(chartDom);
        option && myChart.setOption(option);

        // prob.value = res.data.probability;
        smoke.value = res.data.smoking;
        switch (smoke.value) {
          case "LIGHT":
            smokeC.value = "轻度吸烟";
            break;
          case "NEVER":
            smokeC.value = "不吸烟";
            break;
          case "HEAVY":
            smokeC.value = "重度吸烟";
            break;
        }
        // colorPercent();
        store.commit("changePollid", res.data.pollid);
        store.commit("changeProb", res.data.probability);
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

  console.log(Object.keys(store.getters.getAnswers));
});

const ceDict = {
  BMI: "BMI",
  age: "年龄",
  sex: "性别",
  cancer: "癌症史",
  lung: "家族史",
  smoking: "吸烟状态",
  packYear: "年吸烟量",
  smokingIntensity: "每天吸烟",
  MMEF: "MMEF ml/sec",
  FEV1: "FEV1 %",
  AFP: "AFP ng/ml",
  CEA: "CEA ng/ml",
  CRP: "CRP mg/L",
};
</script>
