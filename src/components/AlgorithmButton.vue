<template>
    <div class="algorithm-button" @click="$emit('click')">
        <div class="icon" :class="iconClass"></div>
        <span class="algorithm-name">{{ name }}</span>
    </div>
</template>

<script lang="ts" setup>
import { computed } from 'vue';

// 定义 Props 接口，描述组件接收的属性类型（TypeScript）
interface Props {
  name: string;
  icon: string;
}

// 传入TypeScript接口作为参数，返回一个对象，包含了所有定义的 props
const { icon, name } = defineProps<Props>(); 

// 创建一个计算属性 iconClass
// 它根据传入的 icon prop 动态生成 CSS 类名
// 例如，如果 icon prop 的值是 "segmentation"，那么生成的类名将是 "segmentation-icon"
const iconClass = computed(() => `${icon}-icon`);
</script>


<style scoped>
.algorithm-button {
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  transition: transform 0.2s;
}

.algorithm-button:hover {
  transform: scale(1.05);
}

.icon {
  width: 120px;
  height: 120px;
  border-radius: 18px;
  margin-bottom: 14px;
  background-size: cover;
}

.segmentation-icon {
  /* background-color: #4CAF50; */
  background-image: url('../assets/icon/16gl-S.svg');
}

.denoising-icon {
  /* background-color: #2196F3; */
  background-image: url('../assets/icon/16gl-D.svg');
}

.algorithm-name {
  color: white;
  font-size: 20px;
}
</style>