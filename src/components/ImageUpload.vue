<template>
    <el-upload
        class="image-upload"
        action="#"
        :auot-upload="false"
        :on-change="handleChange"
        :show-file-list="false"
    >
        <el-button type="primary">Click to upload</el-button>
    </el-upload>
</template>

<script setup lang="ts">
import { UploadFile } from 'element-plus'

const emit = defineEmits(['file-uploaded'])

const handleChange = (file: UploadFile) => {
    if (file.raw) {
        emit('file-uploaded', file.raw)
    }
}  
</script>

