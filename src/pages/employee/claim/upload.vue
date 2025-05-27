<template>
  <div class="min-h-screen bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl mx-auto">
      <!-- Card Container -->
      <div class="bg-white rounded-xl shadow-2xl overflow-hidden transform transition-all hover:shadow-3xl">
        <!-- Card Header -->
        <div class="px-8 py-6 text-center">
          <h2 class="text-2xl font-bold text-[#00246A]">Upload Your Receipts</h2>
          <p class="mt-2 text-[#4077B0] text-sm">Please provide your receipt below</p>
        </div>

        <!-- Card Body -->
        <div class="p-2">
          <!-- Upload Box -->
          <div
            class="mt-2 relative border-2 border-dashed border-gray-300 rounded-lg p-6 transition-all duration-200 ease-in-out px-2 py-10"
            :class="{ 'border-blue-500 bg-blue-50': isDragging }"
            @dragenter.prevent="isDragging = true"
            @dragleave.prevent="isDragging = false"
            @dragover.prevent
            @drop.prevent="handleDrop"
          >
            <div class="text-center">
              <!-- New circular upload icon -->
              <div class="mx-auto h-20 w-20 rounded-full bg-blue-100 flex items-center justify-center mb-4">
                <svg
                  class="h-10 w-10 text-[#4077B0]"
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
              
              <div class="mt-4 flex flex-col items-center justify-center space-y-3">
                <p class="text-gray-400 text-xs">Drop your files here or</p>
                <label
                  class="relative cursor-pointer bg-[#4077B0] rounded-2xl px-10 py-1 text-white hover:bg-[#0353A4] focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-blue-500 transition-colors duration-200"
                >
                  <span class="text-xs">Browse Files</span>
                  <input
                    type="file"
                    class="sr-only"
                    @change="handleFileInput"
                    accept=".pdf,.doc,.docx,.jpg,.jpeg,.png"
                  >
                </label>
               
              </div>
            </div>

            <!-- Preview section with enhanced styling -->
            <div v-if="selectedFile" class="mt-6 bg-gray-50 rounded-lg p-4 border border-gray-200">
              <div class="flex items-center justify-between">
                <div class="flex items-center space-x-3">
                  <div class="flex-shrink-0 bg-blue-100 rounded-full p-2">
                    <svg class="h-6 w-6 text-blue-600" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M4 4a2 2 0 012-2h8a2 2 0 012 2v12a2 2 0 01-2 2H6a2 2 0 01-2-2V4zm2 0v12h8V4H6z" clip-rule="evenodd"/>
                    </svg>
                  </div>
                  <div>
                    <p class="text-sm font-medium text-gray-900">{{ selectedFile.name }}</p>
                    <p class="text-xs text-gray-500">{{ formatFileSize(selectedFile.size) }}</p>
                  </div>
                </div>
                <button
                  @click="removeFile"
                  class="text-sm text-red-600 hover:text-red-800 font-medium focus:outline-none focus:underline transition-colors duration-200"
                >
                  Remove
                </button>
              </div>
            </div>
          </div>

          <p class="text-xs text-[#4077B0] mt-2 text-center">
                Supported formats: PDF, DOC, DOCX, JPG or PNG (max 10MB)
        </p>
          <!-- Upload and Cancel buttons -->
          <div class="mt-6 flex justify-center space-x-10">
            <button
              @click="cancelUpload"
              class="px-6 py-0.5 border-2 border-[#00246A] text-[#00246A] rounded-xl shadow-lg hover:bg-blue-50 focus:outline-none focus:ring-1 focus:ring-offset-2 focus:ring-blue-300 transition-colors duration-200 bg-white text-xs font-medium"
            >
              Cancel
            </button>
            <button
              @click="uploadFile"
              :disabled="!selectedFile"
              class="px-6 py-0.5 rounded-xl shadow-lg text-xs font-medium text-white transition-all duration-200 ease-in-out"
              :class="{
                'bg-[#00246A] hover:bg-[#00246A] focus:ring-2 focus:ring-offset-2 focus:ring-blue-500': selectedFile,
                'bg-gray-400 cursor-not-allowed': !selectedFile
              }"
            >
              <span class="flex items-center">
                <svg v-if="isUploading" class="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                {{ isUploading ? 'Uploading...' : 'Upload' }}
              </span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const isDragging = ref(false)
const selectedFile = ref(null)
const isUploading = ref(false)

const handleDrop = (e) => {
  isDragging.value = false
  const files = e.dataTransfer.files
  if (files.length) {
    selectedFile.value = files[0]
  }
}

const handleFileInput = (e) => {
  const files = e.target.files
  if (files.length) {
    selectedFile.value = files[0]
  }
}

const removeFile = () => {
  selectedFile.value = null
}

const formatFileSize = (bytes) => {
  if (bytes === 0) return '0 Bytes'
  const k = 1024
  const sizes = ['Bytes', 'KB', 'MB', 'GB']
  const i = Math.floor(Math.log(bytes) / Math.log(k))
  return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i]
}

const cancelUpload = () => {
  selectedFile.value = null
}

const uploadFile = async () => {
  if (!selectedFile.value) return

  isUploading.value = true
  
  try {
    const formData = new FormData()
    formData.append('file', selectedFile.value)
    
    // Example upload implementation (uncomment and modify as needed):
    // const response = await fetch('/api/upload', {
    //   method: 'POST',
    //   body: formData
    // })
    // const data = await response.json()
    // console.log('Upload successful:', data)
    
    // Simulate upload delay
    await new Promise(resolve => setTimeout(resolve, 2000))
    
    // Clear the form after successful upload
    selectedFile.value = null
  } catch (error) {
    console.error('Upload failed:', error)
  } finally {
    isUploading.value = false
  }
}
</script>