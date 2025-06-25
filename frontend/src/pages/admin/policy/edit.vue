<template>
  <form @submit.prevent="handleSubmit">
    <div
      class="mx-auto mt-15 h-[65rem] max-w-4xl rounded-2xl border border-gray-200 bg-white px-15 py-10 shadow-lg"
    >
      <div class="pb-12">
        <div class="relative flex items-center justify-center">
          <button @click="handleCancel" type="button" class="absolute left-0">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-6 w-6 text-yellow-500"
              viewBox="0 0 24 24"
              fill="currentColor"
            >
              <path
                d="M19 11H7.14l3.63-4.36a1 1 0 1 0-1.54-1.28l-5 6a1 1 0 0 0-.09.15c0 .05 0 .08-.07.13A1 1 0 0 0 4 12a1 1 0 0 0 .07.36c0 .05 0 .08.07.13a1 1 0 0 0 .09.15l5 6A1 1 0 0 0 10 19a1 1 0 0 0 .64-.23a1 1 0 0 0 .13-1.41L7.14 13H19a1 1 0 0 0 0-2"
              />
            </svg>
          </button>
          <h1 class="flex justify-center text-4xl font-semibold text-blue-950">
            Policy Details
          </h1>
        </div>

        <!-- Loading indicator -->
        <div v-if="policyStore.loading" class="mt-8 flex justify-center">
          <div class="text-blue-800">Loading policies...</div>
        </div>

        <!-- Error message -->
        <!-- <div v-if="policyStore.error" class="mt-8 rounded-md bg-red-50 p-4"> -->
        <!--   <div class="text-red-800">{{ policyStore.error }}</div> -->
        <!-- </div> -->

        <div class="mt-8 grid grid-cols-6 gap-8">
          <div class="sm:col-span-full">
            <label
              for="eligibilityCriteria"
              class="font-semibold text-blue-800"
            >
              Claim Eligibility Criteria
            </label>
            <div class="mt-4">
              <textarea
                v-model="eligibilityCriteria"
                id="eligibilityCriteria"
                name="eligibilityCriteria"
                rows="8"
                :disabled="policyStore.loading"
                class="block w-full rounded-md bg-gray-200 px-3 py-2 text-base text-blue-800 shadow-sm/30 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 disabled:opacity-50"
              ></textarea>
            </div>
          </div>

          <div class="col-span-3 row-span-1 text-blue-800">
            <label for="approvalLimitations1" class="font-semibold">
              Claim Approval & Limitations
            </label>
            <div class="mt-4">
              <textarea
                v-model="approvalLimitations1"
                name="approvalLimitations1"
                id="approvalLimitations1"
                rows="8"
                :disabled="policyStore.loading"
                class="block w-full rounded-md bg-gray-200 px-3 py-2 text-base text-blue-800 shadow-sm/30 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 disabled:opacity-50"
              ></textarea>
            </div>
          </div>

          <div class="col-span-3 row-span-1 space-y-4 text-blue-800">
            <label for="claimDenial1" class="font-semibold">Claim Denial</label>
            <div class="mt-4">
              <textarea
                v-model="claimDenial1"
                name="claimDenial1"
                id="claimDenial1"
                rows="8"
                :disabled="policyStore.loading"
                class="block w-full rounded-md bg-gray-200 px-3 py-2 text-base text-blue-800 shadow-sm/30 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 disabled:opacity-50"
              ></textarea>
            </div>
          </div>

          <div class="col-span-3 row-span-1 space-y-4 text-blue-800">
            <label for="approvalLimitations2" class="font-semibold">
              Claim Approval & Limitations
            </label>
            <div class="mt-4">
              <textarea
                v-model="approvalLimitations2"
                name="approvalLimitations2"
                id="approvalLimitations2"
                rows="8"
                :disabled="policyStore.loading"
                class="block w-full rounded-md bg-gray-200 px-3 py-2 text-base text-blue-800 shadow-sm/30 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 disabled:opacity-50"
              ></textarea>
            </div>
          </div>

          <div class="col-span-3 row-span-1 space-y-4 text-blue-800">
            <label for="claimDenial2" class="font-semibold">Claim Denial</label>
            <div class="mt-4">
              <textarea
                v-model="claimDenial2"
                name="claimDenial2"
                id="claimDenial2"
                rows="8"
                :disabled="policyStore.loading"
                class="block w-full rounded-md bg-gray-200 px-3 py-2 text-base text-blue-800 shadow-sm/30 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 disabled:opacity-50"
              ></textarea>
            </div>
          </div>
          <div class="col-span-full flex justify-center gap-4">
            <button
              class="z-10 ml-10 flex justify-center gap-4 rounded-full bg-blue-800 px-10 py-2 font-bold text-white transition hover:bg-blue-700"
            >
              Cancel
            </button>
            <button
              class="z-10 ml-10 flex justify-center gap-4 rounded-full bg-blue-800 px-10 py-2 font-bold text-white transition hover:bg-blue-700"
              @click="open = true"
            >
              Submit
            </button>
          </div>
          <!-- <div>
            <div class="col-span-full flex justify-center gap-4">
              <button
                type="button"
                class="border-blue rounded-full border bg-white px-10 py-2 font-bold text-blue-800 transition hover:bg-gray-100"
              >
                Cancel
              </button>
              <div>
                <button
                  class="rounded-md bg-blue-950/5 px-2.5 py-1.5 text-sm font-semibold text-blue-900 hover:bg-blue-950/10"
                  @click="console.log(`Hi`)"
                >
                  Submit
                </button>
              </div> -->

          <TransitionRoot as="template" :show="open">
            <Dialog class="relative z-10" @close="open = false">
              <TransitionChild
                as="template"
                enter="ease-out duration-300"
                enter-from="opacity-0"
                enter-to="opacity-100"
                leave="ease-in duration-200"
                leave-from="opacity-100"
                leave-to="opacity-0"
              >
                <div class="fixed inset-0 bg-gray-500/75 transition-opacity" />
              </TransitionChild>

              <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
                <div
                  class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0"
                >
                  <TransitionChild
                    as="template"
                    enter="ease-out duration-300"
                    enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                    enter-to="opacity-100 translate-y-0 sm:scale-100"
                    leave="ease-in duration-200"
                    leave-from="opacity-100 translate-y-0 sm:scale-100"
                    leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                  >
                    <DialogPanel
                      class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg"
                    >
                      <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
                        <div class="sm:flex sm:items-start">
                          <div
                            class="mx-auto flex size-12 shrink-0 items-center justify-center rounded-full bg-blue-100 sm:mx-0 sm:size-10"
                          >
                            <CheckCircleIcon
                              class="size-10 text-blue-900"
                              aria-hidden="true"
                            />
                          </div>
                          <div
                            class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left"
                          >
                            <DialogTitle
                              as="h3"
                              class="text-base font-semibold text-gray-900"
                              >Policy Successfully Submitted</DialogTitle
                            >
                            <div class="mt-2">
                              <p class="text-sm text-gray-500">
                                Your Policy has been successfully been
                                submitted.
                              </p>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div
                        class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6"
                      >
                        <button
                          type="button"
                          class="inline-flex w-full justify-center rounded-md bg-blue-900 px-3 py-2 text-sm font-semibold text-white shadow-xs hover:bg-blue-500 sm:ml-3 sm:w-auto"
                          @click="open = false"
                        >
                          Thank You
                        </button>
                      </div>
                    </DialogPanel>
                  </TransitionChild>
                </div>
              </div>
            </Dialog>
          </TransitionRoot>
        </div>
      </div>
    </div>
  </form>
