import { defineStore } from "pinia";
import axios from "axios";

// Interfaces
interface Invoice {
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
  item_services: any;
  remark: string;
}

interface Claim {
  id: number;
  claim_number: string;
  employee_id: number;
  claim_type: string;
  claim_amount: number;
  reason: string;
  status: string;
  submitted_date: Date;
  reviewed_date: Date;
  resolution: string;
  created_at: number;
  updated_at: number;
  Items: Invoice[];
}

// Helper function
function getClaimsWithStatus(claims: Claim[], status: string): Claim[] {
  return claims.filter((c) => c.status.toLowerCase() === status.toLowerCase());
}

export const useEmployeeClaimStore = defineStore("employeeClaim", {
  state: () => ({
    claims: [] as Claim[],
    categories: [] as string[],
    loading: false,
    error: null as string | null,
    currentEmployeeId: null as number | null,
  }),

  getters: {
    // Basic counts
    totalCount: (state) => state.claims.length,
    approvedCount: (state) => getClaimsWithStatus(state.claims, "approved").length,
    rejectedCount: (state) => getClaimsWithStatus(state.claims, "rejected").length,
    pendingCount: (state) => getClaimsWithStatus(state.claims, "pending").length,

    // Claims by status
    approvedClaims: (state) => getClaimsWithStatus(state.claims, "approved"),
    rejectedClaims: (state) => getClaimsWithStatus(state.claims, "rejected"),
    pendingClaims: (state) => getClaimsWithStatus(state.claims, "pending"),

    // Sort by date
    getClaimsByDateAsc: (state): Claim[] => {
      return [...state.claims].sort((a, b) => 
        new Date(a.submitted_date).getTime() - new Date(b.submitted_date).getTime()
      );
    },

    getClaimsByDateDesc: (state): Claim[] => {
      return [...state.claims].sort((a, b) => 
        new Date(b.submitted_date).getTime() - new Date(a.submitted_date).getTime()
      );
    },
  },

  actions: {
    // Set current employee
    setCurrentEmployee(employeeId: number) {
      this.currentEmployeeId = employeeId;
    },

    // Fetch claims by employee ID
    async fetchClaimsByEmployee(employeeId: number) {
      this.loading = true;
      this.error = null;
      
      try {
        this.currentEmployeeId = employeeId;
        const response = await axios.get<Claim[]>(
          `http://127.0.0.1:8000/employee/${employeeId}/claim/all`
        );
        this.claims = response.data;
        console.log(`Successfully fetched ${this.claims.length} claims for employee ${employeeId}`);
      } catch (error) {
        console.error("Failed to fetch employee claims:", error);
        this.error = error instanceof Error ? error.message : 'Failed to fetch claims';
        this.claims = [];
        throw error;
      } finally {
        this.loading = false;
      }
    },

    // // Create new claim
    // async createClaim(claimData: {
    //   employee_id: number;
    //   claim_type: string;
    //   claim_amount: number;
    //   reason: string;
    //   status?: string;
    // }) {
    //   this.loading = true;
    //   this.error = null;

    //   try {
    //     const response = await axios.post<Claim>(
    //       "http://127.0.0.1:8000/claims",
    //       claimData
    //     );
    //     this.claims.push(response.data);
    //     console.log('Successfully created new claim:', response.data);
    //     return response.data;
    //   } catch (error) {
    //     console.error("Failed to create claim:", error);
    //     this.error = error instanceof Error ? error.message : 'Failed to create claim';
    //     throw error;
    //   } finally {
    //     this.loading = false;
    //   }
    // },

    // // Update existing claim
    // async updateClaim(claimId: number, updates: Partial<Claim>) {
    //   this.loading = true;
    //   this.error = null;

    //   try {
    //     const response = await axios.put<Claim>(
    //       `http://127.0.0.1:8000/claims/${claimId}`,
    //       updates
    //     );
    //     const index = this.claims.findIndex(c => c.id === claimId);
    //     if (index !== -1) {
    //       this.claims[index] = response.data;
    //     }
    //     console.log('Successfully updated claim:', response.data);
    //     return response.data;
    //   } catch (error) {
    //     console.error("Failed to update claim:", error);
    //     this.error = error instanceof Error ? error.message : 'Failed to update claim';
    //     throw error;
    //   } finally {
    //     this.loading = false;
    //   }
    // },

    // // Delete claim
    // async deleteClaim(claimId: number) {
    //   this.loading = true;
    //   this.error = null;

    //   try {
    //     await axios.delete(`http://127.0.0.1:8000/claims/${claimId}`);
    //     this.claims = this.claims.filter(c => c.id !== claimId);
    //     console.log(`Successfully deleted claim ${claimId}`);
    //   } catch (error) {
    //     console.error("Failed to delete claim:", error);
    //     this.error = error instanceof Error ? error.message : 'Failed to delete claim';
    //     throw error;
    //   } finally {
    //     this.loading = false;
    //   }
    // },

    // Refresh current employee's claims
    async refreshClaims() {
      if (this.currentEmployeeId) {
        await this.fetchClaimsByEmployee(this.currentEmployeeId);
      } else {
        console.warn('No current employee ID set');
      }
    },

    // Initialize categories
    initializeCategories() {
      this.categories = [
        "All",
        "Travel Expenses",
        "Accommodation",
        "Meals and Entertainment",
        "Office Supplies and Equipment",
        "Medical Claim",
      ];
    },

    // Initialize store with employee ID
    // Initialize store with employee ID
    async initStore(employeeId: number = 2) { // Add default value
      this.initializeCategories();
      await this.fetchClaimsByEmployee(employeeId);
    },

    // Clear error
    clearError() {
      this.error = null;
    },

    // Clear all data
    clearStore() {
      this.claims = [];
      this.currentEmployeeId = null;
      this.error = null;
      this.loading = false;
    },
  },
});