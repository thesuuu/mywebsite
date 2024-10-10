<template>
  <el-container>
    <el-header>
      <div class="header-content">
        <h1 class="webname-style">MEDIG</h1>
        <el-menu mode="horizontal" router>
          <el-menu-item index="/">Home</el-menu-item>
          <el-menu-item index="/algorithm">Algorithm</el-menu-item>
        </el-menu>
      </div>
    </el-header>
    <el-main>
      <router-view></router-view>
    </el-main>
  </el-container>
</template>

<style scoped>
.el-header {
  padding: 0;  /* 移除默认内边距 */
  background-color: #f5f7fa57;
}

.header-content {
  display: flex;
  align-items: center; /* 垂直居中对齐 */
  justify-content: space-between; /* 水平两端对齐 */
  padding: 0 20px; /* 左右内边距 */
  height: 100%; /* 充满整个header高度 */
  max-width: 1200px; /* 限制最大宽度 */
  margin: 0 auto; /* 水平居中 */
}

h1 {
  margin: 0;
  font-size: 1.5rem;
  color: #303133;
  white-space: nowrap; /* 防止文字换行 */
}

.webname-style {
  /* 设置字体族，优先使用 Arial，如果不可用则使用 Helvetica，最后退回到任何无衬线字体 */
  font-family: 'Arial', 'Helvetica', sans-serif;
  font-weight: 700;
  font-size: 1.8rem;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: #000000;
  background-color: #ffffff;
  padding: 5px 10px;
  display: inline-block;
}

.el-menu {
  min-width: 600px;
  justify-content: flex-end; /* 右对齐 */
  border-bottom: none; /* 移除底部边框 */
  background-color: transparent;
}

.el-menu-item {
  font-size: 1rem;
}

/* 响应式设计：小屏幕适配 */
@media (max-width: 768px) {
  .header-content {
    flex-direction: column; /* 改为垂直排列 */
    align-items: flex-start; /* 左对齐 */
    padding: 10px 20px;
  }

  .el-menu {
    margin-top: 10px;
  }
}

.el-main {
  padding: 20px;
}
</style>