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
        <!-- Claim Information Section -->
        <div class="mb-6 rounded-lg bg-gray-50 p-4">
          <h3 class="mb-3 text-lg font-semibold text-gray-900">Claim Information</h3>
          <div class="grid grid-cols-2 gap-4 text-sm">
            <div>
              <span class="font-medium text-gray-700">Employee ID:</span>
              <span class="ml-2 text-gray-900">{{ data?.employee_id }}</span>
            </div>
            <div>
              <span class="font-medium text-gray-700">Claim Type:</span>
              <span class="ml-2 text-gray-900">{{ data?.claim_type }}</span>
            </div>
            <div>
              <span class="font-medium text-gray-700">Total Amount:</span>
              <span class="ml-2 font-semibold text-gray-900">
                RM {{ formatCurrency(data?.claim_amount) }}
              </span>
            </div>
            <div>
              <span class="font-medium text-gray-700">Status:</span>
              <span class="ml-2">
                <StatusBadge :status="data?.status" />
              </span>
            </div>
            <div>
              <span class="font-medium text-gray-700">Submitted Date:</span>
              <span class="ml-2 text-gray-900">{{ formatDate(data?.submitted_date) }}</span>
            </div>
            <div v-if="data?.reviewed_date">
              <span class="font-medium text-gray-700">Reviewed Date:</span>
              <span class="ml-2 text-gray-900">{{ formatDate(data?.reviewed_date) }}</span>
            </div>
            <div class="col-span-2">
              <span class="font-medium text-gray-700">Reason:</span>
              <span class="ml-2 text-gray-900">{{ data?.reason }}</span>
            </div>
            <div v-if="data?.resolution" class="col-span-2">
              <span class="font-medium text-gray-700">Resolution:</span>
              <span class="ml-2 text-gray-900">{{ data?.resolution }}</span>
            </div>
          </div>
        </div>

        <!-- Invoice Items Table -->
        <h3 class="mb-3 text-lg font-semibold text-gray-900">
          Invoice Details ({{ invoices.length }} items)
        </h3>
        
        <table
          v-if="invoices.length > 0"
          class="col-span-full mt-6 mb-2 w-full min-w-full table-auto divide-y divide-gray-300"
        >
          <thead class="text-sm font-semibold text-gray-600">
            <tr class="text-left">
              <th class="px-4 pb-2">Invoice Date</th>
              <th class="px-4 pb-2">Merchant</th>
              <th class="px-4 pb-2">Category</th>
              <th class="px-4 pb-2">Invoice #</th>
              <th class="px-4 pb-2">Remark</th>
              <th class="pb-2 pl-4 text-right">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(invoice, index) in invoices"
              :key="invoice.id"
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
              <td class="px-4 py-6 text-gray-700">
                {{ invoice.category }}
              </td>
              <td class="px-4 py-6 text-gray-700">
                {{ invoice.invoice_number }}
              </td>
              <td class="max-w-80 px-4 py-6 text-gray-700">
                {{ truncateString(invoice.remark || 'No remark') }}
              </td>
              <td class="px-4 py-6 text-theme-300 hover:underline">
                <div class="text-right">
                  <button 
                    @click="showInvoiceDetails(invoice)"
                    class="text-theme-300 hover:underline"
                  >
                    View Details
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        
        <div v-else class="py-8 text-center text-gray-500">
          <svg class="w-12 h-12 mx-auto text-gray-300 mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
          </svg>
          <p>No invoices found for this claim.</p>
        </div>

        <!-- Invoice Details Expansion -->
        <div v-if="selectedInvoice" class="mt-6 rounded-lg border border-gray-200 bg-gray-50 p-4">
          <div class="flex items-center justify-between mb-3">
            <h4 class="font-semibold text-gray-900">Invoice Details - #{{ selectedInvoice.invoice_number }}</h4>
            <button @click="selectedInvoice = null" class="text-gray-400 hover:text-gray-600">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
              </svg>
            </button>
          </div>
          
          <div class="grid grid-cols-2 gap-4 text-sm">
            <div>
              <span class="font-medium text-gray-700">Invoice ID:</span>
              <span class="ml-2 text-gray-900">{{ selectedInvoice.invoice_id }}</span>
            </div>
            <div>
              <span class="font-medium text-gray-700">Invoice Date:</span>
              <span class="ml-2 text-gray-900">{{ formatDate(selectedInvoice.invoice_date) }}</span>
            </div>
            <div class="col-span-2">
              <span class="font-medium text-gray-700">Merchant Name:</span>
              <span class="ml-2 text-gray-900">{{ selectedInvoice.merchant_name }}</span>
            </div>
            <div class="col-span-2">
              <span class="font-medium text-gray-700">Merchant Address:</span>
              <span class="ml-2 text-gray-900">{{ selectedInvoice.merchant_address }}</span>
            </div>
            <div class="col-span-2">
              <span class="font-medium text-gray-700">Category:</span>
              <span class="ml-2 text-gray-900">{{ selectedInvoice.category }}</span>
            </div>
            <div class="col-span-2">
              <span class="font-medium text-gray-700">Remark:</span>
              <span class="ml-2 text-gray-900">{{ selectedInvoice.remark || 'No remark provided' }}</span>
            </div>
            <div>
              <span class="font-medium text-gray-700">Created:</span>
              <span class="ml-2 text-gray-900">{{ formatTimestamp(selectedInvoice.created_at) }}</span>
            </div>
            <div>
              <span class="font-medium text-gray-700">Updated:</span>
              <span class="ml-2 text-gray-900">{{ formatTimestamp(selectedInvoice.updated_at) }}</span>
            </div>
          </div>

          <!-- Item Services JSON Data -->
          <div v-if="selectedInvoice.item_services" class="mt-4">
            <span class="font-medium text-gray-700 text-sm">Items/Services Data:</span>
            <div class="mt-2 rounded bg-white p-3 text-sm">
              <pre class="whitespace-pre-wrap text-gray-800">{{ formatItemServices(selectedInvoice.item_services) }}</pre>
            </div>
          </div>
        </div>

        <!-- Claim Remark Section -->
        <div
          v-if="data?.reason"
          class="my-6 flex items-center justify-between border-t border-gray-300 pt-4"
        >
          <div>
            <h4 class="mb-2 font-semibold text-gray-700">Claim Reason:</h4>
            <p class="text-sm text-gray-600 italic">{{ data.reason }}</p>
          </div>
        </div>
      </div>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref, watch, computed } from "vue";

