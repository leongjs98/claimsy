import { defineStore } from "pinia";

interface Expense {
  Id: string;
  Name: string;
  Category: string;
  Date: string;
  Quantity: number;
  Remark: string;
  Total: number;
  Status: string;
}

export const useEmployeeClaimStore = defineStore("employeeClaim", {
  state: () => ({
    expenses: [] as Expense[],
    categories: [] as string[],
  }),

  getters: {
    totalCount: (state) => state.expenses.length,

    approvedCount: (state) =>
      state.expenses.filter(
        (expense) => expense.Status.toLowerCase() === "approved",
      ).length,

    rejectedCount: (state) =>
      state.expenses.filter(
        (expense) => expense.Status.toLowerCase() === "rejected",
      ).length,

    getExpensesByDateAsc: (state): Expense[] => {
      return [...state.expenses].sort((a, b) => {
        const dateA = new Date(a.Date.split("/").reverse().join("-"));
        const dateB = new Date(b.Date.split("/").reverse().join("-"));
        return dateA.getTime() - dateB.getTime();
      });
    },

    getExpensesByDateDesc: (state): Expense[] => {
      return [...state.expenses].sort((a, b) => {
        const dateA = new Date(a.Date.split("/").reverse().join("-"));
        const dateB = new Date(b.Date.split("/").reverse().join("-"));
        return dateB.getTime() - dateA.getTime();
      });
    },
  },

  actions: {
    initializeExpenses() {
      this.expenses = [
        {
          Id: "C0001",
          Name: "Laptop",
          Category: "Office Supplies and Equipment",
          Date: "30/01/2025",
          Quantity: 6,
          Remark: "Dell 1.35GHz 8GB 256GB SSD - for new employee sasascdavadfa",
          Total: 48285.0,
          Status: "Approved",
        },
        {
          Id: "C0002",
          Name: "Whiteboard 4x6ft",
          Category: "Office Supplies and Equipment",
          Date: "21/02/2025",
          Quantity: 2,
          Remark: "for training room",
          Total: 1200.0,
          Status: "Approved",
        },
        {
          Id: "C0003",
          Name: "Meeting at Damansara",
          Category: "Travel Expenses",
          Date: "29/03/2025",
          Quantity: 1,
          Remark: "Lunch with client",
          Total: 150.0,
          Status: "Rejected",
        },
        {
          Id: "C0004",
          Name: "Lunch",
          Category: "Meals and Entertainment",
          Date: "29/03/2025",
          Quantity: 10,
          Remark: "team lunch",
          Total: 250.0,
          Status: "Rejected",
        },
        {
          Id: "C0005",
          Name: "Dinner",
          Category: "Meals and Entertainment",
          Date: "18/05/2025",
          Quantity: 6,
          Remark: "Sales team dinner",
          Total: 138.0,
          Status: "Rejected",
        },
        {
          Id: "C0006",
          Name: "Stationery",
          Category: "Office Supplies and Equipment",
          Date: "12/06/2025",
          Quantity: 15,
          Remark: "for new employee",
          Total: 1000.0,
          Status: "Approved",
        },
        {
          Id: "C0007",
          Name: "Flight to Penang",
          Category: "Travel Expenses",
          Date: "29/07/2025",
          Quantity: 2,
          Remark: "Flight tickets for conference",
          Total: 1200.0,
          Status: "Approved",
        },
        {
          Id: "C0008",
          Name: "Hotel at Penang",
          Category: "Accomodation",
          Date: "29/08/2025",
          Quantity: 2,
          Remark: "Company conference",
          Total: 2500.0,
          Status: "Pending",
        },
      ];

      this.getExpensesByDateAsc;
    },

    initializeCategories() {
      this.categories = [
        "All",
        "Travel Expenses",
        "Accomodation",
        "Meals and Entertainment",
        "Office Supplies and Equipment",
        "Medical Claim",
      ];
    },

    initStore() {
      this.initializeExpenses();
      this.initializeCategories();
    },
  },
});
