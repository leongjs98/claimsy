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
              <!-- Circular upload icon -->
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
                  class="relative cursor-pointer rounded-xl bg-theme-100 px-10 py-1 text-white transition-colors duration-200 hover:bg-theme-200"
                >
                  <span
                    class="flex items-center justify-center px-3 py-2 text-xs"
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

            <!-- Preview thumbnails inside card in a responsive grid -->
            <div
              v-if="rawFiles.length > 0"
              class="mt-6 grid grid-cols-2 gap-4 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6"
            >
              <div
                v-for="(file, index) in previewFiles"
                :key="file.name + file.size + index"
                class="flex flex-col items-center"
              >
                <img
                  v-if="file.preview"
                  :src="file.preview"
                  alt="Receipt thumbnail"
                  class="h-24 w-24 rounded-lg object-cover shadow"
                />

                <div
                  v-else
                  class="flex h-24 w-24 items-center justify-center rounded-lg bg-blue-100 text-blue-600 shadow"
                >
                  <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 20 20">
                    <path
                      fill-rule="evenodd"
                      d="M4 4a2 2 0 012-2h8a2 2 0 012 2v12a2 2 0 01-2 2H6a2 2 0 01-2-2V4zm2 0v12h8V4H6z"
                      clip-rule="evenodd"
                    />
                  </svg>
                </div>
                <p class="mt-2 w-24 truncate text-center text-xs text-gray-700">
                  {{ file.name }}
                </p>

                <button
                  @click="removeFile(index)"
                  class="text-sm font-medium text-red-600 transition-colors duration-200 hover:text-red-800 focus:underline focus:outline-none"
                >
                  Remove
                </button>
              </div>
            </div>
          </div>

          <p class="mt-2 pt-2 text-center text-xs text-theme-100">
            Supported formats: PDF, JPEG, JPG, PNG (max 10MB)
          </p>

          <!-- Buttons -->
          <div class="mt-6 flex justify-center space-x-10">
            <button
              @click="cancelUpload"
              class="rounded-xl border border-theme-300 bg-white px-10 py-2 text-xs font-medium text-theme-300 shadow-lg hover:bg-blue-50"
            >
              Cancel
            </button>
            <button
              @click="uploadFile"
              class="hover:bg-theme-400 cursor-pointer rounded-xl bg-theme-300 px-10 py-2 text-xs font-medium text-white shadow-lg"
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
import { ref, computed } from "vue";
import { useEmployeeClaimStore } from "@/stores/employee-claims";

const router = useRouter();
const claimStore = useEmployeeClaimStore();

const isDragging = ref(false);
const rawFiles = ref([]); // actual File instances
const previewFiles = ref([]); // UI previews
const isUploading = ref(false);
const isLoading = computed(() => claimStore.isLoading("uploading"));

const handleDrop = (e) => {
  isDragging.value = false;
  const files = Array.from(e.dataTransfer.files);
  addFiles(files);
};

const handleFileInput = (e) => {
  const files = Array.from(e.target.files);
  addFiles(files);
};

const addFiles = (files) => {
  for (const file of files) {
    const isImage = file.type.startsWith("image/");
    const preview = isImage ? URL.createObjectURL(file) : null;

    rawFiles.value.push(file);
    previewFiles.value.push({
      file,
      name: file.name,
      size: file.size,
      preview,
    });
  }
};

const removeFile = (index) => {
  const file = previewFiles.value[index];
  if (file.preview) URL.revokeObjectURL(file.preview);
  previewFiles.value.splice(index, 1);
  rawFiles.value.splice(index, 1);
};

const cancelUpload = () => {
  previewFiles.value.forEach((f) => {
    if (f.preview) URL.revokeObjectURL(f.preview);
  });
  previewFiles.value = [];
  rawFiles.value = [];
};

const uploadFile = async () => {
  if (!rawFiles.value.length) {
    alert("Please upload a file");
    return;
  }

  const formData = new FormData();
  rawFiles.value.forEach((file) => {
    formData.append("files", file);
  });

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
      if (!firstValid) firstValid = result;
      itemsServices.push(...result.items);
    }

    router.push({
      path: "/employee/invoice/edit",
      query: {
        category: firstValid.category,
        date: firstValid.date,
        merchantName: merchant_Names.join(" | "),
        merchantAddress: merchant_Addresses.join(" | "),
        remark: remarks.join(" | "),
        items: JSON.stringify(itemsServices),
      },
    });

    cancelUpload(); // clear files
  } catch (err) {
    console.error("Upload failed:", err);
    alert("LLM analysis unsuccessful");
  } finally {
    claimStore.stopLoading("uploading");
    isUploading.value = false;
  }
};
</script>
