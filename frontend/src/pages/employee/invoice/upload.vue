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
                  >
                    Browse Files
                  </span>
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
                v-for="(fileEntry, index) in selectedFiles"
                :key="fileEntry.file.name + fileEntry.file.size + index"
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
                      {{ fileEntry.file.name }}
                    </p>
                    <p class="text-xs text-gray-500">
                      {{ formatFileSize(fileEntry.file.size) }}
                    </p>
                  </div>
                </div>
                <div class="flex items-center space-x-2">
                  <button
                    @click="showReceiptPreview(fileEntry)"
                    class="rounded-full p-1 text-blue-600 hover:bg-blue-100 focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 focus:outline-none"
                    title="View Receipt"
                  >
                    <span class="sr-only">View Receipt</span>
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke-width="1.5"
                      stroke="currentColor"
                      class="h-5 w-5"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        d="M2.25 12s3.75-6.75 9.75-6.75S21.75 12 21.75 12s-3.75 6.75-9.75 6.75S2.25 12 2.25 12z"
                      />
                      <circle
                        cx="12"
                        cy="12"
                        r="3"
                        fill="currentColor"
                        stroke="currentColor"
                        stroke-width="1.5"
                      />
                    </svg>
                  </button>
                  <button
                    @click="removeFile(index)"
                    class="rounded-full p-1 text-red-600 hover:bg-red-100 focus:ring-2 focus:ring-red-500 focus:ring-offset-2 focus:outline-none"
                    title="Remove File"
                  >
                    <span class="sr-only">Remove File</span>
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke-width="1.5"
                      stroke="currentColor"
                      class="h-5 w-5"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        d="M6 7h12M9 7V5a3 3 0 0 1 6 0v2m-9 0h12v12a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V7z"
                      />
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        d="M10 11v6m4-6v6"
                      />
                    </svg>
                  </button>
                </div>
              </div>
            </div>
          </div>

          <!-- "Supported Format" text -->
          <p class="mt-2 pt-2 text-center text-xs text-theme-100">
            Supported formats: PDF, JPEG ,JPG or PNG (max 10MB)
          </p>
          <!-- Upload and Cancel buttons -->
          <div class="mt-6 flex items-center justify-center gap-10">
            <SecondaryButton @click="cancelUpload"> Cancel </SecondaryButton>
            <span class="flex items-center justify-center gap-2">
              <PrimaryButton @click="uploadFile()">
                <span v-if="isLoading"> Processing... </span>
                <span v-else> Upload </span>
              </PrimaryButton>
              <svg
                v-if="isLoading"
                class="size-5 animate-spin"
                xmlns="http://www.w3.org/2000/svg"
                width="32"
                height="32"
                viewBox="0 0 24 24"
              >
                <g fill="none" fill-rule="evenodd">
                  <path
                    d="m12.593 23.258l-.011.002l-.071.035l-.02.004l-.014-.004l-.071-.035q-.016-.005-.024.005l-.004.01l-.017.428l.005.02l.01.013l.104.074l.015.004l.012-.004l.104-.074l.012-.016l.004-.017l-.017-.427q-.004-.016-.017-.018m.265-.113l-.013.002l-.185.093l-.01.01l-.003.011l.018.43l.005.012l.008.007l.201.093q.019.005.029-.008l.004-.014l-.034-.614q-.005-.018-.02-.022m-.715.002a.02.02 0 0 0-.027.006l-.006.014l-.034.614q.001.018.017.024l.015-.002l.201-.093l.01-.008l.004-.011l.017-.43l-.003-.012l-.01-.01z"
                  />
                  <path
                    fill="currentColor"
                    d="M12 4.5a7.5 7.5 0 1 0 0 15a7.5 7.5 0 0 0 0-15M1.5 12C1.5 6.201 6.201 1.5 12 1.5S22.5 6.201 22.5 12S17.799 22.5 12 22.5S1.5 17.799 1.5 12"
                    opacity=".1"
                  />
                  <path
                    fill="currentColor"
                    d="M12 4.5a7.46 7.46 0 0 0-5.187 2.083a1.5 1.5 0 0 1-2.075-2.166A10.46 10.46 0 0 1 12 1.5a1.5 1.5 0 0 1 0 3"
                  />
                </g>
              </svg>
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- Receipt View Modal -->
    <v-dialog v-model="showModal" width="850" height="1000">
      <v-card class="flex h-full flex-col rounded-lg shadow-lg">
        <div class="mt-6 flex items-center justify-between px-8">
          <h2 class="text-lg font-semibold text-gray-900">
            {{ currentViewedFile?.file.name }}
          </h2>
          <button
            @click="closeModal"
            class="ml-2 flex items-center justify-center rounded-full p-1 hover:bg-red-600"
            style="width: 32px; height: 32px"
            title="Close"
          >
            <span class="sr-only">Close</span>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="h-5 w-5 text-red-600"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M6 18 18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>
        <div class="flex-1 items-center justify-center overflow-auto p-6">
          <iframe
            v-if="
              currentViewedFile?.type === 'image' &&
              currentViewedFile?.previewUrl
            "
            :src="currentViewedFile.previewUrl"
            class="h-full w-full rounded"
          ></iframe>
          <iframe
            v-else-if="
              currentViewedFile?.type === 'pdf' && currentViewedFile?.previewUrl
            "
            :src="currentViewedFile.previewUrl"
            class="h-full w-full rounded"
          ></iframe>
          <div
            v-else
            class="flex h-full items-center justify-center text-gray-500"
          >
            <p>Cannot display preview for this file type.</p>
          </div>
        </div>
      </v-card>
    </v-dialog>
  </div>
