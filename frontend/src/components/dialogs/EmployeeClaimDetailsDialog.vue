<template>
  <v-dialog v-model="isOpen" max-width="1000">
    <v-card class="rounded-lg shadow-lg">
      <div
        class="flex items-center justify-between rounded-t-xl bg-theme-300 px-6 py-4 text-white"
      >
        <h2 class="text-xl font-semibold">Claim ID: #{{ data?.claim_number }}</h2>
        <button
          @click="isOpen = false"
          class="rounded-full p-1 text-white hover:bg-blue-800"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M6 18L18 6M6 6l12 12"
            />
          </svg>
        </button>
      </div>

      <div class="p-6">

        <!-- Loading State -->
        <div v-if="loading" class="text-center py-8">
          <div class="text-lg">Loading invoices...</div>
        </div>
        <!-- Loading State -->
        <div v-if="loading" class="text-center py-8">
          <div class="text-lg">Loading invoices...</div>
        </div>

        <!-- Invoices Table -->
        <table
          v-else-if="invoices && invoices.length > 0"
          class="col-span-full mt-6 mb-2 w-full min-w-full table-auto divide-y divide-gray-300"
        >
          <thead class="text-sm font-semibold text-gray-600">
            <tr class="text-left">
              <th class="px-4 pb-2">Date</th>
              <th class="px-4 pb-2">Merchant</th>
              <th class="px-4 pb-2">Item/Service</th>
              <th class="px-4 pb-2 text-right">Qty</th>
              <th class="pb-2 pl-4 text-right">Price (RM)</th>
              <th class="pb-2 pl-4"></th>
            </tr>
          </thead>
          <tbody>
            <!-- Loop through invoices and their items -->
            <template v-for="invoice in invoices" :key="invoice.id">
              <tr
                v-for="(item, itemIndex) in invoice.itemsServices"
                :key="`${invoice.id}-${itemIndex}`"
                class="border-b border-gray-100 py-3 text-sm last:border-b-0"
              >
                <td class="px-4 py-6 text-gray-700">
                  <span class="py-6 font-medium text-gray-900">
                    {{ formatDate(invoice.invoice_date) }}
                  </span>
                  <br />
                  <span class="text-xs text-gray-500">
                    {{ invoice.category }}
                  </span>
                </td>
                <td class="px-4 py-6 text-gray-700">
                  <span class="py-6 font-medium text-gray-900">
                    {{ invoice.merchant_name }}
                  </span>
                  <br />
                  <span class="text-xs text-gray-500">
                    {{ truncateString(invoice.merchant_address) }}
                  </span>
                </td>
                <td class="max-w-80 px-4 py-6 text-nowrap text-gray-700">
                  {{ truncateString(item.item) }}
                </td>
                <td class="px-4 py-6 text-right text-gray-700">
                  {{ item.quantity }}
                </td>
                <td class="py-6 text-right font-semibold text-blue-600">
                  {{
                    (item.quantity * item.unit_price).toLocaleString("en-US", {
                      minimumFractionDigits: 2,
                      maximumFractionDigits: 2,
                    })
                  }}
                </td>
                <td class="px-4 py-6 text-theme-300 hover:underline">
                  <div class="text-right">
                    <RouterLink :to="`/employee/invoice/edit/${invoice.id}`">
                      Details
                    </RouterLink>
                  </div>
                </td>
              </tr>
            </template>
            
            <!-- Total Row -->
            <tr class="border-b border-gray-100 py-3 text-sm last:border-b-0">
              <td class="px-4 py-6 font-bold text-gray-800">Total</td>
              <td class="px-4 py-6 text-gray-700"></td>
              <td class="px-4 py-6 text-gray-700"></td>
              <td class="px-4 py-6 text-gray-700"></td>
              <td class="py-6 text-right font-bold text-blue-600">
                {{
                  totalAmount.toLocaleString("en-US", {
                    minimumFractionDigits: 2,
                    maximumFractionDigits: 2,
                  })
                }}
              </td>
              <td class="px-4 py-6 text-right text-gray-700"></td>
            </tr>
          </tbody>
        </table>
        
        <!-- No Invoices -->
        <div v-else class="py-4 text-center text-gray-500">
          No invoices found for this claim.
        </div>

        <div
          class="my-6 flex items-center justify-between border-t border-gray-300 pt-4"
        >
          <div v-if="data?.remark" class="">
            <h4 class="mb-2 font-semibold text-gray-700">Remark:</h4>
            <p class="text-sm text-gray-600 italic">{{ data.remark }}</p>
          </div>
          <div v-else></div>
        </div>
      </div>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref, watch, computed } from "vue";
import { storeToRefs } from "pinia"; // ADD THIS IMPORT
import { useEmployeeClaimStore } from "@/stores/employee-claims.ts";

const props = defineProps({
  modelValue: Boolean,
  data: Object,
});

const emit = defineEmits(["update:modelValue"]);
const claimStore = useEmployeeClaimStore();

// ADD THIS LINE - Use storeToRefs for reactivity
const { claimInvoices, loading } = storeToRefs(claimStore);

const isOpen = ref(props.modelValue);

watch(
  () => props.modelValue,
  (val) => {
    isOpen.value = val;
  },
);

watch(isOpen, (val) => {
  if (!val) {
    emit("update:modelValue", false);
  }
});

// CHANGE THIS - Use the reactive reference
const invoices = computed(() => {
  console.log('Dialog - claimInvoices.value:', claimInvoices.value); // Debug log
  return claimInvoices.value || [];
});

const totalAmount = computed(() => {
  return invoices.value.reduce((sum, invoice) => {
    const invoiceTotal = invoice.item_services?.reduce(
      (itemSum, item) => itemSum + (item.quantity * item.unit_price), 0
    ) || 0;
    return sum + invoiceTotal;
  }, 0);
});

function truncateString(str, maxLength = 30) {
  if (!str) return '';
  if (str.length > maxLength) {
    return str.substring(0, maxLength - 3) + "...";
  } else {
    return str;
  }
}

function formatDate(dateString) {
  if (!dateString) return '';
  return new Date(dateString).toLocaleDateString('en-GB');
}
</script>