<template>
  <div class="w-full flex flex-col items-center pt-4 pb-4">
    <div class="inline-flex gap-4 relative">
      <RouterLink
        to="/employee/claim/all"
        class="px-4 py-2 font-normal rounded transition"
        :class="{
          'bg-[#FFAD05] text-white font-semibold': $route.path === '/employee/claim/all',
          'text-gray-900': $route.path !== '/employee/claim/all'
        }"
      >
        My Expenses
      </RouterLink>
      <RouterLink
        to="/employee/claim/expenses"
        class="px-4 py-2 font-normal rounded transition"
        :class="{
          'bg-theme-200 text-white font-semibold': $route.path === '/employee/claim/expenses',
          'text-gray-900': $route.path !== '/employee/claim/expenses'
        }"
      >
        All Claims
      </RouterLink>
      <RouterLink
        to="/employee/claim/approved"
        class="px-4 py-2 font-normal rounded transition"
        :class="{
          'bg-[#2A9D8F] text-white font-semibold': $route.path === '/employee/claim/approved',
          'text-gray-900': $route.path !== '/employee/claim/approved'
        }"
      >
        Approved Claims
      </RouterLink>
      <RouterLink
        to="/employee/claim/rejected"
        class="px-4 py-2 font-normal rounded transition"
        :class="{
          'bg-red-600 text-white font-semibold': $route.path === '/employee/claim/rejected',
          'text-gray-900': $route.path !== '/employee/claim/rejected'
        }"
      >
        Rejected Claims
      </RouterLink>
      <!-- Horizontal line under tabs -->
      <div class="absolute left-0 -bottom-4 w-full flex justify-center pointer-events-none">
        <div class="h-0.5 bg-gray-300 w-full rounded"></div>
      </div>
    </div>
  </div>
</template>