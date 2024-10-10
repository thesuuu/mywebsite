<template>
    <div class="algorithm">
        <div class="button-group">
            <AlgorithmButton 
                v-for="algo in algorithms"
                :key="algo.name"
                :name="algo.name"
                :icon="algo.icon"
                @click="openDialog(algo.name.toLowerCase())"
            />
        </div>

        <el-dialog
        v-model="dialogVisible"
        width="80%"
        :before-close="handleClose"
        >
        <component :is="currentComponent" @close="dialogVisible = false"></component>
        </el-dialog>
    </div>
</template>

<script setup lang="ts">
import { ref, shallowRef } from 'vue';
import { ElDialog } from 'element-plus';
import AlgorithmButton, { Props as AlgorithmProps } from '../components/AlgorithmButton.vue';

// 导入算法组件
import SegmentationComponent from './Segmentation.vue';
import DenoisingComponent from './Denoising.vue';

const algorithms = ref<AlgorithmProps[]>([
  { name: 'Segmentation', icon: 'segmentation' },
  { name: 'Denoising', icon: 'denoising' },
  // 此处添加算法
]);

const dialogVisible = ref(false);
const currentComponent = shallowRef<any>(null);

const openDialog = (algorithm: string): void => {
  switch(algorithm) {
    case 'segmentation':
      currentComponent.value = SegmentationComponent;
      break;
    case 'denoising':
      currentComponent.value = DenoisingComponent;
      break;
    default:
      console.error(`Unknown algorithm: ${algorithm}`);
      return;
  }
  dialogVisible.value = true;
};

const handleClose = (done: () => void) => {
  // 处理关闭逻辑，留空
  done();
};
</script>

<style scoped>
.button-group {
  display: flex;
  justify-content: center;
  gap: 1rem;
}
</style>