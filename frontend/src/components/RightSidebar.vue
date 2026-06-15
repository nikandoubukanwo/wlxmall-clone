<template>
  <div class="right-sidebar" :class="{ visible: showSidebar }">
    <div class="sidebar-item" v-for="(item, i) in menuItems" :key="i" @click="item.action">
      <div class="sidebar-icon">
        <el-icon :size="20" color="#666">{{ item.icon }}</el-icon>
        <span class="sidebar-tooltip">{{ item.label }}</span>
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

const menuItems = [
  { icon: 'ChatDotRound', label: '在线客服', action: () => window.open('https://wpa1.qq.com/ExeLLyG7?_type=wpa&qidian=true') },
  { icon: 'ChatLineSquare', label: '微信', action: () => alert('微信号: wlxmall') },
  { icon: 'ShoppingCart', label: '购物车', action: () => alert('购物车功能') },
  { icon: 'Message', label: '公众号', action: () => alert('关注公众号') },
  { icon: 'EditPen', label: '投诉建议', action: () => alert('投诉建议功能') },
]

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
</style>
