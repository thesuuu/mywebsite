<template>
    <el-button v-if="downloadUrl" type="primary" @click="downloadImage">
        Download Processed Image
    </el-button>
</template>

<script setup lang="ts">
import { PropType } from 'vue'

const props = defineProps({
    downloadUrl:{
        type: String as PropType<string>,
        require: true
    }
})

const downloadImage = () => {
    if (props.downloadUrl) {
    // 检查 URL 是否是 base64 编码的数据 URL
    if (props.downloadUrl.startsWith('data:image/png;base64,')) {
      // 从 Data URL 中提取 base64 编码的数据
      const base64Data = props.downloadUrl.split(',')[1]
      
      // 将 base64 转换为二进制数据
      const binaryData = atob(base64Data)
      
      // 创建一个 Uint8Array 来存储二进制数据
      const uint8Array = new Uint8Array(binaryData.length)
      for (let i = 0; i < binaryData.length; i++) {
        uint8Array[i] = binaryData.charCodeAt(i)
      }
      
      // 创建 Blob 对象
      const blob = new Blob([uint8Array], {type: 'image/png'})
      
      // 创建下载链接
      const url = URL.createObjectURL(blob)
      const link = document.createElement('a')
      link.href = url
      link.download = 'processed_image.png' // 文件名
      
      // 触发下载
      document.body.appendChild(link)
      link.click()
      
      // 清理
      document.body.removeChild(link)
      URL.revokeObjectURL(url)
    } else {
      // 如果不是 base64 编码的数据 URL，就使用普通的下载方法
      const link = document.createElement('a')
      link.href = props.downloadUrl
      link.download = 'processed_image.png' // 文件名
      document.body.appendChild(link)
      link.click()
      document.body.removeChild(link)
    }
  }
}
</script>


