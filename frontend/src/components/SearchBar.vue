<template>
  <div style="margin: 12px 0;">
    <input v-model="q" placeholder="Cari nama / username..." />
    <button @click="$emit('on-search', q)">Cari</button>
  </div>
</template>

<script setup>
import { ref } from "vue";
const q = ref("");
</script>
