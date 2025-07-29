<template>
  <div class="mx-auto my-14 w-full max-w-6xl bg-gray-100">
    <AdminClaimsCard
      :totalCount="claims.length"
      :approvedCount="adminClaims.approvedClaimsCount"
      :rejectedCount="adminClaims.rejectedClaimsCount"
    />
    <div class="mt-8 flow-root px-4 sm:px-8 lg:px-14">
      <div class="-mx-4 -my-2 sm:-mx-6 lg:-mx-8">
        <div class="min-w-full py-2 align-middle sm:px-6 lg:px-8">
          <Tab
            :tabs="[
              {
                link: '/admin/claim/all',
                routeName: 'All Claims',
              },
              {
                link: '/admin/claim/approved',
                routeName: 'Approved',
              },
              {
                link: '/admin/claim/rejected',
                routeName: 'Rejected',
              },
            ]"
          />
          <div class="shadow-sm ring-1 ring-black/5 sm:rounded-lg">
            <table class="min-w-full divide-y divide-gray-300 bg-gray-100">
              <thead class="rounded-lg bg-green-50 text-green-700">
                <tr>
                  <th
                    scope="col"
                    class="rounded-tl-lg py-3 pr-3.5 pl-4 text-right text-sm font-semibold sm:pl-6"
                  >
                    #
                  </th>
                  <th
                    scope="col"
                    class="py-3.5 pr-3 pl-3.5 text-left text-sm font-semibold"
                  >
                    Name
                  </th>
                  <th
                    scope="col"
                    class="w-fit px-3 py-3.5 text-left text-sm font-semibold"
                  >
                    Type
                  </th>
                  <th class="w-48 px-3 py-3.5 text-left text-sm font-semibold">
                    Status
                  </th>
                  <th class="flex px-3 py-3.5 text-sm font-semibold">
                    <button
                      class="flex items-center gap-2 hover:cursor-pointer"
                      @click="sortDateAsc = !sortDateAsc"
                    >
                      <span> Date </span>
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
                  <th
                    scope="col"
                    class="px-3 py-3.5 text-center text-sm font-semibold"
                  >
                    Item(s)
                  </th>
                  <th
                    scope="col"
                    class="px-3 py-3.5 text-right text-sm font-semibold"
                  >
                    Total (RM)
                  </th>
                  <th
                    scope="col"
                    class="rounded-tr-lg px-3 py-3.5 text-center text-sm font-semibold"
                  ></th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-200 bg-white">
                <tr
                  v-for="(claim, index) in sortedClaims"
                  :key="claim.claim_number"
                  class="shadow-md"
                >
                  <td
                    class="py-4 pr-3 pl-4 text-right text-sm font-medium whitespace-nowrap text-gray-900 sm:pl-6"
                  >
                    {{ index + 1 }}
                  </td>
                  <td class="px-3 py-4 text-sm whitespace-nowrap text-gray-500">
                    <div class="flex flex-col">
                      <span class="font-medium text-gray-900">
                        {{ claim.employee?.name }}
                      </span>
                      <span class="text-xs text-gray-500">
                    {{ claim.employee?.email }}
                      </span>
                    </div>
                  </td>
                  <td
                    class="w-fit px-3 py-4 text-sm whitespace-nowrap text-gray-500"
                  >
                        {{ claim.claim_type }}
                  </td>
                  <td
                    class="w-fit px-3 py-4 text-sm font-semibold whitespace-nowrap"
                  >
                    <div class="flex items-center justify-start gap-2">
                      <StatusBadge :status="capitalizeStatus(claim.status)" />
                      <StatusBadge v-show="claim.is_anomaly" status="Anomaly" />
                    </div>
                  </td>
                  <td class="px-3 py-4 text-sm whitespace-nowrap text-gray-500">
                    {{ formatDate(claim.submitted_date) }}
                  </td>
                  <td
                    class="px-3 py-4 text-center text-sm whitespace-nowrap text-gray-500"
                  >
                    {{ countItems(claim) }}
                  </td>
                  <td
                    class="px-4 py-4 text-right text-sm whitespace-nowrap text-gray-500"
                  >
                    {{ formatCurrency(claim.total) }}
                  </td>
                  <td
                    class="px-4 py-4 text-right text-sm whitespace-nowrap text-theme-300"
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

  <AdminClaimDetailsDialog v-model="showDialog" :data="selectedClaim" />
</template>

<script setup>
  import { ref, computed, onMounted } from "vue";
  import { storeToRefs } from "pinia";
  import { useAdminClaimStore } from "@/stores/admin-claims.ts";

  const adminClaims = useAdminClaimStore();
  const { claims } = storeToRefs(adminClaims);

  onMounted(async () => {
    await adminClaims.initializeAdminClaimStore();
  });

  const sortDateAsc = ref(false);
  const showDialog = ref(false);
  const selectedClaim = ref(null);

  const sortedClaims = computed(() => {
    return sortDateAsc.value
      ? adminClaims.getApprovedClaimsSortedByDate(true) // true = ascending
      : adminClaims.getApprovedClaimsSortedByDate(false);
  });

  const formatDate = (dateString) => {
    if (!dateString) return "";
    const options = { year: "numeric", month: "short", day: "numeric" };
    return new Date(dateString).toLocaleDateString(undefined, options);
  };

  const capitalizeStatus = (status) => {
    if (!status) return "";
    return status.charAt(0).toUpperCase() + status.slice(1).toLowerCase();
  };

  const countItems = (claim) => {
    if (!claim.invoices) return 0;
    return claim.invoices.reduce((total, invoice) => {
      return total + (invoice.itemsServices?.length || 0);
    }, 0);
  };

  const formatCurrency = (amount) => {
    if (amount === null || amount === undefined) return "0.00";
    return `${amount.toFixed(2)}`;
  };

  const openDetails = (claim) => {
    selectedClaim.value = claim;
    showDialog.value = true;
  };
</script>
