<template>
  <div
    class="absolute left-0 top-0 h-soixantedix w-full bg-gray-400 bg-opacity-95"
  >
    <div
      class="absolute bottom-2 w-2/3 left-1/6 h-cinq flex flex-wrap justify-center content-center rounded border-2 font-semibold border-orange-300 bg-red-50 cursor-pointer select-none animatecss animatecss-infinite animatecss-pulse"
      @click="closeDialog()"
    >
      关闭
    </div>
    <div
      class="absolute w-11/12 top-8 left-1/24 h-soixante bg-teal-500 bg-opacity-50 border-4 border-gray-400 rounded-sm shadow shadow-gray-500"
    >
      <div class="flex flex-wrap justify-evenly font-bold">
        <div class="w-1/2 sm:w-1/4 text-left pl-2 my-0.5">
          <span class="text-gray-100"
            >{{ store.getters.getQuestions[0]["title"] }}:
          </span>
          <span class="text-amber-300">{{
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
          <span class="text-amber-300">{{
            store.getters.getQuestions[num]["choice"][
              store.getters.getAnswers[
                store.getters.getQuestions[num]["questionid"]
              ] - 1
            ]
          }}</span>
        </div>
        <div class="w-1/2 sm:w-1/4 text-left pl-2 my-0.5">
          <span class="text-gray-100">吸烟情况: </span>
          <span class="text-amber-300">{{ store.getters.getDetail.smoke }}</span>
        </div>
        <div class="w-1/2 sm:w-1/4 text-left pl-2 my-0.5">
          <span class="text-gray-100">癌症史: </span>
          <span class="text-amber-300">{{
            store.getters.getQuestions[3]["choice"][
              store.getters.getAnswers[
                store.getters.getQuestions[3]["questionid"]
              ] - 1
            ]
          }}</span>
        </div>
        <div class="w-1/2 sm:w-1/4 text-left pl-2 my-0.5">
          <span class="text-gray-100">家族史: </span>
          <span class="text-amber-300">{{
            store.getters.getQuestions[4]["choice"][
              store.getters.getAnswers[
                store.getters.getQuestions[4]["questionid"]
              ] - 1
            ]
          }}</span>
        </div>
        <div
          v-for="num in [8, 9, 10]"
          :key="num"
          class="w-1/2 sm:w-1/4 text-left pl-2 my-0.5 last:w-full last:sm:w-1/2"
        >
          <span class="text-gray-100"
            >{{ ceDict[store.getters.getQuestions[num]["questionid"]] }}:
          </span>
          <span class="text-amber-300">{{
            store.getters.getQuestions[num]["choice"][
              store.getters.getDetail.details[num]["choice"] - 1
            ]
          }}</span>
        </div>
        <div
          v-for="num in [13, 14]"
          :key="num"
          class="w-1/2 sm:w-1/4 text-left pl-2 my-0.5 last:w-full last:sm:w-1/2"
        >
          <span class="text-gray-100"
            >{{ ceDict[store.getters.getQuestions[num]["questionid"]] }}:
          </span>
          <span class="text-amber-300">{{
            store.getters.getQuestions[num]["choice"][
              store.getters.getDetail.details[num - 2]["choice"] - 1
            ]
          }}</span>
        </div>
      </div>
      <div class="w-full flex justify-end sm:mt-6">
        <div
          class="w-2/3 sm:w-1/2 border-2 border-gray-200 shadow-xl rounded bg-gray-50 bg-opacity-10 text-right mr-2 text-lg font-bold hover:shadow-2xl"
        >
          <div class="my-2">您的5年期肺癌预测风险为：</div>
          <div :class="[color, 'pr-4']">
            {{
              store.getters.getDetail.details[
                store.getters.getDetail.details.length - 1
              ].probability
            }}
            %
          </div>
        </div>
      </div>
      <div id="riskChart" class="absolute bottom-0 w-full h-trente"></div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

import { useStore } from "vuex";
import * as echarts from "echarts";

const store = useStore();

const questions = ref();

const closeDialog = () => {
  store.commit("changeDetail", {
    showDialog: false,
    details: [],
  });
};

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
    text: "各因素致预测肺癌风险贡献",
    textStyle: {
      color: "#f3f4f6",
    },
  },
  tooltip: {
    trigger: "axis",
    axisPointer: {
      type: "cross",
    },
    formatter: function (params) {
      var line = params[0];
      var assis = params[1];
      //   console.log(line[0])
      return (
        "累计肺癌风险值: " +
        line.value +
        "% <br/> <b>" +
        line.name +
        "</b> 单因素致肺癌风险增值: " +
        " : " +
        assis.value +
        "%"
      );
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
    boundaryGap: true,
    axisLabel: {
      interval: 0,
      rotate: 35,
      color: "#f3f4f6",
      fontWeight: "bold",
    },
  },
  yAxis: {
    type: "value",
    min: 0,
    splitLine: { show: false },
    axisLabel: {
      interval: 0,
      color: "#f3f4f6",
      fontWeight: "bold",
      formatter: function (value, index) {
        return value + "%";
      },
    },
  },
  series: [
    {
      name: "",
      type: "line",
      stack: "Total",
      areaStyle: {},
      label: {
        show: true,
        position: "top",
        distance: 10,
        rotate: 30,
        color: "#fcd34d",
        fontWeight: "bold",
        formatter: function (params) {
          // console.log(params)
          return params.value + "%";
        },
      },
    },
    {
      name: "",
      type: "bar",
      itemStyle: {
        borderColor: "transparent",
        color: "transparent",
      },
    },
  ],
};

// 算分，并保存
const calScore = () => {
  console.log(store.getters.getDetail.details);
  //   prob_dict.value = store.getters.getProb;
  //   smokeC.value = store.getters.getSmoke;
  colorPercent();
  option.xAxis.data = [];
  var prob1 = []
  store.getters.getDetail.details.forEach((item)=> {
    option.xAxis.data.push(ceDict[item.questionid])
    prob1.push(item.probability)
  })
  var prob2 = [prob1[0]];
  for (var i = 1; i < prob1.length; i++) {
    prob2.push((prob1[i] - prob1[i - 1]).toFixed(2));
  }
  option.series[0].data = prob1;
  option.series[1].data = prob2;

  chartDom = document.getElementById("riskChart");
  myChart = echarts.init(chartDom);
  option && myChart.setOption(option);
};

// 上色
const colorPercent = () => {
  // console.log(prob.value.split("%"));
  if (
    store.getters.getDetail.details[store.getters.getDetail.details.length - 1]
      .probability < 5
  ) {
    risk.value = "低";
    color.value = "text-green-300";
  } else {
    risk.value = "高";
    color.value = "text-red-500";
  }
  // console.log(parseInt(prob.split("%")))
};

const ceDict = {
  BMI: "BMI",
  age: "年龄",
  sex: "性别",
  cancer: "癌症史",
  lung: "家族史",
  smoking: "吸烟状态",
  packYear: "年吸烟量",
  smokingIntensity: "每天吸烟",
  MMEF: "MMEF (ml/sec)",
  FEV1: "FEV1 (%)",
  AFP: "AFP (ng/ml)",
  CEA: "CEA (ng/ml)",
  CRP: "CRP (mg/L)",
};

onMounted(() => {
  calScore();
  //   getQuestions();
});
</script>
