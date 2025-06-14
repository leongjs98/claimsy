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
      :value="modelValue"
      :disabled="disabled"
      class="block w-full rounded-md bg-gray-200 px-4 py-2 text-base text-theme-300 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-theme-200 sm:text-sm/6"
    />
  </div>
</template>

<script>
  export default {
    name: "TextInput",
    props: {
      label: { type: String, required: true },
      type: { type: String, default: "text" },
      name: { type: String, required: true },
      id: { type: String, trequired: true },
      autocomplete: { type: String, default: "off" },
      placeholder: { type: String, default: "" },
      modelValue: { type: [String, Number], default: "" },
      disabled: { type: Boolean, default: false },
    },
  };
</script>
