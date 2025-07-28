<template>
  <form @submit.prevent="handleSubmit">
    <div
      class="mx-auto mt-15 max-w-4xl rounded-2xl border border-gray-200 bg-white px-15 py-10 shadow-lg"
    >
      <div class="pb-12">
        <div class="relative flex items-center justify-center">
          <button @click="router.back" type="button" class="absolute left-0">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-6 w-6"
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
            <label for="validClaimCriteria" class="font-semibold text-blue-800">
              Valid Claim Criteria
            </label>
            <div class="mt-4">
              <textarea
                v-model="validClaimCriteria"
                id="validClaimCriteria"
                name="validClaimCriteria"
                rows="8"
                :disabled="policyStore.loading"
                class="block w-full rounded-md bg-gray-100 p-4 text-base text-theme-300 shadow-sm outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 disabled:opacity-50"
              ></textarea>
            </div>
          </div>

          <div class="col-span-3 row-span-1">
            <label
              for="fraudulentClaimsIndicators"
              class="font-semibold text-blue-800"
            >
              Fraudulent Claims Indicators
            </label>
            <div class="mt-4">
              <textarea
                v-model="fraudulentClaimsIndicators"
                name="fraudulentClaimsIndicators"
                id="fraudulentClaimsIndicators"
                rows="8"
                :disabled="policyStore.loading"
                class="block w-full rounded-md bg-gray-100 p-4 text-base text-theme-300 shadow-sm outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 disabled:opacity-50"
              ></textarea>
            </div>
          </div>

          <div class="col-span-3 row-span-1">
            <label
              for="inappropriateClaimsCharacteristics"
              class="font-semibold text-blue-800"
            >
              Inappropriate Claims Characteristics
            </label>
            <div class="mt-4">
              <textarea
                v-model="inappropriateClaimsCharacteristics"
                name="inappropriateClaimsCharacteristics"
                id="inappropriateClaimsCharacteristics"
                rows="8"
                :disabled="policyStore.loading"
                class="block w-full rounded-md bg-gray-100 p-4 text-base text-theme-300 shadow-sm outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 disabled:opacity-50"
              ></textarea>
            </div>
          </div>

          <div class="col-span-3 row-span-1">
            <label
              for="documentationRequirements"
              class="font-semibold text-blue-800"
            >
              Documentation Requirements
            </label>
            <div class="mt-4">
              <textarea
                v-model="documentationRequirements"
                name="documentationRequirements"
                id="documentationRequirements"
                rows="8"
                :disabled="policyStore.loading"
                class="block w-full rounded-md bg-gray-100 p-4 text-base text-theme-300 shadow-sm outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 disabled:opacity-50"
              ></textarea>
            </div>
          </div>

          <div class="col-span-3 row-span-1">
            <label
              for="spendingLimitViolations"
              class="font-semibold text-blue-800"
            >
              Spending Limit Violations
            </label>
            <div class="mt-4">
              <textarea
                v-model="spendingLimitViolations"
                name="spendingLimitViolations"
                id="spendingLimitViolations"
                rows="8"
                :disabled="policyStore.loading"
                class="block w-full rounded-md bg-gray-100 p-4 text-base text-theme-300 shadow-sm outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 disabled:opacity-50"
              ></textarea>
            </div>
          </div>

          <div class="col-span-3 row-span-1">
            <label
              for="nonReimbursableExpenses"
              class="font-semibold text-blue-800"
            >
              Non-Reimbursable Expenses
            </label>
            <div class="mt-4">
              <textarea
                v-model="nonReimbursableExpenses"
                name="nonReimbursableExpenses"
                id="nonReimbursableExpenses"
                rows="8"
                :disabled="policyStore.loading"
                class="block w-full rounded-md bg-gray-100 p-4 text-base text-theme-300 shadow-sm outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 disabled:opacity-50"
              ></textarea>
            </div>
          </div>

          <div class="col-span-3 row-span-1">
            <label
              for="approvalProcessViolations"
              class="font-semibold text-blue-800"
            >
              Approval Process Violations
            </label>
            <div class="mt-4">
              <textarea
                v-model="approvalProcessViolations"
                name="approvalProcessViolations"
                id="approvalProcessViolations"
                rows="8"
                :disabled="policyStore.loading"
                class="block w-full rounded-md bg-gray-100 p-4 text-base text-theme-300 shadow-sm outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 disabled:opacity-50"
              ></textarea>
            </div>
          </div>

          <!-- <div class="col-span-3 row-span-1 text-blue-800"> -->
          <!--   <label for="approvalLimitations1" class="font-semibold"> -->
          <!--     Claim Approval & Limitations -->
          <!--   </label> -->
          <!--   <div class="mt-4"> -->
          <!--     <textarea -->
          <!--       v-model="approvalLimitations1" -->
          <!--       name="approvalLimitations1" -->
          <!--       id="approvalLimitations1" -->
          <!--       rows="8" -->
          <!--       :disabled="policyStore.loading" -->
          <!--       class="block w-full rounded-md bg-gray-200 px-3 py-2 text-base text-blue-800 shadow-sm/30 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 disabled:opacity-50" -->
          <!--     ></textarea> -->
          <!--   </div> -->
          <!-- </div> -->

          <!-- <div class="col-span-3 row-span-1 space-y-4 text-blue-800"> -->
          <!--   <label for="claimDenial1" class="font-semibold">Claim Denial</label> -->
          <!--   <div class="mt-4"> -->
          <!--     <textarea -->
          <!--       v-model="claimDenial1" -->
          <!--       name="claimDenial1" -->
          <!--       id="claimDenial1" -->
          <!--       rows="8" -->
          <!--       :disabled="policyStore.loading" -->
          <!--       class="block w-full rounded-md bg-gray-200 px-3 py-2 text-base text-blue-800 shadow-sm/30 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 disabled:opacity-50" -->
          <!--     ></textarea> -->
          <!--   </div> -->
          <!-- </div> -->

          <!-- <div class="col-span-3 row-span-1 space-y-4 text-blue-800"> -->
          <!--   <label for="approvalLimitations2" class="font-semibold"> -->
          <!--     Claim Approval & Limitations -->
          <!--   </label> -->
          <!--   <div class="mt-4"> -->
          <!--     <textarea -->
          <!--       v-model="approvalLimitations2" -->
          <!--       name="approvalLimitations2" -->
          <!--       id="approvalLimitations2" -->
          <!--       rows="8" -->
          <!--       :disabled="policyStore.loading" -->
          <!--       class="block w-full rounded-md bg-gray-200 px-3 py-2 text-base text-blue-800 shadow-sm/30 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 disabled:opacity-50" -->
          <!--     ></textarea> -->
          <!--   </div> -->
          <!-- </div> -->

          <!-- <div class="col-span-3 row-span-1 space-y-4 text-blue-800"> -->
          <!--   <label for="claimDenial2" class="font-semibold">Claim Denial</label> -->
          <!--   <div class="mt-4"> -->
          <!--     <textarea -->
          <!--       v-model="claimDenial2" -->
          <!--       name="claimDenial2" -->
          <!--       id="claimDenial2" -->
          <!--       rows="8" -->
          <!--       :disabled="policyStore.loading" -->
          <!--       class="block w-full rounded-md bg-gray-200 px-3 py-2 text-base text-blue-800 shadow-sm/30 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 disabled:opacity-50" -->
          <!--     ></textarea> -->
          <!--   </div> -->
          <!-- </div> -->
          <div class="col-span-full flex justify-center gap-4">
            <RouterLink to="/admin/claim/all">
              <SecondaryButton>Cancel</SecondaryButton>
            </RouterLink>
            <PrimaryButton @click="open = true"> Submit </PrimaryButton>
          </div>

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
                        <RouterLink to="/admin/claim/all">
                          <button
                            type="button"
                            class="inline-flex w-full justify-center rounded-md bg-blue-900 px-3 py-2 text-sm font-semibold text-white shadow-xs hover:bg-blue-500 sm:ml-3 sm:w-auto"
                            @click="open = false"
                          >
                            Thank You
                          </button>
                        </RouterLink>
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

