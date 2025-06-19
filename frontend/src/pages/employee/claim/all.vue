<!-- Employee Claim -->
<template>
  <div class="mx-auto my-14 w-full max-w-6xl bg-gray-100">
    <EmployeeClaimsCard
      :totalCount="totalCount"
      :approvedCount="approvedCount"
      :rejectedCount="rejectedCount"
    />
    <div class="mt-4 mb-2"></div>
    <div class="mt-8 flow-root px-4 sm:px-8 lg:px-14">
      <div class="-mx-4 -my-2 sm:-mx-6 lg:-mx-8">
        <div class="min-w-full py-2 align-middle sm:px-6 lg:px-8">
          <EmployeeClaimsTab />
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
                  Claim ID
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
                <th class="px-3 py-3.5 text-right text-sm font-semibold">
                  Total (RM)
                </th>
                <th class="w-48 px-3 py-3.5 text-center text-sm font-semibold">
                  Status
                </th>
                <th
                  class="sr-only w-48 rounded-tr-lg px-3 py-3.5 text-center text-sm font-semibold"
                >
                  Details
                </th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200 bg-white">
              <tr
                v-for="(group, index) in claimGroups"
                :key="group.ClaimID"
                class="shadow-md"
              >
                <td
                  :class="[
                    'py-4 pr-3 pl-4 text-right text-sm font-medium whitespace-nowrap text-gray-900 sm:pl-6',
                    index === claimGroups.length - 1 ? 'rounded-bl-lg' : '',
                  ]"
                >
                  {{ index + 1 }}
                </td>
                <!-- <td class="px-3 py-4 text-sm whitespace-nowrap text-gray-500">{{ person.Name }}</td> -->
                <td class="px-3 py-4 text-sm whitespace-nowrap text-gray-500">
                  {{ group.ClaimID }}
                </td>
                <td
                  class="px-3 py-4 text-center text-sm whitespace-nowrap text-gray-500"
                >
                  {{ group.Date }}
                </td>
                <td
                  class="px-3 py-4 text-center text-sm whitespace-nowrap text-gray-500"
                >
                  {{ group.Quantity }}
                </td>
                <td
                  class="px-4 py-4 text-right text-sm whitespace-nowrap text-gray-500"
                >
                  {{ group.Total }}
                </td>

                <td
                  class="px-4 py-4 text-center text-sm font-semibold whitespace-nowrap"
                >
                  <StatusBadge :status="group.Status" />
                </td>
                <td
                  :class="[
                    'px-4 py-4 text-right text-sm whitespace-nowrap text-theme-300',
                    index === claimGroups.length - 1 ? 'rounded-br-lg' : '',
                  ]"
                >
                  <button
                    class="text-theme-300 hover:underline"
                    @click="console.log('open details')"
                  >
                    Details
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  // will be connecting to the database later
  import { ref, computed } from "vue";

  const sortKey = ref("Date");
  const sortAsc = ref(false);

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

  // TODO: Shorter way to do sorting
  //sort by date in descending order (default)
  function parseDate(dateStr) {
    // Converts "DD/MM/YYYY" to a Date object
    const [day, month, year] = dateStr.split("/");
    return new Date(`${year}-${month}-${day}`);
  }

  const claimGroups = computed(() => {
    // Get unique ClaimIDs
    const ids = [...new Set(expenses.map((e) => e.ClaimID))];
    // For each ClaimID, get summary info
    let groups = ids.map((claimId) => {
      const group = expenses.filter((e) => e.ClaimID === claimId);
      return {
        ClaimID: claimId,
        Date: group[0]?.Date,
        Quantity: group.length,
        Total: group
          .reduce((sum, e) => sum + Number(e.Total.replace(/,/g, "")), 0)
          .toLocaleString("en-MY", { minimumFractionDigits: 2 }),
        Status: group[0]?.Status,
        Details: group, // all items with this ClaimID
      };
    });

    // Sorting logic
    if (sortKey.value === "Date") {
      groups = groups.sort((a, b) => {
        // Parse dates for comparison
        const dateA = parseDate(a.Date);
        const dateB = parseDate(b.Date);
        return sortAsc.value ? dateA - dateB : dateB - dateA;
      });
    }

    return groups;
  });

  function setSort(key) {
    if (sortKey.value === key) {
      sortAsc.value = !sortAsc.value;
    } else {
      sortKey.value = key;
      sortAsc.value = true;
    }
  }

  const totalCount = computed(() => {
    const ids = new Set(expenses.map((e) => e.ClaimID));
    return ids.size;
  });

  const approvedCount = computed(() => {
    const ids = new Set(
      expenses.filter((e) => e.Status === "Approved").map((e) => e.ClaimID),
    );
    return ids.size;
  });

  const rejectedCount = computed(() => {
    const ids = new Set(
      expenses.filter((e) => e.Status === "Rejected").map((e) => e.ClaimID),
    );
    return ids.size;
  });
</script>
