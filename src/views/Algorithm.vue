<!-- Algorithm.vue -->
<template>
    <div class="algorithm">
      <h2>Choose an Algorithm</h2>
      <div class="button-group">
        <el-button type="primary" @click="openDialog('segmentation')">Segmentation</el-button>
        <el-button type="primary" @click="openDialog('denoising')">Denoising</el-button>
      </div>
  
      <el-dialog
        v-model="dialogVisible"
        :title="currentAlgorithm"
        width="80%"
        :before-close="handleClose"
      >
        <component :is="currentComponent" @close="dialogVisible = false"></component>
      </el-dialog>
    </div>
  </template>
  
  
  <script lang="ts" setup>
  import { ref, shallowRef } from 'vue'
  import Segmentation from './Segmentation.vue'
  import Denoising from './Denoising.vue'
  
  const dialogVisible = ref(false)
  const currentAlgorithm = ref('')
  const currentComponent = shallowRef<typeof Segmentation | typeof Denoising | null>(null)
  
  const openDialog = (algorithm: 'segmentation' | 'denoising') => {
    currentAlgorithm.value = algorithm.charAt(0).toUpperCase() + algorithm.slice(1)
    currentComponent.value = algorithm === 'segmentation' ? Segmentation : Denoising
    dialogVisible.value = true
  }
  
  const handleClose = (done: () => void) => {
    done()
  }
  </script>

<style scoped>
.button-group {
  display: flex;
  justify-content: center;
  gap: 1rem;
}

.el-button {
  font-size: 1.1rem;
  padding: 12px 20px;
}
</style>