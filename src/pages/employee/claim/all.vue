<template>
  <div class="mx-auto my-14 w-full max-w-6xl bg-gray-100">
    <div class="mt-16 sm:flex sm:items-center">
      <div class="sm:flex-auto">
        <h1 class="text-base font-semibold text-gray-900">My Expenses</h1>
        <p class="mt-2 text-sm text-gray-700">
          Expenses list for personID.
        </p>
      </div>
    </div>
    <div class="mt-8 flow-root px-4 sm:px-8 lg:px-14">
      <div class="-mx-4 -my-2 sm:-mx-6 lg:-mx-8">
        <div class="min-w-full py-2 align-middle sm:px-6 lg:px-8">
          <div class="shadow-sm ring-1 ring-black/5 sm:rounded-lg">
            <table class="min-w-full divide-y divide-gray-300 bg-gray-100 drop-shadow-md">
              <thead class="bg-theme-300 text-white">
                <tr>
                  <th class="rounded-tl-lg py-3 pr-3.5 pl-4 text-right text-sm font-semibold sm:pl-6">#</th>
                  <th class="py-3.5 pr-3 pl-3.5 text-left text-sm font-semibold">
                    Category
                    <button @click="setSort('Category')" class="ml-1 text-xs">
                      <span v-if="sortKey === 'Category'">{{ sortAsc ? '▲' : '▼' }}</span>
                      <span v-else>⇅</span>
                    </button>
                  </th>
                  <th class="w-fit px-3 py-3.5 text-center text-sm font-semibold">
                    Date
                    <button @click="setSort('Date')" class="ml-1 text-xs">
                      <span v-if="sortKey === 'Date'">{{ sortAsc ? '▲' : '▼' }}</span>
                      <span v-else>⇅</span>
                    </button>
                  </th>
                  <th class="px-3 py-3.5 text-center text-sm font-semibold">
                    Quantity
                    <button @click="setSort('Item')" class="ml-1 text-xs">
                      <span v-if="sortKey === 'Item'">{{ sortAsc ? '▲' : '▼' }}</span>
                      <span v-else>⇅</span>
                    </button>
                  </th>
                  <th class="px-3 py-3.5 text-left text-sm font-semibold w-48">Remark</th>
                  <th class="px-3 py-3.5 text-right text-sm font-semibold">
                    Total (RM)
                    <button @click="setSort('Total')" class="ml-1 text-xs">
                      <span v-if="sortKey === 'Total'">{{ sortAsc ? '▲' : '▼' }}</span>
                      <span v-else>⇅</span>
                    </button>
                  </th>
                  <th class="px-3 py-3.5 text-center text-sm font-semibold w-48">Action</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-200 bg-white">
                <tr
                  v-for="(product, index) in sortedExpenses"
                  :key="product.Name"
                  class="shadow-md"
                >
                  <td
                    class="py-4 pr-3 pl-4 text-right text-sm font-medium whitespace-nowrap text-gray-900 sm:pl-6"
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
                  <td class="px-3 py-4 text-center text-sm whitespace-nowrap text-gray-500">
                    {{ product.Date }}
                  </td>
                  <td
                    class="px-3 py-4 text-center text-sm whitespace-nowrap text-gray-500"
                  >
                    {{ product.Item }}
                  </td>
                  <td class="px-3 py-4 text-sm text-gray-500 w-32">
                    <span class="block w-48 truncate overflow-hidden text-ellipsis">
                      {{ product.Remark }}
                    </span>
                  </td>

                  <td
                    class="px-4 py-4 text-right text-sm whitespace-nowrap text-gray-500"
                  >
                    {{ product.Total }}
                  </td>
                  <td
                    class="px-4 py-4 text-center text-sm whitespace-nowrap text-theme-300"
                  >
                    <RouterLink class="hover:underline" to="#"
                      >Details</RouterLink
                    >
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
    </div>
  </div>
</template>

<script setup>
  // will be connecting to the database later
import { ref, computed } from 'vue'

const sortKey = ref('Date')
const sortAsc = ref(false)

const expenses = [
    {
      Name: "Laptop",
      Category: "Office Equipment",
      Date: "30/05/2025",
      Item: "6",
      Remark: "Dell 1.35GHz 8GB 256GB SSD - for new employee sasascdavadfa",
      Total: "48,285.00",
    },
    {
      Name: "Whiteboard 4x6ft",
      Category: "Office Equipment",
      Date: "21/05/2025",
      Item: "2",
      Remark: "for training room",
      Total: "1,200.00",
    },
    {
      Name: "Meeting at Damansara",
      Category: "Travel Expenses",
      Date: "29/06/2025",
      Item: "1",
      Remark: "Lunch with client",
      Total: "150.00",
    },
    {
      Name: "Lunch",
      Category: "Food & Beverages",
      Date: "31/07/2025",
      Item: "10",
      Remark: "team lunch",
      Total: "250.00",
    },
    {
      Name: "Dinner",
      Category: "Food & Beverages",
      Date: "18/04/2025",
      Item: "6",
      Remark: "Sales team dinner",
      Total: "138.00",
    },
    {
      Name: "Stationery",
      Category: "Office Supplies",
      Date: "12/02/2025",
      Item: "15",
      Remark: "for new employee",
      Total: "1,000.00",
    },
    {
      Category: "Laptop",
      Date: "29/05/2025",
      Item: "6",
      Remark: "for new employee",
      Total: "48,285.00",
    },

  ];

//sort by date in descending order (default)
  function parseDate(dateStr) {
  // Converts "DD/MM/YYYY" to a Date object
  const [day, month, year] = dateStr.split('/')
  return new Date(`${year}-${month}-${day}`)
}

function getValue(item, key) {
  if (key === 'Date') return parseDate(item.Date)
  if (key === 'Total') return Number(item.Total.replace(/,/g, ''))
  if (key === 'Item') return Number(item.Item)
  if (key === 'Category') return item.Category || ''
  if (key === 'Name') return item.Name || ''
  return item[key] || ''
}

const sortedExpenses = computed(() =>
  expenses.slice().sort((a, b) => {
    const valA = getValue(a, sortKey.value)
    const valB = getValue(b, sortKey.value)
    if (valA < valB) return sortAsc.value ? -1 : 1
    if (valA > valB) return sortAsc.value ? 1 : -1
    return 0
  })
)

function setSort(key) {
  if (sortKey.value === key) {
    sortAsc.value = !sortAsc.value
  } else {
    sortKey.value = key
    sortAsc.value = true
  }
}

</script>
