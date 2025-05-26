<template>
    <div>
      <header class="bg-blue-900 text-white p-4">
        <div class="flex justify-between">

          <nav class="flex items-center">
            <a href="/">
              <img class="w-7" src="/logo.svg" alt="Claimsy Logo">
            </a>
          </nav>
          <nav class="flex gap-8 justify-between items-center">
            <a href="employee/claim/all">My Claims</a>
            <a href="employee/claim/upload">Receipt Upload</a>
            <a href="#">Point & Rewards</a>
            <a href="#">Ask Claimsy</a>
          </nav>
          <nav class="flex gap-2 items-center">
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
