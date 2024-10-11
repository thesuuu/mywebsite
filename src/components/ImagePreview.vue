<template>
    <div class="imagePreview">
        <img v-if="imageUrl" :src="imageUrl" alt="Processed Image" />
        <p v-else>No image to preview</p>
    </div>
</template>

<script setup lang="ts">
defineProps<{
    imageUrl: string
}>()
</script>

<style scoped>
.imagePreview {
    max-width: 400px; /* Set your desired maximum width */
    max-height: 300px; /* Set your desired maximum height */
    overflow: hidden; /* Hide overflow to prevent large images from spilling */
    display: flex; /* Center the content */
    justify-content: center;
    align-items: center;
    border: 2px solid #ccc; /* Optional: Add a border for better visibility */
    border-radius: 8px; /* Optional: Round the corners */
}

.imagePreview img {
    max-width: 100%;
    max-height: 100%;
    height: auto; /* Maintain the aspect ratio */
    object-fit: contain; /* Ensure the image fits within the bounds */
}
</style>
