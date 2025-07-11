<template>
  <div class="mx-auto my-14 w-full max-w-6xl bg-gray-100">
    <div class="mx-auto max-w-3xl">
      <div
        class="hover:shadow-3xl transform overflow-hidden rounded-xl bg-white px-20 py-6 shadow-2xl transition-all"
      >
        <!-- Card Header -->
        <div class="px-8 py-4 pb-0 text-center">
          <h2 class="text-2xl font-bold text-theme-300">Upload Your Policy</h2>
          <p class="mt-2 text-sm text-theme-100">
            Please provide your policy below
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
              v-if="selectedFile"
              class="mt-6 rounded-lg border border-gray-200 bg-gray-50 p-4"
            >
              <div class="flex items-center justify-between">
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
                      {{ selectedFile.name }}
                    </p>
                    <p class="text-xs text-gray-500">
                      {{ formatFileSize(selectedFile.size) }}
                    </p>
                  </div>
                </div>
                <button
                  @click="removeFile"
                  class="text-sm font-medium text-red-600 transition-colors duration-200 hover:text-red-800 focus:underline focus:outline-none"
                >
                  Remove
                </button>
              </div>
            </div>
          </div>

          <!-- "Supported Format" text -->
          <p class="mt-2 pt-2 text-center text-xs text-theme-100">
            Supported formats: PDF, JPG or PNG (max 10MB)
          </p>
          <!-- Upload and Cancel buttons -->
          <div class="mt-6 flex items-center justify-center gap-10">
            <SecondaryButton @click="selectedFile = null">
              Cancel
            </SecondaryButton>
            <span class="flex items-center justify-center gap-2">
              <PrimaryButton @click="handleUpload">
                <span v-if="isUploading"> Processing... </span>
                <span v-else> Upload </span>
              </PrimaryButton>
              <svg
                v-if="isUploading"
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
  </div>
</template>

<script setup>
  import { ref } from "vue";
  import { useRouter } from "vue-router";

  const router = useRouter();

  const props = defineProps({
    title: String,
  });

  const isDragging = ref(false);
  const selectedFile = ref(null);
  const isUploading = ref(false);

  const handleDrop = (e) => {
    isDragging.value = false;
    const files = e.dataTransfer.files;
    if (files.length) {
      selectedFile.value = files[0];
    }
  };

  const handleFileInput = (e) => {
    const files = e.target.files;
    if (files.length) {
      selectedFile.value = files[0];
    }
  };

  const removeFile = () => {
    selectedFile.value = null;
  };

  const formatFileSize = (bytes) => {
    if (bytes === 0) return "0 Bytes";
    const k = 1024;
    const sizes = ["Bytes", "KB", "MB", "GB"];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + " " + sizes[i];
  };

  const handleUpload = async () => {
    // if (!selectedFile.value) {
    //   alert("There's no file");
    //   return;
    // }
    isUploading.value = true;

    try {
      const formData = new FormData();
      formData.append("file", selectedFile.value);

      // Example upload implementation (uncomment and modify as needed):
      // const response = await fetch('/api/upload', {
      //   method: 'POST',
      //   body: formData
      // })
      // const data = await response.json()
      // console.log('Upload successful:', data)

      // Simulate upload delay
      await new Promise((resolve) => setTimeout(resolve, 5000));

      // Clear the form after successful upload
      selectedFile.value = null;
      router.push({
        path: "/admin/policy/edit",
      });
    } catch (error) {
      console.error("Upload failed:", error);
    } finally {
      isUploading.value = false;
    }
  };
</script>
