<template>
  <div class="mx-auto my-8 w-full max-w-5xl bg-gray-100">
    <Tab
      :tabs="[
        {
          link: '/ask-claimsy',
          routeName: 'Chat with Claimsy',
        },
        {
          link: '/ask-claimsy/smart-suggest/',
          routeName: 'Smart Suggest',
        },
      ]"
    />
    <div
      class="relative col-span-4 transform overflow-hidden rounded-xl bg-white text-left shadow-xl transition-all sm:w-full sm:min-w-lg md:min-w-xl"
    >
      <div
        class="relative bg-blue-50 py-5 text-center text-xl font-semibold text-theme-300 shadow-sm"
      >
        <button @click="router.back()" type="button" class="absolute left-4">
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
      </div>
      <div class="flex flex-col items-center justify-between px-4 sm:px-6">
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
                convo.isSenderUser ? 'bg-blue-100' : 'border-2 bg-blue-50'
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
    </div>
  </div>
</template>

<script setup>
  import { ref } from "vue";
  import { useRouter } from "vue-router";
  import { onMounted } from "vue";
  import MarkdownIt from "markdown-it";

  const md = new MarkdownIt();

  const router = useRouter();
  const isOpen = ref(false);
  const conversation = ref([]);
  const savedConvo = [
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
      text: "Yes, my first meeting is March 16th at 10 AM, so I need to be there the night before.",
    },
    {
      isSenderUser: false,
      text: "Understood. What's your budget range or spending authority for this trip?",
    },
    {
      isSenderUser: true,
      text: "Company budget is $4,000 total for flights and hotel.",
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
      text: "I'm Gold status with British Airways and prefer Marriott hotels.",
    },
    {
      isSenderUser: false,
      text: "Excellent! How flexible are your dates if I find better rates or options?",
    },
    {
      isSenderUser: true,
      text: "Departure date is fixed, but I could return March 17th or 19th if there's significant savings.",
    },
    {
      isSenderUser: false,
      text: "Will you need hotel accommodations, and any preferred location?",
    },
    {
      isSenderUser: true,
      text: "Yes, somewhere in Central London, close to the financial district.",
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
      text: "Perfect! I have everything I need. Let me find you the best options with BA flights and a Marriott in Central London within your budget.",
    },
    {
      isSenderUser: false,
      text: `
## **Travel Options Found**

**AI:** Great news! I've found several excellent options that meet your requirements. Here are my top recommendations:

---

### **✈️ FLIGHT OPTIONS**

**Option 1 (Recommended):**
- **British Airways BA117** - JFK to LHR
- **Departure:** March 15, 9:45 PM → **Arrival:** March 16, 8:20 AM +1
- **Return:** BA112 - March 18, 2:15 PM → 5:45 PM same day
- **Class:** World Traveller Plus (Premium Economy)
- **Price:** RM 7,757 roundtrip ($1,847)
- **Benefits:** Extra legroom, priority boarding, arrives well before your 10 AM meeting

**Option 2 (Budget-friendly):**
- **British Airways BA179** - JFK to LHR
- **Departure:** March 15, 7:50 PM → **Arrival:** March 16, 6:35 AM +1
- **Return:** BA178 - March 17, 8:25 PM → 11:55 PM same day
- **Class:** World Traveller (Economy)
- **Price:** RM 5,414 roundtrip ($1,289)
- **Benefits:** Earlier return saves hotel night, still meets your schedule

---

### **🏨 HOTEL OPTIONS**

**Option 1 (Prime Location):**
- **London Marriott Hotel County Hall**
- **Location:** South Bank, 12 mins to Bank/Financial District
- **Dates:** March 15-18 (3 nights)
- **Room:** Executive King with Thames view
- **Price:** RM 7,938 total (RM 2,646/night) [$1,890 total]
- **Amenities:** Executive lounge, 24hr business center, gym

**Option 2 (Business District):**
- **Marriott London City**
- **Location:** Heart of Financial District
- **Dates:** March 15-18 (3 nights)
- **Room:** Superior King
- **Price:** RM 6,930 total (RM 2,310/night) [$1,650 total]
- **Amenities:** Walking distance to meetings, business facilities

---

### **🚗 GROUND TRANSPORTATION**

**Airport Transfers:**
- **Heathrow Express + Taxi:** £45 each way (~RM 470 total) [$112 total]
- **Private car service:** £85 each way (~RM 890 total) [$212 total]
- **Recommendation:** Heathrow Express (15 mins) + short taxi

---

### **💰 TOTAL PACKAGE COSTS**

**Recommended Package:**
- Flight Option 1: RM 7,757 ($1,847)
- Hotel Option 2: RM 6,930 ($1,650)
- Transfers: RM 470 ($112)
- **Total: RM 15,157** (**$3,609**) (under your RM 16,800 budget!)

**Budget Package:**
- Flight Option 2: RM 5,414 ($1,289)
- Hotel Option 2: RM 6,930 ($1,650)
- Transfers: RM 470 ($112)
- **Total: RM 12,814** (**$3,051**) (saves RM 3,986!)

Which option interests you most? I can book immediately and send confirmations to your email.

    `,
    },
  ];

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
