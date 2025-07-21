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
        <div class="flex justify-center items-center gap-2">
        <h1>Travel & Transportation</h1>
          <button type="button" class="hover:cursor-pointer" @click="showInfo=true">
            <svg class="size-6" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><!-- Icon from Majesticons by Gerrit Halfmann - https://github.com/halfmage/majesticons/blob/main/LICENSE --><g fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M2 12C2 6.477 6.477 2 12 2s10 4.477 10 10s-4.477 10-10 10S2 17.523 2 12zm10-5a2 2 0 0 0-2 2a1 1 0 0 1-2 0a4 4 0 1 1 5.31 3.78a.674.674 0 0 0-.273.169a.177.177 0 0 0-.037.054v.497a1 1 0 1 1-2 0V13c0-1.152.924-1.856 1.655-2.11A2.001 2.001 0 0 0 12 7zm1 6.007v-.004v.004zM13 17a1 1 0 1 1-2 0a1 1 0 0 1 2 0z" fill="currentColor"/></g></svg>
          </button>
        </div>
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
                - Client meetings and product demo March 16th
                <br />
                - First meeting: 10 AM March 16th
              </dd>
            </div>
            <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-900">Departure</dt>
              <dd class="mt-1 text-sm/6 text-gray-700 sm:col-span-2 sm:mt-0">
                - March 15th (evening preferred)
              </dd>
            </div>
            <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-900">Return</dt>
              <dd class="mt-1 text-sm/6 text-gray-700 sm:col-span-2 sm:mt-0">
                - March 18th (flexible: 17th or 19th for savings)
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

  <InfoDialog v-model="showInfo">
  <template #title>
    Capabilities
  </template>
  <template #default>
      <div class="mt-8 flow-root">
    <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
      <div class="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
        <div class="overflow-hidden shadow-sm ring-1 ring-black/5 sm:rounded-lg">
          <table class="min-w-full divide-y divide-gray-300">
            <thead class="bg-gray-50">
              <tr>
                <th scope="col" class="py-3.5 pr-3 pl-4 text-left text-sm font-semibold text-gray-900 sm:pl-6">Airport Code</th>
                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Airport Name</th>
                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">City and Country</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200 bg-white">
              <tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">PVG</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Pudong International Airport</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Shanghai, China</td>
</tr>

<tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">LAX</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Los Angeles International Airport</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Los Angeles, CA, USA</td>
</tr>

<tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">CDG</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Charles de Gaulle Airport</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Paris, France</td>
</tr>

<tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">SAW</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Sabiha Gökçen Airport</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Istanbul, Turkey</td>
</tr>

<tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">FDF</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Martinique Aimé Césaire Airport</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Fort-de-France, Martinique</td>
</tr>

<tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">PTP</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Le Raizet Airport</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Pointe-à-Pitre, Guadeloupe</td>
</tr>

<tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">XPG</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Gare du Nord Rail Station</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Paris, France</td>
</tr>

<tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">JFK</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">John F. Kennedy International Airport</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">New York, NY, USA</td>
</tr>

<tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">AUH</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Zayed International Airport</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Abu Dhabi, UAE</td>
</tr>

<tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">ORY</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Orly Airport</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Paris, France</td>
</tr>

<tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">SFO</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">San Francisco International Airport</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">San Francisco, CA, USA</td>
</tr>

<tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">EWR</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Newark Liberty International Airport</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Newark, NJ, USA</td>
</tr>

<tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">MIA</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Miami International Airport</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Miami, FL, USA</td>
</tr>

<tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">AMS</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Schiphol Airport</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Amsterdam, Netherlands</td>
</tr>

<tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">BAH</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Bahrain International Airport</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Manama, Bahrain</td>
</tr>

<tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">IST</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Istanbul Airport</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Istanbul, Turkey</td>
</tr>

<tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">BCN</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Josep Tarradellas Barcelona Airport</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Barcelona, Spain</td>
</tr>

<tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">TUN</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Carthage Airport</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Tunis, Tunisia</td>
</tr>

<tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">LIN</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Linate Airport</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Milan, Italy</td>
</tr>

<tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">MAD</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Adolfo Suárez Madrid-Barajas Airport</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Madrid, Spain</td>
</tr>

<tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">YUL</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Pierre Elliott Trudeau International Airport</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Montreal, QC, Canada</td>
</tr>

<tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">QQS</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">St Pancras International Rail Station</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">London, England, UK</td>
</tr>

<tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">FCO</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Fiumicino Airport</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Rome, Italy</td>
</tr>

<tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">LIS</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Lisbon Airport</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Lisbon, Portugal</td>
</tr>

<tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">CPH</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Kastrup Airport</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Copenhagen, Denmark</td>
</tr>

<tr>
<td class="py-4 pr-3 pl-4 text-sm font-medium text-start whitespace-nowrap text-gray-900 sm:pl-6">RAK</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Menara Airport</td>
<td class="px-3 py-4 text-sm text-start whitespace-nowrap text-gray-500">Marrakech, Morocco</td>
</tr>
              </tbody>
          </table>
        </div>
        </div>
        </div>
        </div>
  </template>
  </InfoDialog>

</template>

<script setup>
  import { ref } from "vue";
  import { useRouter } from "vue-router";
  import { onMounted } from "vue";
  import MarkdownIt from "markdown-it";

  const md = new MarkdownIt();

  const showChat = ref(true);
  const showDetails = ref(true);
  const showInfo = ref(false);
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
  );

  const savedConvo = [
    {
      isSenderUser: false,
      text: "Hi! I'm here to help plan your business travel. What are your departure and destination cities or airports?",
    },
    {
      isSenderUser: true,
      text: "I need to fly from Sydney to Bangkok.",
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
      text: "Yes, my first meeting is August 16th at 10 AM, so I need to be there the night before.",
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
      text: "We have to take at least business class for the flights and stay at 4-star hotels minimum.",
    },
    {
      isSenderUser: false,
      text: "Excellent! How flexible are your dates if I find better rates or options?",
    },
    {
      isSenderUser: true,
      text: "Departure date and return are fixed.",
    },
    {
      isSenderUser: false,
      text: "Will you need hotel accommodations, and any preferred location?",
    },
    {
      isSenderUser: true,
      text: "Yes, somewhere near the Central Bangkok.",
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
        (index + 1) * 0,
      );
    });
  });
</script>
