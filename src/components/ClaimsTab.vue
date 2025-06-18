<template>
  <div class="w-full flex flex-col items-center pt-4">
    <div class="inline-flex relative mb-4">
      <RouterLink
        to="/employee/claim/all"
        class="bg-gray-200 shadow-lg w-50 text-center px-2 py-2 font-normal rounded transition text-sm"
        :class="{
          'bg-theme-200 text-white font-semibold': $route.path === '/employee/claim/all',
          'text-gray-900': $route.path !== '/employee/claim/all'
        }"
      >
        Expenses
      </RouterLink>
      <RouterLink
        to="/employee/claim/expenses"
        class="bg-gray-200 shadow-lg w-50 px-2 py-2 text-center font-normal rounded transition text-sm"
        :class="{
          'bg-theme-200 text-white font-semibold': $route.path === '/employee/claim/expenses',
          'text-gray-900': $route.path !== '/employee/claim/expenses'
        }"
      >
        History
      </RouterLink>
      <!-- <RouterLink
        to="/employee/claim/approved"
        class="bg-gray-200 shadow w-50 text-center px-2 py-2 font-normal rounded transition text-sm"
        :class="{
          'bg-theme-200 text-white font-semibold': $route.path === '/employee/claim/approved',
          'text-gray-900': $route.path !== '/employee/claim/approved'
        }"
      >
        Approved Claims
      </RouterLink>
      <RouterLink
        to="/employee/claim/rejected"
        class="bg-gray-200 shadow-lg w-50 text-center px-2 py-2 font-normal rounded transition text-sm"
        :class="{
          'bg-theme-200 text-white font-semibold': $route.path === '/employee/claim/rejected',
          'text-gray-900': $route.path !== '/employee/claim/rejected'
        }"
      >
        Rejected Claims
      </RouterLink> -->
      <!-- Horizontal line under tabs -->
      <!-- <div class="absolute left-0 -bottom-4 w-full flex justify-center pointer-events-none ">
        <div class="h-0.5 bg-red-300 w-full rounded"></div>
      </div> -->
    </div>
  </div>
</template>