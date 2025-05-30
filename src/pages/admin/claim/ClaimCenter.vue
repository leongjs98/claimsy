<template>
  <div class="px-4 sm:px-6 lg:px-16">
    <!-- Margin top 16  -->
    <div class="sm:flex sm:items-center mt-16">
      <div class="sm:flex-auto">
        <h1 class="text-base font-semibold text-gray-900">Claim Submitted</h1>
        <p class="mt-2 text-sm text-gray-700">A list of all the Employees in your account including their ID, tukar,
          Date, Item(s), Email, Total (RM), Details.</p>
      </div>
      <div class="mt-4 sm:mt-0 sm:ml-16 sm:flex-none">
        <!-- <button type="button" class="block rounded-md bg-indigo-600 px-3 py-2 text-center text-sm font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Add user</button> -->
      </div>
    </div>
    <div class="mt-8 flow-root">
      <div class="-mx-4 -my-2 sm:-mx-6 lg:-mx-8">
        <div class="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8 shadow-black-900 ">
          <div class="shadow-sm ring-1 ring-black/5 sm:rounded-lg blue-xl/20 ">
            <table class="min-w-full divide-y divide-gray-300 shadow-xl/20">
              <thead class="bg-blue-900">
                <tr>
                  <th scope="col" class="py-3.5 pr-3 pl-4 text-left text-sm font-semibold text-red-50 sm:pl-6">ID</th>
                  <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-red-50">Name</th>
                  <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-red-50">Email</th>
                  <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-red-50">Item(s)</th>
                  <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-red-50">Date</th>
                  <th scope="col" class="px-3 py-3.5 text-sm font-semibold text-red-50 text-right">Total (RM)</th>
                  <th scope="col" class="px-3 py-3.5 text-sm font-semibold text-red-50 text-center">Details</th>
                  <!-- <th scope="col" class="relative py-3.5 pl-4 pr-3 sm:pr-6 text-right">
                    <span class="sr-only">Edit</span>
                  </th> -->
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-200 bg-white">
                <tr v-for="person in people" :key="person.email">
                  <td class="py-4 pr-3 pl-4 text-sm font-medium whitespace-nowrap text-gray-900 sm:pl-6">{{ person.ID }}
                  </td>
                  <!-- <td class="px-3 py-4 text-sm whitespace-nowrap text-gray-500">{{ person.Name }}</td> -->
                  <td class="px-3 py-4 text-sm whitespace-nowrap text-gray-500">
                    <div class="flex flex-col">
                      <span class="font-medium text-gray-900">{{ person.Name }}</span>
                      <span class="text-xs text-gray-500">{{ person.title }}</span>
                    </div>
                  </td>
                  <td class="px-3 py-4 text-sm whitespace-nowrap text-gray-500">{{ person.email }}</td>
                  <td class="px-3 py-4 text-sm whitespace-nowrap text-gray-500">{{ person.item }}</td>
                  <td class="px-3 py-4 text-sm whitespace-nowrap text-gray-500">{{ person.Date }}</td>
                  <td class="px-4 py-4 text-sm whitespace-nowrap text-gray-500 text-right">{{ person.Total }}</td>
                  <td class="px-3 py-4 text-sm whitespace-nowrap text-red-500 text-center">
                    <img class="flex justify-center items-center" src="/detail.svg" alt="Claimsy Logo" />
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
// will be connect to the database later

const people = [
  { ID: 'GMD2039', Name: 'Lindsay Walton', title: 'Front-End Developer', email: 'lindsay.walton@example.com', item: 'Banner', Date: '29/05/2025', Total: 'RM85' },
  { ID: 'GMD2040', Name: 'Alex Chen', title: 'UX Designer', email: 'alex.chen@example.com', item: 'Standee', Date: '30/05/2025', Total: 'RM120' },
  { ID: 'GMD2041', Name: 'Sarah Johnson', title: 'Marketing Specialist', email: 'sarah.j@example.com', item: 'Poster', Date: '31/05/2025', Total: 'RM65' },
  { ID: 'GMD2042', Name: 'Michael Brown', title: 'Graphic Designer', email: 'michael.b@example.com', item: 'Flyer', Date: '01/06/2025', Total: 'RM45' },
  { ID: 'GMD2043', Name: 'Emily Wilson', title: 'Content Writer', email: 'emily.w@example.com', item: 'Brochure', Date: '02/06/2025', Total: 'RM90' },
  { ID: 'GMD2044', Name: 'David Lee', title: 'Photographer', email: 'david.lee@example.com', item: 'Backdrop', Date: '03/06/2025', Total: 'RM150' },
  { ID: 'GMD2045', Name: 'Jessica Tan', title: 'Social Media Manager', email: 'jessica.t@example.com', item: 'Digital Ads', Date: '04/06/2025', Total: 'RM200' },
  { ID: 'GMD2046', Name: 'Ryan Wong', title: 'Video Editor', email: 'ryan.w@example.com', item: 'Promo Video', Date: '05/06/2025', Total: 'RM350' },
  { ID: 'GMD2047', Name: 'Amanda Lim', title: 'Event Coordinator', email: 'amanda.l@example.com', item: 'Booth Design', Date: '06/06/2025', Total: 'RM500' },
  { ID: 'GMD2048', Name: 'Daniel Koh', title: 'Print Specialist', email: 'daniel.k@example.com', item: 'Business Cards', Date: '07/06/2025', Total: 'RM80' },
  { ID: 'GMD2049', Name: 'Michelle Ho', title: 'Brand Strategist', email: 'michelle.h@example.com', item: 'Brand Guidelines', Date: '08/06/2025', Total: 'RM600' }
];
  // 
  // More people...

</script>