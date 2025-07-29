<template>
  <form @submit.prevent="submitInvoice">
    <li
      v-for="(formData, i) in formDatas"
      key="i"
      class="mx-auto mt-15 max-w-4xl rounded-2xl border border-gray-200 bg-white px-15 py-10 shadow-lg"
      :class="i <= formDatas.length - 1 ? 'mb-8' : ''"
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
            <!-- Make sure category matches with categories in /backend/db/values.py -->
            <DropdownInput
              label="Category"
              name="category"
              id="categoryID"
              :options="[
                'Supplies and Equipment',
                'Travel Expenses',
                'Medical Expenses',
                'Meals and Entertaiment',
                'Accommodation',
              ]"
              v-model="formData.category"
            />
          </div>

          <div class="sm:col-span-3">
            <CalendarInput
              label="Date (YYYY-MM-DD)"
              name="date"
              id="date"
              v-model="formData.date"
            />
          </div>

          <div class="sm:col-span-full">
            <TextInput
              label="Merchant Name"
              name="merchantName"
              id="MerchantnameID"
              autocomplete="name"
              v-model="formData.merchant_name"
            />
          </div>
          <div class="sm:col-span-full">
            <TextInput
              label="Merchant Address"
              name="merchantAddress"
              id="MerchanaddressID"
              autocomplete="street-address"
              v-model="formData.merchant_address"
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
                <th class="rounded-r-lg px-4 py-2 text-right">
                  Subtotal (RM)
                </th>
              </tr>
            </thead>
            <!-- TODO: change the table rows into label + input tags -->
            <!-- TODO: add delete button on the side of each items -->
            <tbody>
              <tr
                v-for="(item, j) in formData.items"
                :key="j"
                class="bg-gray-200 text-theme-300 shadow-md"
              >
                <td class="rounded-l-lg px-4 py-3">{{ item.description }}</td>
                <td class="px-4 py-3 text-right">{{ item.quantity }}</td>
                <td class="rounded-r-lg px-4 py-3 text-right">
                  {{ formatCurrency(item.unit_price) }}
                </td>
                <td class="rounded-r-lg px-4 py-3 text-right">
                  {{ formatCurrency(item.quantity*item.unit_price) }}
                </td>
              </tr>
              <tr class="text-right font-semibold text-theme-300">
                <td></td>
                <td></td>
                <td class="rounded-l-lg bg-gray-200 px-4 py-3">Total</td>
                <td class="rounded-r-lg bg-gray-200 px-4 py-3">
                  {{ totalAmount(formData.items) }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="mt-6 flex items-center justify-end gap-x-6">
        <SecondaryButton> Cancel </SecondaryButton>
        <span class="flex items-center justify-center gap-2">
          <PrimaryButton @click="submitInvoice($event, i)">
            <span v-if="isSubmitting"> Processing... </span>
            <span v-else> Upload </span>
          </PrimaryButton>
          <svg
            v-if="isSubmitting"
            class="size-5 animate-spin"
            xmlns="http://www.w3.org/2000/svg"
            width="32"
            height="32"
            viewBox="0 0 24 24"
          >
            <g fill="none" fill-rule="evenodd">
              <path
                d="m12.593 23.258l-.011.002l-.071.035l-.02.004l-.014-.004l-.071-.035q-.016-.005-.024.005l-.004.01l-.017.428l.005.02l.01.013l.104.074l.015.004l.012-.004l.104-.074l.012-.016l.004-.017l-.017-.427q-.004-.016-.017-.018m.265-.113l-.013.002l-.185.093l-.01.01l-.003.011l.018.43l.005.012l.008.007l.201.093q.019.005.029-.008l.004-.014l-.034-.614q-.005-.018-.02-.022m-.715.002a.02.02 0 0 0-.027.006l-.006.014l-.034.614q.001.018.017.024l.015-.002l.201-.093l.01-.008l.004-.011l.017-.43l-.003-.012l-.01-.01z"
              />
              <path
                fill="currentColor"
                d="M12 4.5a7.5 7.5 0 1 0 0 15a7.5 7.5 0 0 0 0-15M1.5 12C1.5 6.201 6.201 1.5 12 1.5S22.5 6.201 22.5 12S17.799 22.5 12 22.5S1.5 17.799 1.5 12"
                opacity=".1"
              />
              <path
                fill="currentColor"
                d="M12 4.5a7.46 7.46 0 0 0-5.187 2.083a1.5 1.5 0 0 1-2.075-2.166A10.46 10.46 0 0 1 12 1.5a1.5 1.5 0 0 1 0 3"
              />
            </g>
          </svg>
        </span>
      </div>
    </li>

  </form>
  <SuccessDialog v-model="showSuccessDialog">
    <template #header> Invoice Uploaded </template>
    <template #default>
      <p>This invoice has been uploaded as {{ invoiceNumber }}.</p>
      <p>Remember to submit it as a claim!</p>
    </template>
    <template #button>
        <button
          type="button"
          @click="showSuccessDialog = false; removeFormData()"
          class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
        >
          OK
        </button>
    </template>
  </SuccessDialog>
</template>

<script setup>
  import { useRouter, useRoute } from "vue-router";
  import { computed, ref, onMounted } from "vue";
  import axios from "axios";

  const totalAmount = (items) => {
  return items
    .reduce((sum, item) => sum + item.unit_price * item.quantity, 0)
    .toFixed(2);
};

  const router = useRouter();
  const route = useRoute();
  const isSubmitting = ref(false);
  const showSuccessDialog = ref(false);
  const invoiceNumber = ref("");
  const indexToRemove = ref("");

  const formDatas = ref({});

  onMounted(() => {
      formDatas.value = JSON.parse(route.query.data || "[]").answers;
      console.log(formDatas.value[0].category)
  });

const removeFormData = () => {
    formDatas.value.splice(indexToRemove, 1);
    if (formDatas.value.length <= 0 ) {
          router.push({
            path: "/employee/invoice/unsubmitted",
            });
    }
};

  const submitInvoice = async (event, i) => {
    event.preventDefault();

    if (isSubmitting.value) return;

    isSubmitting.value = true;

    try {
      const invoiceData = {
        invoiceNumber: formDatas.value[i].invoiceNumber || `INV-${Date.now()}`,
        employeeId: 1, // Update this if you're using auth
        invoiceDate: formDatas.value[i].date,
        category: formDatas.value[i].category,
        merchantName: formDatas.value[i].merchant_name,
        merchantAddress: formDatas.value[i].merchant_address,
        itemsServices: formDatas.value[i].items.map((item) => ({
          description: item.description,
          quantity: parseInt(item.quantity),
          unit_price: parseFloat(item.unit_price),
        })),
        remark: formDatas.value[i].remark,
      };

      console.log("=== FRONTEND DEBUG ===");
      console.log("Prepared Invoice Data:", invoiceData);

      const response = await axios.post(
        `http://127.0.0.1:8000/employee/employee/invoice/save`,
        invoiceData,
        {
          headers: {
            "Content-Type": "application/json",
          },
        },
      );

      console.log("SUCCESS:", response.data);
      isSubmitting.value = false;
      showSuccessDialog.value = true;
      invoiceNumber.value = invoiceData.invoiceNumber;
      indexToRemove.value = i;
      // router.push("/employee/claim/all");
    } catch (error) {
      console.error("=== ERROR DEBUG ===");
      console.error("Error object:", error);
      console.error("Error response:", error.response);
      console.error("Error message:", error.message);
      console.error("Error status:", error.response?.status);
      console.error("Error data:", error.response?.data);

      console.error(
        "Validate details:",
        JSON.stringify(error.response?.data?.detail, null, 2),
      );

      alert(`Error: ${JSON.stringify(error.response?.data?.detail, null, 2)}`);
    } finally {
    }
  };

  const formatCurrency = (amount) => {
    if (amount === null || amount === undefined) return "0.00";
    return `${amount.toFixed(2)}`;
  };
</script>

<style scoped>
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.5s ease;
}

.fade-slide-enter-from,
.fade-slide-leave-to {
  opacity: 0;
  transform: translateX(30px);
}
</style>
