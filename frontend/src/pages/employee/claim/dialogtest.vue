<template>
  <div class="mx-auto my-14 w-full max-w-6xl bg-gray-100">
    <!-- Submit Button -->
    <div class="flex justify-center px-4 sm:px-8 lg:px-14">
      <button
        class="hover:bg-theme-400 mt-4 rounded bg-theme-300 px-4 py-2 text-white"
        @click="submitForApproval"
      >
        Submit
      </button>
    </div>

    <!-- Success Dialog -->
    <div v-if="showDialog" class="relative z-10" aria-labelledby="dialog-title" role="dialog" aria-modal="true">
      <!-- Background backdrop -->
      <div class="fixed inset-0 bg-gray-500/75 transition-opacity" aria-hidden="true"></div>

      <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
        <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
          <!-- Dialog panel -->
          <div class="relative transform overflow-hidden rounded-lg bg-white px-4 pt-5 pb-4 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-sm sm:p-6">
            <div>
              <div class="mx-auto flex size-12 items-center justify-center rounded-full bg-green-100">
                <svg class="size-6 text-green-600" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" d="m4.5 12.75 6 6 9-13.5" />
                </svg>
              </div>
              <div class="mt-3 text-center sm:mt-5">
                <h3 class="text-base font-semibold text-gray-900" id="dialog-title">Submission Successful</h3>
                <p class="mt-2 text-sm text-gray-500">Your submission is pending for approval.</p>
              </div>
            </div>
            <div class="mt-5 sm:mt-6">
              <button
                @click="showDialog = false"
                type="button"
                class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white hover:bg-indigo-500"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const showDialog = ref(false);

function submitForApproval() {
  console.log('Submit button clicked!');
  showDialog.value = true;
  console.log('Dialog should show now:', showDialog.value);
}
</script>