<template>
  <div>
    <div class="hidden py-4 sm:block">
      <div class="border-b border-gray-200">
        <nav class="-mb-px flex items-center justify-center" aria-label="Tabs">
          <RouterLink
            to="/admin/claim/all"
            class="w-1/4 border-b-2 px-1 py-4 text-center text-sm font-medium"
            :class="{
              'border-theme-200 text-theme-300':
                $route.path === '/admin/claim/all',
              'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700':
                $route.path !== '/admin/claim/all',
            }"
            :aria-current="{
              page: $route.path === '/admin/claim/all',
            }"
          >
            All Claims
          </RouterLink>
          <RouterLink
            to="/admin/claim/approved"
            class="w-1/4 border-b-2 px-1 py-4 text-center text-sm font-medium"
            :class="{
              'border-theme-200 text-theme-300':
                $route.path === '/admin/claim/approved',
              'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700':
                $route.path !== '/admin/claim/approved',
            }"
            :aria-current="{
              page: $route.path === '/admin/claim/approved',
            }"
          >
            Approved
          </RouterLink>
          <RouterLink
            to="/admin/claim/rejected"
            class="w-1/4 border-b-2 px-1 py-4 text-center text-sm font-medium"
            :class="{
              'border-theme-200 text-theme-300':
                $route.path === '/admin/claim/rejected',
              'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700':
                $route.path !== '/admin/claim/rejected',
            }"
            :aria-current="{
              page: $route.path === '/admin/claim/rejected',
            }"
          >
            Rejected
          </RouterLink>
        </nav>
      </div>
    </div>
  </div>
</template>
