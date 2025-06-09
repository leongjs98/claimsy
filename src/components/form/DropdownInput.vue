<template>
  <label :for="id" class="block text-sm font-medium text-theme-300">
    {{ label }}
  </label>
  <div class="mt-2 grid grid-cols-1">
    <select
      :id="id"
      :name="name"
      :value="modelValue"      
      :disabled="disabled"
      class="col-start-1 row-start-1 w-full appearance-none rounded-md bg-gray-200 py-2 pr-9 pl-4 text-base text-theme-300 outline-1 -outline-offset-1 outline-gray-300 focus:outline-2 focus:-outline-offset-2 focus:outline-theme-200 sm:text-sm/6"
    >
      <option v-for="option in options" :key="option">{{ option }}</option>
    </select>
    <svg
      class="pointer-events-none col-start-1 row-start-1 mr-2 size-5 self-center justify-self-end text-theme-300 sm:size-4"
      viewBox="0 0 16 16"
      fill="currentColor"
      aria-hidden="true"
      data-slot="icon"
    >
      <path
        fill-rule="evenodd"
        d="M4.22 6.22a.75.75 0 0 1 1.06 0L8 8.94l2.72-2.72a.75.75 0 1 1 1.06 1.06l-3.25 3.25a.75.75 0 0 1-1.06 0L4.22 7.28a.75.75 0 0 1 0-1.06Z"
        clip-rule="evenodd"
      />
    </svg>
  </div>
</template>

<script>
  export default {
    name: "TextInput",
    props: {
      label: { type: String, required: true },
      name: { type: String, required: true },
      id: { type: String, required: true },
      options: { type: Array, required: true },
      // autocomplete: {type: String, default: "off"},
      // placeholder: {type: String, default: ""},
      modelValue: { type: [String, Number], default: "" },
      disabled: { type: Boolean, default: false },
    },
  };
</script>
