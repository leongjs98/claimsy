import axios from "axios";
import { defineStore } from "pinia";

interface PolicySection {
  title: string;
  points: string[];
}

interface ClaimPolicyDetails {
  validCriteria: string[]; // Direct array to match backend response
  claim_approval_limitations: PolicySection[];
  claim_denial: PolicySection[];
}

interface PolicyStore {
  claimPolicies: ClaimPolicyDetails | null;
  loading: boolean;
  error: string | null;
  hasChanged: boolean;
}

export const usePolicyDetails = defineStore("get_policy_details", {
  state: (): PolicyStore => ({
    claimPolicies: null,
    loading: false,
    error: null,
    hasChanged: false,
  }),

  getters: {
    // Get claim eligibility criteria as formatted string for textarea
    validClaimCriteriaText: (state) => {
      if (!state.claimPolicies?.validCriteria) return "";
      return state.claimPolicies.validCriteria
        .map((criteria) => `- ${criteria}`)
        .join("\n");
    },

    // Get first approval limitations section as formatted string
    approvalLimitations1Text: (state) => {
      const section = state.claimPolicies?.claim_approval_limitations?.[0];
      if (!section?.points) return "";
      return section.points.map((point) => `- ${point}`).join("\n");
    },

    // Get second approval limitations section as formatted string (if exists)
    approvalLimitations2Text: (state) => {
      const section = state.claimPolicies?.claim_approval_limitations?.[1];
      if (!section?.points) return "";
      return section.points.map((point) => `- ${point}`).join("\n");
    },

    // Get first claim denial section as formatted string
    claimDenial1Text: (state) => {
      const section = state.claimPolicies?.claim_denial?.[0];
      if (!section?.points) return "";
      return section.points.map((point) => `- ${point}`).join("\n");
    },

    // Get second claim denial section as formatted string (if exists)
    claimDenial2Text: (state) => {
      const section = state.claimPolicies?.claim_denial?.[1];
      if (!section?.points) return "";
      return section.points.map((point) => `- ${point}`).join("\n");
    },

    // Check if policies are loaded
    isPoliciesLoaded: (state) => {
      return state.claimPolicies !== null;
    },
  },

  actions: {
    // Fetch claim policies from backend
    async fetchPolicies() {
      this.loading = true;
      this.error = null;

      try {
        const response = await axios.get("http://127.0.0.1:8000/admin/policy");

        // Store the exact response structure from your Python backend
        this.claimPolicies = {
          validCriteria: response.data.validClaimCriteria || [],
          claim_approval_limitations:
            response.data.claim_approval_limitations || [],
          claim_denial: response.data.claim_denial || [],
        };
      } catch (error) {
        this.error =
          error instanceof Error ? error.message : "Failed to fetch policies";
        console.error("Error fetching policies:", error);
      } finally {
        this.loading = false;
      }
    },

    // Update policies (for when user submits the form)
    async updatePolicies(updatedData: {
      validClaimCriteria: string;
      approvalLimitations1: string;
      claimDenial1: string;
      approvalLimitations2?: string;
      claimDenial2?: string;
    }) {
      this.loading = true;
      this.error = null;

      try {
        // Convert textarea strings back to arrays
        const payload = {
          validClaimCriteria: updatedData.validClaimCriteria
            .split("\n")
            .map((line) => line.replace(/^-\s*/, "").trim())
            .filter((line) => line.length > 0),

          claim_approval_limitations: [
            {
              title: "Claim Approval & Limitations",
              points: updatedData.approvalLimitations1
                .split("\n")
                .map((line) => line.replace(/^-\s*/, "").trim())
                .filter((line) => line.length > 0),
            },
          ],

          claim_denial: [
            {
              title: "Claim Denial",
              points: updatedData.claimDenial1
                .split("\n")
                .map((line) => line.replace(/^-\s*/, "").trim())
                .filter((line) => line.length > 0),
            },
          ],
        };

        // Add second sections if they exist
        if (updatedData.approvalLimitations2?.trim()) {
          payload.claim_approval_limitations.push({
            title: "Additional Approval Limitations",
            points: updatedData.approvalLimitations2
              .split("\n")
              .map((line) => line.replace(/^-\s*/, "").trim())
              .filter((line) => line.length > 0),
          });
        }

        if (updatedData.claimDenial2?.trim()) {
          payload.claim_denial.push({
            title: "Additional Claim Denial Conditions",
            points: updatedData.claimDenial2
              .split("\n")
              .map((line) => line.replace(/^-\s*/, "").trim())
              .filter((line) => line.length > 0),
          });
        }

        // Send PUT/POST request to update policies
        const response = await axios.put(
          "http://127.0.0.1:8000/admin/policy",
          payload,
        );

        // Update local state
        this.claimPolicies = response.data;
        this.hasChanged = false;
      } catch (error) {
        this.error =
          error instanceof Error ? error.message : "Failed to update policies";
        console.error("Error updating policies:", error);
        throw error; // Re-throw so component can handle it
      } finally {
        this.loading = false;
      }
    },

    // Mark as changed when user edits
    markAsChanged() {
      this.hasChanged = true;
    },

    // Reset error state
    clearError() {
      this.error = null;
    },

    // Reset all state
    resetState() {
      this.claimPolicies = null;
      this.loading = false;
      this.error = null;
      this.hasChanged = false;
    },
  },
});

// Export types for use in components
export type { ClaimPolicyDetails, PolicySection };
