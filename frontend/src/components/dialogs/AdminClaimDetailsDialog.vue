<template>
  <v-dialog v-model="isOpen" max-width="1000">
    <v-card class="rounded-lg shadow-lg">
      <div
        class="flex items-center justify-between rounded-t-xl bg-theme-300 px-6 py-4 text-white"
      >
        <h2 class="flex items-center gap-4 text-xl font-semibold">
          <span> Claim ID: #{{ data.Id }} </span>
          <span
            class="flex w-fit items-center rounded-md px-2 py-1 text-base font-medium"
            :class="{
              'bg-emerald-100 text-emerald-600': data.Status === 'Approved',
              'bg-red-100 text-red-600': data.Status === 'Rejected',
              'bg-yellow-100 text-yellow-600': data.Status === 'Pending',
              'bg-orange-100 text-orange-600': data.Status === 'Fraud',
              'bg-black text-white': data.Status === 'Anomaly',
            }"
          >
            {{ data.Status }}
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
          v-if="data && data.Items && data.Items.length"
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
            <tr
              v-for="(item, index) in data.Items"
              :key="`${item}-${index}`"
              class="border-b border-gray-100 py-3 text-sm last:border-b-0"
            >
              <td class="px-4 py-6 text-gray-700">
                <span class="py-6 font-medium text-gray-900">
                  {{ item.date }}
                </span>
                <br />
                <span class="text-xs text-gray-500">
                  {{ item.category }}
                </span>
              </td>
              <td class="px-4 py-6 text-gray-700">
                <span class="py-6 font-medium text-gray-900">
                  {{ item.merchantName }}
                </span>
                <br />
                <span class="text-xs text-gray-500">
                  {{ truncateString(item.merchantAddress) }}
                </span>
              </td>
              <td class="max-w-80 px-4 py-6 text-nowrap text-gray-700">
                {{ truncateString(item.description) }}
              </td>
              <td class="px-4 py-6 text-right text-gray-700">
                {{ item.quantity }}
              </td>
              <td class="py-6 text-right font-semibold text-blue-600">
                {{
                  (item.quantity * item.unitPrice).toLocaleString("en-US", {
                    minimumFractionDigits: 2,
                    maximumFractionDigits: 2,
                  })
                }}
              </td>
              <td class="px-4 py-6 text-theme-300 hover:underline">
                <div class="text-right">
                  <!-- TODO: change to dynamic link -->
                  <!-- TODO: admin will view admin version, employee = employee version-->
                  <RouterLink :to="`/admin/invoice/review/420`">
                    Details
                  </RouterLink>
                </div>
              </td>
            </tr>
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
        <div v-else class="py-4 text-center text-gray-500">
          No items in this claim.
        </div>

        <div
          class="my-6 flex items-center justify-between border-t border-gray-300 pt-4"
        >
          <div v-if="data.remark" class="">
            <h4 class="mb-2 font-semibold text-gray-700">Remark:</h4>
            <p class="text-sm text-gray-600 italic">{{ data.remark }}</p>
          </div>
          <div v-else></div>
          <div class="mt-6 flex items-center justify-end gap-x-6">
              <button type="button" class="rounded-md bg-red-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-xs hover:bg-red-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-red-600">
              Reject
              </button>
              <button type="button" class="rounded-md bg-green-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-xs hover:bg-green-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-green-600">
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

  const props = defineProps({
    modelValue: Boolean,
    // Expected: { id: string, remark: string, items: Array<{ category: string, date: string, merchantName: string, merchantAddress: string, description: string, quantity: number, unitPrice: number }> }
    data: Object,
  });
  const emit = defineEmits(["update:modelValue"]);

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

  const totalAmount = computed(() => {
    if (props.data && props.data.Items) {
      return props.data.Items.reduce(
        (sum, item) => sum + item.quantity * item.unitPrice,
        0,
      );
    }
    return 0;
  });

  function truncateString(str, maxLength = 30) {
    if (str.length > maxLength) {
      return str.substring(0, maxLength - 3) + "...";
    } else {
      return str;
    }
  }
</script>
