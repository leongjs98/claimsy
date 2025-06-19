<template>
  <div class="mx-auto my-14 w-full max-w-6xl bg-gray-100">
    <!-- Cards Row -->
    <ClaimsCard :expenses="expenses" />
    <!-- Expenses Table -->
    <div class="mt-4 mb-2"></div>
    <div class="mt-8 flow-root px-4 sm:px-8 lg:px-14">
      <div class="-mx-4 -my-2 sm:-mx-6 lg:-mx-8">
        <div class="min-w-full py-2 align-middle sm:px-6 lg:px-8">
          <!-- Tabs Row -->
          <ClaimsTab />
          <table
            class="min-w-full divide-y divide-gray-300 rounded-b-lg bg-gray-100 drop-shadow-md"
          >
            <thead class="rounded-lg bg-blue-50 text-theme-300">
              <tr>
                <th
                  class="rounded-tl-lg py-3 pr-3.5 pl-4 text-right text-sm font-semibold sm:pl-6"
                >
                  #
                </th>
                <th class="py-3.5 pr-3 pl-3.5 text-left text-sm font-semibold">
                  <div
                    @mouseenter="showCategoryDropdown = true"
                            @mouseleave="showCategoryDropdown = false"
                    class="flex items-center gap-2"
                  >
                    <button @click="setSort('Category')"> Category </button>
                    <div class="w-full relative inline-block text-left">
                      <div>
                        <button
                          type="button"
                          class="hover:text--600 flex items-center justify-center rounded-full bg-gray-100 text-theme-300 focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 focus:ring-offset-gray-100 focus:outline-hidden"
                          id="menu-button"
                          aria-expanded="true"
                          aria-haspopup="true"
                        >
                          <span class="sr-only">Open options</span>
                          <svg
                            class="size-4"
                            xmlns="http://www.w3.org/2000/svg"
                            width="32"
                            height="32"
                            viewBox="0 0 24 24"
                          >
                            <path
                              fill="currentColor"
                              d="M11 20q-.425 0-.712-.288T10 19v-6L4.2 5.6q-.375-.5-.112-1.05T5 4h14q.65 0 .913.55T19.8 5.6L14 13v6q0 .425-.288.713T13 20z"
                            />
                          </svg>
                        </button>
                      </div>

      <Transition name="dropdown-menu">
                      <div
