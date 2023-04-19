<template>
  <div>
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
            v-model="name"
            placeholder="请输入姓名"
          />
        </div>
        <div class="grid grid-cols-3 w-full my-2">
          <div class="text-lg font-bold">电话:</div>
          <input
            class="col-span-2 pl-2 font-bold"
            v-model="phone"
            placeholder="请输入电话"
          />
        </div>
      </div>
      <div class="w-2/3 flex flex-wrap justify-evenly text-lg font-bold my-4">
        <div
          class="w-1/3 cursor-pointer rounded ring-4 ring-gray-700 hover:bg-gray-300"
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
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const name = ref("");
const phone = ref("");

// 清空内容
const clear = () => {
  name.value = "";
  phone.value = "";
};
</script>
