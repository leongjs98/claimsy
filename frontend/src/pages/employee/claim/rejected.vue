<template>
  <div class="mx-auto my-14 w-full max-w-6xl bg-gray-100">
    <!-- Cards Row -->
    <EmployeeClaimsCard
      :totalCount="totalCount"
      :approvedCount="approvedCount"
      :rejectedCount="rejectedCount"
    />
    <!-- Expenses Table -->
    <div class="mt-4 mb-2"></div>
    <div class="mt-8 flow-root px-4 sm:px-8 lg:px-14">
      <div class="-mx-4 -my-2 sm:-mx-6 lg:-mx-8">
        <div class="min-w-full py-2 align-middle sm:px-6 lg:px-8">
          <!-- Tabs Row -->
          <EmployeeClaimsTab />
          <table
            class="min-w-full divide-y divide-gray-300 rounded-b-lg bg-gray-100 drop-shadow-md"
          >
            <thead class="rounded-lg bg-blue-50 text-theme-300">
              <tr>
                <th
                  class="rounded-tl-lg py-3 pr-3.5 pl-4 text-right text-sm font-semibold sm:pl-6"
                >
                  #
                </th>
                <th class="py-3.5 pr-3 pl-3.5 text-left text-sm font-semibold">
                  Claim ID
                </th>
                <th
                  class="flex justify-center px-3 py-3.5 text-sm font-semibold"
                >
                  <button
                    class="flex items-center justify-center gap-2 hover:cursor-pointer"
                    @click="sortDateAsc = !sortDateAsc"
                  >
                    <span>Date</span>
                    <svg
                      v-if="sortDateAsc"
                      class="h-5 w-5"
                      xmlns="http://www.w3.org/2000/svg"
                      width="32"
                      height="32"
                      viewBox="0 0 24 24"
                    >
                      <path
                        fill="currentColor"
                        d="M21 17h3l-4 4l-4-4h3V3h2zM8 16h3v-3H8zm5-11h-1V3h-2v2H6V3H4v2H3c-1.11 0-2 .89-2 2v11c0 1.11.89 2 2 2h10c1.11 0 2-.89 2-2V7c0-1.11-.89-2-2-2M3 18v-7h10v7z"
                      />
                    </svg>
                    <svg
                      v-else
                      class="h-5 w-5"
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 24 24"
                    >
                      <path
                        fill="currentColor"
                        d="M19 7h-3l4-4l4 4h-3v14h-2zM8 16h3v-3H8zm5-11h-1V3h-2v2H6V3H4v2H3c-1.11 0-2 .89-2 2v11c0 1.11.89 2 2 2h10c1.11 0 2-.89 2-2V7c0-1.11-.89-2-2-2M3 18v-7h10v7z"
                      />
                    </svg>
                  </button>
                </th>
                <th class="px-3 py-3.5 text-center text-sm font-semibold">
                  Quantity
                </th>
                <th class="px-3 py-3.5 text-right text-sm font-semibold">
                  Total (RM)
                </th>
                <th class="w-48 px-3 py-3.5 text-center text-sm font-semibold">
                  Status
                </th>
                <th
                  class="w-48 rounded-tr-lg px-3 py-3.5 text-center text-sm font-semibold"
                ></th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200 bg-white">
              <tr
                v-for="(expense, index) in sortedRejectedExpenses"
                :key="expense.Id"
                class="shadow-md"
              >
                <td
                  :class="[
                    'py-4 pr-3 pl-4 text-right text-sm font-medium whitespace-nowrap text-gray-900 sm:pl-6',
                    index === sortedRejectedExpenses.length - 1
                      ? 'rounded-bl-lg'
                      : '',
                  ]"
                >
                  {{ index + 1 }}
                </td>
                <!-- <td class="px-3 py-4 text-sm whitespace-nowrap text-gray-500">{{ person.Name }}</td> -->
                <td class="px-3 py-4 text-sm whitespace-nowrap text-gray-500">
                  {{ expense.Id }}
                </td>
                <td
                  class="px-3 py-4 text-center text-sm whitespace-nowrap text-gray-500"
                >
                  {{ expense.Date }}
                </td>
                <td
                  class="px-3 py-4 text-center text-sm whitespace-nowrap text-gray-500"
                >
                  {{ expense.Quantity }}
                </td>
                <td
                  class="px-4 py-4 text-right text-sm whitespace-nowrap text-gray-500"
                >
                  {{
                    expense.Total.toLocaleString("en-US", {
                      minimumFractionDigits: 2,
                      maximumFractionDigits: 2,
                    })
                  }}
                </td>

                <td
                  class="px-4 py-4 text-center text-sm font-semibold whitespace-nowrap"
                >
                  <StatusBadge :status="expense.Status" />
                </td>
                <td
                  :class="[
                    'px-4 py-4 text-center text-sm whitespace-nowrap text-gray-500',
                    index === sortedRejectedExpenses.length - 1
                      ? 'rounded-br-lg'
                      : '',
                  ]"
                >
                  Details
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, computed } from "vue";
  import { storeToRefs } from "pinia";
  import { useEmployeeClaimStore } from "@/stores/employee-claims.ts";

  const sortDateAsc = ref(false);
  const claimStore = useEmployeeClaimStore();
  const { totalCount, approvedCount, rejectedCount } = storeToRefs(claimStore);

  const sortedRejectedExpenses = computed(() => {
    const sortedExpenses = sortDateAsc.value
      ? claimStore.getExpensesByDateAsc
      : claimStore.getExpensesByDateDesc;
    return sortedExpenses.filter(
      (sortedExpenses) => sortedExpenses.Status.toLowerCase() === "rejected",
    );
  });

  onMounted(async () => {
    claimStore.initStore();
  });
</script>