v-show="showCategoryDropdown"
                            @mouseleave="showCategoryDropdown = false"
                        class="absolute left-0 z-20 mt-2 w-56 origin-top-left rounded-md bg-white shadow-lg ring-1 ring-black/5 focus:outline-hidden"
                        role="menu"
                        aria-orientation="vertical"
                        aria-labelledby="menu-button"
                        tabindex="-1"
                      >
                        <div class="py-1" role="none">
                          <button
                            v-for="cat in categories"
                            :key="cat"
                            @click="
                              selectedCategory = cat;
                              showCategoryDropdown = false;
                            "
                            :class="{
                              'bg-blue-50 text-theme-200 outline-hidden':
                                selectedCategory === cat,
                              'text-gray-700': selectedCategory !== cat,
                            }"
                            showCategoryDropdown="false;"
                            href="#"
                            class="text-left w-full block px-4 py-2 text-sm text-gray-700 focus:text-theme-200 focus:bg-blue-50 hover:text-theme-200 hover:bg-blue-50"
                            role="menuitem"
                            tabindex="-1"
                            id="menu-item-2"
                          >
                            {{ cat }}
                          </button>
                        </div>
                      </div>
      </Transition>
                    </div>
                    <!-- <span class="flex items-center relative ml-1 cursor-pointer rounded-tl-lg text-xs" -->
                    <!--   @mouseenter="showCategoryDropdown = true"> -->
                    <!--   <button class="focus:outline-none" @click="setSort('Category')"> -->
                    <!--     <svg class="w-4 h-4" xmlns="http://www.w3.org/2000/svg" width="32" height="32" -->
                    <!--       viewBox="0 0 24 24"> -->
                    <!--       <path fill="currentColor" -->
                    <!--         d="M11 20q-.425 0-.712-.288T10 19v-6L4.2 5.6q-.375-.5-.112-1.05T5 4h14q.65 0 .913.55T19.8 5.6L14 13v6q0 .425-.288.713T13 20z" /> -->
                    <!--     </svg> -->
                    <!--   </button> -->
                    <!--   <div v-show="showCategoryDropdown" -->
                    <!--     class="absolute left-0 z-10 mt-2 w-48 rounded bg-white font-normal text-theme-300 shadow-xl" -->
                    <!--     @mouseenter="showCategoryDropdown = true" @mouseleave="showCategoryDropdown = false"> -->
                    <!--     <ul> -->
                    <!--       <li v-for="cat in categories" :key="cat" @click=" -->
                    <!--         selectedCategory = cat; -->
                    <!--       showCategoryDropdown = false; -->
                    <!-- " class="cursor-pointer rounded px-4 py-2 hover:bg-[#FFAD05] hover:text-white" -->
                    <!-- :class="{ 'bg-theme-200 text-white': selectedCategory === cat, }"> -->
                    <!--         {{ cat }} -->
                    <!--       </li> -->
                    <!--     </ul> -->
                    <!--   </div> -->
                    <!-- </span> -->
                  </div>
                </th>
                <th
                  class="flex justify-center px-3 py-3.5 text-sm font-semibold"
                >
                  <button
                    class="flex items-center justify-center gap-2 hover:cursor-pointer"
                    @click="setSort('Date')"
                  >
                    <span> Date </span>
                    <svg
                      v-show="!sortAsc"
                      class="h-5 w-5"
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 24 24"
                    >
                      <!-- Icon from Material Design Icons by Pictogrammers - https://github.com/Templarian/MaterialDesign/blob/master/LICENSE -->
                      <path
                        fill="currentColor"
                        d="M19 7h-3l4-4l4 4h-3v14h-2zM8 16h3v-3H8zm5-11h-1V3h-2v2H6V3H4v2H3c-1.11 0-2 .89-2 2v11c0 1.11.89 2 2 2h10c1.11 0 2-.89 2-2V7c0-1.11-.89-2-2-2M3 18v-7h10v7z"
                      />
                    </svg>
                    <svg
                      v-show="sortAsc"
                      class="h-5 w-5"
                      xmlns="http://www.w3.org/2000/svg"
                      width="32"
                      height="32"
                      viewBox="0 0 24 24"
                    >
                      <!-- Icon from Material Design Icons by Pictogrammers - https://github.com/Templarian/MaterialDesign/blob/master/LICENSE -->
                      <path
                        fill="currentColor"
                        d="M21 17h3l-4 4l-4-4h3V3h2zM8 16h3v-3H8zm5-11h-1V3h-2v2H6V3H4v2H3c-1.11 0-2 .89-2 2v11c0 1.11.89 2 2 2h10c1.11 0 2-.89 2-2V7c0-1.11-.89-2-2-2M3 18v-7h10v7z"
                      />
                    </svg>
                  </button>
                </th>
                <th class="px-3 py-3.5 text-center text-sm font-semibold">
                  Quantity
                </th>
                <th class="w-48 px-3 py-3.5 text-left text-sm font-semibold">
                  Remark
                </th>
                <th class="px-3 py-3.5 text-right text-sm font-semibold">
                  Total (RM)
                </th>
                <th
                  class="w-48 rounded-tr-lg px-3 py-3.5 text-center text-sm font-semibold"
                >
                Select
                </th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200 bg-white">
              <tr
                v-for="(product, index) in sortedExpenses"
                :key="product.Name"
                class="shadow-md"
              >
                <td
                  :class="[
                    'py-4 pr-3 pl-4 text-right text-sm font-medium whitespace-nowrap text-gray-900 sm:pl-6',
                    index === sortedExpenses.length - 1 ? 'rounded-bl-lg' : '',
                  ]"
                >
                  {{ index + 1 }}
                </td>
                <!-- <td class="px-3 py-4 text-sm whitespace-nowrap text-gray-500">{{ person.Name }}</td> -->
                <td class="px-3 py-4 text-sm whitespace-nowrap text-gray-500">
                  <div class="flex flex-col">
                    <span class="font-medium text-gray-900">{{
                      product.Name
                    }}</span>
                    <span class="text-xs text-gray-500">{{
                      product.Category
                    }}</span>
                  </div>
                </td>
                <td
                  class="px-3 py-4 text-center text-sm whitespace-nowrap text-gray-500"
                >
                  {{ product.Date }}
                </td>
                <td
                  class="px-3 py-4 text-center text-sm whitespace-nowrap text-gray-500"
                >
                  {{ product.Item }}
                </td>
                <td class="w-32 px-3 py-4 text-sm text-gray-500">
                  <span
                    class="block w-48 truncate overflow-hidden text-ellipsis"
                  >
                    {{ product.Remark }}
                  </span>
                </td>

                <td
                  class="px-4 py-4 text-right text-sm whitespace-nowrap text-gray-500"
                >
                  {{ product.Total }}
                </td>
                <td
                  :class="[
                    'min-h-[69px] px-4 py-4 text-center text-sm whitespace-nowrap text-amber-500',
                    index === sortedExpenses.length - 1 ? 'rounded-br-lg' : '',
                  ]"
                >
                  <div class="flex items-center justify-center">
                    <input
                      type="checkbox"
                      :value="product"
                      v-model="selectedExpenses"
                      :id="`checkbox-product-${index}`"
                      class="checkbox-input sr-only"
                    />

                    <!-- Visual representation of the checkbox -->
                    <label
                      :for="`checkbox-product-${index}`"
                      class="checkbox-label relative flex h-6 w-6 cursor-pointer items-center justify-center overflow-hidden rounded-md border-1 border-theme-200 transition-colors ease-in-out hover:border-theme-300 focus:border-theme-300"
                    >
                      <!-- The expanding fill element -->
                      <div class="checkbox-fill absolute bg-theme-300"></div>
                    </label>
                  </div>
                </td>
                <!-- <td class="relative py-4 pr-4 pl-3 text-right text-sm font-medium whitespace-nowrap sm:pr-6">
                    <a href="#" class="text-indigo-600 hover:text-indigo-900">Edit<span class="sr-only">, {{ person.name
                        }}</span></a>
                  </td> -->
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <div class="flex justify-center px-4 sm:px-8 lg:px-14">
      <button
        class="hover:bg-theme-400 mt-4 rounded bg-theme-300 px-4 py-2 text-white"
        :disabled="selectedExpenses.length === 0"
        @click="submitForApproval"
      >
        Submit
      </button>
    </div>
  </div>
