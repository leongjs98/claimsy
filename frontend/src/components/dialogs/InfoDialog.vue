  <template>
    <div>
      <TransitionRoot as="template" :show="isOpen">
        <Dialog class="relative z-10" @close="isOpen = false">
          <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
            leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
            <div class="fixed inset-0 bg-gray-500/75 transition-opacity" />
          </TransitionChild>

          <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
            <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
              <TransitionChild as="template" enter="ease-out duration-300"
                enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
                leave-from="opacity-100 translate-y-0 sm:scale-100"
                leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
                <DialogPanel
                  class="relative transform rounded-lg bg-white px-4 pt-5 pb-4 text-left shadow-xl transition-all sm:my-8 sm:w-fit sm:p-6">
                  <div>
                    <div class="mt-3 text-center sm:mt-5">
                      <DialogTitle as="h3" class="text-base font-semibold text-gray-900">
                        <slot name="title"></slot>
                      </DialogTitle>
                      <div class="mt-2">
                        <p class="max-h-[70vh] text-sm overflow-scroll text-gray-500 sm:w-fit">
                          <slot></slot>
                        </p>
                      </div>
                    </div>
                  </div>
                  <div class="mt-5 sm:mt-6">
                    <button type="button"
                      class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                      @click="isOpen = false">Go back</button>
                  </div>
                </DialogPanel>
              </TransitionChild>
            </div>
          </div>
        </Dialog>
      </TransitionRoot>
    </div>

  </template>

<script setup lang="ts">
import { ref, watch, computed } from "vue";
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'

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

const open = ref(true)
</script>
