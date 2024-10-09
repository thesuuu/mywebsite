<template>
    <div class="error-message" v-if="message"> 
        {{ message }}
    </div>
</template>

<script lang="ts" setup>
defineProps<{
    message: string;
}>();
</script>

<style scoped>
.error-message{
    color: #ff0000;
    margin-top: 10px;
    text-align: center;
}
</style>