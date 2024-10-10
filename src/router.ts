import { createRouter, createWebHistory } from 'vue-router'
import Home from './views/Home.vue'
import Algorithm from './views/Algorithm.vue'
import Segmentation from './views/Segmentation.vue'
import Denoising from './views/Denoising.vue'

// createRouter 用于创建一个新的路由器实例
// createWebHistory 是一个用于创建基于HTML5历史API的路由历史记录的函数

const routes = [
    {path: '/', component: Home},
    {path: '/Algorithm', component: Algorithm },
    {path: '/Segmentation', component: Segmentation},
    {path: '/Denoising', component: Denoising},
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

// 将创建的路由器实例导出为默认导出
// 在 Vue 应用的入口文件导入并使用这个路由器实例
export default router
