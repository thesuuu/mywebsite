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
.image-preview img {
    max-width: 100%;
    height: auto;
}
</style>