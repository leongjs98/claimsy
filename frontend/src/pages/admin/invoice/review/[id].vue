<template>
  <form>
    <!-- Content Border -->
    <div class="mx-auto mt-15 max-w-4xl rounded-2xl border border-gray-200 bg-white px-15 py-10 shadow-lg">
      <!-- Back Button -->
      <div class="space-x-1 border-b border-gray-900/10 pb-12">
        <div class="relative flex items-center">
          <button @click="router.back()" type="button" class="">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-6" viewBox="0 0 24 24" fill="currentColor">
              <path
                d="M19 11H7.14l3.63-4.36a1 1 0 1 0-1.54-1.28l-5 6a1 1 0 0 0-.09.15c0 .05 0 .08-.07.13A1 1 0 0 0 4 12a1 1 0 0 0 .07.36c0 .05 0 .08.07.13a1 1 0 0 0 .09.15l5 6A1 1 0 0 0 10 19a1 1 0 0 0 .64-.23a1 1 0 0 0 .13-1.41L7.14 13H19a1 1 0 0 0 0-2" />
            </svg>
          </button>

          <h1 class="ml-4 flex items-center justify-center gap-4 text-2xl font-bold text-blue-950">
            <template v-if="loading">Loading...</template>
            <template v-else-if="error">{{ error }}</template>
            <template v-else-if="staff && claim">
              Invoice #{{ invoice.employee?.id }} {{ invoice.employee?.name }}
            </template>
            <template v-else>No data found</template>
          </h1>
        </div>

        <!-- Receipt Details -->
        <!-- Category -->
        <div v-if="claim" class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
          <!-- Date -->
          <div class="sm:col-span-3">
            <CalendarInput label="Date (YYYY-MM-DD)" :model-value="formatDate(invoice.invoice_date)" name="date"
              id="date" v-model="claim.date" disabled />
          </div>

          <!-- Merchant Name -->
          <div class="sm:col-span-full">
            <TextInput label="Merchant Name" name="merchantName" id="merchant-name" autocomplete="name"
              :model-value="invoice.merchantName" disabled />
          </div>

          <!-- Merchant Address -->
          <div class="sm:col-span-full">
            <TextInput label="Merchant Address" name="merchantAddress" id="merchant-address"
              autocomplete="street-address" :model-value="invoice.merchantAddress" disabled />
          </div>

          <!-- Remark -->
          <div class="sm:col-span-full">
            <TextInput label="Remark" name="remark" id="remark" :model-value="claim.remark" disabled />
          </div>
        </div>
      </div>

      <!-- Items/Services -->
      <div v-if="claim" class="grid grid-cols-1 gap-x-6 gap-y-8 pb-12 sm:grid-cols-6">
        <div class="sm:col-span-full">
          <h2 class="mt-6 text-sm font-medium text-theme-300">Invoices</h2>
          <table class="col-span-full w-full border-separate border-spacing-y-4">
            <thead class="bg-blue-950 text-white">
              <tr class="">
                <th class="rounded-l-lg px-4 py-2 text-left">Description</th>
                <th class="rounded-l-lg px-4 py-2 text-left">Category</th>
                <th class="px-4 py-2 text-right">Quantity</th>
                <th class="rounded-r-lg px-4 py-2 text-right">Total (RM)</th>
              </tr>
            </thead>

            <tbody>
              <tr v-for="(item, index) in claim.items" :key="index" class="bg-gray-200 text-theme-300">
                <td class="rounded-l-lg px-4 py-3">{{ item.item }}</td>
                <td class="rounded-l-lg px-4 py-3">{{ invoice.category }}</td>
                <td class="px-4 py-3 text-right">{{ item.quantity }}</td>
                <td class="rounded-r-lg px-4 py-3 text-right">
                  {{
                    formatCurrency(item.unit_price)
                  }}
                </td>
                <td>
                  {{ formatCurrency(item.unit_price * item.quantity) }}
                </td>
              </tr>
              <tr class="bg-gray-200 font-semibold">
                <td colspan="4" class="px-4 py-3 text-right">Invoice Total:</td>
                <td class="rounded-r-lg px-4 py-3 text-right">
                  {{formatCurrency(invoice.itemsServices.reduce((sum, item) => sum + (item.unit_price * item.quantity),
                  0))
                  }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </form>
</template>

<script setup>
import { useRouter } from "vue-router";
import { ref, computed, onMounted } from "vue";
import { useAdminClaimStore } from "@/stores/admin-claims.ts";
import { storeToRefs } from "pinia";

const adminClaims = useAdminClaimStore();
const router = useRouter();
const route = useRoute();

const staff = ref(null);
const claim = ref(null);
const loading = ref(true);
const error = ref("");

// Example: Fetching from mock JSON (replace with your API endpoints)
onMounted(async () => {
  try {
    loading.value = true;
    const claimId = Number(route.params.id)

    const claimData = await adminClaims.fetchClaimDetails(claimId);
    claim.value = claimData;
  } catch (err) {
    console.error("Error fetching claim details", err);
    error.value = "Failed to load claim details";
  } finally {
    loading.value = false;
  }
});

const formatDate = (dateString) => {
  if (!dateString) return '';
  const options = { year: 'numeric', month: 'short', day: 'numeric' };
  return new Date(dateString).toLocaleDateString(undefined, options);
};

const formatCurrency = (amount) => {
  if (amount === null || amount === undefined) return '0.00';
  return `${amount.toFixed(2)}`;
};

</script>
