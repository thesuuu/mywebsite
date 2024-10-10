<template>
  <el-container>
    <el-header>
      <h1>Image Processing Web</h1>
      <el-menu mode="horizontal" router>
        <el-menu-item index="/">Home</el-menu-item>
        <el-menu-item index="/algorithm">Algorithm</el-menu-item>
      </el-menu>
    </el-header>
    <el-main>
      <router-view></router-view>
    </el-main>
  </el-container>
</template>

<style scoped>
.el-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
  background-color: #f5f7fa;
}

h1 {
  margin: 0;
  font-size: 1.5rem;
  color: #303133;
}

.el-main {
  padding: 20px;
}
</style>