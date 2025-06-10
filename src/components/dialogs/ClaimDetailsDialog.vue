<template>
  <v-dialog v-model="isOpen" max-width="800">
    <v-card class="rounded-lg shadow-lg">
      <div
        class="bg-theme-300 text-white px-6 py-4 flex justify-between items-center rounded-t-xl"
      >
        <h2 class="text-xl font-semibold">Claim Details</h2>
        <button
          @click="close"
          class="text-white hover:bg-blue-800 p-1 rounded-full"
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
          <h3 class="text-lg font-bold text-gray-800">Claim ID: #{{ data.id }}</h3>
        </div>

        <div
          class="grid grid-cols-7 gap-x-4 items-center mb-2 pb-2 border-b border-gray-200"
        >
          <span class="font-semibold text-sm text-gray-600">Category</span>
          <span class="font-semibold text-sm text-gray-600">Date</span>
          <span class="font-semibold text-sm text-gray-600 col-span-2"
            >Merchant</span
          >
          <span class="font-semibold text-sm text-gray-600">Item/Service</span>
          <span class="font-semibold text-sm text-gray-600 text-right"
            >Qty</span
          >
          <span class="font-semibold text-sm text-gray-600 text-right"
            >Price (RM)</span
          >
        </div>

        <div v-if="data && data.items && data.items.length">
          <div
            v-for="(item, index) in data.items"
            :key="index"
            class="grid grid-cols-7 gap-x-4 items-center py-3 text-sm border-b border-gray-100 last:border-b-0"
          >
            <span class="text-gray-700">{{ item.category }}</span>
            <span class="text-gray-700">{{ item.date }}</span>
            <div class="col-span-2">
              <span class="font-medium text-gray-900">{{ item.merchantName }}</span
              ><br />
              <span class="text-xs text-gray-500">{{ item.merchantAddress }}</span>
            </div>
            <span class="text-gray-700">{{ item.description }}</span>
            <span class="text-gray-700 text-right">{{ item.quantity }}</span>
            <span class="text-blue-600 font-semibold text-right">{{
              (item.quantity * item.unitPrice).toFixed(2)
            }}</span>
          </div>
        </div>
        <div v-else class="text-center py-4 text-gray-500">
          No items in this claim.
        </div>

        <div
          class="grid grid-cols-7 gap-x-4 items-center mt-6 pt-3 border-t border-gray-200"
        >
          <span class="font-bold text-gray-800 text-sm col-span-6">Total</span>
          <span class="font-bold text-blue-600 text-sm text-right">{{
            totalAmount.toFixed(2)
          }}</span>
        </div>

        <div v-if="data.remark" class="mt-6 pt-4 border-t border-gray-200">
          <h4 class="font-semibold text-gray-700 mb-2">Remark:</h4>
          <p class="text-sm text-gray-600 italic">{{ data.remark }}</p>
        </div>
      </div>
    </v-card>
  </v-dialog>
</template>

<script setup>
import { ref, watch, computed } from 'vue';

const props = defineProps({
  modelValue: Boolean,
  data: Object, // Expected: { id: string, remark: string, items: Array<{ category: string, date: string, merchantName: string, merchantAddress: string, description: string, quantity: number, unitPrice: number }> }
});
const emit = defineEmits(['update:modelValue']);

const isOpen = ref(props.modelValue);

watch(
  () => props.modelValue,
  (val) => {
    isOpen.value = val;
  }
);

watch(isOpen, (val) => {
  if (!val) {
    emit('update:modelValue', false);
  }
});

const totalAmount = computed(() => {
  if (props.data && props.data.items) {
    return props.data.items.reduce((sum, item) => sum + item.quantity * item.unitPrice, 0);
  }
  return 0;
});

const close = () => {
  isOpen.value = false;
};
</script>

<style scoped>
/* You can add any additional scoped styles here if needed,
    though Tailwind should cover most styling. */
.bg-blue-900 {
  background-color: #1e3a8a; /* Example: Tailwind's blue-900 */
}
.text-blue-600 {
  color: #2563eb; /* Example: Tailwind's blue-600 */
}
</style>