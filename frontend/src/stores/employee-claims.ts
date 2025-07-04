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
  Items: {
    category: string;
    date: string;
    merchantName: string;
    merchantAddress: string;
    description: string;
    quantity: number;
    unitPrice: number;
  }[];
}

// TODO: complete these functions
function getClaimsWithStatus(claims, status) {}
function getClaimsWithDateSorted(claims, ascending) {}
function getClaimsWithPriceSorted(claims, ascending) {}

export const useEmployeeClaimStore = defineStore("employeeClaim", {
  state: () => ({
    expenses: [] as Expense[],
    categories: [] as string[],
    loadArr: [] as Array<string>,
  }),

  getters: {
    isLoading: (state) => (task: string) => state.loadArr.includes(task),
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
    startLoading(task: string) {
      if (!this.loadArr.includes(task)) {
        this.loadArr.push(task);
      }
    },

    stopLoading(task: string) {
      this.loadArr = this.loadArr.filter((t) => t !== task);
    },
  },
});
