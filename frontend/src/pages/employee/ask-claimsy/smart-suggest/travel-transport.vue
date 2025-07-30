<template>
  <div class="mx-auto my-8 w-full max-w-5xl bg-gray-100">
    <div
      class="relative col-span-4 transform overflow-hidden rounded-xl bg-white text-left shadow-sm transition-all sm:w-full sm:min-w-lg md:min-w-xl"
    >
      <div
        class="flex items-center justify-between bg-blue-50 px-4 py-5 text-center text-xl font-semibold text-theme-300 shadow-sm"
      >
        <button @click="router.back()" type="button" class="">
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
        <h1>Travel & Transportation</h1>
        <button @click="showChat = !showChat" class="hover:cursor-pointer">
          <svg
            v-if="showChat"
            class="h-6 w-6"
            xmlns="http://www.w3.org/2000/svg"
            width="32"
            height="32"
            viewBox="0 0 24 24"
          >
            <!-- Icon from Material Symbols by Google - https://github.com/google/material-design-icons/blob/master/LICENSE -->
            <path fill="currentColor" d="m7 14l5-5l5 5z" />
          </svg>
          <svg
            v-else
            class="h-6 w-6"
            xmlns="http://www.w3.org/2000/svg"
            width="32"
            height="32"
            viewBox="0 0 24 24"
          >
            <!-- Icon from Google Material Icons by Material Design Authors - https://github.com/material-icons/material-icons/blob/master/LICENSE -->
            <path fill="currentColor" d="m7 10l5 5l5-5z" />
          </svg>
        </button>
      </div>
      <Transition name="dropdown-smart-suggest">
        <div
          v-show="showChat"
          class="flex flex-col items-center justify-between px-4 sm:px-6"
        >
          <div
            id="chatbox"
            class="mt-8 h-[40rem] w-full space-y-6 overflow-y-auto rounded-xl px-4 py-6 inset-shadow-sm inset-shadow-indigo-500/20"
          >
            <div
              v-for="(convo, index) in conversation"
              :key="`convo-${index}`"
              class="flex"
              :class="convo.isSenderUser ? 'justify-end' : ''"
            >
              <p
                v-html="md.render(convo.text)"
                class="w-fit max-w-lg rounded-lg p-3"
                :class="
                  convo.isSenderUser ? 'bg-blue-100' : 'bg-theme-200 text-white'
                "
              ></p>
            </div>
          </div>
          <form @submit.prevent="" class="grid w-full grid-cols-1 py-8">
            <label for="chat-input" class="hidden"> Chat Input </label>
            <input
              type="text"
              id="chat-input"
              name="chatInput"
              class="col-start-1 row-start-1 w-full appearance-none rounded-md bg-gray-200 py-2 pr-9 pl-4 text-base text-theme-300 outline-1 -outline-offset-1 outline-gray-300 focus:outline-2 focus:-outline-offset-2 focus:outline-theme-200 sm:text-sm/6"
            />
            <button
              type="button"
              class="col-start-1 row-start-1 mr-2 size-7 self-center justify-self-end text-theme-300 transition hover:text-theme-200 sm:size-6"
            >
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                <path
                  fill="currentColor"
                  fill-opacity="0"
                  stroke="currentColor"
                  stroke-dasharray="40"
                  stroke-dashoffset="40"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M8 6l10 6l-10 6Z"
                >
                  <animate
                    fill="freeze"
                    attributeName="fill-opacity"
                    begin="0.5s"
                    dur="0.5s"
                    values="0;1"
                  />
                  <animate
                    fill="freeze"
                    attributeName="stroke-dashoffset"
                    dur="0.5s"
                    values="40;0"
                  />
                </path>
              </svg>
            </button>
          </form>
        </div>
      </Transition>
    </div>

    <div class="mt-8 overflow-hidden bg-white shadow-sm sm:rounded-lg">
      <div
        class="flex items-center justify-between bg-blue-50 px-4 py-6 text-xl font-semibold text-theme-300 sm:px-6"
      >
        <h3 class="text-lg font-semibold text-theme-300">
          Conversation Details
        </h3>
        <button
          @click="showDetails = !showDetails"
          class="hover:cursor-pointer"
        >
          <svg
            v-if="showDetails"
            class="h-6 w-6"
            xmlns="http://www.w3.org/2000/svg"
            width="32"
            height="32"
            viewBox="0 0 24 24"
          >
            <!-- Icon from Material Symbols by Google - https://github.com/google/material-design-icons/blob/master/LICENSE -->
            <path fill="currentColor" d="m7 14l5-5l5 5z" />
          </svg>
          <svg
            v-else
            class="h-6 w-6"
            xmlns="http://www.w3.org/2000/svg"
            width="32"
            height="32"
            viewBox="0 0 24 24"
          >
            <!-- Icon from Google Material Icons by Material Design Authors - https://github.com/material-icons/material-icons/blob/master/LICENSE -->
            <path fill="currentColor" d="m7 10l5 5l5-5z" />
          </svg>
        </button>
      </div>
      <Transition name="dropdown-smart-suggest">
        <div v-show="showDetails" class="border-t border-gray-100">
          <dl class="divide-y divide-gray-100">
            <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-900">Trip Purpose</dt>
              <dd class="mt-1 text-sm/6 text-gray-700 sm:col-span-2 sm:mt-0">
                - Client meetings and product demo August 16th
                <br />
                - First meeting: 10 AM August 16th
              </dd>
            </div>
            <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-900">Departure</dt>
              <dd class="mt-1 text-sm/6 text-gray-700 sm:col-span-2 sm:mt-0">
                - August 15th (evening preferred)
              </dd>
            </div>
            <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-900">Return</dt>
              <dd class="mt-1 text-sm/6 text-gray-700 sm:col-span-2 sm:mt-0">
                - August 18th (flexible: 17th or 19th for savings)
              </dd>
            </div>
            <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-900">Route</dt>
              <dd class="mt-1 text-sm/6 text-gray-700 sm:col-span-2 sm:mt-0">
                - From: New York JFK
                <br />
                - To: London Heathrow
              </dd>
            </div>
            <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-900">Budget</dt>
              <dd class="mt-1 text-sm/6 text-gray-700 sm:col-span-2 sm:mt-0">
                - $4,000 total (flights + hotel)
              </dd>
            </div>
            <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-900">Accommodation</dt>
              <dd class="mt-1 text-sm/6 text-gray-700 sm:col-span-2 sm:mt-0">
                - Central London, financial district
                <br />
                - 4-star minimum
                <br />
                - Marriott preferred
              </dd>
            </div>
            <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-900">Transport</dt>
              <dd class="mt-1 text-sm/6 text-gray-700 sm:col-span-2 sm:mt-0">
                - Airport Transfers
                <br />
                - Taxis for meetings
              </dd>
            </div>
            <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-900">
                Loyalty Programs
              </dt>
              <dd class="mt-1 text-sm/6 text-gray-700 sm:col-span-2 sm:mt-0">
                - British Airways Gold status
                <br />
                - Marriott hotels
              </dd>
            </div>
            <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-900">Travel Policies</dt>
              <dd class="mt-1 text-sm/6 text-gray-700 sm:col-span-2 sm:mt-0">
                - Approved vendors only
                <br />
                - 4-star hotel minimum
              </dd>
            </div>
            <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-900">Flexibility</dt>
              <dd class="mt-1 text-sm/6 text-gray-700 sm:col-span-2 sm:mt-0">
                - Departure date: Fixed
                <br />
                - Return date: Flexible for savings
              </dd>
            </div>
          </dl>
          <hr class="m-4 text-blue-100" />
          <div
            class="flex items-center justify-end gap-4 px-4 py-6 text-xl font-semibold sm:px-6"
          >
            <SecondaryButton>Regenerate</SecondaryButton>
            <PrimaryButton @click="getAnswer">Confirm</PrimaryButton>
          </div>
        </div>
      </Transition>
    </div>

    <p
      v-show="showAnswer"
      v-html="md.render(answer)"
      class="markdown-it mt-8 w-full rounded-lg bg-white px-4 py-6 shadow-sm lg:px-6"
    ></p>
  </div>
