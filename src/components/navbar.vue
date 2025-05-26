<template>
    <v-app-bar class="pa-2 bg-indigo-darken-4" density="compact">
      <template v-slot:prepend>
        <a href="/">
          <v-img width="30" aspect-ratio="1/1" cover src="/logo.svg"></v-img>
        </a>
      </template>

      <v-spacer></v-spacer>
      <div class="d-flex ga-2">
        <a href="employee/claim/upload">Receipt Upload</a>
        <a href="employee/claim/all">My Claims</a>
        <a href="#">Points & Rewards</a>
        <a href="#">Ask Claimsy</a>
        <!-- <a href="admin/claim/upload">Admin Claim Upload</a> -->
        <!-- <a href="admin/claim/all">Admin Claim All</a> -->
      </div>
      <v-spacer></v-spacer>

      <template v-slot:append>
        <div class="d-flex">
          <v-btn icon="mdi-bell-outline" size="x-large"></v-btn>
          <v-btn icon="mdi-account-circle" size="x-large"></v-btn>
        </div>
      </template>
    </v-app-bar>
    <v-container>
    </v-container>
  </template>
