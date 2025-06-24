import { defineStore } from 'pinia';
import axios from 'axios';

interface ItemService {
  description: string
  quantity: number
  unit_price: number
  total: number
}

interface Invoice {
    invoice_id: number;
    invoice_number: string
    invoice_date: string 
    created_at: string 
    updated_at: string 
    category: string
    merchant_name: string
    merchant_address: string
    items_services: ItemService[] 
    remark: string | null 
}

const API_BASE_URL = 'http://localhost:8000/admin/claim/details';

export const useInvoiceStore = defineStore('invoice', {
  state: () => ({
    invoice: null as Invoice | null, 
    loading: false,
    error: null as string | null,
  }),
 
  actions: {
    async fetchInvoice(invoiceId: number) {
      this.loading = true;
      this.error = null;
      try {
        const response = await axios.get(`${API_BASE_URL}/${invoiceId}`); 
        this.invoice = response.data;
      } catch (error: any) {
        if (error.response) {
          this.error = error.response.data.detail || 'Failed to fetch invoice.';
        } else if (error.request) {
          this.error = 'No response from server. Check your network or backend.';
        } else {
          this.error = 'Error setting up the request: ' + error.message;
        }
        console.error('Error fetching invoice:', error);
      } finally {
        this.loading = false;
      }
    },
  },
  getters: {
    formattedInvoiceDate: (state) => {
      if (state.invoice && state.invoice.invoice_date) {
        const dateObj = new Date(state.invoice.invoice_date);
        return dateObj.toLocaleDateString('en-MY', {
          day: '2-digit',
          month: '2-digit',
          year: 'numeric',
        });
      }
      return '';
    },
    totalAmount: (state) => {
      if (state.invoice && state.invoice.items_services) {
        return state.invoice.items_services.reduce(
          (sum, item) => sum + item.quantity * item.unit_price,
          0,
        ).toLocaleString("en-MY", {
          minimumFractionDigits: 2,
          maximumFractionDigits: 2,
        });
      }
      return '0.00';
    },
  },
});