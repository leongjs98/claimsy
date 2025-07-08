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
      class="divide-y divide-gray-200 overflow-hidden rounded-lg bg-gray-200 shadow-sm sm:grid sm:grid-cols-2 sm:gap-px sm:divide-y-0"
    >
      <div
        class="group relative rounded-tl-lg rounded-tr-lg bg-white p-6 focus-within:ring-2 focus-within:ring-indigo-500 focus-within:ring-inset sm:rounded-tr-none"
      >
        <div>
          <span
            class="inline-flex rounded-lg bg-sky-50 p-3 text-sky-700 ring-4 ring-white"
          >
            <!-- <svg class="size-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true" data-slot="icon"> -->
            <!--   <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" /> -->
            <!-- </svg> -->
            <svg
              class="size-6"
              xmlns="http://www.w3.org/2000/svg"
              width="32"
              height="32"
              viewBox="0 0 24 24"
            >
              <!-- Icon from Stash Icons by Pingback LLC - https://github.com/stash-ui/icons/blob/master/LICENSE -->
              <path
                fill="currentColor"
                fill-rule="evenodd"
                d="M20.633 2.276c.224.035.51.125.738.353c.229.229.318.514.353.738c.037.23.03.473.005.7c-.052.458-.195.976-.376 1.474c-.354.972-.93 2.07-1.506 2.646l-.015.015l-1.688 1.595l2.02 5.334a1.8 1.8 0 0 1-.354 1.93l-1.397 1.48a.757.757 0 0 1-1.16-.083l-3.303-4.696l-.912.863c-.52.519-1.028.995-1.522 1.354c-.224.163-.46.313-.707.433l.844 2.138c.26.66.07 1.393-.396 1.886l-1.022 1.08a.757.757 0 0 1-1.13-.047l-2.922-3.652l-3.651-2.922a.757.757 0 0 1-.047-1.13l1.08-1.021c.492-.466 1.226-.658 1.885-.397l2.139.845c.12-.248.27-.484.432-.708c.359-.494.835-1.002 1.355-1.522l.862-.912l-4.696-3.304a.757.757 0 0 1-.083-1.159l1.48-1.397a1.8 1.8 0 0 1 1.93-.353l5.334 2.019l1.595-1.688l.015-.015C16.39 3.576 17.487 3 18.46 2.647c.498-.181 1.016-.324 1.474-.376c.227-.025.47-.032.7.005M16.88 5.207l-1.93 2.042a.75.75 0 0 1-.811.187L8.325 5.235l-.03-.012a.3.3 0 0 0-.326.057l-.813.768l4.654 3.274c.368.26.423.801.113 1.129L10.458 12l-.014.014c-.513.513-.922.954-1.21 1.35c-.291.403-.406.688-.425.891a.757.757 0 0 1-1.022.627l-2.888-1.141c-.262-.104-.6.371-.757.52l3.043 2.436a1 1 0 0 1 .118.117l2.435 3.043c.149-.157.624-.495.52-.757l-1.14-2.887a.757.757 0 0 1 .626-1.023c.203-.019.488-.134.89-.426c.397-.287.838-.696 1.35-1.209l.016-.014l1.55-1.465a.758.758 0 0 1 1.128.113l3.274 4.654l.768-.813a.3.3 0 0 0 .058-.325l-.013-.03l-2.2-5.815a.75.75 0 0 1 .186-.81l2.042-1.931c.347-.351.826-1.2 1.15-2.092c.148-.405.292-.842.306-1.277c-.435.014-.872.158-1.277.306c-.891.324-1.74.803-2.092 1.15"
                clip-rule="evenodd"
              />
            </svg>
          </span>
        </div>
        <div class="mt-8">
          <h3 class="text-base font-semibold text-gray-900">
            <RouterLink
              to="/ask-claimsy/smart-suggest/travel-transport"
              class="focus:outline-hidden"
            >
              <!-- Extend touch target to entire panel -->
              <span class="absolute inset-0" aria-hidden="true"></span>
              Travel & Transport
            </RouterLink>
          </h3>
          <p class="mt-2 text-sm text-gray-500">
            Book flights, hotels, and transport for your business trip
          </p>
        </div>
        <span
          class="pointer-events-none absolute top-6 right-6 text-gray-300 group-hover:text-theme-300"
          aria-hidden="true"
        >
          <svg class="size-6" fill="currentColor" viewBox="0 0 24 24">
            <path
              d="M20 4h1a1 1 0 00-1-1v1zm-1 12a1 1 0 102 0h-2zM8 3a1 1 0 000 2V3zM3.293 19.293a1 1 0 101.414 1.414l-1.414-1.414zM19 4v12h2V4h-2zm1-1H8v2h12V3zm-.707.293l-16 16 1.414 1.414 16-16-1.414-1.414z"
            />
          </svg>
        </span>
      </div>
      <div
        class="group relative bg-white p-6 focus-within:ring-2 focus-within:ring-indigo-500 focus-within:ring-inset sm:rounded-tr-lg"
      >
        <div>
          <span
            class="inline-flex rounded-lg bg-yellow-50 p-3 text-yellow-700 ring-4 ring-white"
          >
            <svg
              class="size-6"
              xmlns="http://www.w3.org/2000/svg"
              width="32"
              height="32"
              viewBox="0 0 24 24"
            >
              <!-- Icon from Fluent UI System Icons by Microsoft Corporation - https://github.com/microsoft/fluentui-system-icons/blob/main/LICENSE -->
              <path
                fill="currentColor"
                d="M3.193 3.726A1.89 1.89 0 0 1 5.085 2c.45 0 .866.156 1.193.417A2 2 0 0 1 7.5 2c.46 0 .884.155 1.222.417A1.9 1.9 0 0 1 9.915 2c.976 0 1.807.737 1.892 1.726c.084.975.193 2.483.193 3.774a4.5 4.5 0 0 1-2.176 3.854c-.222.134-.28.3-.274.386c.127 1.934.45 6.952.45 7.757a2.5 2.5 0 0 1-5 0c0-.805.323-5.823.45-7.757c.005-.087-.052-.252-.274-.386A4.5 4.5 0 0 1 3 7.5c0-1.29.109-2.799.193-3.774M9.5 7.25a.75.75 0 0 1-1.5 0V4a.5.5 0 0 0-1 0v3.25a.75.75 0 0 1-1.5 0V3.915a.415.415 0 0 0-.415-.415a.393.393 0 0 0-.398.355C4.604 4.82 4.5 6.275 4.5 7.5c0 1.09.58 2.044 1.452 2.57c.545.33 1.047.96.995 1.768c-.13 1.98-.447 6.918-.447 7.66a1 1 0 1 0 2 0c0-.742-.317-5.68-.447-7.66c-.052-.808.45-1.438.995-1.768A3 3 0 0 0 10.5 7.5c0-1.224-.104-2.68-.187-3.645a.393.393 0 0 0-.398-.355a.415.415 0 0 0-.415.415zm3.5.5A5.75 5.75 0 0 1 18.75 2a.75.75 0 0 1 .75.75v8.5c0 .318.106 1.895.225 3.642l.005.083c.13 1.908.27 3.983.27 4.522a2.5 2.5 0 0 1-5 0c0-.514.128-2.611.252-4.534c.062-.971.125-1.912.172-2.61l.023-.353h-.697A1.75 1.75 0 0 1 13 10.25zm3.998 3.552l-.021.314a798 798 0 0 0-.229 3.444c-.126 1.96-.248 3.986-.248 4.437a1 1 0 1 0 2 0c0-.48-.138-2.526-.272-4.504l-.007-.104C18.108 13.23 18 11.627 18 11.25V3.566a4.25 4.25 0 0 0-3.5 4.184v2.5c0 .138.112.25.25.25h1.5a.75.75 0 0 1 .748.802"
              />
            </svg>
          </span>
        </div>
        <div class="mt-8">
          <h3 class="text-base font-semibold text-gray-900">
            <RouterLink
              to="/ask-claimsy/smart-suggest/meals-entertainment"
              class="focus:outline-hidden"
            >
              <!-- Extend touch target to entire panel -->
              <span class="absolute inset-0" aria-hidden="true"></span>
              Meals & Entertainment
            </RouterLink>
          </h3>
          <p class="mt-2 text-sm text-gray-500">
            Find restaurants, food delivery, and local entertainment
          </p>
        </div>
        <span
          class="pointer-events-none absolute top-6 right-6 text-gray-300 group-hover:text-theme-300"
          aria-hidden="true"
        >
          <svg class="size-6" fill="currentColor" viewBox="0 0 24 24">
            <path
              d="M20 4h1a1 1 0 00-1-1v1zm-1 12a1 1 0 102 0h-2zM8 3a1 1 0 000 2V3zM3.293 19.293a1 1 0 101.414 1.414l-1.414-1.414zM19 4v12h2V4h-2zm1-1H8v2h12V3zm-.707.293l-16 16 1.414 1.414 16-16-1.414-1.414z"
            />
          </svg>
        </span>
      </div>
      <div
        class="group relative bg-white p-6 focus-within:ring-2 focus-within:ring-indigo-500 focus-within:ring-inset sm:rounded-bl-lg"
      >
        <div>
          <span
            class="inline-flex rounded-lg bg-rose-50 p-3 text-rose-700 ring-4 ring-white"
          >
            <svg
              class="size-6"
              xmlns="http://www.w3.org/2000/svg"
              width="32"
              height="32"
              viewBox="0 0 24 24"
            >
              <!-- Icon from Material Symbols by Google - https://github.com/google/material-design-icons/blob/master/LICENSE -->
              <path
                fill="currentColor"
                d="m12 21l-1.45-1.3q-2.525-2.275-4.175-3.925T3.75 12.812T2.388 10.4T2 8.15Q2 5.8 3.575 4.225T7.5 2.65q1.3 0 2.475.55T12 4.75q.85-1 2.025-1.55t2.475-.55q2.35 0 3.925 1.575T22 8.15q0 1.15-.387 2.25t-1.363 2.412t-2.625 2.963T13.45 19.7zm0-2.7q2.4-2.15 3.95-3.687t2.45-2.675t1.25-2.026T20 8.15q0-1.5-1-2.5t-2.5-1q-1.175 0-2.175.662T12.95 7h-1.9q-.375-1.025-1.375-1.687T7.5 4.65q-1.5 0-2.5 1t-1 2.5q0 .875.35 1.763t1.25 2.025t2.45 2.675T12 18.3m0-6.825"
              />
            </svg>
          </span>
        </div>
        <div class="mt-8">
          <h3 class="text-base font-semibold text-gray-900">
            <RouterLink
              to="/ask-claimsy/smart-suggest/health-wellness"
              class="focus:outline-hidden"
            >
              <!-- Extend touch target to entire panel -->
              <span class="absolute inset-0" aria-hidden="true"></span>
              Health & Wellness
            </RouterLink>
          </h3>
          <p class="mt-2 text-sm text-gray-500">
            Access healthcare, fitness, and wellness services
          </p>
        </div>
        <span
          class="pointer-events-none absolute top-6 right-6 text-gray-300 group-hover:text-theme-300"
          aria-hidden="true"
        >
          <svg class="size-6" fill="currentColor" viewBox="0 0 24 24">
            <path
              d="M20 4h1a1 1 0 00-1-1v1zm-1 12a1 1 0 102 0h-2zM8 3a1 1 0 000 2V3zM3.293 19.293a1 1 0 101.414 1.414l-1.414-1.414zM19 4v12h2V4h-2zm1-1H8v2h12V3zm-.707.293l-16 16 1.414 1.414 16-16-1.414-1.414z"
            />
          </svg>
        </span>
      </div>
      <div
        class="group relative rounded-br-lg rounded-bl-lg bg-white p-6 focus-within:ring-2 focus-within:ring-indigo-500 focus-within:ring-inset sm:rounded-bl-none"
      >
        <div>
          <span
            class="inline-flex rounded-lg bg-indigo-50 p-3 text-indigo-700 ring-4 ring-white"
          >
            <svg
              class="size-6"
              xmlns="http://www.w3.org/2000/svg"
              width="32"
              height="32"
              viewBox="0 0 24 24"
            >
              <!-- Icon from Material Symbols by Google - https://github.com/google/material-design-icons/blob/master/LICENSE -->
              <path
                fill="currentColor"
                d="m19.275 19.8l.7-.7L12 11.125q.475-.575.738-1.3T13 8.3q0-1.875-1.313-3.175T8.5 3.825h-.25L11.325 6.9l-4.25 4.225L4 8.05v.275Q4 10.2 5.312 11.5T8.5 12.8q.8 0 1.513-.263T11.3 11.8l7.975 8ZM5.375 3.25q0-.725.775-1.088T8.5 1.8q2.725 0 4.612 1.888T15 8.3q0 .65-.125 1.288T14.5 10.8l6.875 6.875q.575.575.588 1.413T21.4 20.5l-.675.7q-.575.6-1.413.613t-1.437-.588l-6.9-6.9q-.575.25-1.2.363t-1.25.112q-2.725 0-4.612-1.887T2.025 8.3q0-1.6.35-2.363t1.075-.762q.25 0 .463.088t.387.262L7.075 8.3L8.5 6.9L5.725 4.125q-.175-.175-.263-.4t-.087-.475ZM9.2 9Z"
              />
            </svg>
          </span>
        </div>
        <div class="mt-8">
          <h3 class="text-base font-semibold text-gray-900">
            <RouterLink
              to="/ask-claimsy/smart-suggest/supplies_and_equipments"
              class="focus:outline-hidden"
            >
              <!-- Extend touch target to entire panel -->
              <span class="absolute inset-0" aria-hidden="true"></span>
              Supplies & Equipments
            </RouterLink>
          </h3>
          <p class="mt-2 text-sm text-gray-500">
            Handle various business needs like office supplies, professional
            services etc.
          </p>
        </div>
        <span
          class="pointer-events-none absolute top-6 right-6 text-gray-300 group-hover:text-theme-300"
          aria-hidden="true"
        >
          <svg class="size-6" fill="currentColor" viewBox="0 0 24 24">
            <path
              d="M20 4h1a1 1 0 00-1-1v1zm-1 12a1 1 0 102 0h-2zM8 3a1 1 0 000 2V3zM3.293 19.293a1 1 0 101.414 1.414l-1.414-1.414zM19 4v12h2V4h-2zm1-1H8v2h12V3zm-.707.293l-16 16 1.414 1.414 16-16-1.414-1.414z"
            />
          </svg>
        </span>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref } from "vue";
  const isOpen = ref(false);
  let conversation = [
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
