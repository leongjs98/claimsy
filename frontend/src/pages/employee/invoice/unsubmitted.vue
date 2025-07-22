Unsubmitted.vue
<template>
  <div class="mx-auto my-14 w-full max-w-6xl bg-gray-100">
    <!-- Cards Row -->
    <EmployeeClaimsCard 
      :totalCount="claimStore.totalCount" 
      :approvedCount="claimStore.approvedCount" 
      :rejectedCount="claimStore.rejectedCount" 
    />

     <!-- Loading state -->
    <div v-if="claimStore.loading" class="flex justify-center items-center py-8">
      <div class="text-lg text-gray-600">Loading claims...</div>
    </div>
    <!-- Error handling -->
    <div v-if="claimStore.error" class="mx-4 my-4 p-4 bg-red-100 border border-red-400 text-red-700 rounded">
      <p>{{ claimStore.error }}</p>
      <button @click="claimStore.clearError()" class="mt-2 px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600">
        Clear Error
      </button>
    </div>

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
                  <div class="flex items-center gap-2">
                    <button @click="setSort('Category')">Category</button>
                    <div class="relative inline-block w-full text-left">
                      <div>
                        <button
                          type="button"
                          class="hover:text--600 flex items-center justify-center rounded-full bg-gray-100 text-theme-300 focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 focus:ring-offset-gray-100 focus:outline-hidden"
                          id="menu-button"
                          aria-expanded="true"
                          aria-haspopup="true"
                          @click="showCategoryDropdown = !showCategoryDropdown"
                        >
                          <span class="sr-only">Open options</span>
                          <svg
                            class="size-4"
                            xmlns="http://www.w3.org/2000/svg"
                            width="32"
                            height="32"
                            viewBox="0 0 24 24"
                          >
                            <path
                              fill="currentColor"
                              d="M11 20q-.425 0-.712-.288T10 19v-6L4.2 5.6q-.375-.5-.112-1.05T5 4h14q.65 0 .913.55T19.8 5.6L14 13v6q0 .425-.288.713T13 20z"
                            />
                          </svg>
                        </button>
                      </div>

                      <Transition name="dropdown-menu">
                        <div
                          v-show="showCategoryDropdown"
                          class="absolute left-0 z-20 mt-2 w-56 origin-top-left rounded-md bg-white shadow-lg ring-1 ring-black/5 focus:outline-hidden"
                          role="menu"
                          aria-orientation="vertical"
                          aria-labelledby="menu-button"
                          tabindex="-1"
                        >
                          <div class="py-1" role="none">
                            <button
                              v-for="cat in claimStore.categories"
                              :key="cat"
                              @click="
                                selectedCategory = cat;
                                showCategoryDropdown = false;
                              "
                              :class="{
                                'bg-blue-50 text-theme-200 outline-hidden':
                                  selectedCategory === cat,
                                'text-gray-700': selectedCategory !== cat,
                              }"
                              href="#"
                              class="block w-full px-4 py-2 text-left text-sm text-gray-700 hover:bg-blue-50 hover:text-theme-200 focus:bg-blue-50 focus:text-theme-200"
                              role="menuitem"
                              tabindex="-1"
                              :id="`menu-item-${cat}`"
                            >
                              {{ cat }}
                            </button>
                          </div>
                        </div>
                      </Transition>
                    </div>
                  </div>
                </th>
                <th
                  class="flex justify-center px-3 py-3.5 text-sm font-semibold"
                >
                  <button
                    class="flex items-center justify-center gap-2 hover:cursor-pointer"
                    @click="setSort('Date')"
                  >
                    <span> Date </span>
                    <svg
                      v-show="!sortAsc"
                      class="h-5 w-5"
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 24 24"
                    >
                      <!-- Icon from Material Design Icons by Pictogrammers - https://github.com/Templarian/MaterialDesign/blob/master/LICENSE -->
                      <path
                        fill="currentColor"
                        d="M19 7h-3l4-4l4 4h-3v14h-2zM8 16h3v-3H8zm5-11h-1V3h-2v2H6V3H4v2H3c-1.11 0-2 .89-2 2v11c0 1.11.89 2 2 2h10c1.11 0 2-.89 2-2V7c0-1.11-.89-2-2-2M3 18v-7h10v7z"
                      />
                    </svg>
                    <svg
                      v-show="sortAsc"
                      class="h-5 w-5"
                      xmlns="http://www.w3.org/2000/svg"
                      width="32"
                      height="32"
                      viewBox="0 0 24 24"
                    >
                      <!-- Icon from Material Design Icons by Pictogrammers - https://github.com/Templarian/MaterialDesign/blob/master/LICENSE -->
                      <path
                        fill="currentColor"
                        d="M21 17h3l-4 4l-4-4h3V3h2zM8 16h3v-3H8zm5-11h-1V3h-2v2H6V3H4v2H3c-1.11 0-2 .89-2 2v11c0 1.11.89 2 2 2h10c1.11 0 2-.89 2-2V7c0-1.11-.89-2-2-2M3 18v-7h10v7z"
                      />
                    </svg>
                  </button>
                </th>
                <th class="px-3 py-3.5 text-center text-sm font-semibold">
                  Quantity
                </th>
                <th class="w-48 px-3 py-3.5 text-left text-sm font-semibold">
                  Remark
                </th>
                <th class="px-3 py-3.5 text-right text-sm font-semibold">
                  Price (RM)
                </th>
                <th
                  class="w-48 rounded-tr-lg px-3 py-3.5 text-center text-sm font-semibold"
                >
                  Select
                </th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200 bg-white">
              {{ console.log('sortedInvoices', sortedInvoices) }}
              <tr
                v-for="(invoice, index) in sortedInvoices"
                :key="invoice.id"
                class="shadow-md"
              >
                <td
                  :class="[
                    'py-4 pr-3 pl-4 text-right text-sm font-medium whitespace-nowrap text-gray-900 sm:pl-6',
                    index === sortedInvoices.length - 1 ? 'rounded-bl-lg' : '',
                  ]"
                >
                  {{ index + 1 }}
                </td>
                <!-- <td class="px-3 py-4 text-sm whitespace-nowrap text-gray-500">{{ person.Name }}</td> -->
                <td class="px-3 py-4 text-sm whitespace-nowrap text-gray-500">
                  <div class="flex flex-col">
                    <span class="font-medium text-gray-900">{{
                      invoice.category
                    }}</span>
                    <!-- <span class="text-xs text-gray-500">
                      Claim #{{ getClaimNumber(invoice.claim_id) }}
                    </span> -->
                  </div>
                </td>
                <td class="px-3 py-4 text-center text-sm whitespace-nowrap text-gray-500">
                  {{ formatDate(invoice.invoiceDate) }}
                </td>
                <td class="px-4 py-4 text-right text-sm whitespace-nowrap text-gray-500">
                  {{ getItemCount(invoice) }}
                </td>
                <td class="w-32 px-3 py-4 text-sm text-gray-500">
                  <span class="block w-48 truncate overflow-hidden text-ellipsis" :title="invoice.remark">
                    {{ invoice.remark || 'No remark' }}
                  </span>
                </td>
                <td class="px-4 py-4 text-right text-sm whitespace-nowrap text-gray-500">
                  {{ formatCurrency(getTotalPrice(invoice)) }}
                </td>
                <td
                  :class="[
                    'min-h-[69px] px-4 py-4 text-center text-sm whitespace-nowrap text-amber-500',
                    index === sortedInvoices.length - 1 ? 'rounded-br-lg' : '',
                  ]"
                >
                  <div class="flex items-center justify-center">
                    <input
                      type="checkbox"
                      :value="invoice"
                      v-model="selectedInvoices"
                      :id="`checkbox-invoice-${index}`"
                      class="checkbox-input sr-only"
                    />

                    <!-- Visual representation of the checkbox -->
                    <label
                      :for="`checkbox-invoice-${index}`"
                      class="checkbox-label relative flex h-6 w-6 cursor-pointer items-center justify-center overflow-hidden rounded-md border-1 border-theme-200 transition-colors ease-in-out hover:border-theme-300 focus:border-theme-300"
                    >
                      <!-- The expanding fill element -->
                      <div class="checkbox-fill absolute bg-theme-300"></div>
                    </label>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <div class="flex justify-end px-4 sm:px-8 lg:px-14">
      <button
        class="hover:bg-theme-400 z-25 mt-5 rounded bg-theme-300 px-13 py-2 text-white disabled:bg-gray-400 disabled:cursor-not-allowed"
        :disabled="selectedInvoices.length === 0 || isSubmitting"
        @click="submitSelectedInvoices"
      >
        <span v-if="isSubmitting">Submitting...</span>
        <span v-else>Submit ({{ selectedInvoices.length }})</span>
      </button>
    </div>
  </div>
  <div>
    <div
      v-show="openDialog"
      class="relative z-30"
      aria-labelledby="dialog-title"
      role="dialog"
      aria-modal="true"
    >
      <Transition name="backdrop">
        <div
          class="fixed inset-0 bg-gray-500/75 transition-opacity"
          aria-hidden="true"
        ></div>
      </Transition>

      <Transition name="pane">
        <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
          <div
            class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0"
          >
            <div
              class="relative transform overflow-hidden rounded-lg bg-white px-4 pt-5 pb-4 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-sm sm:p-6"
            >
              <div>
                <div
                  class="mx-auto flex size-12 items-center justify-center rounded-full bg-green-100"
                >
                  <svg
                    class="size-6 text-green-600"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke-width="1.5"
                    stroke="currentColor"
                    aria-hidden="true"
                    data-slot="icon"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      d="m4.5 12.75 6 6 9-13.5"
                    />
                  </svg>
                </div>
                <div class="mt-3 text-center sm:mt-5">
                  <h3
                    class="text-base font-semibold text-gray-900"
                    id="dialog-title"
                  >
                    Submission successful
                  </h3>
                  <div class="mt-2">
                    <p class="text-sm text-gray-500">
                      Successfully submitted {{ selectedInvoices.length }} invoices for approval.
                    </p>
                  </div>
                </div>
              </div>
              <div class="mt-5 sm:mt-6">
                <button
                  @click="openDialog = false"
                  type="button"
                  class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                >
                  Go back
                </button>
              </div>
            </div>
          </div>
        </div>
      </Transition>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { useEmployeeClaimStore } from "@/stores/employee-claims.ts";
