<template>
  <form>
    <div
      class="max-w-4xl mx-auto mt-15 rounded-2xl shadow-lg border border-gray-200 bg-white py-10 px-15"
    >
      <div class="border-b border-gray-900/10 pb-12 space-y-1">
        <h1
          class="text-4xl font-semibold text-blue-950 flex justify-center relative"
        >
          <button @click="goBack" class="absolute left-0 p-4">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="w-6 h-6"
              viewBox="0 0 24 24"
              fill="currentColor"
            >
              <path
                d="M19 11H7.14l3.63-4.36a1 1 0 1 0-1.54-1.28l-5 6a1 1 0 0 0-.09.15c0 .05 0 .08-.07.13A1 1 0 0 0 4 12a1 1 0 0 0 .07.36c0 .05 0 .08.07.13a1 1 0 0 0 .09.15l5 6A1 1 0 0 0 10 19a1 1 0 0 0 .64-.23a1 1 0 0 0 .13-1.41L7.14 13H19a1 1 0 0 0 0-2"
              />
            </svg>
          </button>
          Receipt Details
        </h1>

        <div class="grid grid-cols-2 gap-10 mt-10">
          <div>
            <label
              for="category"
              class="block text-sm font-medium text-blue-900"
              >Category</label
            >
            <select
              id="category"
              name="category"
              class="w-full rounded-md bg-gray-200 mt-2 py-1.5 px-1.5 text-blue-900 text-sm focus:outline-indigo-600"
            >
              <option>Gadgets</option>
              <option>Travel Expenses</option>
              <option>Accommodation</option>
              <option>Meals and Entertainment</option>
              <option>Communication</option>
            </select>
          </div>

          <div>
            <label for="date" class="block text-sm font-medium text-blue-900"
              >Date</label
            >
            <div class="relative">
              <div
                class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none"
              >
                <svg
                  class="w-4 h-4 text-blue-900"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                >
                  <path
                    d="M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z"
                  />
                </svg>
              </div>
              <input
                id="date"
                type="text"
                placeholder="Select date"
                class="pl-10 w-full bg-gray-200 border border-blue-900 text-blue-900 text-sm rounded-lg p-2.5"
              />
            </div>
          </div>
        </div>

        <div class="mt-10 space-y-4">
          <TextInput
            label="Merchant Name"
            name="merchantName"
            id="merchant-name"
            autocomplete="name"
          />
          <TextInput
            label="Merchant Address"
            name="merchantAddress"
            id="merchant-address"
            autocomplete="street-address"
          />
          <TextInput label="Item(s) / Service(s)" name="items" id="items" />
        </div>
      </div>

      <div class="border-b border-gray-900/10 pb-12 mt-8">
        <h2 class="text-base text-blue-900">Remark</h2>
        <input
          type="text"
          name="remark"
          id="remark"
          placeholder="Optional remarks..."
          class="mt-2 block w-full rounded-md bg-gray-200 px-3 py-1.5 text-base text-blue-900 outline-1 outline-gray-300 focus:outline-indigo-600"
        />

        <h2 class="text-base text-blue-900 mt-6">Attachment</h2>
        <table class="w-full mt-4 border-separate border-spacing-y-4">
          <thead class="bg-blue-950 text-white rounded-xl">
            <tr>
              <th class="rounded-l-lg px-4 py-2 text-left">Description</th>
              <th class="px-4 py-2 text-right">Quantity</th>
              <th class="rounded-r-lg px-4 py-2 text-right">Unit Price (RM)</th>
            </tr>
          </thead>
          <tbody>
            <tr class="bg-gray-200 text-blue-900 shadow-md">
              <td class="rounded-l-lg px-4 py-3">Galaxy Tab S10 Ultra</td>
              <td class="text-right px-4 py-3">1</td>
              <td class="text-right rounded-r-lg px-4 py-3">4,299.00</td>
            </tr>
            <tr class="bg-gray-200 text-blue-900 shadow-md">
              <td class="rounded-l-lg px-4 py-3">24" Essential Monitor S3</td>
              <td class="text-right px-4 py-3">1</td>
              <td class="text-right rounded-r-lg px-4 py-3">399.00</td>
            </tr>
            <tr>
              <td class="rounded-l-lg px-4 py-3"></td>
              <td
                class="bg-gray-200 font-semibold text-blue-900 rounded-l-lg text-right px-4 py-3"
              >
                Total
              </td>
              <td
                class="bg-gray-200 font-semibold text-blue-900 text-right rounded-l-lgtext-right rounded-r-lg px-4 py-3"
              >
                4,698.00
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="mt-6 flex items-center justify-end gap-x-6">
        <button type="button" class="text-sm font-semibold text-gray-900">
          Cancel
        </button>
        <button
          type="submit"
          class="rounded-md bg-blue-950 px-3 py-2 text-sm font-semibold text-white hover:bg-indigo-500"
        >
          Submit
        </button>
      </div>
    </div>
  </form>
</template>

<script>
import TextInput from "@/components/TextInput.vue";

export default {
  components: {
    TextInput,
  },
  methods: {
    goBack() {
      this.$router.go(-1);
    },
  },
};
</script>
