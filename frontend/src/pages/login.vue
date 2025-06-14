<template>
  <div class="mx-auto w-full max-w-6xl py-14">
    <div>
      <RouterLink
        to="/admin/dashboard"
        class="focus:ring-opacity-75 m-2 inline-block rounded-lg bg-blue-500 px-6 py-3 font-semibold text-white shadow-md hover:bg-blue-600 focus:ring-2 focus:ring-blue-400 focus:outline-none"
      >
        Admin
      </RouterLink>

      <RouterLink
        to="/employee/claim/all"
        class="focus:ring-opacity-75 m-2 inline-block rounded-lg bg-green-500 px-6 py-3 font-semibold text-white shadow-md hover:bg-green-600 focus:ring-2 focus:ring-green-400 focus:outline-none"
      >
        Employee
      </RouterLink>
    </div>
  </div>
</template>
