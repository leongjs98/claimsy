<template>
  <label :for="id" class="block text-sm font-medium text-theme-300">
    {{ label }}
  </label>
  <div class="mt-2">
    <input
      :type="type"
      :name="name"
      :id="id"
      :autocomplete="autocomplete"
      :placeholder="placeholder"
      class="block w-full rounded-md bg-gray-200 px-4 py-2 text-base text-theme-300 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-theme-100 focus:outline-2 focus:-outline-offset-2 focus:outline-theme-200 sm:text-sm/6"
    />
    <!-- <svg class="h-4 w-4 text-theme-300" fill="currentColor" viewBox="0 0 20 20"> -->
    <!--   <path -->
    <!--     d="M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z" /> -->
    <!-- </svg> -->
  </div>
</template>

<script>
  export default {
    name: "CalendarInput",
    props: {
      label: { type: String, required: true },
      type: { type: String, default: "text" },
      name: { type: String, required: true },
      id: { type: String, trequired: true },
      autocomplete: { type: String, default: "off" },
      placeholder: { type: String, default: "" },
    },
  };
</script>
