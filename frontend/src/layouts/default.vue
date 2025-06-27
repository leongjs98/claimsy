<template>
  <div class="min-h-screen bg-gray-100">
    <Navbar />

    <div class="mb-40">
      <router-view />
    </div>

    <!-- <AppFooter /> -->
    <Chatbot v-if="!route.path.includes('ask-claimsy')" />
  </div>
</template>

<script setup>
  import { useRoute } from "vue-router";
  const route = useRoute();
</script>
