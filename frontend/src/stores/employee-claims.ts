import { defineStore } from "pinia";
import axios from "axios";

// Interfaces
interface ItemService {
  item: string;
  quantity: number;
  unit_price: number;
}

function sortClaimsByDate(claims: ClaimResponseSchema[], ascending: boolean) {
  if (ascending) {
    return [...claims].sort(
      (a, b) =>
        new Date(a.submitted_date).getTime() -
        new Date(b.submitted_date).getTime(),
    );
  } else {
    return [...claims].sort(
      (a, b) =>
        new Date(b.submitted_date).getTime() -
        new Date(a.submitted_date).getTime(),
    );
  }
}

type ClaimStatusType = "pending" | "approved" | "rejected";

interface EmployeeScheme {
  employee_id?: string;
  name?: string;
  email?: string;
  department?: string;
}

interface InvoiceResponseSchema {
  id: number;
  invoice_id: number;
  invoice_number: string;
  invoice_date: Date;
  claim_id: number;
  employee_id: number;
  created_at: number;
  updated_at: number;
  category: string;
  merchant_name: string;
  merchant_address: string;
  itemsServices: ItemService[];
  remark: string;
  employee?: EmployeeScheme;
}

interface ClaimResponseSchema {
  id: number;
  claim_number: string;
  employee_id: number;
  claim_type: string;
  reason: string;
  status: ClaimStatusType;
  submitted_date: Date;
  reviewed_date: Date;
  resolution: string;
  created_at: number;
  updated_at: number;
  invoices: InvoiceResponseSchema[];
  employee?: EmployeeScheme;
  is_anomaly: boolean;
  total: number;
}

// Helper function
function getClaimsWithStatus(claims: ClaimResponseSchema[], status: string): ClaimResponseSchema[] {
  return claims.filter((c) => c.status.toLowerCase() === status.toLowerCase());
}

