<template>
  <div class="mx-auto w-full max-w-6xl">
    <header
      class="rounded-2xl bg-blue-900 px-4 text-white shadow-xl/30 shadow-blue-900"
    >
      <div class="flex justify-between">
        <nav class="flex items-center">
          <a href="/">
            <img class="w-7" src="/logo.svg" alt="Claimsy Logo" />
          </a>
        </nav>
        <nav
          class="flex items-center justify-between gap-8 text-lg font-semibold"
        >
          <a class="py-4" href="employee/claim/all">My Claims</a>
          <a class="py-4" href="employee/claim/upload">Receipt Upload</a>
          <a class="py-4" href="#">Point & Rewards</a>
          <a class="py-4" href="#">Ask Claimsy</a>
          <!-- <a class="py-4 border-b-blue-900 border-b-5" href="employee/claim/all">My Claims</a> -->
          <!-- <a class="py-4 border-b-yellow-500 border-b-5" href="employee/claim/upload">Receipt Upload</a> -->
          <!-- <a class="py-4 border-b-blue-900 border-b-5" href="#">Point & Rewards</a> -->
          <!-- <a class="py-4 border-b-blue-900 border-b-5" href="#">Ask Claimsy</a> -->
        </nav>
        <nav class="flex items-center gap-2">
          <button>
            <v-icon icon="mdi-bell-outline"></v-icon>
          </button>
          <button>
            <v-icon size="36px" icon="mdi-account-circle"></v-icon>
          </button>
          <!-- <v-btn icon="mdi-bell-outline"></v-btn> -->
          <!-- <v-btn icon="mdi-account-circle"></v-btn> -->
        </nav>
      </div>
    </header>
  </div>
</template>
