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
    <div class="mt-8 flow-root px-4 sm:px-6 lg:px-8">
      <div class="-mx-4 -my-2 sm:-mx-6 lg:-mx-8">
        <div class="min-w-full py-2 align-middle sm:px-6 lg:px-8">
          <div class="shadow-sm ring-1 ring-black/5 sm:rounded-lg">
            <table class="min-w-full divide-y divide-gray-300 bg-gray-100 drop-shadow-md">
              <thead class="bg-theme-300 text-white">
                <tr>
                  <th
                    scope="col"
                    class="rounded-tl-lg py-3 pr-3.5 pl-4 text-right text-sm font-semibold sm:pl-6"
                  >
                    #
                  </th>
                  <th
                    scope="col"
                    class="py-3.5 pr-3 pl-3.5 text-left text-sm font-semibold"
                  >
                    Category
                  </th>
                  <th
                    scope="col"
                    class="w-fit px-3 py-3.5 text-left text-sm font-semibold"
                  >
                    Date
                  </th>
                  <th
                    scope="col"
                    class="px-3 py-3.5 text-center text-sm font-semibold"
                  >
                    Item(s)
                  </th>
                  <th
                    scope="col"
                    class="px-3 py-3.5 text-left text-sm font-semibold"
                  >
                    Remark
                  </th>
                  <th
                    scope="col"
                    class="px-3 py-3.5 text-right text-sm font-semibold"
                  >
                    Total (RM)
                  </th>
                  <th
                    scope="col"
                    class="rounded-tr-lg px-3 py-3.5 text-center text-sm font-semibold"
                  ></th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-200 bg-white">
                <tr
                  v-for="(person, index) in people"
                  :key="person.email"
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
                        person.Name
                      }}</span>
                      <span class="text-xs text-gray-500">{{
                        person.title
                      }}</span>
                    </div>
                  </td>
                  <td class="px-3 py-4 text-sm whitespace-nowrap text-gray-500">
                    {{ person.Date }}
                  </td>
                  <td
                    class="px-3 py-4 text-center text-sm whitespace-nowrap text-gray-500"
                  >
                    {{ person.item }}
                  </td>
                  <td
                    class="w-fit px-3 py-4 text-sm whitespace-nowrap text-gray-500"
                  >
                    {{ person.email }}
                  </td>

                  <td
                    class="px-4 py-4 text-right text-sm whitespace-nowrap text-gray-500"
                  >
                    {{ person.Total }}
                  </td>
                  <td
                    class="px-4 py-4 text-right text-sm whitespace-nowrap text-theme-300"
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

  const people = [
    {
      ID: "GMD2039",
      Name: "Lindsay Walton",
      title: "Front-End Developer",
      email: "lindsay.walton@example.com",
      item: "6",
      Date: "29/05/2025",
      Total: 1285.00,
    },
    {
      ID: "GMD2040",
      Name: "Alex Chen",
      title: "UX Designer",
      email: "alex.chen@example.com",
      item: "12",
      Date: "30/05/2025",
      Total: "120.00",
    },
    {
      ID: "GMD2041",
      Name: "Sarah Johnson",
      title: "Marketing Specialist",
      email: "sarah.j@example.com",
      item: "1",
      Date: "31/05/2025",
      Total: "65.00",
    },
    {
      ID: "GMD2042",
      Name: "Michael Brown",
      title: "Graphic Designer",
      email: "michael.b@example.com",
      item: "9",
      Date: "01/06/2025",
      Total: "45.00",
    },
    {
      ID: "GMD2043",
      Name: "Emily Wilson",
      title: "Content Writer",
      email: "emily.w@example.com",
      item: "5",
      Date: "02/06/2025",
      Total: "90.00",
    },
    {
      ID: "GMD2044",
      Name: "David Lee",
      title: "Photographer",
      email: "david.lee@example.com",
      item: "18",
      Date: "03/06/2025",
      Total: "150.00",
    },
    {
      ID: "GMD2045",
      Name: "Jessica Tan",
      title: "Social Media Manager",
      email: "jessica.t@example.com",
      item: "1",
      Date: "04/06/2025",
      Total: "200.00",
    },
    {
      ID: "GMD2046",
      Name: "Ryan Wong",
      title: "Video Editor",
      email: "ryan.w@example.com",
      item: "3",
      Date: "05/06/2025",
      Total: "350.00",
    },
    {
      ID: "GMD2047",
      Name: "Amanda Lim",
      title: "Event Coordinator",
      email: "amanda.l@example.com",
      item: "2",
      Date: "06/06/2025",
      Total: "500.00",
    },
    {
      ID: "GMD2048",
      Name: "Daniel Koh",
      title: "Print Specialist",
      email: "daniel.k@example.com",
      item: "50",
      Date: "07/06/2025",
      Total: "80.00",
    },
    {
      ID: "GMD2049",
      Name: "Michelle Ho",
      title: "Brand Strategist",
      email: "michelle.h@example.com",
      item: "3",
      Date: "08/06/2025",
      Total: "600.00",
    },
  ];
</script>