</template>

<script setup>
  import axios from "axios";
  import { useRouter } from "vue-router";
  import { ref, computed, onBeforeUnmount } from "vue";
  import { useEmployeeClaimStore } from "@/stores/employee-claims";

  const router = useRouter();

  const isDragging = ref(false);
  const selectedFiles = ref([]);
  const claimStore = useEmployeeClaimStore();
  const isLoading = computed(() => claimStore.isLoading("uploading"));

  // State for the modal
  const showModal = ref(false);
  const currentViewedFile = ref(null);
  const MAX_FILE_SIZE_BYTES = 10 * 1024 * 1024; // 10MB

  // Helper function to process files (validation and preview URL creation)
  const processFiles = (files) => {
    const processed = [];
    for (const file of files) {
      const fileType = file.type;
      const fileName = file.name;

      // Validate file type
      if (
        !["application/pdf", "image/jpeg", "image/png"].includes(fileType) &&
        !fileName.toLowerCase().endsWith(".jpg") // Catch .jpg if mime type is generic
      ) {
        alert(
          `File "${fileName}" is not a supported format. Please upload PDF, JPEG, JPG, or PNG.`,
        );
        continue;
      }

      // Validate file size
      if (file.size > MAX_FILE_SIZE_BYTES) {
        alert(
          `File "${fileName}" exceeds the maximum size of 10MB. Please upload a smaller file.`,
        );
        continue;
      }

      let previewUrl = null;
      let type = "other";

      // Create object URL for both images and PDFs for modal viewing
      if (fileType.startsWith("image/")) {
        previewUrl = URL.createObjectURL(file);
        type = "image";
      } else if (fileType === "application/pdf") {
        previewUrl = URL.createObjectURL(file);
        type = "pdf";
      }

      processed.push({ file, type, previewUrl });
    }
    return processed;
  };

  const handleDrop = (e) => {
    isDragging.value = false;
    const files = e.dataTransfer.files;
    if (files.length) {
      selectedFiles.value.push(...processFiles(Array.from(files)));
    }
  };

  const handleFileInput = (e) => {
    const files = e.target.files;
    if (files.length) {
      selectedFiles.value.push(...processFiles(Array.from(files)));
      // Clear the input to allow selecting the same file again if needed
      e.target.value = "";
    }
  };

  const removeFile = (indexToRemove) => {
    const fileEntry = selectedFiles.value[indexToRemove];
    // Revoke the object URL to free up memory
    if (fileEntry && fileEntry.previewUrl) {
      URL.revokeObjectURL(fileEntry.previewUrl);
    }
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
    // Revoke all object URLs before clearing the array
    selectedFiles.value.forEach((fileEntry) => {
      if (fileEntry.previewUrl) {
        URL.revokeObjectURL(fileEntry.previewUrl);
      }
    });
    selectedFiles.value = [];
    closeModal(); // Close modal if open
  };

  // Functions for modal
  const showReceiptPreview = (fileEntry) => {
    currentViewedFile.value = fileEntry;
    showModal.value = true;
  };

  const closeModal = () => {
    showModal.value = false;
    currentViewedFile.value = null;
  };

  const uploadFile = async () => {
    if (!selectedFiles.value || selectedFiles.value.length === 0) {
      alert("Please select at least one file to upload.");
      return;
    }

    const formData = new FormData();
    selectedFiles.value.forEach((fileEntry) => {
      formData.append("files", fileEntry.file); // Append the actual File object
    });

    try {
      claimStore.startLoading("uploading");
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
      const itemsServices = [];
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

        const mergedNames = merchant_Names.join(" | ");
        const mergedAddresses = merchant_Addresses.join(" | ");
        const mergedremarks = remarks.join(" | ");
        itemsServices.push(...result.items);

        // Ensure firstValid exists before navigating
        if (firstValid) {
          router.push({
            path: "/employee/invoice/edit/first",
            query: {
              category: firstValid.category,
              date: firstValid.date,
              merchantName: mergedNames,
              merchantAddress: mergedAddresses,
              remark: mergedremarks,
              items: JSON.stringify(itemsServices),
            },
          });
        } else {
          alert("No valid invoice data was extracted from the uploaded files.");
        }
      }
    } catch (err) {
      console.error("Upload failed:", err);
      alert(
        "LLM analysis unsuccessful. Please try again or upload different files.",
      );
    } finally {
      claimStore.stopLoading("uploading");
      // Clear files after successful or failed upload attempt
      cancelUpload();
    }
  };

  // Lifecycle hook to clean up object URLs when the component is unmounted
  onBeforeUnmount(() => {
    cancelUpload(); // This will revoke all URLs and close modal
  });
</script>
