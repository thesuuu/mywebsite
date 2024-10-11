<template>
    <div class="Segmentation">
        <h2>Segmentation</h2>

        <!-- 添加算法描述-->
        <div class="description">
            <h3>
            <p>
                该分割算法采用OpenCV的自适应阈值分割函数实现,适用于灰度图像中的目标分割。
            </p>
            <ol>
                <li>点击"Click to upload"按钮上传一张图片。</li>
                <li>处理完成后，您可以在下方预览分割结果。</li>
                <li>如果满意，可以点击"Download Processed Image"下载处理后的图像。</li>
            </ol>
            </h3>
        </div>

        <!-- 触发事件处理器 -->
        <ImageUpload @file-uploaded="handleFileUpload" />  

        <!-- 加载指示器 -->
        <LoadingOverlay :is-loading="isLoading" message="Processing image..." />

        <!-- 图像预览 -->
        <ImagePreview :image-url="processedImageUrl" /> 

        <!-- 下载按钮 -->
        <DownloadButton :download-url="processedImageUrl" /> 

        <!-- 错误消息显示 -->
        <ErrorMessage :message="errorMessage" />
    </div>
</template>


<script lang="ts" setup> // 采用typescipt
import {ref} from 'vue'
import axios from 'axios'
import ImageUpload from '../components/ImageUpload.vue'
import ImagePreview from '../components/ImagePreview.vue'
import DownloadButton from '../components/DownloadButton.vue'
import LoadingOverlay from '../components/LoadingOverlay.vue'
import ErrorMessage from '../components/ErrorMessage.vue'

const processedImageUrl = ref<string>('')
const isLoading = ref<boolean>(false)
const errorMessage = ref<string>('')

const handleFileUpload = async (file: File) => {  // 异步函数
    const formData = new FormData()
    formData.append('image', file)
    formData.append('algrithm', 'segmentation')

    isLoading.value = true
    errorMessage.value = ''

    try{
        const response = await axios.post('https://06a8-210-75-253-166.ngrok-free.app/process', formData, {  // ngrok url
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
        processedImageUrl.value = `data:image/png;base64,${response.data.processed_image}`
    } catch(error){
        console.error('Error processing image:', error)
        errorMessage.value = 'An error occurred while processing the image.'
    } finally {
        isLoading.value = false
    }
}
</script>

<style scoped>
.description{
    background-color: #f5f5f5;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 15px;
    margin-bottom: 20px;
}

.description h3 {
    margin-top: 0;
    color: black;
}

.description p, .description ol {
    color: #666;
}

.description ol {
    padding-left: 20px;
}
</style>