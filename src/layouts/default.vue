<template>
  <div class="min-h-screen bg-gray-100">
    <Navbar />

    <v-main>
      <router-view />
    </v-main>

    <!-- <AppFooter /> -->
    <Chatbot
              v-show="!route.path.includes('ask-claimsy')"
    />
  </div>
</template>

<script setup>
  import { useRoute } from "vue-router";
  const route = useRoute();
</script>
