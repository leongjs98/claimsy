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
            <thead class="rounded-lg bg-theme-300 text-white">
              <tr>
                <th
                  class="rounded-tl-lg py-3 pr-3.5 pl-4 text-right text-sm font-semibold sm:pl-6"
                >
                  #
                </th>
                <th class="py-3.5 pr-3 pl-3.5 text-left text-sm font-semibold">
                  Claim ID
                </th>
                <th class="w-fit px-3 py-3.5 text-center text-sm font-semibold">
                  Date
                  <button class="focus:outline-none" @click="setSort('Date')">
                    ⇅
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
                  class="w-48 rounded-tr-lg px-3 py-3.5 text-center text-sm font-semibold"
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
                    'px-4 py-4 text-center text-sm whitespace-nowrap text-gray-500',
                    index === claimGroups.length - 1 ? 'rounded-br-lg' : '',
                  ]"
                >
                  Details
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
  import ClaimsCard from "@/components/ClaimsCard.vue";

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
    // Add more sortKey options if needed

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
</script>
