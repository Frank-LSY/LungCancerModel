<template>
  <div class="bg-sky-50 h-screen w-full">
    <div
      class="w-full h-cinquante"
      style="background-color: rgba(0, 78, 162, 1)"
    >
      <img src="@assets/img/zju.png" class="py-3 pl-6" />
    </div>
    <div class="w-full h-cinquante text-3xl font-bold border-y-4 border-gray-100">
      <div class="pt-7">肺癌风险预测调查</div>
    </div>
    <div>
      <router-view
        v-slot="{ Component }"
        id="main"
        class=" pt-2 h-soixantedix overflow-auto"
      >
        <!-- 切页面时导航栏不动 -->
        <keep-alive>
          <transition :name="transitionName" appear>
            <component :is="Component" />
          </transition>
        </keep-alive>
      </router-view>
    </div>
  </div>
</template>

<script setup>
import { onBeforeRouteUpdate } from "vue-router";
import { ref } from "vue";

const transitionName = ref("slide-up");

onBeforeRouteUpdate((to, from) => {
  if (to.meta.index > from.meta.index) {
    transitionName.value = "slide-up";
  } else {
    transitionName.value = "slide-down";
  }
});
</script>

<style scoped>
.slide-down-enter-active,
.slide-down-leave-active,
.slide-up-enter-active,
.slide-up-leave-active {
  will-change: transform;
  transition: all 500ms;
  position: absolute;
}
.slide-down-enter-from {
  opacity: 0;
  transform: translate3d(0, -100%, 0);
}
.slide-down-leave-active {
  opacity: 0;
  transform: translate3d(0, 100%, 0);
}
.slide-up-enter-from {
  opacity: 0;
  transform: translate3d(0, 100%, 0);
}
.slide-up-leave-active {
  opacity: 0;
  transform: translate3d(0, -100%, 0);
}
</style>
