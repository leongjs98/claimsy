<template>
    <div class="mx-auto w-full max-w-6xl">
      <header class="rounded-2xl bg-blue-900 px-4 text-white shadow-xl/30 shadow-blue-900">
        <div class="flex justify-between">
          <nav class="flex items-center">
            <a href="/">
              <img class="w-7" src="/logo.svg" alt="Claimsy Logo" />
            </a>
          </nav>

          <nav
            class="navbar__menu absolute left-0 right-0 top-16 z-40 origin-top border-b-8 border-b-yellow-300 pb-8 pt-14 font-semibold transition-transform delay-200 ease-in-out md:static md:flex md:h-16 md:items-end md:justify-end md:border-none md:p-0">
            <ul class="flex flex-col items-center justify-end gap-4 md:flex-row md:gap-5">
              <Link name="My Claims" link="employee/claim/all" :isActive="false">
              </Link>
              <Link name="Receipt Upload" link="employee/claim/upload" :isActive="false">
              </Link>
              <Link name="Point & Rewards" link="#" :isActive="false">
              </Link>
              <Link name="Ask Claimsy" link="#" :isActive="false">
              </Link>
            </ul>
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
