<template>
  <div class="mx-auto my-14 w-full max-w-6xl bg-gray-100">
    <div class="mx-auto max-w-3xl">
      <div
        class="hover:shadow-3xl transform overflow-hidden rounded-xl bg-white px-20 py-6 shadow-2xl transition-all"
      >
        <!-- Card Header -->
        <div class="px-8 py-4 pb-0 text-center">
          <h2 class="text-2xl font-bold text-theme-300">
            Upload Your Receipts
          </h2>
          <p class="mt-2 text-sm text-theme-100">
            Please provide your receipt below
          </p>
        </div>

        <!-- Card Body -->
        <div class="p-2">
          <!-- Upload Box -->
          <div
            class="relative mt-2 rounded-lg border-2 border-dashed border-gray-300 p-6 py-10 transition-all duration-200 ease-in-out"
            :class="{ 'border-blue-500 bg-blue-50': isDragging }"
            @dragenter.prevent="isDragging = true"
            @dragleave.prevent="isDragging = false"
            @dragover.prevent
            @drop.prevent="handleDrop"
          >
            <div class="text-center">
              <!-- New circular upload icon -->
              <div
                class="mx-auto mb-4 flex h-20 w-20 items-center justify-center rounded-full bg-blue-100"
              >
                <svg
                  class="h-10 w-10 text-theme-100"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
                  />
                </svg>
              </div>

              <div
                class="mt-4 flex flex-col items-center justify-center space-y-3"
              >
                <p class="text-xs text-gray-400">Drop your files here or</p>
                <label
                  class="relative cursor-pointer rounded-xl bg-theme-100 px-10 py-1 text-white transition-colors duration-200 focus-within:ring-2 focus-within:ring-blue-500 focus-within:ring-offset-2 focus-within:outline-none hover:bg-theme-200"
                >
                  <span
                    class="flex items-center justify-center px-3 py-2 text-center text-xs"
                    >Browse Files</span
                  >
                  <input
                    type="file"
                    class="sr-only"
                    @change="handleFileInput"
                    accept=".pdf,.jpg,.jpeg,.png"
                    multiple
                  />
                </label>
              </div>
            </div>

            <!-- Preview section with enhanced styling -->
            <div
              v-if="selectedFiles.length > 0"
              class="mt-6 rounded-lg border border-gray-200 bg-gray-50 p-4"
            >
              <div
                v-for="(file, index) in selectedFiles"
                :key="file.name + file.size + index"
                class="flex items-center justify-between py-2"
                :class="{
                  'border-b border-gray-200': index < selectedFiles.length - 1,
                }"
              >
                <div class="flex items-center space-x-3">
                  <div class="flex-shrink-0 rounded-full bg-blue-100 p-2">
                    <svg
                      class="h-6 w-6 text-blue-600"
                      fill="currentColor"
                      viewBox="0 0 20 20"
                    >
                      <path
                        fill-rule="evenodd"
                        d="M4 4a2 2 0 012-2h8a2 2 0 012 2v12a2 2 0 01-2 2H6a2 2 0 01-2-2V4zm2 0v12h8V4H6z"
                        clip-rule="evenodd"
                      />
                    </svg>
                  </div>
                  <div>
                    <p class="text-sm font-medium text-gray-900">
                      {{ file.name }}
                    </p>
                    <p class="text-xs text-gray-500">
                      {{ formatFileSize(file.size) }}
                    </p>
                  </div>
                </div>
                <button
                  @click="removeFile(index)"
                  class="text-sm font-medium text-red-600 transition-colors duration-200 hover:text-red-800 focus:underline focus:outline-none"
                >
                  Remove
                </button>
              </div>
            </div>
          </div>

          <!-- "Supported Format" text -->
          <p class="mt-2 pt-2 text-center text-xs text-theme-100">
            Supported formats: PDF, JPEG ,JPG or PNG (max 10MB)
          </p>
          <!-- Upload and Cancel buttons -->
          <div class="mt-6 flex justify-center space-x-10">
            <button
              @click="cancelUpload"
              class="rounded-xl border-1 border-theme-300 bg-white px-10 py-2 text-xs font-medium text-theme-300 shadow-lg transition-colors duration-200 hover:bg-blue-50 focus:ring-1 focus:ring-blue-300 focus:ring-offset-2 focus:outline-none"
            >
              Cancel
            </button>
            <!-- Hardcoded here might change to dynamic later -->
            <button
              @click="uploadFile(selectedFiles)"
              class="cursor-pointer rounded-xl bg-theme-300 px-10 py-2 text-xs font-medium text-white shadow-lg transition-all duration-200 ease-in-out hover:bg-theme-300 focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
            >
              Upload
            </button>
          </div>
          <div v-if="isLoading" class="mt-4 flex justify-center text-blue-600">
            Uploading...Please wait
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { useRouter } from "vue-router";
import { ref } from "vue";
import { useEmployeeClaimStore } from "@/stores/employee-claims";

