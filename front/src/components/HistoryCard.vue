<template>
  <div
    class="relative w-11/12 border-4 border-sky-200 shadow-lg rounded font-semibold my-2"
  >
    <div
      class="absolute cursor-pointer bottom-2 left-2 bg-sky-600 bg-opacity-70 text-gray-100 rounded p-1"
      @click="showDetail()"
    >
      查看详情
    </div>
    <div class="text-left ml-2">时间：{{ calcTime() }}</div>
    <div>您的5年期肺癌风险为：</div>
    <div :class="[color, 'text-5xl']">
      {{ props.history.probability }}%
    </div>
    <div class="text-right mr-4">您是 {{ smokeC() }}</div>
    <div class="text-right mr-4">
      您的肺癌风险 <span :class="color">{{ calcRisk() }}</span>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useStore } from "vuex";

const store = useStore();

const props = defineProps({
  history: Object,
});

const color = ref("text-green-500");

const calcColor = () => {
  if (props.history.probability.split("%")[0] < 5) {
    color.value = "text-green-500";
  } else {
    color.value = "text-red-500";
  }
};

const calcTime = () => {
  var dt = new Date(props.history.time).toLocaleString("chinese");
  return dt;
};

const smokeC = () => {
  switch (props.history.smoke) {
    case "NEVER":
      return "不吸烟者";
    case "LIGHT":
      return "轻度吸烟者";
    case "HEAVY":
      return "重度吸烟者";
  }
};

const calcRisk = () => {
  if (props.history.probability.split("%")[0] < 5) {
    return "低";
  } else {
    return "高";
  }
};

onMounted(() => {
  calcColor();
});

// 查看历史详情
const showDetail = () => {
  var showDialog = true;
  var details = props.history.detail;
  console.log({
    showDialog: showDialog,
    details: details,
  })

  store.commit("changeDetail", {
    showDialog: showDialog,
    details: details,
  });
};
</script>
