<template>
  <div class="mx-auto w-full max-w-6xl py-14">
    <div class="flex w-min flex-col gap-3">
      <RouterLink
        class="w-max border-b border-b-blue-900 hover:font-semibold hover:text-blue-900"
        to="employee/claim/upload"
      >
        Employee: Upload Receipt
      </RouterLink>
      <RouterLink
        class="w-max border-b border-b-blue-900 hover:font-semibold hover:text-blue-900"
        to="employee/claim/edit"
      >
        Employee: Edit Receipt
      </RouterLink>
      <RouterLink
        class="w-max border-b border-b-blue-900 hover:font-semibold hover:text-blue-900"
        to="admin/claim/all"
      >
        Admin: Claim Center
      </RouterLink>
      <RouterLink
        class="w-max border-b border-b-blue-900 hover:font-semibold hover:text-blue-900"
        to="admin/policy/upload"
      >
        Admin: Upload Policy
      </RouterLink>
    </div>
  </div>
</template>
