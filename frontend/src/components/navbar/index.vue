<template>
  <div class="z-50 mx-auto mt-8 w-full max-w-6xl">
    <header
      class="rounded-2xl bg-theme-300 px-4 text-white shadow-xl/30 shadow-blue-900"
    >
      <div class="flex justify-between">
        <nav class="flex items-center">
          <RouterLink to="/">
            <!-- <img class="w-7" src="/logo.svg" alt="Claimsy Logo" /> -->
            <img class="w-32" src="/logo_with_title.svg" alt="Claimsy Logo" />
          </RouterLink>
        </nav>

        <nav
          class="navbar__menu absolute top-16 right-0 left-0 z-40 origin-top border-b-8 border-b-yellow-300 pt-14 pb-8 font-semibold transition-transform delay-200 ease-in-out md:static md:flex md:h-16 md:items-end md:justify-end md:border-none md:p-0"
        >
          <ul
            class="flex flex-col items-center justify-end gap-4 md:flex-row md:gap-5"
          >
            <NavLink
              name="Dashboard"
              link="/admin/dashboard"
              v-if="route.path.includes('admin')"
            >
            </NavLink>
            <NavLink
              name="Claim Center"
              link="/admin/claim/all"
              v-if="route.path.includes('admin')"
            >
            </NavLink>
            <NavLink
              name="Policy Management"
              link="/admin/policy/upload"
              v-if="route.path.includes('admin')"
            >
            </NavLink>
            <NavLink
              name="My Claims"
              link="/employee/claim/all"
              v-if="!route.path.includes('admin')"
            >
            </NavLink>

            <NavLink
              name="Upload Receipt"
              link="/employee/claim/upload"
              v-if="!route.path.includes('admin')"
            >
            </NavLink>
            <!-- <NavLink -->
            <!--   name="Point & Rewards" -->
            <!--   link="/employee/rewards" -->
            <!--   v-if="!route.path.includes('admin')" -->
            <!-- > -->
            <!-- </NavLink> -->
            <NavLink name="Ask Claimsy" link="/ask-claimsy"> </NavLink>
          </ul>
        </nav>
        <nav class="flex items-center gap-2">
          <button>
            <v-icon icon="mdi-bell-outline"></v-icon>
          </button>
          <RouterLink to="/login">
            <v-icon size="36px" icon="mdi-account-circle"></v-icon>
          </RouterLink>
        </nav>
      </div>
    </header>
  </div>
</template>

<script setup>
  import { useRoute } from "vue-router";
  const route = useRoute();
</script>
