<template>
  <div class="bg-sky-50">
    <div
      class="w-full h-cinquante"
      style="background-color: rgba(0, 78, 162, 1)"
    >
      <img src="@assets/img/zju.png" class="py-3 pl-6" />
    </div>
    <div class="w-full h-vint text-3xl font-bold">
      <div class="pt-10">肺癌风险预测调查</div>
    </div>
    <router-view class="h-soixantecinq overflow-auto"></router-view>
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
