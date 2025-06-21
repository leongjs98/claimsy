<template>
  <div class="mx-auto my-32 w-full max-w-6xl bg-gray-100 text-center">
    <svg
      class="mx-auto size-12 text-gray-400"
      xmlns="http://www.w3.org/2000/svg"
      width="32"
      height="32"
      viewBox="0 0 24 24"
    >
      <!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE -->
      <g
        fill="none"
        stroke="currentColor"
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="2"
      >
        <rect width="20" height="8" x="2" y="6" rx="1" />
        <path
          d="M17 14v7M7 14v7M17 3v3M7 3v3m3 8L2.3 6.3M14 6l7.7 7.7M8 6l8 8"
        />
      </g>
    </svg>
    <h3 class="mt-2 text-sm font-semibold text-gray-900">Under Construction</h3>
    <p class="mt-1 text-sm text-gray-500">Empty Page</p>
    <div class="mt-6">
      <button
        @click="router.back()"
        type="button"
        class="inline-flex items-center gap-2 rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
      >
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
        Go Back
      </button>
    </div>
  </div>
</template>

<script setup>
  import { useRouter } from "vue-router";

  const router = useRouter();
</script>