</template>

<style scoped>
  /* The expanding fill element */
  .checkbox-fill {
    /* Initial state: completely collapsed at the center */
    width: 0;
    height: 0;
    top: 50%;
    /* Position at vertical center */
    left: 50%;
    /* Position at horizontal center */
    transform: translate(-50%, -50%);
    /* Adjust to truly center the element */
    transition:
      width 0.15s ease-out,
      height 0.15s ease-out;
    /* Smooth transition for width and height */
    /* Removed rounded-md from here, as parent's overflow-hidden handles the rounding */
  }

  /* State when checkbox is checked */
  .checkbox-input:checked + .checkbox-label .checkbox-fill {
    width: 100%;
    /* Expands to fill the container width */
    height: 100%;
    /* Expands to fill the container height */
  }
</style>

<script setup>
  // will be connecting to the database later
  import { ref, computed } from "vue";
  import ClaimsCard from "@/components/ClaimsCard.vue";
  import ClaimsTab from "@/components/ClaimsTab.vue";

  const sortKey = ref("Date");
  const sortAsc = ref(false);
  const showCategoryDropdown = ref(false);

  const expenses = [
    {
      ClaimID: "C0001",
      Name: "Laptop",
      Category: "Office Supplies and Equipment",
      Date: "30/01/2025",
      Item: "6",
      Remark: "Dell 1.35GHz 8GB 256GB SSD - for new employee sasascdavadfa",
      Total: "48,285.00",
      Status: "Approved",
    },
    {
      ClaimID: "C0002",
      Name: "Whiteboard 4x6ft",
      Category: "Office Supplies and Equipment",
      Date: "21/02/2025",
      Item: "2",
      Remark: "for training room",
      Total: "1,200.00",
      Status: "Approved",
    },
    {
      ClaimID: "C0003",
      Name: "Meeting at Damansara",
      Category: "Travel Expenses",
      Date: "29/03/2025",
      Item: "1",
      Remark: "Lunch with client",
      Total: "150.00",
      Status: "Rejected",
    },
    {
      ClaimID: "C0003",
      Name: "Lunch",
      Category: "Meals and Entertainment",
      Date: "29/03/2025",
      Item: "10",
      Remark: "team lunch",
      Total: "250.00",
      Status: "Rejected",
    },
    {
      ClaimID: "C0005",
      Name: "Dinner",
      Category: "Meals and Entertainment",
      Date: "18/05/2025",
      Item: "6",
      Remark: "Sales team dinner",
      Total: "138.00",
      Status: "Rejected",
    },
    {
      ClaimID: "C0006",
      Name: "Stationery",
      Category: "Office Supplies and Equipment",
      Date: "12/06/2025",
      Item: "15",
      Remark: "for new employee",
      Total: "1,000.00",
      Status: "Approved",
    },
    {
      ClaimID: "C0007",
      Name: "Flight to Penang",
      Category: "Travel Expenses",
      Date: "29/07/2025",
      Item: "2",
      Remark: "Flight tickets for conference",
      Total: "1,200.00",
      Status: "Approved",
    },

    {
      ClaimID: "C0008",
      Name: "Hotel at Penang",
      Category: "Accomodation",
      Date: "29/08/2025",
      Item: "2",
      Remark: "Company conference",
      Total: "2,500.00",
      Status: "Pending",
    },
  ];

  const categories = [
    "All",
    "Travel Expenses",
    "Accomodation",
    "Meals and Entertainment",
    "Office Supplies and Equipment",
    "Medical Claim",
  ];

  const selectedCategory = ref("All");

  const selectedExpenses = ref([]); // store selected expense indexes or IDs

  //sort by date in descending order (default)
  function parseDate(dateStr) {
    // Converts "DD/MM/YYYY" to a Date object
    const [day, month, year] = dateStr.split("/");
    return new Date(`${year}-${month}-${day}`);
  }

  const filteredExpenses = computed(() =>
    selectedCategory.value === "All"
      ? expenses
      : expenses.filter(
          (e) =>
            e.Category &&
            e.Category.toLowerCase() === selectedCategory.value.toLowerCase(),
        ),
  );

  const sortedExpenses = computed(() => {
    // Only sort by Date, otherwise keep original order
    if (sortKey.value === "Date") {
      return filteredExpenses.value.slice().sort((a, b) => {
        const dateA = parseDate(a.Date);
        const dateB = parseDate(b.Date);
        return sortAsc.value ? dateA - dateB : dateB - dateA;
      });
    }
    return filteredExpenses.value;
  });

  function setSort(key) {
    if (key === "Date") {
      if (sortKey.value === key) {
        sortAsc.value = !sortAsc.value;
      } else {
        sortKey.value = key;
        sortAsc.value = true;
      }
    }
  }
</script>
