<template>
  <div class="mx-auto my-14 w-full max-w-6xl bg-gray-100">
    <AdminClaimsCard :totalCount="people.length" :approvedCount="approvedCount" :rejectedCount="rejectedCount" />
    <AdminClaimsTab />
    <div class="mt-8 flow-root">
      <div class="-mx-4 -my-2 sm:-mx-6 lg:-mx-8">
        <div class="min-w-full py-2 align-middle sm:px-6 lg:px-8">
          <div class="shadow-sm ring-1 ring-black/5 sm:rounded-lg">
            <table class="min-w-full divide-y divide-gray-300 bg-gray-100">
              <thead class="rounded-lg bg-blue-50 text-theme-300">
                <tr>
                  <th scope="col" class="rounded-tl-lg py-3 pr-3.5 pl-4 text-right text-sm font-semibold sm:pl-6">
                    #
                  </th>
                  <th scope="col" class="py-3.5 pr-3 pl-3.5 text-left text-sm font-semibold">
                    Name
                  </th>
                  <th scope="col" class="w-fit px-3 py-3.5 text-left text-sm font-semibold">
                    Email
                  </th>
                  <th class="flex px-3 py-3.5 text-sm font-semibold">
                    <button class="flex items-center gap-2 hover:cursor-pointer" @click="setSort('Date')">
                      <span> Date </span>
                      <svg v-show="!sortAsc" class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                        <!-- Icon from Material Design Icons by Pictogrammers - https://github.com/Templarian/MaterialDesign/blob/master/LICENSE -->
                        <path fill="currentColor"
                          d="M19 7h-3l4-4l4 4h-3v14h-2zM8 16h3v-3H8zm5-11h-1V3h-2v2H6V3H4v2H3c-1.11 0-2 .89-2 2v11c0 1.11.89 2 2 2h10c1.11 0 2-.89 2-2V7c0-1.11-.89-2-2-2M3 18v-7h10v7z" />
                      </svg>
                      <svg v-show="sortAsc" class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" width="32" height="32"
                        viewBox="0 0 24 24">
                        <!-- Icon from Material Design Icons by Pictogrammers - https://github.com/Templarian/MaterialDesign/blob/master/LICENSE -->
                        <path fill="currentColor"
                          d="M21 17h3l-4 4l-4-4h3V3h2zM8 16h3v-3H8zm5-11h-1V3h-2v2H6V3H4v2H3c-1.11 0-2 .89-2 2v11c0 1.11.89 2 2 2h10c1.11 0 2-.89 2-2V7c0-1.11-.89-2-2-2M3 18v-7h10v7z" />
                      </svg>
                    </button>
                  </th>
                  <th class="w-48 px-3 py-3.5 text-center text-sm font-semibold">
                    Status
                  </th>
                  <th scope="col" class="px-3 py-3.5 text-center text-sm font-semibold">
                    Item(s)
                  </th>
                  <th scope="col" class="px-3 py-3.5 text-right text-sm font-semibold">
                    Total (RM)
                  </th>
                  <th scope="col" class="rounded-tr-lg px-3 py-3.5 text-center text-sm font-semibold"></th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-200 bg-white">
                <tr v-for="(person, index) in approvedPeople" :key="person.email" class="shadow-md">
                  <td class="py-4 pr-3 pl-4 text-right text-sm font-medium whitespace-nowrap text-gray-900 sm:pl-6">
                    {{ index + 1 }}
                  </td>
                  <td class="px-3 py-4 text-sm whitespace-nowrap text-gray-500">
                    <div class="flex flex-col">
                      <span class="font-medium text-gray-900">
                        {{ person.Name }}
                      </span>
                      <span class="text-xs text-gray-500">
                        {{ person.title }}
                      </span>
                    </div>
                  </td>
                  <td class="w-fit px-3 py-4 text-sm whitespace-nowrap text-gray-500">
                    {{ person.email }}
                  </td>
                  <td class="px-3 py-4 text-sm whitespace-nowrap text-gray-500">
                    {{ person.Date }}
                  </td>
                  <td class="px-4 py-4 text-center text-sm font-semibold whitespace-nowrap">
                    <StatusBadge :status="person.Status" />
                  </td>
                  <td class="px-3 py-4 text-center text-sm whitespace-nowrap text-gray-500">
                    {{ person.items ? person.items.length : 0 }}
                  </td>
                  <td class="px-4 py-4 text-right text-sm whitespace-nowrap text-gray-500">
                    {{ person.Total }}
                  </td>
                  <td class="px-4 py-4 text-right text-sm whitespace-nowrap text-theme-300">
                    <button class="text-theme-300 hover:underline" @click="openDetails(person)">
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
  </div>

  <ClaimDetailsDialog v-model="showDialog" :data="selectedPerson" />