</template>

<script setup>
  import { ref } from "vue";
  import { useRouter } from "vue-router";
  import { onMounted } from "vue";
  import MarkdownIt from "markdown-it";

  const md = new MarkdownIt();

  const showChat = ref(true);
  const showDetails = ref(false);
  const showAnswer = ref(false);
  const router = useRouter();
  const isOpen = ref(false);
  const conversation = ref([]);
  const answer = ref(
    `
## **Travel Options Found**

**AI:** Great news! I've found several excellent options that meet your requirements. Here are my top recommendations:

---

### **✈️ FLIGHT OPTIONS**

**Option 1 (Recommended):**
- **Singapore Airlines SQ108** - KUL to SIN
- **Departure:** August 15, 7:30 PM → **Arrival:** August 15, 8:45 PM
- **Return:** SQ103 - August 18, 2:15 PM → 3:30 PM same day
- **Class:** Premium Economy
- **Price:** RM 1,680 roundtrip ($400)
- **Benefits:** Extra legroom, priority boarding, arrives with plenty of time to rest before your 10 AM meeting

**Option 2 (Budget-friendly):**
- **Singapore Airlines SQ106** - KUL to SIN
- **Departure:** August 15, 6:15 PM → **Arrival:** August 15, 7:30 PM
- **Return:** SQ105 - August 17, 8:25 PM → 9:40 PM same day
- **Class:** Economy
- **Price:** RM 980 roundtrip ($233)
- **Benefits:** Earlier return saves hotel night, still meets your schedule

---

### **🏨 HOTEL OPTIONS**

**Option 1 (Prime Location):**
- **The Ritz-Carlton, Millenia Singapore**
- **Location:** Marina Bay, 8 mins to CBD/Financial District
- **Dates:** August 15-18 (3 nights)
- **Room:** Deluxe Marina Bay View
- **Price:** RM 4,200 total (RM 1,400/night) [$1,000 total]
- **Amenities:** Club lounge, 24hr business center, gym, Marina Bay views

**Option 2 (Business District):**
- **JW Marriott Hotel Singapore South Beach**
- **Location:** Heart of CBD/Financial District
- **Dates:** August 15-18 (3 nights)
- **Room:** Premier King
- **Price:** RM 3,360 total (RM 1,120/night) [$800 total]
- **Amenities:** Walking distance to meetings, business facilities, rooftop pool

---

### **🚗 GROUND TRANSPORTATION**

**Airport Transfers:**
- **MRT + Taxi:** S$25 each way (~RM 160 total) [$38 total]
- **Private car service:** S$45 each way (~RM 290 total) [$69 total]
- **Grab/Taxi direct:** S$35 each way (~RM 225 total) [$54 total]
- **Recommendation:** Direct Grab/Taxi (30 mins door-to-door)

---

### **💰 TOTAL PACKAGE COSTS**

**Recommended Package:**
- Flight Option 1: RM 1,680 ($400)
- Hotel Option 1: RM 4,200 ($1,000)
- Transfers: RM 225 ($54)
- **Total: RM 6,105** (**$1,454**) (well under your RM 10,500 budget!)

**Budget Package:**
- Flight Option 2: RM 980 ($233)
- Hotel Option 2: RM 3,360 ($800)
- Transfers: RM 225 ($54)
- **Total: RM 4,565** (**$1,087**) (saves RM 5,935!)

**Premium Package:**
- Flight Option 1: RM 1,680 ($400)
- Hotel Option 1: RM 4,200 ($1,000)
- Private transfers: RM 290 ($69)
- **Total: RM 6,170** (**$1,469**) (still under budget with premium comfort!)

Which option interests you most? I can book immediately and send confirmations to your email.
    `,
  );

  const savedConvo = [
    {
      isSenderUser: false,
      text: "Hi! I'm here to help plan your business travel. What are your departure and destination cities or airports?",
    },
    {
      isSenderUser: true,
      text: "I need to fly from Kuala Lumpur KUL to Singapore Changi SIN.",
    },
    {
      isSenderUser: false,
      text: "Perfect! What are your preferred travel dates and times?",
    },
    {
      isSenderUser: true,
      text: "I need to leave August 15th, preferably evening, and return August 18th.",
    },
    {
      isSenderUser: false,
      text: "Got it. What's the purpose of your trip?",
    },
    {
      isSenderUser: true,
      text: "Client meetings and a product demo on August 16th.",
    },
    {
      isSenderUser: false,
      text: "Important meetings! Do you need to arrive by a specific time for your business commitments?",
    },
    {
      isSenderUser: true,
      text: "Client meetings and a product demo on August 16th.",
    },
    {
      isSenderUser: false,
      text: "Important meetings! Do you need to arrive by a specific time for your business commitments?",
    },
    {
      isSenderUser: true,
      text: "Yes, my first meeting is August 16th at 10 AM, so I need to be there the night before.",
    },
    {
      isSenderUser: false,
      text: "Understood. What's your budget range or spending authority for this trip?",
    },
    {
      isSenderUser: true,
      text: "Company budget is $2,500 total for flights and hotel.",
    },
    {
      isSenderUser: false,
      text: "Thanks! Are there any company travel policies I should consider?",
    },
    {
      isSenderUser: true,
      text: "We have to book through approved vendors and stay at 4-star hotels minimum.",
    },
    {
      isSenderUser: false,
      text: "Noted. Do you have any airline or hotel loyalty programs or preferred vendors?",
    },
    {
      isSenderUser: true,
      text: "I'm Gold status with Singapore Airlines and prefer Marriott hotels.",
    },
    {
      isSenderUser: false,
      text: "Excellent! How flexible are your dates if I find better rates or options?",
    },
    {
      isSenderUser: true,
      text: "Departure date is fixed, but I could return August 17th or 19th if there's significant savings.",
    },
    {
      isSenderUser: false,
      text: "Will you need hotel accommodations, and any preferred location?",
    },
    {
      isSenderUser: true,
      text: "Yes, somewhere in Central Singapore, close to the Marina Bay or CBD area.",
    },
    {
      isSenderUser: false,
      text: "Last question - will you need rental car or other ground transportation?",
    },
    {
      isSenderUser: true,
      text: "No car needed, just airport transfers and taxis for meetings.",
    },
    {
      isSenderUser: false,
      text: "Perfect! I have everything I need. Let me find you the best options with Singapore Airlines flights and a Marriott in Central Singapore within your budget.",
    },
];

  function getAnswer() {
    showAnswer.value = true;
  }

  const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

  const scrollToBottom = () => {
    const chatbox = document.getElementById("chatbox");
    chatbox.scrollTop = chatbox.scrollHeight;
  };

  onMounted(() => {
    savedConvo.forEach((message, index) => {
      setTimeout(
        () => {
          conversation.value.push(message);
          scrollToBottom();
        },
        (index + 1) * 500,
      );
    });
  });
</script>

