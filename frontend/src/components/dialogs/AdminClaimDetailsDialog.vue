<template>
  <v-dialog v-model="isOpen" max-width="1000">
    <v-card class="rounded-lg shadow-lg">
      <div class="flex items-center justify-between rounded-t-xl bg-theme-300 px-6 py-4 text-white">
        <h2 class="flex items-center gap-4 text-xl font-semibold">
          <span> Claim ID: #{{ data.claim_number }} </span>
          <span
            class="flex w-fit items-center rounded-md px-2 py-1 text-base font-medium"
            :class="{
              'bg-emerald-100 text-emerald-600': data.status === 'approved',
              'bg-red-100 text-red-600': data.status === 'rejected',
              'bg-yellow-100 text-yellow-600': data.status === 'pending'
            }"
          >
            {{ data.status }}
          </span>
        </h2>
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
        <table
          v-if="data && data.invoices && data.invoices.length"
          class="col-span-full mt-6 mb-2 w-full min-w-full table-auto divide-y divide-gray-300"
        >
          <thead class="text-sm font-semibold text-gray-600">
            <tr class="text-left">
              <th class="px-4 pb-2">Date</th>
              <th class="px-4 pb-2">Merchant</th>
              <th class="px-4 pb-2">Item/Service</th>
              <th class="px-4 pb-2 text-right">Quantity</th>
              <th class="pb-2 pl-4 text-right">Price (RM)</th>
              <th class="pb-2 pl-4"></th>
            </tr>
          </thead>
          <tbody>
            <template v-for="(invoice, invoiceIndex) in data.invoices" :key="`invoice-${invoiceIndex}`">
              <tr
                v-for="(item, itemIndex) in invoice.itemsServices"
                :key="`item-${itemIndex}`"
                class="border-b border-gray-100 py-3 text-sm last:border-b-0"
              >
                <!-- Date Column -->
                <td class="px-4 py-6 text-gray-700">
                  <span class="py-6 font-medium text-gray-900">
                    {{ formatDate(invoice.invoiceDate) }}
                  </span>
                  <br />
                  <span class="text-xs text-gray-500">
                    {{ invoice.invoiceNumber }}
                  </span>
                </td>
                
                <!-- Merchant Column -->
                <td class="px-4 py-6 text-gray-700">
                  <span class="py-6 font-medium text-gray-900">
                    {{ invoice.merchantName || 'N/A' }}
                  </span>
                  <br />
                  <span class="text-xs text-gray-500">
                    {{ truncateString(invoice.merchantAddress || '') }}
                  </span>
                </td>
                
                <!-- Item/Service Column -->
                <td class="max-w-80 px-4 py-6 text-nowrap text-gray-700">
                  {{ item.item }}
                </td>
                
                <!-- Quantity Column -->
                <td class="px-4 py-6 text-right text-gray-700">
                  {{ item.quantity }}
                </td>
                
                <!-- Price Column -->
                <td class="py-6 text-right font-semibold text-blue-600">
                  {{ formatCurrency(item.unit_price) }}
                </td>
                
                <!-- Details Link -->
                <td class="px-4 py-6 text-theme-300 hover:underline">
                  <div class="text-right">
                    <RouterLink :to="`/admin/invoice/review/${invoice.invoiceId}`">
                      Details
                    </RouterLink>
                  </div>
                </td>
              </tr>
            </template>
            <tr class="border-b border-gray-100 py-3 text-sm last:border-b-0">
              <td class="px-4 py-6 font-bold text-gray-800">Total</td>
              <td class="px-4 py-6 text-gray-700"></td>
              <td class="px-4 py-6 text-gray-700"></td>
              <td class="px-4 py-6 text-gray-700"></td>
              <td class="py-6 text-right font-bold text-blue-600">
                {{ formatCurrency(data.claim_amount) }}
              </td>
              <td class="px-4 py-6 text-right text-gray-700"></td>
            </tr>
          </tbody>
        </table>
        <div v-else class="py-4 text-center text-gray-500">
          No invoices in this claim.
        </div>

        <div class="my-6 flex items-center justify-between border-t border-gray-300 pt-4">
          <div v-if="data.reason" class="">
            <h4 class="mb-2 font-semibold text-gray-700">Reason:</h4>
            <p class="text-sm text-gray-600 italic">{{ data.reason }}</p>
          </div>
          <div v-else></div>
          <div class="mt-6 flex items-center justify-end gap-x-6">
            <button
              type="button"
              class="rounded-md bg-red-400 px-5.5 py-2.5 text-sm font-semibold text-white transition-colors hover:bg-red-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-theme-200"
              @click="resolveClaim(false)"
            >
              Reject
            </button>
            <button
              type="button"
              class="rounded-md bg-green-400 px-3.5 py-2.5 text-sm font-semibold text-white transition-colors hover:bg-green-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-theme-200"
              @click="resolveClaim(true)"
            >
              Approve
            </button>
          </div>
        </div>
      </div>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref, watch, computed } from "vue";
import { useAdminClaimStore } from "@/stores/admin-claims";

const props = defineProps({
  modelValue: Boolean,
  data: {
    type: Object as () => {
      id: number;
      claim_number: string;
      status: 'pending' | 'approved' | 'rejected';
      claim_amount?: number;
      reason?: string;
      invoices: Array<{
        id?: number;
        invoiceId: number;
        invoiceNumber: string;
        invoiceDate: string;
        merchantName?: string;
        merchantAddress?: string;
        itemsServices: Array<{
          item: string;
          quantity: number;
          unit_price: number;
        }>;
      }>;
    },
    required: true
  }
});

const emit = defineEmits(["update:modelValue"]);
const adminClaims = useAdminClaimStore();

const isOpen = ref(props.modelValue);

watch(
  () => props.modelValue,
  (val) => {
    isOpen.value = val;
  }
);

watch(isOpen, (val) => {
  if (!val) {
    emit("update:modelValue", false);
  }
});

// Format date for display
const formatDate = (dateString: string) => {
  if (!dateString) return '';
  const options: Intl.DateTimeFormatOptions = { year: 'numeric', month: 'short', day: 'numeric' };
  return new Date(dateString).toLocaleDateString(undefined, options);
};

// Format currency (RM)
const formatCurrency = (amount?: number) => {
  if (amount === null || amount === undefined) return '0.00';
  return `${amount.toFixed(2)}`;
};

// Truncate long strings
const truncateString = (str?: string, maxLength = 30) => {
  if (!str) return '';
  if (str.length > maxLength) {
    return str.substring(0, maxLength - 3) + '...';
  }
  return str;
};

// Handle claim resolution
const resolveClaim = async (approved: boolean) => {
  if (!props.data?.id) return;
  
  try {
    await adminClaims.resolveClaim(props.data.id, approved);
    isOpen.value = false;
  } catch (error) {
    console.error("Failed to resolve claim:", error);
  }
};
</script>