<template>
    <div class="home">
        <h2>Welcome to Image Processing Web</h2>
        <p>Choose an algorithm to process your image:</p>
        <el-button @click="$router.push('/Segmentation')">Segmentation</el-button>
        <el-button @click="$router.push('/Denoising')">Denoising</el-button>
    </div>
</template>

<!-- <script>
export default {
    name: 'Home',
}
</script> -->
