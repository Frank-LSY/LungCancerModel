<template>
  <div class=" w-full h-soixantedix">
    <div class="flex flex-wrap justify-end w-19/20">
      <Avatar
        :size="30"
        :name="store.getters.getName"
        variant="sunset"
        :colors="['#004EA2', '#A30300', '#00A0A3', '#1F8BFF', '#00A354']"
      />
      <div class="text-xl font-bold mx-4">
        <span style="color: rgba(0, 78, 162, 1)">{{
          store.getters.getName
        }}</span>，您好!

      </div>
    </div>
    <div @click="goBack()">返回</div>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import Avatar from "vue-boring-avatars";

const store = useStore();
const router = useRouter();

const goBack = () => {
  router.push("check");
};
</script>
