<template>
  <div class=" w-full h-soixantedix">
    <div class="h-vint overflow-auto">介绍一下这个问卷</div>
    <div
      class="w-full h-quarantecinq overflow-auto flex flex-wrap justify-evenly content-start"
    >
      <div class="w-2/3 my-2 text-gray-400 font-semibold text-lg">
        输入姓名及手机号以开始
      </div>
      <div class="w-2/3 my-4">
        <div class="grid grid-cols-3 w-full my-2">
          <div class="text-lg font-bold">姓名:</div>
          <input
            class="col-span-2 pl-2 font-bold"
            v-model="name" type="text"
            placeholder="请输入姓名"
          />
        </div>
        <div class="grid grid-cols-3 w-full my-2">
          <div class="text-lg font-bold">电话:</div>
          <input
            class="col-span-2 pl-2 font-bold"
            v-model="phone" type="number"
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

const store = useStore();
const router = useRouter();

const name = ref(store.state.name);
const phone = ref(store.state.phone);
const showAlarm = ref(false);
const confirm = () => {
  if (name.value !== "" && phone.value !== "") {
    console.log(name.value, phone.value);
    store.commit("changeName", name.value);
    store.commit("changePhone", phone.value);
    showAlarm.value = false;
    router.push("questions");
  } else {
    showAlarm.value = true;
  }
};

// 清空内容
const clear = () => {
  name.value = "";
  phone.value = "";
  showAlarm.value = false;
};
</script>
