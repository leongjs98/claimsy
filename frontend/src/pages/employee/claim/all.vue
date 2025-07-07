<!-- Employee Claim -->
<template>
    <div class="mx-auto my-14 w-full max-w-6xl bg-gray-100">
    <!-- Loading State -->
    <div v-if="claimStore.loading" class="flex justify-center py-8">
      <div class="text-lg">Loading claims...</div>
    </div>

    <!-- Error State -->
    <div v-if="claimStore.error" class="mx-4 p-4 bg-red-100 text-red-700 rounded">
      {{ claimStore.error }}
    </div>

    <!-- Main Content -->
    <div v-if="!claimStore.loading">
      <EmployeeClaimsCard
        :totalCount="totalCount"
        :approvedCount="approvedCount"
        :rejectedCount="rejectedCount"
      />

    <div class="mt-4 mb-2"></div>
    <div class="mt-8 flow-root px-4 sm:px-8 lg:px-14">
      <div class="-mx-4 -my-2 sm:-mx-6 lg:-mx-8">
        <div class="min-w-full py-2 align-middle sm:px-6 lg:px-8">
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
                  class="sr-only w-48 rounded-tr-lg px-3 py-3.5 text-left text-sm font-semibold"
                >
                  Details
                </th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200 bg-white">
              <tr
                v-for="(claim, index) in sortedExpenses"
                :key="claim.id"
                class="shadow-md"
              >
                <td
                  :class="[
                    'py-4 pr-3 pl-4 text-right text-sm font-medium whitespace-nowrap text-gray-900 sm:pl-6',
                    index === sortedExpenses.length - 1 ? 'rounded-bl-lg' : '',
                  ]"
                >
                  {{ index + 1 }}
                </td>
                <!-- <td class="px-3 py-4 text-sm whitespace-nowrap text-gray-500">{{ person.Name }}</td> -->
                <td class="px-3 py-4 text-sm whitespace-nowrap text-gray-500">
                  {{ claim.claim_number }}
                </td>
                <td
                  class="px-3 py-4 text-center text-sm whitespace-nowrap text-gray-500"
                >
                  {{ formatDate(claim.submitted_date) }}
                </td>
                <td
                  class="px-3 py-4 text-center text-sm whitespace-nowrap text-gray-500"
                >
                  {{ claim.Items?.length || 0 }}
                </td>
                <td
                  class="px-4 py-4 text-right text-sm whitespace-nowrap text-gray-500"
                >
                  {{
                      claim.claim_amount.toLocaleString("en-US", {
                      minimumFractionDigits: 2,
                      maximumFractionDigits: 2,
                    })
                  }}
                </td>

                <td
                  class="px-4 py-4 text-center text-sm font-semibold whitespace-nowrap"
                >
                  <StatusBadge :status="claim.status" />
                </td>
                <td
                  :class="[
                    'px-4 py-4 text-center text-sm whitespace-nowrap text-theme-300',
                    index === sortedExpenses.length - 1 ? 'rounded-br-lg' : '',
                  ]"
                >
                  <button
                    class="text-theme-300 hover:underline"
                    @click="openDetails(claim)"
                  >
                    Details
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</div>

  <EmployeeClaimDetailsDialog v-model="showDialog" :data="selectedClaim" />
</template>

<script setup>
  import { ref, computed, onMounted } from "vue";
  import { storeToRefs } from "pinia";
  import { useEmployeeClaimStore } from "@/stores/employee-claims.ts";

  const showDialog = ref(false);
  const selectedClaim = ref();
  const sortDateAsc = ref(false);
  const claimStore = useEmployeeClaimStore();
  const {
    totalCount,
    approvedCount,
    rejectedCount,
    getClaimsByDateAsc, 
    getClaimsByDateDesc,
  } = storeToRefs(claimStore);

  const sortedExpenses = computed(() => {
    return sortDateAsc.value
      ? claimStore.getClaimsByDateAsc  // Updated to match store getters
      : claimStore.getClaimsByDateDesc;
  });

  // helper function
  const formatDate = (dateString) => {
    if (!dateString) return '';
    return new Date(dateString).toLocaleDateString('en-GB'); // DD/MM/YYYY format
  };

  onMounted(async () => {
    const employeeId = 1; // Get this from your auth system
    await claimStore.initStore(employeeId); // Pass employee ID
  });

  const openDetails = (expense) => {
    selectedClaim.value = expense;
    showDialog.value = true;
  };
</script>
