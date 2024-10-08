<template>
    <div class="Denoising">
        <h2>Denoising</h2>

        <!-- 添加算法描述-->
        <div class="description">
            <h3>
            <p>
                该去噪算法采用OpenCV的高斯滤波函数实现,适用于消除高斯噪声。
            </p>
            <ol>
                <li>点击"Click to upload"按钮上传一张图片。</li>
                <li>处理完成后，您可以在下方预览去噪结果。</li>
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
const emit = defineEmits(['close'])

const handleFileUpload = async (file: File) => {  // 异步函数
    const formData = new FormData()
    formData.append('image', file)

    isLoading.value = true
    errorMessage.value = ''

    try{
        const response = await axios.post('', formData, {  // ngrok url
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
        processedImageUrl.value = response.data.processedImageUrl
    } catch(error){
        console.error('Error processing image:', error)
        errorMessage.value = 'Failed to process image. Please try again later.'
    } finally{
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
    color: #333;
}

.description p, .description ol {
    color: #666;
}

.description ol {
    padding-left: 20px;
}
</style>