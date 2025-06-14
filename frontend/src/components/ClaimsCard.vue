<template>
  <div class="mb-8 flex gap-6 px-4 sm:px-8 lg:px-14">
    <RouterLink
      to="/employee/claim/expenses"
      class="flex flex-1 cursor-pointer flex-col items-center justify-center rounded-2xl bg-white px-6 py-8 shadow-xl transition hover:bg-blue-100"
    >
      <div class="text-3xl font-bold text-theme-300">
        {{ totalCount }}
      </div>
      <div class="mt-2 font-semibold text-theme-300">Claims</div>
    </RouterLink>
    <RouterLink
      to="/employee/claim/approved"
      class="flex flex-1 cursor-pointer flex-col items-center rounded-2xl bg-white px-6 py-8 shadow-xl transition hover:bg-[#B0F4EC]"
    >
      <div class="text-3xl font-bold text-[#2A9D8F]">
        {{ approvedCount }}
      </div>
      <div class="mt-2 font-semibold text-[#2A9D8F]">Approved</div>
    </RouterLink>
    <RouterLink
      to="/employee/claim/rejected"
      class="flex flex-1 cursor-pointer flex-col items-center rounded-2xl bg-white px-6 py-8 shadow-xl transition hover:bg-red-100"
    >
      <div class="text-3xl font-bold text-red-600">
        {{ rejectedCount }}
      </div>
      <div class="mt-2 font-semibold text-red-600">Rejected</div>
    </RouterLink>
  </div>
</template>

<script setup>
  import { computed } from "vue";

  const props = defineProps({
    expenses: {
      type: Array,
      required: true,
    },
  });

  const totalCount = computed(() => {
    const ids = new Set(props.expenses.map((e) => e.ClaimID));
    return ids.size;
  });

  const approvedCount = computed(() => {
    const ids = new Set(
      props.expenses
        .filter((e) => e.Status === "Approved")
        .map((e) => e.ClaimID),
    );
    return ids.size;
  });

  const rejectedCount = computed(() => {
    const ids = new Set(
      props.expenses
        .filter((e) => e.Status === "Rejected")
        .map((e) => e.ClaimID),
    );
    return ids.size;
  });
</script>
