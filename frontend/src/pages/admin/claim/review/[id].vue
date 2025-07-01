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
              #{{ claim.id }} {{ staff.name }}
              <span
                class="flex text-base items-center rounded-md px-2 py-1 font-medium"
                :class="{
                  'bg-emerald-100 text-emerald-600':
                    claim.status === 'Approved',
                  'bg-red-100 text-red-600': claim.status === 'Rejected',
                  'bg-yellow-100 text-yellow-600': claim.status === 'Pending',
                  'bg-orange-100 text-orange-600': claim.status === 'Fraud',
                  'bg-black text-white': claim.status === 'Anomaly',
                }"
              >
                {{ claim.status }}
              </span>
            </template>
            <template v-else>No data found</template>
          </h1>
        </div>

        <!-- Receipt Details -->
        <!-- Category -->
        <div v-if="claim" class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
          <div class="sm:col-span-3">
            <DropdownInput
              label="Status"
              name="status"
              id="status"
              :options="[
                'Pending',
                'Approved',
                'Rejected',
              ]"
              v-model="claim.status"
            />
          </div>

          <!-- Date -->
          <div class="sm:col-span-3">
            <CalendarInput label="Date" type="text" name="date" id="date" :model-value="claim.date" disabled />
          </div>

          <!-- Merchant Name -->
          <div class="sm:col-span-full">
            <TextInput label="Merchant Name" name="merchantName" id="merchant-name" autocomplete="name"
              :model-value="claim.merchantName" disabled />
          </div>

          <!-- Merchant Address -->
          <div class="sm:col-span-full">
            <TextInput label="Merchant Address" name="merchantAddress" id="merchant-address"
              autocomplete="street-address" :model-value="claim.merchantAddress" disabled />
          </div>

          <!-- Remark -->
          <div class="sm:col-span-full">
            <TextInput label="Remark" name="remark" id="remark" :model-value="claim.remark" disabled />
          </div>
        </div>
      </div>

      <!-- Items/Services -->
      <div v-if="claim" class="grid grid-cols-1 gap-x-6 gap-y-8 border-b border-gray-900/10 pb-12 sm:grid-cols-6">
        <div class="sm:col-span-full">
          <h2 class="mt-6 text-sm font-medium text-theme-300">
            Invoices
          </h2>
          <table class="col-span-full w-full border-separate border-spacing-y-4">
            <thead class="bg-blue-950 text-white">
              <tr class="">
                <th class="rounded-l-lg px-4 py-2 text-left">Description</th>
                <th class="rounded-l-lg px-4 py-2 text-left">Category</th>
                <th class="px-4 py-2 text-right">Quantity</th>
                <th class="rounded-r-lg px-4 py-2 text-right">
                  Total (RM)
                </th>
              </tr>
            </thead>

            <tbody>
              <tr v-for="(item, index) in claim.items" :key="index" class="bg-gray-200 text-theme-300">
                <td class="rounded-l-lg px-4 py-3">{{ item.description }}</td>
                <td class="rounded-l-lg px-4 py-3">Category name</td>
                <td class="px-4 py-3 text-right">{{ item.quantity }}</td>
                <td class="rounded-r-lg px-4 py-3 text-right">
                  {{
                    item.unitPrice.toLocaleString("en-MY", {
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
        <button type="button"
          class="rounded-md bg-red-400 px-5.5 py-2.5 text-sm font-semibold text-white transition-colors hover:bg-red-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-theme-200">
          Reject
        </button>
        <button type="button"
          class="rounded-md bg-green-400 px-3.5 py-2.5 text-sm font-semibold text-white transition-colors hover:bg-green-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-theme-200">
          Approve
        </button>
      </div>
    </div>
  </form>
</template>

<script setup>
import { useRouter } from "vue-router";
import { ref, computed, onMounted } from "vue";
import DropdownInput from "@/components/form/DropdownInput.vue";
import CalendarInput from "@/components/form/CalendarInput.vue";
import TextInput from "@/components/form/TextInput.vue";

const router = useRouter();
const staff = ref(null);
const claim = ref(null);
const loading = ref(true);
const error = ref("");
const isStored = ref(false); // <-- This flag controls the logic
const categories = [
  "Gadget",
  "Travel Expenses",
  "Meals and Entertainment",
  "Accommodation",
  "Communication",
];

// Example: Fetching from mock JSON (replace with your API endpoints)
onMounted(async () => {
  loading.value = true;
  try {
    // Replace with your actual endpoints or logic

    // const staffRes = await fetch("/api/staff/1"); Makes a network request to your backend API to get staff data.
    // staff.value = await staffRes.json(); Parses the JSON response and assigns it to your staff ref.

    // const staffRes = await fetch("/api/staff/1");
    // staff.value = await staffRes.json();

    // const claimRes = await fetch("/api/claims/1");
    // claim.value = await claimRes.json();

    // const claimRes = await fetch("/api/claims/1");
    // claim.value = await claimRes.json();

    // Mock data for demonstration
    // ...fetch logic...
    staff.value = { id: "001", name: "John Doe" };
    claim.value = {
      id: "001",
      status: "Pending",
      category: "Gadget",
      date: "06/05/2025",
      merchantName: "Samsung Store",
      merchantAddress: "123 Main St",
      remark: "For project use",
      items: [
        {
          description: "Galaxy Tab S10 Ultra",
          quantity: 1,
          unitPrice: 4299.0,
        },
        {
          description: '24" Essential Monitor S3',
          quantity: 1,
          unitPrice: 399.0,
        },
      ],
    };
    // Simulate claim is already stored (set to true after saving)
    isStored.value = true;
  } catch (e) {
    error.value = "Failed to load data.";
  } finally {
    loading.value = false;
  }
});

const totalAmount = computed(() =>
  claim.value
    ? claim.value.items.reduce(
      (sum, item) => sum + item.quantity * item.unitPrice,
      0,
    )
    : 0,
);
</script>
