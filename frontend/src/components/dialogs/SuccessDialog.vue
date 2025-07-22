<template>
  <div
    v-show="isOpen"
    class="relative z-30"
    aria-labelledby="dialog-title"
    role="dialog"
    aria-modal="true"
  >
    <Transition name="backdrop">
      <div
        class="fixed inset-0 bg-gray-500/75 transition-opacity"
        aria-hidden="true"
      ></div>
    </Transition>

    <Transition name="pane">
      <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
        <div
          class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0"
        >
          <div
            class="relative transform overflow-hidden rounded-lg bg-white px-4 pt-5 pb-4 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-sm sm:p-6"
          >
            <div>
              <div
                class="mx-auto flex size-12 items-center justify-center rounded-full bg-green-100"
              >
                <svg
                  class="size-6 text-green-600"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  aria-hidden="true"
                  data-slot="icon"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="m4.5 12.75 6 6 9-13.5"
                  />
                </svg>
              </div>
              <div class="mt-3 text-center sm:mt-5">
                <h3
                  class="text-base font-semibold text-gray-900"
                  id="dialog-title"
                >
                  <slot name="header"></slot>
                </h3>
                <div class="mt-2">
                  <p class="text-sm text-gray-500">
                    <slot></slot>
                  </p>
                </div>
              </div>
            </div>
            <div class="mt-5 sm:mt-6">
              <slot name="button">
                <button
                  @click="isOpen = false"
                  type="button"
                  class="inline-flex w-full justify-center rounded-md bg-theme-300 px-3 py-2 text-sm font-semibold text-white shadow-xs hover:bg-theme-200 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-theme-300"
                >
                  Go back
                </button>
              </slot>
            </div>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup lang="ts">
  import { ref, watch, computed } from "vue";

  const props = defineProps({
    modelValue: Boolean,
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
</script>
