<template>
  <div class="relative">
    <span
      class="capitalize inline-flex items-center rounded-md px-2 py-1 text-xs font-medium"
      :class="{
        'bg-emerald-100 text-emerald-600': status.toLowerCase() === 'approved',
        'bg-red-100 text-red-600': status.toLowerCase() === 'rejected',
        'bg-yellow-100 text-yellow-600': status.toLowerCase() === 'pending',
        'bg-orange-100 text-orange-600 cursor-pointer': status.toLowerCase() === 'anomaly',
      }"
      @click="handleClick"
    >
      {{ status }}
    </span>

    <!-- Popup for anomaly reason -->
    <div
      v-if="showPopup && status.toLowerCase() === 'anomaly'"
      class="absolute z-10 mt-2 p-3 bg-white border border-gray-300 rounded-lg shadow-lg w-64"
      style="top: 100%; left: 0;"
    >
        <div class="sm:flex sm:items-start">
          <div class="mx-auto flex size-12 shrink-0 items-center justify-center rounded-full bg-orange-100 sm:mx-0 sm:size-10">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" data-slot="icon" aria-hidden="true" class="size-6 text-orange-600">
              <path d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126ZM12 15.75h.007v.008H12v-.008Z" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
          </div>
          <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
            <h3 id="dialog-title" class="text-base font-semibold text-gray-900">Reason</h3>
            <div class="mt-2">
              <p class="text-sm text-gray-500 whitespace-normal break-words">{{ anomalyReason || 'No reason provided' }}</p>
            </div>
          </div>
        </div>
        <div class="mt-5 sm:mt-4 sm:flex sm:flex-row-reverse">
          <button @click="closePopup" type="button" command="close" commandfor="dialog" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-xs ring-1 ring-gray-300 ring-inset hover:bg-gray-50 sm:mt-0 sm:w-auto">Close</button>
        </div>
    </div>

    <!-- Backdrop to close popup when clicking outside -->
    <div
      v-if="showPopup"
      class="fixed inset-0 z-5"
      @click="closePopup"
    ></div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  status: String,
  anomalyReason: {
    type: String,
    required: false,
    default: null
  }
});

const showPopup = ref(false)

const handleClick = () => {
  if (props.status.toLowerCase() === 'anomaly') {
    showPopup.value = true
  }
}

const closePopup = () => {
  showPopup.value = false
}
</script>
