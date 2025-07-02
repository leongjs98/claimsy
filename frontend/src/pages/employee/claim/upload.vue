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
            <RouterLink
              to="/employee/claim/edit"
              class="rounded-xl bg-theme-300 px-10 py-2 text-xs font-medium text-white shadow-lg transition-all duration-200 ease-in-out hover:bg-theme-300 focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
            >
              Upload
            </RouterLink>
            <!-- <button -->
            <!--   @click="uploadFile" -->
            <!--   :disabled="!selectedFile" -->
            <!--   class="rounded-xl px-10 py-2 text-xs font-medium text-white shadow-lg transition-all duration-200 ease-in-out" -->
            <!--   :class="{ -->
            <!--     'bg-theme-300 hover:bg-theme-300 focus:ring-2 focus:ring-blue-500 focus:ring-offset-2': -->
            <!--       selectedFile, -->
            <!--     'cursor-not-allowed bg-gray-400': !selectedFile, -->
            <!--   }" -->
            <!-- > -->
            <!--   <span class="flex items-center"> -->
            <!--     <svg -->
            <!--       v-if="isUploading" -->
            <!--       class="mr-2 -ml-1 h-4 w-4 animate-spin text-white" -->
            <!--       xmlns="http://www.w3.org/2000/svg" -->
            <!--       fill="none" -->
            <!--       viewBox="0 0 24 24" -->
            <!--     > -->
            <!--       <circle -->
            <!--         class="opacity-25" -->
            <!--         cx="12" -->
            <!--         cy="12" -->
            <!--         r="10" -->
            <!--         stroke="currentColor" -->
            <!--         stroke-width="4" -->
            <!--       ></circle> -->
            <!--       <path -->
            <!--         class="opacity-75" -->
            <!--         fill="currentColor" -->
            <!--         d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" -->
            <!--       ></path> -->
            <!--     </svg> -->
            <!--     {{ isUploading ? "Uploading..." : "Upload" }} -->
            <!--   </span> -->
            <!-- </button> -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref } from "vue";

  const isDragging = ref(false);
  const selectedFiles = ref([]);
  const isUploading = ref(false);

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

  const uploadFile = async () => {
    if (selectedFiles.value.length === 0) return;

    isUploading.value = true;

    try {
      //I need to append multiple files but I dont think the receiver is ready for it. Therefore, I make it append one by one for now.
      //not ready because the receipt details will only generate data from the hardcoded one.
      const formData = new FormData();
      selectedFiles.value.forEach((file) => {
        formData.append("files", file);
      });

      // Example upload implementation (uncomment and modify as needed):
      // const response = await fetch('/api/upload', {
      //   method: 'POST',
      //   body: formData
      // })
      // const data = await response.json()
      // console.log('Upload successful:', data)

      // Simulate upload delay
      await new Promise((resolve) => setTimeout(resolve, 2000));

      // Clear the form after successful upload
      selectedFiles.value = [];
    } catch (error) {
      console.error("Upload failed:", error);
    } finally {
      isUploading.value = false;
    }
  };
</script>
