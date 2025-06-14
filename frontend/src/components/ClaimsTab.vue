<template>
  <div class="flex w-full flex-col items-center pt-4 pb-4">
    <div class="relative inline-flex gap-4">
      <RouterLink
        to="/employee/claim/expenses"
        class="rounded px-4 py-2 font-normal transition"
        :class="{
          'bg-[#FFAD05] font-semibold text-white':
            $route.path === '/employee/claim/expenses',
          'text-gray-900': $route.path !== '/employee/claim/expenses',
        }"
      >
        My Expenses
      </RouterLink>
      <RouterLink
        to="/employee/claim/all"
        class="rounded px-4 py-2 font-normal transition"
        :class="{
          'bg-theme-200 font-semibold text-white':
            $route.path === '/employee/claim/all',
          'text-gray-900': $route.path !== '/employee/claim/all',
        }"
      >
        All Claims
      </RouterLink>
      <RouterLink
        to="/employee/claim/approved"
        class="rounded px-4 py-2 font-normal transition"
        :class="{
          'bg-[#2A9D8F] font-semibold text-white':
            $route.path === '/employee/claim/approved',
          'text-gray-900': $route.path !== '/employee/claim/approved',
        }"
      >
        Approved Claims
      </RouterLink>
      <RouterLink
        to="/employee/claim/rejected"
        class="rounded px-4 py-2 font-normal transition"
        :class="{
          'bg-red-600 font-semibold text-white':
            $route.path === '/employee/claim/rejected',
          'text-gray-900': $route.path !== '/employee/claim/rejected',
        }"
      >
        Rejected Claims
      </RouterLink>
      <!-- Horizontal line under tabs -->
      <div
        class="pointer-events-none absolute -bottom-4 left-0 flex w-full justify-center"
      >
        <div class="h-0.5 w-full rounded bg-gray-300"></div>
      </div>
    </div>
  </div>
</template>
