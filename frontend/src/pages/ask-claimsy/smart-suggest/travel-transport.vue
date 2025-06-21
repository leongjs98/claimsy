<template>
  <div class="mx-auto my-8 w-full max-w-6xl bg-gray-100">
    <Tab :tabs="[
      {
        link: '/ask-claimsy',
        routeName: 'Chat with Claimsy',
      },
      {
        link: '/ask-claimsy/smart-suggest/',
        routeName: 'Smart Suggest',
      },
    ]" />
    <div
      class="relative col-span-4 transform overflow-hidden rounded-xl bg-white text-left shadow-xl transition-all sm:w-full sm:min-w-lg md:min-w-xl">
      <div class="shadow-sm relative text-xl bg-blue-50 py-5 text-center font-semibold text-theme-300">
        <button @click="router.back()" type="button" class="absolute left-4">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 24 24" fill="currentColor">
            <path
              d="M19 11H7.14l3.63-4.36a1 1 0 1 0-1.54-1.28l-5 6a1 1 0 0 0-.09.15c0 .05 0 .08-.07.13A1 1 0 0 0 4 12a1 1 0 0 0 .07.36c0 .05 0 .08.07.13a1 1 0 0 0 .09.15l5 6A1 1 0 0 0 10 19a1 1 0 0 0 .64-.23a1 1 0 0 0 .13-1.41L7.14 13H19a1 1 0 0 0 0-2" />
          </svg>
        </button>
        <h1>
          Travel & Transportation
        </h1>
      </div>
      <div class="flex flex-col items-center justify-between px-4 sm:px-6">
        <div class="w-full space-y-6 h-[40rem] overflow-y-auto mt-8 py-6 px-4 rounded-xl inset-shadow-sm inset-shadow-indigo-500/20">
          <div v-for="(convo, index) in conversation" :key="`convo-${index}`" class="flex"
            :class="convo.isSenderUser ? 'justify-end' : ''">
            <p class="w-fit max-w-lg rounded-lg p-3" :class="convo.isSenderUser ? 'bg-blue-100' : 'bg-theme-200 text-white'
              ">
              {{ convo.text }}
            </p>
          </div>
        </div>
        <form @submit.prevent="" class="w-full grid grid-cols-1 py-8">
          <label for="chat-input" class="hidden"> Chat Input </label>
          <input type="text" id="chat-input" name="chatInput"
            class="col-start-1 row-start-1 w-full appearance-none rounded-md bg-gray-200 py-2 pr-9 pl-4 text-base text-theme-300 outline-1 -outline-offset-1 outline-gray-300 focus:outline-2 focus:-outline-offset-2 focus:outline-theme-200 sm:text-sm/6" />
          <button type="button"
            class="col-start-1 row-start-1 mr-2 size-7 self-center justify-self-end text-theme-300 transition hover:text-theme-200 sm:size-6">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
              <path fill="currentColor" fill-opacity="0" stroke="currentColor" stroke-dasharray="40"
                stroke-dashoffset="40" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M8 6l10 6l-10 6Z">
                <animate fill="freeze" attributeName="fill-opacity" begin="0.5s" dur="0.5s" values="0;1" />
                <animate fill="freeze" attributeName="stroke-dashoffset" dur="0.5s" values="40;0" />
              </path>
            </svg>
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const isOpen = ref(false);
let conversation = ref([
  {
    isSenderUser: false,
    text: "Hi! I'm here to help plan your business travel. What are your departure and destination cities or airports?",
  },
  {
    isSenderUser: true,
    text: "I need to fly from New York JFK to London Heathrow.",
  },
  {
    isSenderUser: false,
    text: "Perfect! What are your preferred travel dates and times?",
  },
  {
    isSenderUser: true,
    text: "I need to leave March 15th, preferably evening, and return March 18th.",
  },
  {
    isSenderUser: false,
    text: "Got it. What's the purpose of your trip?",
  },
  {
    isSenderUser: true,
    text: "Client meetings and a product demo on March 16th.",
  },
  {
    isSenderUser: false,
    text: "Important meetings! Do you need to arrive by a specific time for your business commitments?",
  },
  {
    isSenderUser: true,
    text: "Client meetings and a product demo on March 16th.",
  },
  {
    isSenderUser: false,
    text: "Important meetings! Do you need to arrive by a specific time for your business commitments?",
  },
  {
    isSenderUser: true,
    text: "Yes, my first meeting is March 16th at 10 AM, so I need to be there the night before."
  },
  {
    isSenderUser: false,
    text: "Understood. What's your budget range or spending authority for this trip?"
  },
  {
    isSenderUser: true,
    text: "Company budget is $4,000 total for flights and hotel."
  },
  {
    isSenderUser: false,
    text: "Thanks! Are there any company travel policies I should consider?"
  },
  {
    isSenderUser: true,
    text: "We have to book through approved vendors and stay at 4-star hotels minimum."
  },
  {
    isSenderUser: false,
    text: "Noted. Do you have any airline or hotel loyalty programs or preferred vendors?"
  },
  {
    isSenderUser: true,
    text: "I'm Gold status with British Airways and prefer Marriott hotels."
  },
  {
    isSenderUser: false,
    text: "Excellent! How flexible are your dates if I find better rates or options?"
  },
  {
    isSenderUser: true,
    text: "Departure date is fixed, but I could return March 17th or 19th if there's significant savings."
  },
  {
    isSenderUser: false,
    text: "Will you need hotel accommodations, and any preferred location?"
  },
  {
    isSenderUser: true,
    text: "Yes, somewhere in Central London, close to the financial district."
  },
  {
    isSenderUser: false,
    text: "Last question - will you need rental car or other ground transportation?"
  },
  {
    isSenderUser: true,
    text: "No car needed, just airport transfers and taxis for meetings."
  },
  {
    isSenderUser: false,
    text: "Perfect! I have everything I need. Let me find you the best options with BA flights and a Marriott in Central London within your budget."
  }
]);
</script>
