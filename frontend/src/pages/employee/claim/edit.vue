<template>
  <form>
    <div
      class="mx-auto mt-15 max-w-4xl rounded-2xl border border-gray-200 bg-white px-15 py-10 shadow-lg"
    >
      <div class="space-y-1 border-b border-gray-900/10 pb-12">
        <div class="relative flex items-center justify-center">
          <button @click="router.back()" type="button" class="absolute left-0">
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
          <h1 class="flex justify-center text-4xl font-semibold text-blue-950">
            Receipt Details
          </h1>
        </div>

        <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
          <div class="sm:col-span-3">
            <DropdownInput
              label="Category"
              name="category"
              id="categoryID"
              :options="[
                'Gadget',
                'Travel Expenses',
                'Meals and Entertainment',
                'Accommodation',
                'Communication',
              ]"
              v-model="formData.category"
            />
          </div>

          <div class="sm:col-span-3">
            <CalendarInput
              label="Date"
              type="text"
              name="date"
              id="DateID"
              v-model="formData.date"
            />
          </div>

          <div class="sm:col-span-full">
            <TextInput
              label="Merchant Name"
              name="merchantName"
              id="MerchantnameID"
              autocomplete="name"
              v-model="formData.merchantName"
            />
          </div>
          <div class="sm:col-span-full">
            <TextInput
              label="Merchant Address"
              name="merchantAddress"
              id="MerchanaddressID"
              autocomplete="street-address"
              v-model="formData.merchantAddress"
            />
          </div>
          <div class="sm:col-span-full">
            <TextInput
              label="Remark"
              name="remark"
              id="RemarkID"
              v-model="formData.remark"
            />
          </div>
        </div>
      </div>

      <div
        class="grid grid-cols-1 gap-x-6 gap-y-8 border-b border-gray-900/10 pb-12 sm:grid-cols-6"
      >
        <div class="sm:col-span-full">
          <h2 class="mt-6 text-sm font-medium text-theme-300">
            Items / Services
          </h2>
          <table
            class="col-span-full w-full border-separate border-spacing-y-4"
          >
            <thead class="bg-blue-950 text-white">
              <tr class="">
                <th class="rounded-l-lg px-4 py-2 text-left">Description</th>
                <th class="px-4 py-2 text-right">Quantity</th>
                <th class="rounded-r-lg px-4 py-2 text-right">
                  Unit Price (RM)
                </th>
              </tr>
            </thead>
            <!-- TODO: change the table rows into label + input tags -->
            <!-- TODO: add delete button on the side of each items -->
            <tbody>
              <tr class="bg-gray-200 text-theme-300 shadow-md">
                <td class="rounded-l-lg px-4 py-3">Galaxy Tab S10 Ultra</td>
                <td class="px-4 py-3 text-right">1</td>
                <td class="rounded-r-lg px-4 py-3 text-right">4,299.00</td>
              </tr>
              <tr class="bg-gray-200 text-theme-300 shadow-md">
                <td class="rounded-l-lg px-4 py-3">24" Essential Monitor S3</td>
                <td class="px-4 py-3 text-right">1</td>
                <td class="rounded-r-lg px-4 py-3 text-right">399.00</td>
              </tr>
              <tr class="text-right font-semibold text-theme-300">
                <td></td>
                <td class="rounded-l-lg bg-gray-200 px-4 py-3">Total</td>
                <td class="rounded-r-lg bg-gray-200 px-4 py-3">4,698.00</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="mt-6 flex items-center justify-end gap-x-6">
        <button
          type="button"
          class="rounded-md bg-white px-3.5 py-2.5 text-sm font-semibold text-gray-900 shadow-xs ring-1 ring-gray-300 ring-inset hover:bg-gray-50"
        >
          Cancel
        </button>
        <RouterLink
          to="/employee/claim/all"
          class="rounded-md bg-theme-300 px-3.5 py-2.5 text-sm font-semibold text-white shadow-xs hover:bg-theme-300 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-theme-200"
        >
          Submit
        </RouterLink>
        <!-- <button -->
        <!--   type="button" -->
        <!--   class="rounded-md bg-theme-300 px-3.5 py-2.5 text-sm font-semibold text-white shadow-xs hover:bg-theme-300 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-theme-200" -->
        <!-- > -->
        <!--   Submit -->
        <!-- </button> -->
      </div>
    </div>
  </form>
</template>

<script setup>
  import { useRouter, useRoute } from "vue-router";

  const formData = ref({
    category: "",
    date: "",
    merchantName: "",
    merchantAddress: "",
    remark: "",
  });
  const router = useRouter();
  const route = useRoute();

  onMounted(() => {
    // Check if query parameters exist and populate the form fields
    if (route.query.categoryID) {
      formData.value.category = route.query.categoryID;
    }
    if (route.query.DateID) {
      formData.value.date = route.query.DateID;
    }
    if (route.query.MerchantnameID) {
      formData.value.merchantName = route.query.MerchantnameID;
    }
    if (route.query.MerchanaddressID) {
      formData.value.merchantAddress = route.query.MerchanaddressID;
    }
    if (route.query.RemarkID) {
      formData.value.remark = route.query.RemarkID;
    }
  });
</script>
