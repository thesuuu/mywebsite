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
    if (props.downloadUrl){
        window.open(props.downloadUrl, '_blank')
    }
}
</script>


