<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload Component</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/vuetify@3.x/dist/vuetify.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/@mdi/font@6.x/css/materialdesignicons.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/vuetify@3.x/dist/vuetify.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        /* Custom styles for drag-and-drop area */
        .drag-area {
            border: 2px dashed #d1d5db; /* gray-300 */
            background-color: #f9fafb; /* gray-50 */
            transition: all 0.3s ease-in-out;
        }
        .drag-area.dragging {
            border-color: #3b82f6; /* blue-500 */
            background-color: #eff6ff; /* blue-50 */
        }
        .v-btn {
            text-transform: none !important; /* Prevent Vuetify from uppercasing button text */
        }
    </style>
</head>
<body class="min-h-screen bg-gray-100 flex items-center justify-center p-4">
    <div id="app" class="w-full h-full flex items-center justify-center">
        </div>

    <script>
        const { createApp, ref } = Vue;
        const { createVuetify } = Vuetify;

        const vuetify = createVuetify({
            icons: {
                defaultSet: 'mdi',
            },
        });

        // Define the UploadComponent
        const UploadComponent = {
            template: `
                <div class="w-full h-full flex items-center justify-center">
                    <v-dialog
                        v-model="dialog"
                        max-width="500px"
                        persistent
                        class="rounded-xl shadow-2xl"
                    >
                        <v-card class="rounded-xl p-6 md:p-8">
                            <v-card-title class="text-h5 font-semibold text-gray-800 text-center mb-2">
                                Upload Your Receipts
                            </v-card-title>
                            <v-card-subtitle class="text-gray-600 text-center mb-6">
                                Drag and drop files here or click to browse
                            </v-card-subtitle>

                            <v-card-text>
                                <div
                                    class="drag-area rounded-lg p-8 text-center flex flex-col items-center justify-center"
                                    :class="{ 'dragging': isDragging }"
                                    @dragover.prevent="handleDragOver"
                                    @dragleave.prevent="handleDragLeave"
                                    @drop.prevent="handleDrop"
                                >
                                    <div class="mb-4">
                                        <v-icon size="64" color="grey-lighten-1">mdi-cloud-upload-outline</v-icon>
                                    </div>
                                    <p class="text-gray-500 mb-4">Drop files here or</p>

                                    <input
                                        type="file"
                                        multiple
                                        ref="fileInput"
                                        class="hidden"
                                        @change="handleFileSelect"
                                    />
                                    <v-btn
                                        color="blue-darken-2"
                                        class="rounded-md shadow-sm text-white px-6 py-3"
                                        @click="$refs.fileInput.click()"
                                    >
                                        Browse Files
                                    </v-btn>
                                </div>

                                <div v-if="files.length > 0" class="mt-4 text-sm text-gray-700">
                                    <p class="font-medium">Selected files:</p>
                                    <ul class="list-disc list-inside">
                                        <li v-for="(file, index) in files" :key="index">
                                            {{ file.name }} ({{ Math.round(file.size / 1024) }} KB)
                                        </li>
                                    </ul>
                                </div>

                                <p class="text-gray-500 text-sm mt-6 text-center">
                                    Supported file types: JPG, PNG, PDF
                                </p>
                                <p class="text-gray-500 text-sm text-center mb-8">
                                    Maximum file size: 10MB
                                </p>
                            </v-card-text>

                            <v-card-actions class="flex justify-end space-x-4 pt-0">
                                <v-btn
                                    variant="outlined"
                                    class="rounded-lg text-gray-700 hover:bg-gray-100 px-6 py-3"
                                    @click="dialog = false"
                                >
                                    Cancel
                                </v-btn>
                                <v-btn
                                    color="blue-darken-2"
                                    class="rounded-lg shadow-md text-white px-6 py-3"
                                    @click="uploadFiles"
                                >
                                    Upload
                                </v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                </div>
            `,
            setup() {
                const dialog = ref(true); // Controls the visibility of the dialog, set to true by default
                const isDragging = ref(false); // Controls drag-and-drop visual feedback
                const files = ref([]); // Stores selected files

                // Handle drag over event
                const handleDragOver = (e) => {
                    isDragging.value = true;
                };

                // Handle drag leave event
                const handleDragLeave = (e) => {
                    isDragging.value = false;
                };

                // Handle file drop event
                const handleDrop = (e) => {
                    isDragging.value = false;
                    const droppedFiles = Array.from(e.dataTransfer.files);
                    files.value = [...files.value, ...droppedFiles]; // Add dropped files
                    console.log('Dropped files:', droppedFiles);
                };

                // Handle file selection via input
                const handleFileSelect = (e) => {
                    const selectedFiles = Array.from(e.target.files);
                    files.value = [...files.value, ...selectedFiles]; // Add selected files
                    console.log('Selected files:', selectedFiles);
                };

                // Simulate file upload
                const uploadFiles = () => {
                    if (files.value.length > 0) {
                        console.log('Uploading files:', files.value);
                        // In a real application, you would send these files to a server
                        // For demonstration, we just close the dialog
                        dialog.value = false;
                        files.value = []; // Clear files after upload
                    } else {
                        console.log('No files to upload.');
                    }
                };

                return {
                    dialog,
                    isDragging,
                    files,
                    handleDragOver,
                    handleDragLeave,
                    handleDrop,
                    handleFileSelect,
                    uploadFiles,
                };
            }
        };

        // Create and mount the Vue app with the UploadComponent
        createApp(UploadComponent).use(vuetify).mount('#app');
    </script>
</body>
</html>
