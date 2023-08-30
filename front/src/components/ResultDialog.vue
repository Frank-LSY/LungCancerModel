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
          <span class="text-amber-300">{{ smokeC }}</span>
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
          v-for="num in [8, 9, 10, 13, 14]"
          :key="num"
          class="w-1/2 sm:w-1/4 text-left pl-2 my-0.5 last:w-full last:sm:w-1/2"
        >
          <span class="text-gray-100"
            >{{ ceDict[store.getters.getQuestions[num]["questionid"]] }}:
          </span>
          <span class="text-amber-300">{{
            store.getters.getQuestions[num]["choice"][
              store.getters.getAnswers[
                store.getters.getQuestions[num]["questionid"]
              ] - 1
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
            {{ Object.values(prob_dict).pop() }} %
          </div>
        </div>
      </div>
      <div id="riskChart" class="absolute bottom-0 w-full h-trente"></div>
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
    position: [45, 22],
    textStyle: { fontSize: 10 },

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
        (assis.value > 0 ? '<span style="color:red">' : "") +
        assis.value +
        (assis.value > 0 ? "</span>" : "") +
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
    // {
    //   name: "",
    //   type: "bar",
    //   stack: "Total",
    //   itemStyle: {
    //     borderColor: "transparent",
    //     color: "transparent",
    //   },
    //   emphasis: {
    //     itemStyle: {
    //       borderColor: "transparent",
    //       color: "transparent",
    //     },
    //   },
    // },
    // {
    //   name: "",
    //   type: "bar",
    //   stack: "Total",
    //   label: {
    //     show: true,
    //     position: "inside",
    //   },
    // },
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
  if (store.getters.getPollid) {
    infoMessage("已保存");
    prob_dict.value = store.getters.getProb;
    console.log(prob_dict.value);
    smokeC.value = store.getters.getSmoke;
    colorPercent();
    var keys = Object.keys(prob_dict.value);
    console.log(keys);
    option.xAxis.data = [];
    keys.forEach((item) => {
      option.xAxis.data.push(ceDict[item]);
    });

    // prob.value.pop(0);
    // prob.value.unshift(0);
    var prob1 = Object.values(prob_dict.value);
    var prob2 = [prob1[0]];
    for (var i = 1; i < prob1.length; i++) {
      prob2.push((prob1[i] - prob1[i - 1]).toFixed(2));
    }
    option.series[0].data = prob1;
    option.series[1].data = prob2;

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
        // console.log(res.data.probability);
        prob_dict.value = res.data.probability;
        var keys = Object.keys(prob_dict.value);
        console.log(keys);
        option.xAxis.data = [];
        keys.forEach((item) => {
          option.xAxis.data.push(ceDict[item]);
        });
        var prob1 = Object.values(prob_dict.value);
        var prob2 = [prob1[0]];
        for (var i = 1; i < prob1.length; i++) {
          prob2.push((prob1[i] - prob1[i - 1]).toFixed(2));
        }
        option.series[0].data = prob1;
        option.series[1].data = prob2;

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
        colorPercent();
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
  // console.log(Object.values(prob_dict.value));
  if (
    Object.values(prob_dict.value)[Object.values(prob_dict.value).length - 1] <
    5
  ) {
    risk.value = "低";
    color.value = "text-green-300";
  } else {
    risk.value = "高";
    color.value = "text-red-500";
  }
  // console.log(parseInt(prob.split("%")))
};

onMounted(() => {
  calScore();

  //   console.log(Object.keys(store.getters.getAnswers));
});

const ceDict = {
  BMI: "BMI",
  age: "年龄",
  sex: "性别",
  cancer: "癌症史",
  lung: "家族史",
  smoking: "吸烟状态",
  packYear: "年吸烟量",
  smokingIntensity: "日吸烟量",
  MMEF: "MMEF (ml/sec)",
  FEV1: "FEV1 (%)",
  AFP: "AFP (ng/ml)",
  CEA: "CEA (ng/ml)",
  CRP: "CRP (mg/L)",
};
</script>
