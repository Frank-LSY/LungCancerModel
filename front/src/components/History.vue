<template>
  <div class="w-full h-soixantedix bg-sky-100 bg-opacity-70">
    <div class="flex flex-wrap justify-between w-full h-cinq text-right">
      <div class="text-lg font-bold ml-2" @click="goBack()">返回</div>
      <div class="flex flex-wrap justify-center">
        <Avatar
          :size="25"
          :name="store.getters.getName"
          variant="sunset"
          :colors="['#004EA2', '#A30300', '#00A0A3', '#1F8BFF', '#00A354']"
        />
        <div class="text-lg font-bold mx-2 text-left">
          <span style="color: rgba(0, 78, 162, 1)">{{
            store.getters.getName
          }}</span
          >，您好!
        </div>
      </div>
    </div>
    <div class="text-lg font-bold">
      您之前共有
      <span style="color: rgba(0, 78, 162, 1)">{{ cnt }}</span> 条问卷记录
    </div>
    <div class="h-soixantecinq overflow-auto flex flex-wrap justify-center content-start">
      <history-card
        v-for="history in historyList"
        :key="history" :history="history"
      ></history-card>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import Avatar from "vue-boring-avatars";
import historyAPI from "@/api/history";
import { errorMessage } from "@/assets/js/common";
import HistoryCard from "./HistoryCard.vue";

const store = useStore();
const router = useRouter();

const goBack = () => {
  router.push("check");
};

const historyList = ref([]);
const cnt = ref(0);

const getHistory = () => {
  historyAPI
    .listHistory({
      userid: store.getters.getUserid,
    })
    .then((res) => {
      historyList.value = res.data.data;
      cnt.value = res.data.count;
    })
    .catch((err) => {
      errorMessage(err);
    });
};

onMounted(() => {
  getHistory();
});
</script>