import { storeToRefs } from "pinia";

// Pinia store
const claimStore = useEmployeeClaimStore();

console.log("success")
// Reactive data
const sortKey = ref("Date");
const sortAsc = ref(false);
const showCategoryDropdown = ref(false);
const selectedCategory = ref("All");
const selectedInvoices = ref([]);
const openDialog = ref(false);
const isSubmitting = ref(false); // Add loading state

// sho - calling this action on mount to initialize the store
onMounted(async () => {
  const employeeId = 1; // or get from auth/route
  await claimStore.fetchUnsubmittedInvoices(employeeId);
});

// Helper functions (keep all your existing helper functions)
function formatDate(dateString) {
  const date = new Date(dateString);
  return date.toLocaleDateString('en-GB');
}

function formatCurrency(amount) {
  return new Intl.NumberFormat('en-MY', {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2
  }).format(amount);
}

function getCategoryFromType(claimType) {
  const categoryMap = {
    'Travel': 'Travel Expenses',
    'Accommodation': 'Accommodation', 
    'Meals': 'Meals and Entertainment',
    'Office': 'Office Supplies and Equipment',
    'Medical': 'Medical Claim'
  };
  return categoryMap[claimType] || 'Other';
}

const allInvoices = computed(() => claimStore.invoices);

const filteredInvoices = computed(() => {
  const invoices = allInvoices.value;
  if (selectedCategory.value === "All") {
    return invoices;
  }
  return invoices.filter(invoice => {
    return invoice.category.toLowerCase() === selectedCategory.value.toLowerCase();
  });
});

