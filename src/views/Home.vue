<template>
    <div class="home">
      <div class="container">
        <h1>Image Processing</h1>
        <p>Enhance your images with our advanced algorithms</p>
      </div>
    </div>
</template>
  
<style scoped>
  .home {
    display: flex; /*弹性盒模型*/
    justify-content: center; /*在主轴上的对齐方式*/
    align-items: center; /*在交叉轴上的对齐方式*/
    height: 100vh; /*设置了容器的高度,1vh 等于视口高度的 1%*/
    background-color: transparent;
  }
  
  .container {
    text-align: center; 
    padding: 2rem; 
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  }
  
  h1 {
    font-size: 2.5rem;
    color: #303133;
    margin-bottom: 1rem;
  }
  
  p {
    font-size: 1.2rem;
    color: #606266;
    margin-bottom: 2rem;
  }
</style>