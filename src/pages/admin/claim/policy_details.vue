<template>
  <form>
    <div
      class="mx-auto mt-15 h-[65rem] max-w-4xl rounded-2xl border border-gray-200 bg-white px-15 py-10 shadow-lg"
    >
      <div class="pb-12">
        <div class="relative flex items-center justify-center">
          <button @click="router.back()" type="button" class="absolute left-0">
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
                class="block w-full rounded-md bg-gray-200 px-3 py-2 text-base text-blue-800 shadow-sm/30 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600"
              >
                <p>You typed: {{ eligibilityCriteria }}</p>
              </textarea>
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
                class="block w-full rounded-md bg-gray-200 px-3 py-2 text-base text-blue-800 shadow-sm/30 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600"
              >
                <p>You typed: {{ approvalLimitations1 }}</p>
              </textarea>
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
                class="block w-full rounded-md bg-gray-200 px-3 py-2 text-base text-blue-800 shadow-sm/30 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600"
              >
                <p>You typed: {{ claimDenial1 }}</p>
              </textarea>
            </div>
          </div>
          <div class="col-span-3 row-span-1 space-y-4 text-blue-800">
            <label for="approvalLimitations2" class="font-semibold"
              >Claim Approval & Limitations</label
            >
            <div class="mt-4">
              <textarea
                v-model="approvalLimitations2"
                name="approvalLimitations2"
                id="approvalLimitations2"
                rows="8"
                class="block w-full rounded-md bg-gray-200 px-3 py-2 text-base text-blue-800 shadow-sm/30 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600"
              >
                <p>You typed: {{ approvalLimitations2 }}</p>
              </textarea>
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
                class="block w-full rounded-md bg-gray-200 px-3 py-2 text-base text-blue-800 shadow-sm/30 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600"
              >
                <p>You typed: {{ claimDenial2 }}</p>
              </textarea>
            </div>
          </div>
          <div class="col-span-full flex justify-center gap-4">
            <button
              class="border-blue rounded-full border bg-white px-10 py-2 font-bold text-blue-800 transition hover:bg-gray-100"
            >
              Cancel
            </button>
            <button
              class="ml-10 rounded-full bg-blue-800 px-10 py-2 font-bold text-white transition hover:bg-blue-700"
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
  import { ref } from "vue";

  const eligibilityCriteria =
    ref(`- Conditions under which a claim is considered valid.
- Timeframe in which a claim must be filled after the incident or purchase.
- Required documentation (e.g., receipts, proof of damage, photos, police reports).`);

  const approvalLimitations1 = ref(`- Criteria for approval or rejection.
- Forms of compensation(e.g., payment, replacement, repair).
- Settlement process (e.g., bank transfer, in-store credit`);

  const claimDenial1 =
    ref(`- Grounds for denial (e.g., lack of documentation, excluded events).
- Right to appeal or request re-evaluation.
- Rejection communication process.`);

  const approvalLimitations2 = ref(`- Steps to contest a denied claim.
- Timeframe for appeals and final decisions.`);

  const claimDenial2 = ref(`- Scenarios not covered by the policy.
- Specific exceptions (e.g., acts of war, intentional damage, expired warranties).`);
</script>
