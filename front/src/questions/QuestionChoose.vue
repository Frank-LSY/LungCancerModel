<template>
  <div>
    <div style="color: rgba(0, 78, 162, 1)" class="my-2 py-1 text-xl font-bold">
      {{ props.title }}
    </div>
    <div class="flex flex-wrap justify-center">
      <div
        v-for="i in props.size"
        :key="i"
        class="w-2/3 text-lg font-bold ring-2 ring-gray-400 rounded my-1.5 py-1 cursor-pointer hover:bg-sky-200"
      >
        {{ props.choices[i - 1] }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from "vue";

const props = defineProps({
  size: Number,
  title: String,
  choices: Array,
});
</script>