</template>

<script setup>
import { ref, onMounted, computed, watch, onUnmounted } from "vue";
import { useRouter } from "vue-router";
import { usePolicyDetails } from "@/stores/policy";
import axios from "axios";

const showDialog = ref(false);
import {
  Dialog,
  DialogPanel,
  DialogTitle,
  TransitionChild,
  TransitionRoot,
} from "@headlessui/vue";
import { CheckCircleIcon } from "@heroicons/vue/24/solid";

const open = ref(false);

const router = useRouter();
const policyStore = usePolicyDetails();

const eligibilityCriteria = ref("");
const approvalLimitations1 = ref("");
const claimDenial1 = ref("");
const approvalLimitations2 = ref("");
const claimDenial2 = ref("");

const originalValues = ref({});

const hasChanges = computed(() => {
  if (!originalValues.value.eligibilityCriteria) return false;
  return (
    eligibilityCriteria.value !== originalValues.value.eligibilityCriteria ||
    approvalLimitations1.value !== originalValues.value.approvalLimitations1 ||
    claimDenial1.value !== originalValues.value.claimDenial1 ||
    approvalLimitations2.value !== originalValues.value.approvalLimitations2 ||
    claimDenial2.value !== originalValues.value.claimDenial2
  );
});

onMounted(async () => {
  try {
    await policyStore.fetchPolicies();

    const defaultEligibility = `- Conditions under which a claim is considered valid.
- Timeframe in which a claim must be filled after the incident or purchase.
- Required documentation (e.g., receipts, proof of damage, photos, police reports).`;

    const defaultApproval1 = `- Criteria for approval or rejection.
- Forms of compensation(e.g., payment, replacement, repair).
- Settlement process (e.g., bank transfer, in-store credit`;

    const defaultDenial1 = `- Grounds for denial (e.g., lack of documentation, excluded events).
- Right to appeal or request re-evaluation.
- Rejection communication process.`;

    const defaultApproval2 = `- Steps to contest a denied claim.
- Timeframe for appeals and final decisions.`;

    const defaultDenial2 = `- Scenarios not covered by the policy.
- Specific exceptions (e.g., acts of war, intentional damage, expired warranties).`;

    eligibilityCriteria.value =
      policyStore.eligibilityCriteriaText || defaultEligibility;
    approvalLimitations1.value =
      policyStore.approvalLimitations1Text || defaultApproval1;
    claimDenial1.value = policyStore.claimDenial1Text || defaultDenial1;
    approvalLimitations2.value =
      policyStore.approvalLimitations2Text || defaultApproval2;
    claimDenial2.value = policyStore.claimDenial2Text || defaultDenial2;

    originalValues.value = {
      eligibilityCriteria: eligibilityCriteria.value,
      approvalLimitations1: approvalLimitations1.value,
      claimDenial1: claimDenial1.value,
      approvalLimitations2: approvalLimitations2.value,
      claimDenial2: claimDenial2.value,
    };
  } catch (error) {
    console.error("Failed to load policies:", error);
  }
});

const handleSubmit = async () => {
  try {
    window.removeEventListener("beforeunload", beforeUnloadHandler);
    const response = await axios.get("http://127.0.0.1:8000/admin/policy");
    const data = await response.data();

    eligibilityCriteria.value = data.claim_eligibility_criteria.join("\n");
    const approval =
      data.claim_approval_limitations?.[0]?.points?.join("\n") || "";
    const denial = data.claim_denial?.[0]?.points?.join("\n") || "";

    approvalLimitations1.value = approval;
    approvalLimitations2.value = approval;
    claimDenial1.value = denial;
    claimDenial2.value = denial;

    alert("Policy data loaded from backend!");

    showDialog.value = true;
  } catch (error) {
    console.error("Failed to fetch policy data:", error);
  }
};

const handleCancel = () => {
  if (hasChanges.value) {
    const confirmLeave = confirm(
      "You have unsaved changes. Are you sure you want to leave?",
    );
    if (!confirmLeave) return;
  }
  window.removeEventListener("beforeunload", beforeUnloadHandler);
  policyStore.clearError();
  router.back();
};

watch(hasChanges, (newValue) => {
  console.log("Has changes:", newValue);
});

onUnmounted(() => {
  policyStore.setError("Error");
});
</script>
