import { defineStore } from "pinia";
import axios from "axios";

interface ItemService {
  item: string;
  quantity: number;
  unit_price: number;
}

interface InvoiceResponseSchema {
  id?: number;
  invoiceId: number;
  invoiceNumber: string;
  claimId?: number;
  employeeId: number;
  invoiceDate: string;
  category?: string;
  merchantName?: string;
  merchantAddress?: string;
  itemsServices: ItemService[];
  remark?: string;
  employee?: EmployeeScheme;
}

type ClaimStatusType = "pending" | "approved" | "rejected";

interface EmployeeScheme {
  employee_id?: string;
  name?: string;
  email?: string;
  department?: string;
}

interface ClaimResponseSchema {
  id: number;
  claim_number: string;
  employee_id: number;
  claim_type?: string;
  claim_amount?: number;
  reason?: string;
  status: ClaimStatusType;
  submitted_date?: string;
  reviewed_date?: string;
  resolution?: string;
  created_at: string;
  updated_at: string;
  invoices: InvoiceResponseSchema[];
  employee?: EmployeeScheme;
  // is_anomaly?: boolean; // Uncomment if added to backend ClaimSchema
  // is_fraud?: boolean;   // Uncomment if added to backend ClaimSchema
}

function filterClaimsByStatus(
  claims: ClaimResponseSchema[],
  status: string,
): ClaimResponseSchema[] {
  return claims.filter(
    (claim) => claim.status?.toLowerCase() === status.toLowerCase(),
  );
}

function sortClaimsByDate(
  claims: ClaimResponseSchema[],
  ascending: boolean,
): ClaimResponseSchema[] {
  return [...claims].sort((a, b) => {
    const dateA = a.submitted_date ? new Date(a.submitted_date) : new Date(0);
    const dateB = b.submitted_date ? new Date(b.submitted_date) : new Date(0);
    return ascending
      ? dateA.getTime() - dateB.getTime()
      : dateB.getTime() - dateA.getTime();
  });
}

function sortClaimsByAmount(
  claims: ClaimResponseSchema[],
  ascending: boolean,
): ClaimResponseSchema[] {
  return [...claims].sort((a, b) => {
    const amountA = a.claim_amount || 0;
    const amountB = b.claim_amount || 0;
    return ascending ? amountA - amountB : amountB - amountA;
  });
}

export const useAdminClaimStore = defineStore("adminClaim", {
  state: () => ({
    claims: [] as ClaimResponseSchema[],
  }),

  getters: {
    totalClaimCount: (state) => state.claims.length,

    approvedClaimsCount: (state) =>
      filterClaimsByStatus(state.claims, "approved").length,
    rejectedClaimsCount: (state) =>
      filterClaimsByStatus(state.claims, "rejected").length,
    pendingClaimsCount: (state) =>
      filterClaimsByStatus(state.claims, "pending").length,

    getApprovedClaims: (state) =>
      filterClaimsByStatus(state.claims, "approved"),
    getRejectedClaims: (state) =>
      filterClaimsByStatus(state.claims, "rejected"),
    getPendingClaims: (state) => filterClaimsByStatus(state.claims, "pending"),
    getClaimsByStatus: (state) => (status: ClaimStatusType | string) =>
      filterClaimsByStatus(state.claims, status),

    getClaimsSortedByDate: (state) => (ascending: boolean) =>
      sortClaimsByDate(state.claims, ascending),
    getClaimsSortedByAmount: (state) => (ascending: boolean) =>
      sortClaimsByAmount(state.claims, ascending),
  },

  actions: {
    async fetchAdminClaims() {
      try {
        const response = await axios.get<ClaimResponseSchema[]>(
          "http://localhost:8000/admin/claim/all",
        );
        this.claims = response.data;
      } catch (error) {
        console.error("Failed to fetch all admin claims:", error);
        this.claims = [];
        throw error;
      }
    },

    async fetchClaimDetails(claimId: number): Promise<ClaimResponseSchema> {
      try {
        const response = await axios.get<ClaimResponseSchema>(
          `http://localhost:8000/admin/claim/${claimId}/details`,
        );
        return response.data;
      } catch (error) {
        console.error(`Failed to fetch details for claim ${claimId}:`, error);
        throw error;
      }
    },

    async fetchInvoiceDetails(
      invoiceId: number,
    ): Promise<InvoiceResponseSchema> {
      try {
        const response = await axios.get<InvoiceResponseSchema>(
          `http://localhost:8000/admin/invoice/${invoiceId}`,
        );
        return response.data;
      } catch (error) {
        console.error(
          `Failed to fetch details for invoice ${invoiceId}:`,
          error,
        );
        throw error;
      }
    },

    async resolveClaim(
      claimId: number,
      approved: boolean,
    ): Promise<ClaimResponseSchema> {
      try {
        const response = await axios.post<ClaimResponseSchema>(
          `http://localhost:8000/admin/claim/${claimId}/resolve/${approved}`,
        );
        const updatedClaim = response.data;

        const index = this.claims.findIndex((claim) => claim.id === claimId);
        if (index !== -1) {
          this.claims[index] = updatedClaim;
        } else {
          console.warn(
            `Resolved claim ${claimId} not found in store after update. Re-fetching all claims.`,
          );
          await this.fetchAdminClaims();
        }
        return updatedClaim;
      } catch (error) {
        console.error(`Failed to resolve claim ${claimId}:`, error);
        throw error;
      }
    },

    async initializeAdminClaimStore() {
      await this.fetchAdminClaims();
    },
  },
});
