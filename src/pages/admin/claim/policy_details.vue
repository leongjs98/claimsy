<template>
    <form>
        <div class=" h-[65rem] bg-white mx-auto mt-15 max-w-4xl rounded-2xl border border-gray-200 px-15 py-10 shadow-lg">
            <div class="space-y-1 border-b border-gray-900/10 pb-12">
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
                    <h1 class="flex justify-center text-4xl font-semibold text-blue-950"> Policy Details</h1>
                </div>
                <div class="grid grid-cols-6">
                    <label for="about" class="block text-sm/6  mt-6 font-medium text-blue-800 sm:col-span-full">Claim Eligibility Criteria</label> 
                    <div class="mt-2 sm:col-span-full  bg-gray-200">
                        <textarea v-model="Description" id="eligibility" rows="8" class="block w-full rounded-md font-semibold px-3 py-1.5 text-base text-blue-800 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6 shadow-xl/30">
                        <p>You typed: {{ Description }}</p>
                    </textarea>
                    </div>   
                </div>
                <div class="mt-8 grid grid-cols-6 gap-8">
                    <div class="col-span-3 row-span-1 text-blue-800">Claim Approval & Limitations <p>
                    <textarea v-model="BulletText" name="one" id="one" rows="8" class="block w-full font-semibold rounded-md bg-gray-200 px-3 py-1.5 text-base text-blue-800 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6 shadow-xl/30">
                        <p>You typed: {{ BulletText }}</p>
                    </textarea>
                    </p></div>
                    <div class="col-span-3 row-span-1 text-blue-800">Claim Denial <p>
                    <textarea v-model="bulletText" name="two" id="two" rows="8" class="block w-full font-semibold rounded-md bg-gray-200 px-3 py-1.5 text-base text-blue-800 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6 shadow-xl/30">
                        <p>You typed: {{ bulletText }}</p>
                    </textarea>

                    </p></div>
                    <div class="col-span-3 row-span-1 text-blue-800">Claim Approval & Limitations<p>
                    <textarea v-model="bullettext" name="three" id="three" rows="8" class="block w-full font-semibold rounded-md bg-gray-200 px-3 py-1.5 text-base text-blue-800 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6 shadow-xl/30">
                        <p>You typed: {{ bullettext }}</p>
                    </textarea>
                    </p></div>
                    <div class="col-span-3 row-span-1 text-blue-800">Claim Denial<p>
                    <textarea v-model="Bullettext" name="two" id="two" rows="8" class="block w-full font-semibold rounded-md bg-gray-200 px-3 py-1.5 text-base text-blue-800 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6 shadow-xl/30">
                        <p>You typed: {{ Bullettext }}</p>
                    </textarea>
                    </p></div>
                      <div class="col-span-full flex justify-center gap-4">
                    <button class="bg-white hover:bg-gray-100 text-blue-800 border border-blue font-bold py-2 px-10 rounded-full">Cancel</button>
                    <button class="bg-blue-800 hover:bg-blue-700 text-white font-bold py-2 px-10 ml-10 rounded-full">Submit</button>
                </div>
                </div>
                </div>
            </div>
    </form>  
</template>

<script>
import TextInput from '@/components/form/TextInput.vue';
export default {
    data() {
        return {
            Description: `-Conditions under which a claim is considered valid. \n-Timeframe in which a claim must be filled after the incident or purchase. \n-Required documentation (e.g., receipts, proof of damage, photos, police reports).`,
            BulletText: `-Criteria for apporoval or rejection.\n-Forms of compensation(e.g., payment, replacement, repair).\n-Settlement process (e.g., bank transfer, in-store credit\n`,
            bulletText: `-Grounds for denial (e.g., lack of documentation, excluded events).\n-Right to appeal or request re-evaluation.\n-Rejection communication process.`,
            bullettext: `-Steps to contest a denied claim.\n-Timeframe for appeals and final decisions.`,
            Bullettext: `-Scenarios not covered by the policy.\n-Specific exceptions (e.g., acts of war, intentional damage, expired warranties).`,
        };

    },
};

</script>