<template>
  <Tab
            :tabs="[
              {
                link: '/employee/invoice/unsubmitted',
                routeName: 'Unsubmitted Invoices',
              },
              {
                link: '/employee/claim/all',
                routeName: 'All Claims',
              },
              {
                link: '/employee/claim/approved',
                routeName: 'Approved',
              },
              {
                link: '/employee/claim/rejected',
                routeName: 'Rejected',
              },
            ]"
          />
</template>


