<template>
  <div class="mx-auto my-14 w-full max-w-6xl bg-gray-100">
    <Tab
      :tabs="[
        {
          link: '/ask-claimsy',
          routeName: 'Chat with Claimsy',
        },
        {
          link: '/ask-claimsy/smart-suggest',
          routeName: 'Smart Suggest',
        },
      ]"
    />
    <div
      class="mx-auto mt-15 grid h-[55rem] max-w-5xl grid-cols-6 gap-4 rounded-2xl border border-gray-200 bg-white px-15 py-10 pb-12 shadow-lg"
    >
      <div
        class="col-span-2 h-full transform rounded-xl bg-white p-4 shadow-xl transition-all"
      >
        <button
          type="button"
          class="w-full rounded-xl border border-theme-300 px-4 py-2.5 text-sm font-semibold text-theme-300 shadow-xs transition hover:cursor-pointer hover:bg-theme-200 hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-theme-300"
        >
          New Chat
        </button>
        <ul class="mt-8 space-y-4 divide-y divide-gray-200">
          <li v-for="(chat, index) in chatHistory" class="py-4">
            <button
              class="transition-300 text-left transition hover:cursor-pointer hover:text-theme-200"
              :class="index == 1 ? 'font-semibold text-theme-300' : ''"
            >
              {{ chat }}
            </button>
          </li>
        </ul>
      </div>
      <div
        class="relative col-span-4 grid transform grid-rows-12 overflow-hidden rounded-xl bg-white text-left shadow-xl transition-all sm:w-full sm:min-w-lg md:min-w-xl"
      >
        <div
          class="row-span-1 bg-theme-300 py-5 text-center font-semibold text-white"
        >
          {{ chatHistory[1] }}
        </div>
        <div
          class="row-span-10 flex flex-col items-center justify-between px-4 sm:px-6"
        >
          <div class="w-full space-y-6 overflow-y-auto pt-8 pr-2 pb-4">
            <div
              v-for="(convo, index) in conversation"
              :key="`convo-${index}`"
              class="flex"
              :class="convo.isSenderUser ? 'justify-end' : ''"
            >
              <p
                class="w-fit max-w-lg rounded-lg p-3"
                :class="
                  convo.isSenderUser ? 'bg-blue-100' : 'bg-theme-200 text-white'
                "
              >
                {{ convo.text }}
              </p>
            </div>
          </div>
          <form
            action
            class="absolute right-5 bottom-5 left-5 grid grid-cols-1"
          >
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
  </div>
</template>

<script setup>
  import { ref } from "vue";
  const isOpen = ref(false);
  let conversation = [
    {
      isSenderUser: true,
      text: "Is Grab ride claimable?",
    },
    {
      isSenderUser: false,
      text: "Generally, yes, Grab rides can be claimed as business expenses, but it depends on your specific circumstances and your company's policies. Are you claiming this for business purposes?",
    },
    {
      isSenderUser: true,
      text: "Yes, it was for a client meeting.",
    },
    {
      isSenderUser: false,
      text: "Okay. In that case, it's likely claimable. You'll typically need to provide documentation like the Grab ride receipt showing the date, time, origin, destination, and cost. Check with your company's finance department or expense policy for specific requirements.",
    },
    {
      isSenderUser: true,
      text: "Great, thanks!",
    },
    {
      isSenderUser: false,
      text: "You're welcome! Is there anything else I can help you with regarding expense claims?",
    },
    {
      isSenderUser: true,
      text: "Great, thanks!",
    },
    {
      isSenderUser: false,
      text: "You're welcome! Is there anything else I can help you with regarding expense claims?",
    },
  ];

  let chatHistory = [
    "WFH Setup Claims: What's Covered and What’s Not",
    "Transportation Claims: Rules, Limits, and Exceptions",
    "Gray Area Claims: What Happens When It’s Not So Clear",
    "How do i claim travel days vs work days?",
    "WiFi subsidy still active?",
    "Submitted wrong amount—can i edit a claim?",
  ];
</script>
