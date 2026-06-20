<template>
  <div class="right-sidebar" :class="{ visible: showSidebar }">
    <div class="sidebar-item" @mouseenter="showWechat = true" @mouseleave="showWechat = false">
      <div class="sidebar-icon">
        <el-icon :size="20" color="#666"><ChatLineSquare /></el-icon>
        <span class="sidebar-tooltip">微信</span>
      </div>
      <div class="wechat-popup" v-show="showWechat">
        <img src="/wechat.jpg" alt="微信二维码" />
        <span class="wechat-label">扫一扫添加微信</span>
      </div>
    </div>
    <div class="sidebar-item back-top" v-show="showBackTop" @click="scrollToTop">
      <div class="sidebar-icon">
        <el-icon :size="20" color="#666"><Top /></el-icon>
        <span class="sidebar-tooltip">返回顶部</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const showSidebar = ref(false)
const showBackTop = ref(false)
const showWechat = ref(false)

function handleScroll() {
  showBackTop.value = window.scrollY > 300
  showSidebar.value = true
}

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
  handleScroll()
})

onBeforeUnmount(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.right-sidebar {
  position: fixed;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  z-index: 999;
  display: flex;
  flex-direction: column;
  opacity: 0;
  transition: opacity var(--transition-normal);
}
.right-sidebar.visible {
  opacity: 1;
}
.sidebar-item {
  position: relative;
}
.sidebar-icon {
  width: 42px;
  height: 42px;
  background: var(--color-white);
  border: 1px solid var(--color-gray-7);
  border-right: none;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all var(--transition-fast);
  position: relative;
}
.sidebar-icon:hover {
  background: var(--color-primary);
  border-color: var(--color-primary);
}
.sidebar-icon:hover :deep(.el-icon) {
  color: #fff !important;
}
.sidebar-tooltip {
  position: absolute;
  right: 100%;
  top: 50%;
  transform: translateY(-50%);
  background: var(--color-dark);
  color: var(--color-white);
  padding: 6px 12px;
  font-size: 12px;
  border-radius: 4px;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: all var(--transition-fast);
  margin-right: 4px;
}
.sidebar-icon:hover .sidebar-tooltip {
  opacity: 1;
}

.back-top {
  border-top: 1px solid var(--color-gray-7);
}

.wechat-popup {
  position: absolute;
  right: calc(100% + 12px);
  top: 50%;
  transform: translateY(-50%);
  background: var(--color-white);
  border: 1px solid var(--color-gray-7);
  border-radius: 8px;
  padding: 12px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.12);
  z-index: 1000;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}
.wechat-popup img {
  width: 150px;
  height: 150px;
  display: block;
}
.wechat-label {
  font-size: 12px;
  color: var(--color-gray-2);
  white-space: nowrap;
}
</style>