const validClaimCriteria = ref(`- Must fall under eligible categories
- Medical, Supplies/Equipment, Travel, Meals/Entertainment, Accommodation
- Submitted within required timeframes (30 days general, 60 days medical)
- Include original receipts and completed expense forms
- Have proper business justification and manager approval
- Stay within spending limits (Medical: RM500, Meals: RM50/day travel, RM25/person business)
- Medical claims require medical certificates
  `);
const fraudulentClaimsIndicators =
  ref(`- False or altered receipts and signatures
- Double claiming same expense
- Personal expenses claimed as business
- Deliberately inflated amounts
- Claims for non-existent expenses
- Fake medical certificates
  `);
const inappropriateClaimsCharacteristics =
  ref(`- Exceeding spending limits or standards
- Unauthorized purchases without approval
- Policy guideline violations
- Poor business judgment in spending
- Missing or incomplete documentation
- Claims submitted past deadlines
`);
const documentationRequirements = ref(`- Original receipts (digital accepted)
- Completed expense claim form
- Business purpose explanation
- Manager approval signature
- Medical certificates for medical claims
- Project or client codes
`);
const spendingLimitViolations = ref(`- Medical over RM500 per incident
- Equipment over RM200 without approval
- Non-economy flights
- Meals over RM50/day or RM25/person
- Accommodation over RM300/night
- Tips over 20%
`);
const nonReimbursableExpenses = ref(`- Personal medical expenses
- Personal meals, travel, accommodation
- Personal supplies and equipment
- Traffic fines and penalties
- Family members' expenses
- Client or conference-paid expenses
`);
const approvalProcessViolations = ref(`- Missing manager approval
- No HR review for medical claims
- Bypassing approval thresholds
- Self-approval of expenses
- Missing documentation review
`);