const router = useRouter();

const isDragging = ref(false);
const selectedFiles = ref([]);
const isUploading = ref(false);
const claimStore = useEmployeeClaimStore();
const isLoading = computed(() => claimStore.isLoading("uploading"));

const handleDrop = (e) => {
  isDragging.value = false;
  const files = e.dataTransfer.files;
  if (files.length) {
    selectedFiles.value.push(...Array.from(files));
  }
};

const handleFileInput = (e) => {
  const files = e.target.files;
  if (files.length) {
    selectedFiles.value.push(...Array.from(files));
  }
};

const removeFile = (indexToRemove) => {
  selectedFiles.value.splice(indexToRemove, 1);
};

const formatFileSize = (bytes) => {
  if (bytes === 0) return "0 Bytes";
  const k = 1024;
  const sizes = ["Bytes", "KB", "MB", "GB"];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + " " + sizes[i];
};

const cancelUpload = () => {
  selectedFiles.value = [];
};

const uploadFile = async (file) => {
  if (!selectedFiles.value || selectedFiles.value.length === 0) {
    alert("Please upload a file");
    return;
  }

  const formData = new FormData(); //this will give you only the first one
  for (let i = 0; i < selectedFiles.value.length; i++) {
    formData.append("files", selectedFiles.value[i]);
  }

  try {
    claimStore.startLoading("uploading");
    isUploading.value = true;
    const { data } = await axios.post(
      "http://127.0.0.1:8000/employee/analyze/invoice",
      formData,
      {
        headers: {
          accept: "application/json",
          "Content-Type": "multipart/form-data",
        },
      },
    );

    console.log("Raw answers:", data.answers);
    const combinedItems = [];
    let firstValid = null;

    let merchant_Names = [];
    let merchant_Addresses = [];
    let remarks = [];

    for (const result of data.answers) {
      if (!result || result.error || !result.items) continue;

      if (result.merchant_name) merchant_Names.push(result.merchant_name);
      if (result.merchant_address)
        merchant_Addresses.push(result.merchant_address);
      if (result.remark) remarks.push(result.remark);

      if (!firstValid) {
        firstValid = result;
      }

      combinedItems.push(...result.items);
    }

    const mergedNames = merchant_Names.join(" | ");
    const mergedAddresses = merchant_Addresses.join(" | ");
    const mergedremarks = remarks.join(" | ");

    router.push({
      path: "/employee/claim/edit",
      query: {
        category: firstValid.category,
        date: firstValid.date,
        merchantName: mergedNames,
        merchantAddress: mergedAddresses,
        remark: mergedremarks,
        items: JSON.stringify(combinedItems),
      },
    });
  } catch (err) {
    console.error("Upload failed:", err);
    alert("LLM analysis unsuccessful");
  } finally {
    claimStore.stopLoading("uploading");
    isUploading.value = false;
  }
};
</script>