const props = defineProps({
  modelValue: Boolean,
  data: Object, // This will be the Claim object with Items: Invoice[]
});

const emit = defineEmits(["update:modelValue"]);

const isOpen = ref(props.modelValue);
const selectedInvoice = ref(null);

watch(
  () => props.modelValue,
  (val) => {
    isOpen.value = val;
  },
);

watch(isOpen, (val) => {
  if (!val) {
    emit("update:modelValue", false);
    selectedInvoice.value = null; // Reset selected invoice when dialog closes
  }
});

// Get invoices from the claim data
const invoices = computed(() => {
  return props.data?.Items || [];
});

// Calculate total amount from claim_amount (not from individual invoices)
const totalAmount = computed(() => {
  return props.data?.claim_amount || 0;
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

function formatCurrency(amount) {
  if (!amount) return '0.00';
  return amount.toLocaleString('en-US', {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  });
}

function formatTimestamp(timestamp) {
  if (!timestamp) return '';
  // Convert epoch timestamp to readable date
  return new Date(timestamp * 1000).toLocaleString('en-GB');
}

function formatItemServices(itemServices) {
  if (!itemServices) return 'No items/services data';
  
  if (typeof itemServices === 'string') {
    try {
      return JSON.stringify(JSON.parse(itemServices), null, 2);
    } catch {
      return itemServices;
    }
  }
  return JSON.stringify(itemServices, null, 2);
}

function showInvoiceDetails(invoice) {
  selectedInvoice.value = invoice;
}
</script>