// const approvalLimitations1 = ref("");
// const claimDenial1 = ref("");
// const approvalLimitations2 = ref("");
// const claimDenial2 = ref("");

const originalValues = ref({});

const hasChanges = computed(() => {
  if (!originalValues.value.validClaimCriteria) return false;
  return (
    validClaimCriteria.value !== originalValues.value.validClaimCriteria ||
    approvalLimitations1.value !== originalValues.value.approvalLimitations1 ||
    claimDenial1.value !== originalValues.value.claimDenial1 ||
    approvalLimitations2.value !== originalValues.value.approvalLimitations2 ||
    claimDenial2.value !== originalValues.value.claimDenial2
  );
});

//   onMounted(async () => {
//     try {
//       await policyStore.fetchPolicies();
//
//       const defaultEligibility = `- Conditions under which a claim is considered valid.
// - Timeframe in which a claim must be filled after the incident or purchase.
// - Required documentation (e.g., receipts, proof of damage, photos, police reports).`;
//
//       const defaultApproval1 = `- Criteria for approval or rejection.
// - Forms of compensation(e.g., payment, replacement, repair).
// - Settlement process (e.g., bank transfer, in-store credit`;
//
//       const defaultDenial1 = `- Grounds for denial (e.g., lack of documentation, excluded events).
// - Right to appeal or request re-evaluation.
// - Rejection communication process.`;
//
//       const defaultApproval2 = `- Steps to contest a denied claim.
// - Timeframe for appeals and final decisions.`;
//
//       const defaultDenial2 = `- Scenarios not covered by the policy.
// - Specific exceptions (e.g., acts of war, intentional damage, expired warranties).`;
//
//       validClaimCriteria.value =
//         policyStore.validClaimCriteriaText || defaultEligibility;
//       approvalLimitations1.value =
//         policyStore.approvalLimitations1Text || defaultApproval1;
//       claimDenial1.value = policyStore.claimDenial1Text || defaultDenial1;
//       approvalLimitations2.value =
//         policyStore.approvalLimitations2Text || defaultApproval2;
//       claimDenial2.value = policyStore.claimDenial2Text || defaultDenial2;
//
//       originalValues.value = {
//         validClaimCriteria: validClaimCriteria.value,
//         approvalLimitations1: approvalLimitations1.value,
//         claimDenial1: claimDenial1.value,
//         approvalLimitations2: approvalLimitations2.value,
//         claimDenial2: claimDenial2.value,
//       };
//     } catch (error) {
//       console.error("Failed to load policies:", error);
//     }
//   });

const handleSubmit = async () => {
  try {
    window.removeEventListener("beforeunload", beforeUnloadHandler);
    const response = await axios.get("http://127.0.0.1:8000/admin/policy");
    const data = await response.data();

    validClaimCriteria.value = data.claim_eligibility_criteria.join("\n");
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

// onUnmounted(() => {
//   policyStore.setError("Error");
// });
</script>
