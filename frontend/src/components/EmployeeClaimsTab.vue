<template>
  <div>
    <div class="hidden py-4 sm:block">
      <div class="border-b border-gray-200">
        <nav class="-mb-px flex" aria-label="Tabs">
          <RouterLink
            to="/employee/claim/expenses"
            class="w-1/4 border-b-2 px-1 py-4 text-center text-sm font-medium"
            :class="{
              'border-theme-200 text-theme-300':
                $route.path === '/employee/claim/expenses',
              'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700':
                $route.path !== '/employee/claim/expenses',
            }"
            :aria-current="{
              page: $route.path === '/employee/claim/expenses',
            }"
          >
            Unsubmitted Invoices
          </RouterLink>
          <RouterLink
            to="/employee/claim/all"
            class="w-1/4 border-b-2 px-1 py-4 text-center text-sm font-medium"
            :class="{
              'border-theme-200 text-theme-300':
                $route.path === '/employee/claim/all',
              'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700':
                $route.path !== '/employee/claim/all',
            }"
            :aria-current="{
              page: $route.path === '/employee/claim/all',
            }"
          >
            All Claims
          </RouterLink>
          <RouterLink
            to="/employee/claim/approved"
            class="w-1/4 border-b-2 px-1 py-4 text-center text-sm font-medium"
            :class="{
              'border-theme-200 text-theme-300':
                $route.path === '/employee/claim/approved',
              'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700':
                $route.path !== '/employee/claim/approved',
            }"
            :aria-current="{
              page: $route.path === '/employee/claim/approved',
            }"
          >
            Approved
          </RouterLink>
          <RouterLink
            to="/employee/claim/rejected"
            class="w-1/4 border-b-2 px-1 py-4 text-center text-sm font-medium"
            :class="{
              'border-theme-200 text-theme-300':
                $route.path === '/employee/claim/rejected',
              'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700':
                $route.path !== '/employee/claim/rejected',
            }"
            :aria-current="{
              page: $route.path === '/employee/claim/rejected',
            }"
          >
            Rejected
          </RouterLink>
        </nav>
      </div>
    </div>
  </div>
</template>