const sortedInvoices = computed(() => {
  const invoices = filteredInvoices.value;
  if (sortKey.value === "Date") {
    return invoices.slice().sort((a, b) => {
      const dateA = new Date(a.invoiceDate);
      const dateB = new Date(b.invoiceDate);
      return sortAsc.value ? dateA - dateB : dateB - dateA;
    });
  }
  return invoices;
});

function getClaimNumber(claimId) {
  const claim = claimStore.claims.find(c => c.id === claimId);
  return claim ? claim.claim_number : 'Unknown';
}

function truncateString(str, maxLength = 30) {
  if (!str) return '';
  if (str.length > maxLength) {
    return str.substring(0, maxLength - 3) + "...";
  }
  return str;
}

function getItemCount(invoice) {
  const items = invoice.itemsServices;
  return items.length;
}

function getTotalPrice(invoice) {
  const items = invoice.itemsServices;
  return items
    .map(item => (item.quantity || 0) * (item.unit_price || 0))
    .reduce((sum, val) => sum + val, 0);
}

function setSort(key) {
  if (key === "Date") {
    if (sortKey.value === key) {
      sortAsc.value = !sortAsc.value;
    } else {
      sortKey.value = key;
      sortAsc.value = true;
    }
  }
}

function handleDialogClose() {
  openDialog.value = false;
  selectedInvoices.value = [];
}

async function refreshClaims() {
  await claimStore.refreshClaims();
}

// aisya - Submit selected invoices function
async function submitSelectedInvoices() {
  if (selectedInvoices.value.length === 0) {
    alert('Please select at least one invoice to submit.');
    return;
  }

  try {
    const employeeId = 1;
    const invoiceIds = selectedInvoices.value.map(invoice => invoice.id);
    
    // Use the store action instead of direct fetch
    const newClaim = await claimStore.submitInvoicesIntoClaim(
      employeeId,
      invoiceIds,
      "travel", // or make this dynamic
      "Business expense reimbursement"
    );
    
    console.log('Claim created successfully:', newClaim);
    
    // Show success dialog
    openDialog.value = true;
    
    // Clear selections
    selectedInvoices.value = [];
    
  } catch (error) {
    console.error('Failed to submit invoices:', error);
    alert(`Failed to submit invoices: ${error.message}`);
  }
}
</script>

<style scoped>
  /* The expanding fill element */
  .checkbox-fill {
    /* Initial state: completely collapsed at the center */
    width: 0;
    height: 0;
    top: 50%;
    /* Position at vertical center */
    left: 50%;
    /* Position at horizontal center */
    transform: translate(-50%, -50%);
    /* Adjust to truly center the element */
    transition:
      width 0.15s ease-out,
      height 0.15s ease-out;
    /* Smooth transition for width and height */
    /* Removed rounded-md from here, as parent's overflow-hidden handles the rounding */
  }

  /* State when checkbox is checked */
  .checkbox-input:checked + .checkbox-label .checkbox-fill {
    width: 100%;
    /* Expands to fill the container width */
    height: 100%;
    /* Expands to fill the container height */
  }
</style>



