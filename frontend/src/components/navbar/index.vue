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
            <!-- TODO: make employee's and admin's version of ask claimsy separted -->
            <NavLink name="Ask Claimsy" link="/ask-claimsy"> </NavLink>
          </ul>
        </nav>
        <nav class="flex items-center gap-2">
          <button>
            <svg
              class="size-7"
              xmlns="http://www.w3.org/2000/svg"
              width="32"
              height="32"
              viewBox="0 0 24 24"
            >
              <!-- Icon from Material Symbols by Google - https://github.com/google/material-design-icons/blob/master/LICENSE -->
              <path
                fill="currentColor"
                d="M4 19v-2h2v-7q0-2.075 1.25-3.687T10.5 4.2v-.7q0-.625.438-1.062T12 2t1.063.438T13.5 3.5v.7q2 .5 3.25 2.113T18 10v7h2v2zm8 3q-.825 0-1.412-.587T10 20h4q0 .825-.587 1.413T12 22m-4-5h8v-7q0-1.65-1.175-2.825T12 6T9.175 7.175T8 10z"
              />
            </svg>
          </button>
          <RouterLink to="/login">
            <svg
              class="size-7"
              xmlns="http://www.w3.org/2000/svg"
              width="32"
              height="32"
              viewBox="0 0 24 24"
            >
              <!-- Icon from Material Symbols by Google - https://github.com/google/material-design-icons/blob/master/LICENSE -->
              <path
                fill="currentColor"
                d="M5.85 17.1q1.275-.975 2.85-1.537T12 15t3.3.563t2.85 1.537q.875-1.025 1.363-2.325T20 12q0-3.325-2.337-5.663T12 4T6.337 6.338T4 12q0 1.475.488 2.775T5.85 17.1M12 13q-1.475 0-2.488-1.012T8.5 9.5t1.013-2.488T12 6t2.488 1.013T15.5 9.5t-1.012 2.488T12 13m0 9q-2.075 0-3.9-.788t-3.175-2.137T2.788 15.9T2 12t.788-3.9t2.137-3.175T8.1 2.788T12 2t3.9.788t3.175 2.137T21.213 8.1T22 12t-.788 3.9t-2.137 3.175t-3.175 2.138T12 22"
              />
            </svg>
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