</template>

<script setup>
import { ref, computed } from "vue";

const sortKey = ref("Date");
const sortAsc = ref(false);
const showDialog = ref(false);
const selectedPerson = ref(null);
const openDetails = (person) => {
  selectedPerson.value = person;
  showDialog.value = true;
};

const people = ref([
  {
    id: "GMD2039",
    Name: "Lindsay Walton",
    title: "Front-End Developer",
    email: "lindsay.walton@example.com",
    Date: "29/05/2025",
    Total: "85.00",
    Status: "Approved",
    remark: "Claim for essential software and professional development.",
    items: [
      {
        category: "Software License",
        date: "29/05/2025",
        merchantName: "Software Central",
        merchantAddress: "Level 2, Digital Mall, Petaling Jaya, Selangor",
        description: "Vue.js Development Tools Subscription",
        quantity: 1,
        unitPrice: 50.0,
      },
      {
        category: "Online Course",
        date: "29/05/2025",
        merchantName: "CodeAcademy Malaysia",
        merchantAddress: "Unit 10, Jaya One, Petaling Jaya, Selangor",
        description: "Advanced JavaScript & Vue.js Course",
        quantity: 1,
        unitPrice: 35.0,
      },
    ],
  },
  {
    id: "GMD2040",
    Name: "Alex Chen",
    title: "UX Designer",
    email: "alex.chen@example.com",
    Date: "30/05/2025",
    Total: "120.00",
    Status: "Pending",
    remark: "Expenses for improving design workflow and ergonomics.",
    items: [
      {
        category: "Design Software Subscription",
        date: "30/05/2025",
        merchantName: "Creative Suite MY",
        merchantAddress: "Menara TM, Jalan Pantai Baharu, Kuala Lumpur",
        description: "Adobe Creative Cloud Annual Plan",
        quantity: 1,
        unitPrice: 70.0,
      },
      {
        category: "Hardware",
        date: "30/05/2025",
        merchantName: "All IT Hypermarket",
        merchantAddress: "Low Yat Plaza, Jalan Bukit Bintang, Kuala Lumpur",
        description: "Logitech MX Master 3S Ergonomic Mouse",
        quantity: 1,
        unitPrice: 50.0,
      },
    ],
  },
  {
    id: "GMD2041",
    Name: "Sarah Johnson",
    title: "Marketing Specialist",
    email: "sarah.j@example.com",
    Date: "31/05/2025",
    Total: "65.00",
    Status: "Rejected",
    remark: "Funding for ongoing digital marketing initiatives.",
    items: [
      {
        category: "Advertising",
        date: "31/05/2025",
        merchantName: "Digital Marketing Agency (Local)",
        merchantAddress: "Level 5, The Gardens Mid Valley, Kuala Lumpur",
        description: "Social Media Ad Campaign - Q2",
        quantity: 1,
        unitPrice: 65.0,
      },
    ],
  },
  {
    id: "GMD2042",
    Name: "Michael Brown",
    title: "Graphic Designer",
    email: "michael.b@example.com",
    Date: "01/06/2025",
    Total: "45.00",
    Status: "Approved",
    remark: "Essential supplies for graphic design work.",
    items: [
      {
        category: "Subscription",
        date: "01/06/2025",
        merchantName: "Creative Stock MY",
        merchantAddress: "Online Service (Based in Malaysia)",
        description: "Local Stock Photo & Vector Subscription",
        quantity: 1,
        unitPrice: 25.0,
      },
      {
        category: "Supplies",
        date: "01/06/2025",
        merchantName: "CzipLee",
        merchantAddress: "1 Jalan Telawi 3, Bangsar, Kuala Lumpur",
        description: "Wacom Pen Nibs (Pack of 5)",
        quantity: 1,
        unitPrice: 20.0,
      },
    ],
  },
  {
    id: "GMD2043",
    Name: "Emily Wilson",
    title: "Content Writer",
    email: "emily.w@example.com",
    Date: "02/06/2025",
    Total: "90.00",
    Status: "Pending",
    remark: "Resources for content quality and research.",
    items: [
      {
        category: "Software",
        date: "02/06/2025",
        merchantName: "Language AI Solutions",
        merchantAddress: "Menara Axis, Petaling Jaya, Selangor",
        description: "Premium Grammar & Plagiarism Checker",
        quantity: 1,
        unitPrice: 40.0,
      },
      {
        category: "Book",
        date: "02/06/2025",
        merchantName: "MPH Bookstores",
        merchantAddress: "Mid Valley Megamall, Kuala Lumpur",
        description: "Essential Guide to Content Marketing",
        quantity: 1,
        unitPrice: 50.0,
      },
    ],
  },
  {
    id: "GMD2044",
    Name: "David Lee",
    title: "Photographer",
    email: "david.lee@example.com",
    Date: "03/06/2025",
    Total: "150.00",
    Status: "Approved",
    remark: "Equipment and studio rental for professional shoots.",
    items: [
      {
        category: "Equipment",
        date: "03/06/2025",
        merchantName: "Foto Shangri-La",
        merchantAddress: "Jalan Pudu, Kuala Lumpur",
        description: "Camera Lens Cleaning Kit",
        quantity: 1,
        unitPrice: 100.0,
      },
      {
        category: "Rental",
        date: "03/06/2025",
        merchantName: "Studio Rente",
        merchantAddress: "Sunway Damansara, Petaling Jaya, Selangor",
        description: "Photography Studio Rental - Half Day",
        quantity: 1,
        unitPrice: 50.0,
      },
    ],
  },
  {
    id: "GMD2045",
    Name: "Jessica Tan",
    title: "Social Media Manager",
    email: "jessica.t@example.com",
    Date: "04/06/2025",
    Total: "200.00",
    Status: "Rejected",
    remark: "Tools and ad spend for social media campaigns.",
    items: [
      {
        category: "Software",
        date: "04/06/2025",
        merchantName: "SocialReach MY",
        merchantAddress: "Online Service (Kuala Lumpur Office)",
        description: "Social Media Management Platform Subscription",
        quantity: 1,
        unitPrice: 120.0,
      },
      {
        category: "Advertising",
        date: "04/06/2025",
        merchantName: "Facebook / Instagram Ads Malaysia",
        merchantAddress: "Level 10, TRX Exchange 106, Kuala Lumpur",
        description: "Instagram Ad Campaign Budget",
        quantity: 1,
        unitPrice: 80.0,
      },
    ],
  },
  {
    id: "GMD2046",
    Name: "Ryan Wong",
    title: "Video Editor",
    email: "ryan.w@example.com",
    Date: "05/06/2025",
    Total: "350.00",
    Status: "Pending",
    remark: "Claim for video production software and assets.",
    items: [
      {
        category: "Software",
        date: "05/06/2025",
        merchantName: "ProEdit Solutions",
        merchantAddress: "Cyberjaya City Centre, Cyberjaya, Selangor",
        description: "Video Editing Software License (Annual)",
        quantity: 1,
        unitPrice: 250.0,
      },
      {
        category: "Subscription",
        date: "05/06/2025",
        merchantName: "Malay Stock Footage",
        merchantAddress: "Online Platform (Based in KL)",
        description: "Premium Stock Footage Subscription",
        quantity: 1,
        unitPrice: 100.0,
      },
    ],
  },
  {
    id: "GMD2047",
    Name: "Amanda Lim",
    title: "Event Coordinator",
    email: "amanda.l@example.com",
    Date: "06/06/2025",
    Total: "500.00",
    Status: "Approved",
    remark: "Deposits for upcoming corporate event.",
    items: [
      {
        category: "Venue",
        date: "06/06/2025",
        merchantName: "KL Convention Centre",
        merchantAddress:
          "Jalan Pinang, Kuala Lumpur City Centre, Kuala Lumpur",
        description: "Exhibition Hall Booking Deposit",
        quantity: 1,
        unitPrice: 300.0,
      },
      {
        category: "Catering",
        date: "06/06/2025",
        merchantName: "Big Plate Catering",
        merchantAddress: "Jalan PJS 11/15, Bandar Sunway, Selangor",
        description: "Event Catering Service Deposit",
        quantity: 1,
        unitPrice: 200.0,
      },
    ],
  },
  {
    id: "GMD2048",
    Name: "Daniel Koh",
    title: "Print Specialist",
    email: "daniel.k@example.com",
    Date: "07/06/2025",
    Total: "80.00",
    Status: "Pending",
    remark: "Replenishing printing supplies for the office.",
    items: [
      {
        category: "Supplies",
        date: "07/06/2025",
        merchantName: "MR. D.I.Y.",
        merchantAddress:
          "Various outlets, e.g., Mid Valley Megamall, Kuala Lumpur",
        description: "A4 Printing Paper (10 reams)",
        quantity: 10,
        unitPrice: 3.0,
      },
      {
        category: "Supplies",
        date: "07/06/2025",
        merchantName: "Inkjet Refill Store",
        merchantAddress: "Digital Mall, Petaling Jaya, Selangor",
        description: "Compatible Ink Cartridges (Multi-pack)",
        quantity: 2,
        unitPrice: 25.0,
      },
    ],
  },
  {
    id: "GMD2049",
    Name: "Michelle Ho",
    title: "Brand Strategist",
    email: "michelle.h@example.com",
    Date: "08/06/2025",
    Total: "600.00",
    Status: "Approved",
    remark: "Investment in market intelligence and team development.",
    items: [
      {
        category: "Research",
        date: "08/06/2025",
        merchantName: "Fusion Analytics MY",
        merchantAddress: "The Vertical, Bangsar South, Kuala Lumpur",
        description: "Malaysian Consumer Market Report Q1 2025",
        quantity: 1,
        unitPrice: 400.0,
      },
      {
        category: "Workshop",
        date: "08/06/2025",
        merchantName: "Local Branding Experts",
        merchantAddress: "Co-Labs Coworking, The Starling, Petaling Jaya",
        description: "Effective Brand Communication Workshop",
        quantity: 1,
        unitPrice: 200.0,
      },
    ],
  },
]);

const approvedPeople = computed(() => {
  return people.value.filter(person => person.Status == 'Approved')
})

//sort by date in descending order (default)
function parseDate(dateStr) {
  // Converts "DD/MM/YYYY" to a Date object
  const [day, month, year] = dateStr.split("/");
  return new Date(`${year}-${month}-${day}`);
}

const approvedCount = computed(() => {
  const ids = new Set(
    people.value
      .filter((e) => e.Status === "Approved")
      .map((e) => e.id),
  );
  return ids.size;
});

const rejectedCount = computed(() => {
  const ids = new Set(
    people.value
      .filter((e) => e.Status === "Rejected")
      .map((e) => e.id),
  );
  return ids.size;
});
</script>