export const useEmployeeClaimStore = defineStore("employeeClaim", {
  state: () => ({
    claims: [] as ClaimResponseSchema[],
    invoices: [] as InvoiceResponseSchema[],
    claimInvoices: [] as InvoiceResponseSchema[],
    // categories: [] as string[],
    isLoading: false,
    error: null as string | null,
    currentEmployeeId: null as number | null,
  }),

  getters: {
    // Basic counts
    totalCount: (state) => state.claims.length,
    approvedCount: (state) =>
      getClaimsWithStatus(state.claims, "approved").length,
    rejectedCount: (state) =>
      getClaimsWithStatus(state.claims, "rejected").length,
    pendingCount: (state) =>
      getClaimsWithStatus(state.claims, "pending").length,

    // Claims by status
    approvedClaims: (state) => getClaimsWithStatus(state.claims, "approved"),
    rejectedClaims: (state) => getClaimsWithStatus(state.claims, "rejected"),
    pendingClaims: (state) => getClaimsWithStatus(state.claims, "pending"),

    // Sort by date
    getClaimsSortedByDate: (state) => (isAscending: boolean) =>
      sortClaimsByDate(state.claims, isAscending),
    getApprovedClaimsSortedByDate: (state) => (isAscending: boolean) =>
      sortClaimsByDate(
        getClaimsWithStatus(state.claims, "approved"),
        isAscending,
      ),
    getRejectedClaimsSortedByDate: (state) => (isAscending: boolean) =>
      sortClaimsByDate(
        getClaimsWithStatus(state.claims, "rejected"),
        isAscending,
      ),

    // getClaimsByDateAsc: (state): ClaimResponseSchema[] => {
    //   return [...state.claims].sort(
    //     (a, b) =>
    //       new Date(a.submitted_date).getTime() -
    //       new Date(b.submitted_date).getTime(),
    //   );
    // },
    // getClaimsByDateDesc: (state): ClaimResponseSchema[] => {
    //   return [...state.claims].sort(
    //     (a, b) =>
    //       new Date(b.submitted_date).getTime() -
    //       new Date(a.submitted_date).getTime(),
    //   );
    // },

    // aisya-category
    categories: (state) => {
      const uniqueCategories = new Set<string>();
      uniqueCategories.add("All"); // Always include 'All' option
      state.invoices.forEach((invoice) => {
        if (invoice.category) {
          // Ensure the category property exists
          uniqueCategories.add(invoice.category);
        }
      });
      return Array.from(uniqueCategories);
    },

    getInvoicesByClaimId: (state) => (claimId: number) => {
      return state.invoices.filter((invoice) => invoice.claim_id === claimId);
    },
  },

  actions: {
    // Set current employee
    setCurrentEmployee(employeeId: number) {
      this.currentEmployeeId = employeeId;
    },

    // sho - pinia store to fetch unsubmitted invoice
    async fetchUnsubmittedInvoices(employeeId: number) {
      this.isLoading = true;
      try {
        const response = await axios.get<InvoiceResponseSchema[]>(
          `http://127.0.0.1:8000/employee/${employeeId}/invoice/unsubmitted`,
        );
        this.invoices = Array.isArray(response.data) ? response.data : [];
      } catch (error) {
        this.error = "Failed to load unsubmitted invoices.";
        this.invoices = [];
      } finally {
        this.isLoading = false;
      }
    },

    //aisya
    async submitInvoicesIntoClaim(
      employeeId: number,
      invoiceIds: number[],
      claimType: string,
      reason: string,
    ) {
      this.isLoading = true;
      try {
        const response = await axios.post(
          `http://127.0.0.1:8000/employee/${employeeId}/invoice/submit-into-claim`,
          {
            invoice_ids: invoiceIds,
            claim_type: claimType,
            reason: reason,
          },
        );

        // Refresh the invoices list after successful submission
        await this.fetchUnsubmittedInvoices(employeeId);

        return response.data; // Return the created claim
      } catch (error) {
        this.error = "Failed to submit claim.";
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    // aisya - Fetch claims by employee ID
    async fetchClaimsByEmployee(employeeId: number) {
      this.isLoading = true;
      this.error = null;

      try {
        this.currentEmployeeId = employeeId;
        const response = await axios.get<ClaimResponseSchema[]>(
          `http://127.0.0.1:8000/employee/${employeeId}/claim/all`,
        );
        this.claims = response.data;
    for (const claim of this.claims) {
      let claimTotal = 0;

      for (const invoice of claim.invoices) {
        let invoiceTotal = 0;

        for (const item of invoice.itemsServices) {
          invoiceTotal += item.quantity * item.unit_price;
        }

        claimTotal += invoiceTotal;
      }

      // Add the total to the claim object
      claim.total = claimTotal;
    }
        // console.log(`Successfully fetched ${this.claims.length} claims for employee ${employeeId}`);
      } catch (error) {
        console.error("Failed to fetch employee claims:", error);
        this.error =
          error instanceof Error ? error.message : "Failed to fetch claims";
        this.claims = [];
        throw error;
      } finally {
        this.isLoading = false;
      }

      this.totalCount;
      this.approvedCount;
      this.rejectedCount;
    },

    async fetchInvoicesByClaimId(claimId: number) {
      this.isLoading = true;
      this.error = null;

      try {
        const response = await axios.get<InvoiceResponseSchema[]>(
          `http://127.0.0.1:8000/employee/${claimId}/invoice/all`,
        );
        this.claimInvoices = Array.isArray(response.data) ? response.data : [];
        return this.claimInvoices;
      } catch (error) {
        this.error = "Failed to load claim invoices.";
        this.claimInvoices = [];
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    // Refresh current employee's claims
    async refreshClaims() {
      if (this.currentEmployeeId) {
        await this.fetchClaimsByEmployee(this.currentEmployeeId);
      } else {
        console.warn("No current employee ID set");
      }
    },

    // sho - changing the initStore to fetch claims by employee ID = 1
    async initStore(employeeId: number) {
      this.isLoading = true;
      try {
        this.fetchClaimsByEmployee(employeeId)
      } catch (error) {
        this.error = "Failed to load claims.";
        console.error(error);
        this.claims = [];
      } finally {
        this.isLoading = false;
      }
    },
    // until here --------------

    // Clear error
    clearError() {
      this.error = null;
    },

    // Clear all data
    clearStore() {
      this.claims = [];
      this.invoices = [];
      this.claimInvoices = [];
      this.currentEmployeeId = null;
      this.error = null;
      this.isLoading = false;
    },
  },
});
