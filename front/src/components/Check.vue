<template>
  <div class="w-full h-soixantedix">
    <div class="h-trentecinq overflow-auto flex flex-wrap justify-center content-center">
      <div class="text-gray-500 w-11/12 text-justify">
        <p class="py-2 text-lg">
          <span class="text-gray-900 font-bold">肺癌 </span
          >是中国发病率和死亡率最高的癌症之一。本模型由浙江大学公共卫生学院建立，可供个人及机构评估某个体五年期肺癌的风险。
        </p>
        <!-- <p class="text-gray-300 py-1">
          <span class="text-gray-900 font-semibold">模型基于 </span>Wu, X., Wen,
          C., Ye, Y. et al. Personalized Risk Assessment in Never, Light, and
          Heavy Smokers in a prospective cohort in Taiwan. Sci Rep 6, 36482
          (2016). https://doi.org/10.1038/srep36482
        </p> -->
        <p class="py-1 italic text-gray-400">
          * 问卷给出的五年期肺癌概率仅供参考，具体请前往正规医疗机构并咨询专业医生。
        </p>
      </div>
    </div>
    <div
      class="w-full h-trente overflow-auto flex flex-wrap justify-evenly content-start"
    >
      <div class="w-2/3 my-2 text-gray-400 font-semibold text-lg">
        输入姓名及手机号以开始
      </div>
      <div class="w-2/3 my-4">
        <div class="grid grid-cols-3 w-full my-2">
          <div class="text-lg font-bold">姓名:</div>
          <input
            class="col-span-2 pl-2 font-bold"
            v-model="name"
            type="text"
            placeholder="请输入姓名"
          />
        </div>
        <div class="grid grid-cols-3 w-full my-2">
          <div class="text-lg font-bold">电话:</div>
          <input
            class="col-span-2 pl-2 font-bold"
            v-model="phone"
            type="number"
            placeholder="请输入电话"
          />
        </div>
      </div>
      <div class="w-2/3 flex flex-wrap justify-evenly text-lg font-bold my-4">
        <div
          class="w-1/3 cursor-pointer rounded ring-4 ring-gray-700 hover:bg-gray-300"
          @click="confirm()"
        >
          确定
        </div>
        <div
          class="w-1/3 cursor-pointer rounded ring-4 ring-gray-700 hover:bg-red-100"
          @click="clear()"
        >
          清空
        </div>
      </div>
      <div
        class="w-2/3 text-lg font-bold text-red-600 animatecss animatecss-fadeIn"
        v-if="showAlarm"
      >
        请输入姓名及电话！
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import userAPI from "@/api/user";
import { errorMessage, infoMessage, successMessage } from "@/assets/js/common";

const store = useStore();
const router = useRouter();

const name = ref(store.state.name);
const phone = ref(store.state.phone);
const showAlarm = ref(false);
const confirm = () => {
  if (name.value !== "" && phone.value !== "") {
    userAPI
      .checkUser({
        username: name.value,
        phone: phone.value,
      })
      .then((res) => {
        store.commit("changeName", name.value);
        store.commit("changePhone", phone.value);
        store.commit("changeUserid", res.data);
        // console.log(res.data);
        // infoMessage("老用户!");
        showAlarm.value = false;
        router.push("history");
      })
      .catch((err) => {
        infoMessage(err);
        userAPI
          .createUser({
            username: name.value,
            phone: phone.value,
          })
          .then((result) => {
            store.commit("changeName", name.value);
            store.commit("changePhone", phone.value);
            store.commit("changeUserid", result.data.data);
            store.commit("changeAnswer", {});
            console.log(result.data);
            successMessage(result.message);
            router.push("questions");
          })
          .catch((error) => {
            errorMessage(error);
          });
        console.log(err);
      });
  } else {
    showAlarm.value = true;
  }

  // if (name.value !== "" && phone.value !== "") {
  //   console.log(name.value, phone.value);
  //   store.commit("changeName", name.value);
  //   store.commit("changePhone", phone.value);
  //   showAlarm.value = false;
  //   router.push("questions");
  // } else {
  //   showAlarm.value = true;
  // }
};

// 清空内容
const clear = () => {
  name.value = "";
  phone.value = "";
  showAlarm.value = false;
};
</script>
