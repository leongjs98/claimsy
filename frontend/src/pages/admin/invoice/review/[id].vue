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
            <template v-else-if="staff && invoice">
            #{{ invoice.invoiceNumber }} {{ invoice.employee?.name }}
            </template>
            <template v-else>No data found</template>
          </h1>
        </div>

        <!-- Receipt Details -->
        <!-- Category -->
        <div v-if="invoice" class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
          <!-- Date -->
          <div class="sm:col-span-3">
            <CalendarInput label="Date (YYYY-MM-DD)" :model-value="formatDate(invoice?.invoiceDate)" name="date"
              id="date" model-value="invoice?.invoiceDate" disabled />
          </div>

          <!-- Merchant Name -->
          <div class="sm:col-span-full">
            <TextInput label="Merchant Name" name="merchantName" id="merchant-name" autocomplete="name"
              :model-value="invoice?.merchantName" disabled />
          </div>

          <!-- Merchant Address -->
          <div class="sm:col-span-full">
            <TextInput label="Merchant Address" name="merchantAddress" id="merchant-address"
              autocomplete="street-address" :model-value="invoice?.merchantAddress" disabled />
          </div>

          <!-- Remark -->
          <div class="sm:col-span-full">
            <TextInput label="Remark" name="remark" id="remark" :model-value="invoice?.remark" disabled />
          </div>
        </div>
      </div>

      <!-- Items/Services -->
      <div 
      v-if="invoice"  
      class="grid grid-cols-1 gap-x-6 gap-y-8 border-b border-gray-900/10 pb-12 sm:grid-cols-6">

        <div class="sm:col-span-full">
          <h2 class="mt-6 text-sm font-medium text-theme-300">Items/Services</h2>
          <table class="col-span-full w-full border-separate border-spacing-y-4">
            <thead class="bg-blue-950 text-white">
              <tr>
                <th class="rounded-l-lg px-4 py-2 text-left">Description</th>
                <th class="px-4 py-2 text-left">Category</th>
                <th class="px-4 py-2 text-right">Quantity</th>
                <th class="rounded-r-lg px-4 py-2 text-right">Total (RM)</th>
              </tr>
            </thead>

            <tbody>
              <tr 
              v-for="(item, index) in invoice?.itemsServices" 
              :key="index" 
              class="bg-gray-200 text-theme-300 text-sm">
                <td class="rounded-l-lg px-4 py-3">{{ item.item }}</td>
                <td class="px-4 py-3">{{ invoice?.category }}</td>
                <td class="px-4 py-3 text-right">{{ item.quantity }}</td>
                <td class="rounded-r-lg px-4 py-3 text-right">
                  {{
                    item.unit_price.toLocaleString("en-MY", {
                      minimumFractionDigits: 2,
                      maximumFractionDigits: 2,
                    })
                  }}
                </td>
              </tr>
              <tr class="text-right font-bold text-theme-300 text-sm">
                <td></td>
                <td></td>
                <td class="rounded-l-lg bg-gray-200 px-4 py-3">Total</td>
                <td class="rounded-r-lg bg-gray-200 px-4 py-3">
                  {{
                    invoice?.itemsServices
                      .reduce(
                        (sum, item) => sum + item.quantity * item.unit_price,
                        0,
                      )
                      .toLocaleString("en-MY", {
                        minimumFractionDigits: 2,
                        maximumFractionDigits: 2,
                      })
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
import { useRouter, useRoute } from "vue-router";
import { ref, onMounted } from "vue";
import { useAdminClaimStore } from "@/stores/admin-claims.ts";
import { storeToRefs } from "pinia";

const adminClaims = useAdminClaimStore();
const router = useRouter();
const route = useRoute();

const staff = ref(null);
const invoice = ref(null);
const loading = ref(true);
const error = ref("");

// Example: Fetching from mock JSON (replace with your API endpoints)
onMounted(async () => {
  try {
    loading.value = true;
    const invoiceId = Number(route.params.id)
    console.log("Fetching claim ID:", invoiceId);

    const invoiceData = await adminClaims.fetchInvoiceDetails(invoiceId);
    console.log("API Response:", invoiceData);
    if (!invoiceData) {
      throw new Error("Claim not found");
    }
    invoice.value = invoiceData;
    if (invoiceData.employee) {
      staff.value = invoiceData.employee;
    }
  } catch (err) {
    console.error("Error fetching claim details", err);
    error.value = "Failed to load invoice details";
  } finally {
    loading.value = false;
  }
});

const formatDate = (dateString) => {
  if (!dateString) {
    return '';
  }
  const date = new Date(dateString);
  if (isNaN(date.getTime())) {
    console.error("Invalid date string provided:", dateString);
    return ''; 
  }
  const year = date.getFullYear();
  const month = (date.getMonth() + 1).toString().padStart(2, '0');
  const day = date.getDate().toString().padStart(2, '0');
  return `${year}-${month}-${day}`;
};

</script>
