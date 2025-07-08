<template>
  <div
    class="fadeInRight fixed inset-x-0 bottom-8 mx-auto flex w-full max-w-6xl justify-end"
  >
    <div
      class="relative z-10"
      aria-labelledby="claimsy-chatbot"
      role="dialog"
      aria-modal="true"
    >
      <Transition name="backdrop">
        <div
          class="fixed inset-0 bg-gray-200/75 transition-opacity"
          aria-hidden="true"
          v-show="isOpen"
          @click="isOpen = false"
        ></div>
      </Transition>
      <Transition name="pane">
        <div
          v-show="isOpen"
          class="absolute right-8 bottom-20 z-20 h-[70vh] transform overflow-hidden rounded-xl bg-white text-left shadow-xl transition-all sm:w-full sm:min-w-lg md:min-w-xl"
        >
          <!-- <h2 class="absolute inset-x-0 h-16 bg-theme-300 py-4 text-center text-xl font-semibold text-white"> -->
          <!--   Claimsy AI -->
          <!-- </h2> -->
          <div
            class="flex h-full flex-col items-center justify-between px-4 pb-5 sm:p-6"
          >
            <div class="h-full w-full space-y-6 overflow-y-auto py-4 pr-2">
              <div
                v-for="(convo, index) in conversation"
                :key="`convo-${index}`"
                class="flex"
                :class="convo.isSenderUser ? 'justify-end' : ''"
              >
                <p
                  class="w-fit max-w-80 rounded-lg p-3"
                  :class="
                    convo.isSenderUser
                      ? 'bg-blue-100'
                      : 'bg-theme-200 text-white'
                  "
                >
                  {{ convo.text }}
                </p>
              </div>
            </div>
            <form action class="grid w-full grid-cols-1">
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
      </Transition>
    </div>
    <button
      @click="isOpen = !isOpen"
      class="z-50 rounded-full bg-theme-300 p-4 shadow-xl/30 shadow-blue-900 transition hover:bg-theme-200 hover:shadow-xl/20 focus:bg-theme-200 focus:shadow-xl/20"
    >
      <img class="w-10" src="/logo.svg" alt="Claimsy Logo" />
    </button>
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
  ];
</script>

<style scoped>
  @keyframes fadeInRight {
    from {
      opacity: 0;
      transform: translate3d(10%, 0, 0);
    }

    to {
      opacity: 1;
      transform: translate3d(0, 0, 0);
    }
  }

  .fadeInRight {
    animation: fadeInRight;
    animation-duration: 2s;
  }
</style>
