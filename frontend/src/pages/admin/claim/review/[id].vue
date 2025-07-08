<template>
  <form>
    <!-- Content Border -->
    <div
      class="mx-auto mt-15 max-w-4xl rounded-2xl border border-gray-200 bg-white px-15 py-10 shadow-lg"
    >
      <!-- Back Button -->
      <div class="space-y-1 border-b border-gray-900/10 pb-12">
        <div class="relative flex items-center justify-center">
          <button @click="router.back()" type="button" class="absolute left-0">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-8 w-6"
              viewBox="0 0 24 24"
              fill="currentColor"
            >
              <path
                d="M19 11H7.14l3.63-4.36a1 1 0 1 0-1.54-1.28l-5 6a1 1 0 0 0-.09.15c0 .05 0 .08-.07.13A1 1 0 0 0 4 12a1 1 0 0 0 .07.36c0 .05 0 .08.07.13a1 1 0 0 0 .09.15l5 6A1 1 0 0 0 10 19a1 1 0 0 0 .64-.23a1 1 0 0 0 .13-1.41L7.14 13H19a1 1 0 0 0 0-2"
              />
            </svg>
          </button>

          <!-- Header -->
          <h1
            class="mr-130 flex justify-center text-2xl font-bold text-blue-950"
          >
            <template v-if="loading">Loading...</template>
            <template v-else-if="error">{{ error }}</template>
            <template v-else-if="invoice">
              #{{ invoice.invoice_id }} {{ dummyStaff_name }}
            </template>
            <template v-else>No data found</template>
          </h1>
        </div>

        <!-- Receipt Details -->

        <!-- Status -->
        <div
          v-if="claim.status"
          class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6"
        >
          <div class="sm:col-span-3">
            <DropdownInput
              v-if="!isStored"
              label="Category"
              name="category"
              id="category"
              :options="categories"
              :model-value="invoice.category"
              disabled
            />
            <TextInput
              v-else
              label="Category"
              name="category"
              id="category"
              :model-value="invoice.category"
              disabled
            />
          </div>

          <!-- Date -->
          <div class="sm:col-span-3">
            <CalendarInput
              label="Date (YYYY-MM-DD)"
              name="date"
              id="date"
              :model-value="invoice.invoice_date"
              disabled
            />
          </div>

          <!-- Merchant Name -->
          <div class="sm:col-span-full">
            <TextInput
              label="Merchant Name"
              name="merchantName"
              id="merchant-name"
              autocomplete="name"
              :model-value="invoice.merchant_name"
              disabled
            />
          </div>

          <!-- Merchant Address -->
          <div class="sm:col-span-full">
            <TextInput
              label="Merchant Address"
              name="merchantAddress"
              id="merchant-address"
              autocomplete="street-address"
              :model-value="invoice.merchant_address"
              disabled
            />
          </div>

          <!-- Remark -->
          <div class="sm:col-span-full">
            <TextInput
              label="Remark"
              name="remark"
              id="remark"
              :model-value="invoice.remark"
              disabled
            />
          </div>
        </div>
      </div>

      <!-- Items/Services -->
      <div
        v-if="invoice"
        class="grid grid-cols-1 gap-x-6 gap-y-8 border-b border-gray-900/10 pb-12 sm:grid-cols-6"
      >
        <div class="sm:col-span-full">
          <h2 class="mt-6 text-sm font-medium text-theme-300">
           Items/Services
          </h2>
          <table
            class="col-span-full w-full border-separate border-spacing-y-4"
          >
            <thead class="bg-blue-950 text-white">
              <tr class="">
                <th class="rounded-l-lg px-4 py-2 text-left">Description</th>
                <th class="px-4 py-2 text-left">Category</th>
                <th class="px-4 py-2 text-right">Quantity</th>
                <th class="rounded-r-lg px-4 py-2 text-right">Total (RM)</th>
              </tr>
            </thead>

            <tbody>
              <tr
                v-for="(item, index) in invoice.items_services"
                :key="index"
                class="bg-gray-200 text-theme-300"
              >
                <td class="rounded-l-lg px-4 py-3 text-sm">{{ item.description }}</td>
                <td class="px-4 py-3 text-right text-sm">{{ item.quantity }}</td>
                <td class="rounded-r-lg px-4 py-3 text-right text-sm">
                  {{
                    item.unit_price.toLocaleString("en-MY", {
                      minimumFractionDigits: 2,
                      maximumFractionDigits: 2,
                    })
                  }}
                </td>
              </tr>

              <tr class="text-right font-semibold text-theme-300">
                <td></td>
                <td class="rounded-l-lg bg-gray-200 px-4 py-3">Total</td>
                <td class="rounded-r-lg bg-gray-200 px-4 py-3 text-sm">
                  {{
                    invoice.items_services
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

      <!-- Button -->
      <div class="mt-6 flex items-center justify-end gap-x-6">
        <button
          type="button"
          class="rounded-md bg-red-400 px-5.5 py-2.5 text-sm font-semibold text-white transition-colors hover:bg-red-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-theme-200 relative z-50"
        >
          Reject
        </button>
        <button
          type="button"
          class="rounded-md bg-green-400 px-3.5 py-2.5 text-sm font-semibold text-white transition-colors hover:bg-green-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-theme-200 relative z-50"
        >
          Approve
        </button>
      </div>
    </div>
  </form>
</template>

<script setup>
import { storeToRefs } from "pinia";
import { useRouter } from "vue-router";
import { ref, computed, onMounted } from "vue";

import DropdownInput from "@/components/form/DropdownInput.vue";
import CalendarInput from "@/components/form/CalendarInput.vue";
import TextInput from "@/components/form/TextInput.vue";

import { useInvoiceStore } from "@/stores/invoice";

const router = useRouter();
const invoiceStore = useInvoiceStore();

const { invoice, loading, error } = storeToRefs(invoiceStore);

const isStored = ref(true);
const dummyStaff_name = ref("John Doe");

onMounted(async () => {
const invoiceId = router.currentRoute.value.params.id;
await invoiceStore.fetchInvoice(invoiceId);
});

const totalAmount = computed(() =>
invoice.value 
    ? invoice.value.items_services.reduce(
        (sum, item) => sum + item.quantity * item.unit_price,
        0,
    )
    : 0,
);
</script>
