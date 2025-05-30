<template>
  <div class="sm:col-span-full">
    <label :for="id" class="block text-sm font-medium text-blue-900">
      {{ label }}
    </label>
    <div class="mt-2">
      <input
        :type="type"
        :name="name"
        :id="id"
        :autocomplete="autocomplete"
        :placeholder="placeholder"
        class="block w-full rounded-md bg-gray-200 px-3 py-1.5 text-base text-blue-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm"
      />
    </div>
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
  },
};
</script>
