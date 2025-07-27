<template>
  <div
    class="bg-opacity-50 fixed inset-0 z-50 flex items-center justify-center bg-black"
    @click.self="$emit('close')"
  >
    <div class="w-full max-w-2xl rounded-lg bg-white p-6 shadow-xl">
      <h2 class="mb-4 text-xl font-semibold text-gray-800">
        Confirm Your Selected Expenses
      </h2>

      <ul class="mb-4 max-h-60 space-y-2 overflow-y-auto text-sm text-gray-700">
        <li
          v-for="(item, index) in selected"
          :key="index"
          class="rounded border p-2"
        >
          <div class="font-medium">{{ item.Name }} ({{ item.Category }})</div>
          <div class="text-xs text-gray-500">
            {{ item.Date }} | Qty: {{ item.Item }} | RM {{ item.Total }}
          </div>
        </li>
      </ul>

      <div class="mt-6 flex justify-end space-x-2">
        <button
          class="rounded bg-gray-200 px-4 py-2 text-sm hover:bg-gray-300"
          @click="$emit('close')"
        >
          Cancel
        </button>
        <button
          class="hover:bg-theme-400 rounded bg-theme-300 px-4 py-2 text-sm text-white"
          @click="$emit('confirm', selected)"
        >
          Confirm Submission
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
  defineProps({
    selected: {
      type: Array,
      required: true,
    },
  });
  defineEmits(["close", "confirm"]);
</script>
