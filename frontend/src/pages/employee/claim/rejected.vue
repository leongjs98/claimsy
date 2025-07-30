<!-- Rejected Claims -->
<template>
  <div class="mx-auto my-14 w-full max-w-6xl bg-gray-100">
    <!-- Loading State -->
    <div v-if="claimStore.loading" class="flex justify-center py-8">
      <div class="text-lg">Loading rejected claims...</div>
    </div>

    <!-- Error State -->
    <div
      v-if="claimStore.error"
      class="mx-4 rounded bg-red-100 p-4 text-red-700"
    >
      {{ claimStore.error }}
    </div>

    <!-- Always Show Main Content (Card, Tab, Table) -->
    <div v-if="!claimStore.loading">
      <EmployeeClaimsCard />

      <div class="mt-4 mb-2"></div>
      <div class="mt-8 flow-root px-4 sm:px-8 lg:px-14">
        <div class="-mx-4 -my-2 sm:-mx-6 lg:-mx-8">
          <div class="min-w-full py-2 align-middle sm:px-6 lg:px-8">
            <EmployeeClaimsTab />
            <table
              class="min-w-full divide-y divide-gray-300 rounded-b-lg bg-gray-100 drop-shadow-md"
            >
              <thead class="rounded-lg bg-red-50 text-red-700">
                <tr>
                  <th
                    class="rounded-tl-lg py-3 pr-3.5 pl-4 text-right text-sm font-semibold sm:pl-6"
                  >
                    #
                  </th>
                  <th
                    class="py-3.5 pr-3 pl-3.5 text-left text-sm font-semibold"
                  >
                    Claim ID
                  </th>
                  <th class="w-48 px-3 py-3.5 text-left text-sm font-semibold">
                    Status
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
                    Invoices No.
                  </th>
                  <th class="px-3 py-3.5 text-right text-sm font-semibold">
                    Total (RM)
                  </th>
                  <th
                    class="sr-only w-48 rounded-tr-lg px-3 py-3.5 text-left text-sm font-semibold"
                  >
                    Details
                  </th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-200 bg-white">
                <!-- No Rejected Claims Row -->
                <tr v-if="sortedRejectedClaims.length === 0" class="shadow-md">
                  <td
                    colspan="7"
                    class="rounded-b-lg py-8 text-center text-gray-500"
                  >
                    <div class="flex flex-col items-center space-y-2">
                      <svg
                        class="h-12 w-12 text-gray-300"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                        ></path>
                      </svg>
                      <p class="text-lg font-medium">
                        No rejected claims found
                      </p>
                      <p class="text-sm">
                        All your claims are either approved or pending review.
                      </p>
                    </div>
                  </td>
                </tr>

                <!-- Rejected Claims Rows -->
                <tr
                  v-for="(claim, index) in sortedRejectedClaims"
                  :key="claim.id"
                  class="shadow-md"
                >
                  <td
                    :class="[
                      'py-4 pr-3 pl-4 text-right text-sm font-medium whitespace-nowrap text-gray-900 sm:pl-6',
                      index === sortedRejectedClaims.length - 1
                        ? 'rounded-bl-lg'
                        : '',
                    ]"
                  >
                    {{ index + 1 }}
                  </td>
                  <td class="px-3 py-4 text-sm whitespace-nowrap text-gray-500">
                    {{ claim.claim_number }}
                  </td>
                  <td
                    class="w-fit px-3 py-4 text-sm font-semibold whitespace-nowrap"
                  >
                    <div class="flex items-center justify-start gap-2">
                      <StatusBadge :status="claim.status" />
                    </div>
                  </td>
                  <td
                    class="px-3 py-4 text-center text-sm whitespace-nowrap text-gray-500"
                  >
                    {{ formatDate(claim.submitted_date) }}
                  </td>
                  <td
                    class="px-3 py-4 text-center text-sm whitespace-nowrap text-gray-500"
                  >
                    {{ claim.invoices?.length || 0 }}
                  </td>
                  <td
                    class="px-4 py-4 text-right text-sm whitespace-nowrap text-gray-500"
                  >
                    {{ formatCurrency(claim.total) }}
                  </td>
                  <td
                    :class="[
                      'px-4 py-4 text-center text-sm whitespace-nowrap text-theme-300',
                      index === sortedRejectedClaims.length - 1
                        ? 'rounded-br-lg'
                        : '',
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

  <EmployeeClaimDetailsDialog
      v-model="showDialog"
      :data="selectedClaim"
    :invoices="claimStore.claimInvoices"
    :loading="claimStore.loading"
  />
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useEmployeeClaimStore } from "@/stores/employee-claims.ts";

const showDialog = ref(false);
const selectedClaim = ref();
const sortDateAsc = ref(false);
const claimStore = useEmployeeClaimStore();

const { totalCount, approvedCount, rejectedCount, rejectedClaims } =
  storeToRefs(claimStore);

// Filter and sort only rejected claims
const sortedRejectedClaims = computed(() => {
  const rejected = claimStore.rejectedClaims; // Get rejected claims from store

  return rejected.slice().sort((a, b) => {
    const dateA = new Date(a.submitted_date);
    const dateB = new Date(b.submitted_date);
    return sortDateAsc.value ? dateA - dateB : dateB - dateA;
  });
});

// Helper function
const formatDate = (dateString) => {
  if (!dateString) return "";
  return new Date(dateString).toLocaleDateString("en-GB"); // DD/MM/YYYY format
};

onMounted(async () => {
  const employeeId = 1; // Get this from your auth system
  await claimStore.initStore(employeeId); // Pass employee ID
});

const openDetails = async (claim) => {
  selectedClaim.value = claim;

  // Fetch invoices for this claim
  try {
    await claimStore.fetchInvoicesByClaimId(claim.id);
    showDialog.value = true;
  } catch (error) {
    console.error("Failed to load claim invoices:", error);
    // Still show dialog even if invoices fail to load
    showDialog.value = true;
  }
};

const formatCurrency = (amount) => {
  if (amount === null || amount === undefined) return "0.00";
  return `${amount.toFixed(2)}`;
};
</script>
