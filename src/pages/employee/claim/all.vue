<template>
  <div class="mx-auto my-14 w-full max-w-6xl bg-gray-100">
    <!-- Cards Row -->
    <ClaimsCard
      :expenses="expenses"
    />
    <!-- Expenses Table -->
    <div class="mt-4 mb-2"></div>
    <div class="mt-8 flow-root px-8 sm:px-8 lg:px-14">
      <div class="-mx-4 -my-2 sm:-mx-6 lg:-mx-8">
        <div class="min-w-full py-2 align-middle sm:px-6 lg:px-8">
            <!-- Tabs Row -->
            <ClaimsTab />
            <table
              class="min-w-full divide-gray-300 drop-shadow-md rounded-b-lg text-xs"
            >
              <thead class="rounded-lg bg-theme-300 text-white">
                <tr>
                  <th
                    class="rounded-tl-lg py-3 pr-3.5 pl-4 text-right text-sm font-semibold sm:pl-6"
                  >
                    #
                  </th>
                  <th
                    class="py-3.5 pr-3 pl-3.5 text-left text-sm font-semibold"
                  >
                    Category
                    <span
                      class="rounded-tl-lg relative ml-1 cursor-pointer text-xs"
                      @mouseenter="showCategoryDropdown = true"
                    >
                      <button class="focus:outline-none" @click="setSort('Category')">
                        ⇅
                      </button>
                      <div
                        v-show="showCategoryDropdown"
                        class="absolute left-0 z-10 mt-2 w-48 rounded bg-white shadow-xl font-normal text-theme-300"
                        @mouseenter="showCategoryDropdown = true"
                        @mouseleave="showCategoryDropdown = false"
                        
                      >
                        <ul>
                          <li
                            v-for="cat in categories"
                            :key="cat"
                            @click="
                              selectedCategory = cat;
                              showCategoryDropdown = false;
                            "
                            class="cursor-pointer rounded px-4 py-2 hover:bg-[#FFAD05] hover:text-white"
                            :class="{
                              'bg-theme-200 text-white':
                                selectedCategory === cat,
                            }"
                          >
                            {{ cat }}
                          </li>
                        </ul>
                      </div>
                    </span>
                  </th>
                  <th
                    class="w-fit px-3 py-3.5 text-center text-sm font-semibold"
                  >
                    Date
                    <button class="focus:outline-none" @click="setSort('Date')">
                      ⇅
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
                    Action
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
                      index === sortedExpenses.length - 1 ? 'rounded-bl-lg' : ''
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
                      'px-4 py-4 text-center text-sm whitespace-nowrap text-[#FFAD05]',
                      index === sortedExpenses.length - 1 ? 'rounded-br-lg' : ''
                    ]"
                  >
                    <input
                      type="checkbox"
                      :value="product"
                      v-model="selectedExpenses"
                      class="form-checkbox h-5 w-5 accent-[#FFAD05] bg-white rounded border-gray-300 focus:ring-[#FFAD05] checked:bg-[#FFAD05]"
                    />
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
            class="mt-4 px-4 py-2 bg-theme-300 text-white rounded hover:bg-theme-400"
            :disabled="selectedExpenses.length === 0"
            @click="submitForApproval"
          >
            Submit
          </button>
    </div>
  </div>
  
</template>

<script setup>
  // will be connecting to the database later
  import { ref, computed } from "vue";
  import ClaimsCard from '@/components/ClaimsCard.vue'
  import ClaimsTab from '@/components/ClaimsTab.vue'

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
          e.Category.toLowerCase() === selectedCategory.value.toLowerCase()
      )
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
