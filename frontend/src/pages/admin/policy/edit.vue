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
        <div v-if="policyStore.error" class="mt-8 rounded-md bg-red-50 p-4">
          <div class="text-red-800">{{ policyStore.error }}</div>
        </div>

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
              @click="handleCancel"
              type="button"
              class="border-blue pointer-events: none rounded-full border bg-white px-10 py-2 font-bold text-blue-800 transition hover:bg-gray-100"
            >
              Cancel
            </button>
            <button
              type="submit"
              class="pointer-events: none ml-10 rounded-full bg-blue-800 px-10 py-2 font-bold text-white transition hover:bg-blue-700"
            >
              Submit
            </button>
          </div>
        </div>
      </div>
    </div>
  </form>
</template>

<script setup>
import { ref, onMounted, computed, watch, onUnmounted } from "vue";
import { useRouter } from "vue-router";
import { usePolicyDetails } from "@/stores/policy";

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
    const response = await fetch(
      "http://localhost:8000/docs#/Admin/get_policy_details_admin_policy_get",
    );
    const data = await response.json();

    // Fill Vue form fields with backend response
    eligibilityCriteria.value = data.claim_eligibility_criteria.join("\n");

    const approval =
      data.claim_approval_limitations?.[0]?.points?.join("\n") || "";
    const denial = data.claim_denial?.[0]?.points?.join("\n") || "";

    approvalLimitations1.value = approval;
    approvalLimitations2.value = approval;

    claimDenial1.value = denial;
    claimDenial2.value = denial;

    alert("Policy data loaded from backend!");
  } catch (error) {
    console.error("Failed to fetch policy data:", error);
    alert("Error fetching policy data");
  }
};

const handleCancel = () => {
  if (hasChanges.value) {
    const confirmLeave = confirm(
      "You have unsaved changes. Are you sure you want to leave?",
    );
    if (!confirmLeave) return;
  }
  policyStore.clearError();
  router.back();
};

watch(hasChanges, (newValue) => {
  console.log("Has changes:", newValue);
});

onUnmounted(() => {
  policyStore.clearError();
});
</script>
