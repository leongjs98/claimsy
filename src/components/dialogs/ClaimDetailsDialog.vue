<template>
  <v-dialog v-model="isOpen" max-width="1000">
    <v-card class="rounded-lg shadow-lg">
      <div
        class="flex items-center justify-between rounded-t-xl bg-theme-300 px-6 py-4 text-white"
      >
        <h2 class="text-xl font-semibold">Claim Details</h2>
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
        <div class="mb-6">
          <h3 class="text-lg font-bold text-gray-800">
            Claim ID: #{{ data.id }}
          </h3>
        </div>

        <table
          v-if="data && data.items && data.items.length"
          class="col-span-full mb-2 w-full min-w-full table-auto divide-y divide-gray-300"
        >
          <thead class="text-sm font-semibold text-gray-600">
            <tr class="text-left">
              <th class="pr-4 pb-2">Category</th>
              <th class="px-4 pb-2">Date</th>
              <th class="px-4 pb-2">Merchant</th>
              <th class="px-4 pb-2">Item/Service</th>
              <th class="px-4 pb-2 text-right">Qty</th>
              <th class="pb-2 pl-4 text-right">Price (RM)</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(item, index) in data.items"
              :key="`${item}-${index}`"
              class="border-b border-gray-100 py-3 text-sm last:border-b-0"
            >
              <td class="py-6 pr-4 text-gray-700">{{ item.category }}</td>
              <td class="px-4 py-6 text-gray-700">{{ item.date }}</td>
              <td class="px-4 py-6 text-gray-700">
                <span class="py-6 font-medium text-gray-900">
                  {{ item.merchantName }}
                </span>
                <br />
                <span class="text-xs text-gray-500">
                  {{ item.merchantAddress }}
                </span>
              </td>
              <td class="max-w-80 px-4 py-6 text-nowrap text-gray-700">
                {{ truncateString(item.description) }}
              </td>
              <td class="px-4 py-6 text-right text-gray-700">
                {{ item.quantity }}
              </td>
              <td class="py-6 text-right font-semibold text-blue-600">
                {{ (item.quantity * item.unitPrice).toFixed(2) }}
              </td>
            </tr>
            <tr class="border-b border-gray-100 py-3 text-sm last:border-b-0">
              <td class="py-6 pr-4 font-bold text-gray-800">Total</td>
              <td class="px-4 py-6 text-gray-700"></td>
              <td class="px-4 py-6 text-gray-700"></td>
              <td class="px-4 py-6 text-gray-700"></td>
              <td class="px-4 py-6 text-right text-gray-700"></td>
              <td class="py-6 text-right font-bold text-blue-600">
                {{ totalAmount.toFixed(2) }}
              </td>
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

          <div class="mt-4 sm:mt-0 sm:ml-16 sm:flex-none">
            <RouterLink
              to="/employee/claim/edit"
              class="block rounded-md bg-theme-200 px-3 py-2 text-center text-sm font-semibold text-white shadow-xs hover:bg-theme-300 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-theme-100"
            >
              More Details
            </RouterLink>
          </div>
        </div>
      </div>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
  import { defineProps, PropType } from "vue";

  interface Item {
    category: string;
    date: string;
    merchantName: string;
    merchantAddress: string;
    description: string;
    quantity: number;
    unitPrice: number;
  }

  interface Data {
    id: string;
    remark: string;
    items: Item[];
  }

  const props = defineProps({
    modelValue: {
      type: Boolean,
      required: false, // Or true, depending on whether it's required
    },
    data: {
      type: Object as PropType<Data | undefined>,
      required: false, // Or true, depending on whether it's required
      default: undefined,
      validator: (value: any): boolean => {
        if (value === undefined) {
          return true; // Allow undefined if not required
        }

        if (typeof value !== "object" || value === null) {
          return false;
        }

        const data = value as Data;

        if (typeof data.id !== "string") {
          return false;
        }

        if (typeof data.remark !== "string") {
          return false;
        }

        if (!Array.isArray(data.items)) {
          return false;
        }

        for (const item of data.items) {
          if (typeof item.category !== "string") return false;
          if (typeof item.date !== "string") return false;
          if (typeof item.merchantName !== "string") return false;
          if (typeof item.merchantAddress !== "string") return false;
          if (typeof item.description !== "string") return false;
          if (typeof item.quantity !== "number") return false;
          if (typeof item.unitPrice !== "number") return false;
        }

        return true;
      },
    },
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
    if (props.data && props.data.items) {
      return props.data.items.reduce(
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
