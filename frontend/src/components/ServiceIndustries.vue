<template>
  <div class="industry-section section-white">
    <div class="section-title">服务行业</div>
    <p class="section-subtitle">覆盖八大关键领域，赋能产业升级</p>
    <div class="industry-container">
      <button class="nav-arrow prev" @click="scrollLeft" :disabled="scrollPos <= 0">
        <el-icon><ArrowLeft /></el-icon>
      </button>
      <div class="industry-grid" ref="gridRef" @scroll="updateScrollPos">
        <div class="industry-item" v-for="(item, i) in industries" :key="i">
          <div class="industry-icon" :style="{ background: item.bg }">
            <el-icon :size="32" color="#fff">{{ item.icon }}</el-icon>
          </div>
          <span class="industry-label">{{ item.label }}</span>
        </div>
      </div>
      <button class="nav-arrow next" @click="scrollRight">
        <el-icon><ArrowRight /></el-icon>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const gridRef = ref(null)
const scrollPos = ref(0)

const industries = [
  { label: '工业应用', icon: 'Setting', bg: 'linear-gradient(135deg, #1565c0, #42a5f5)' },
  { label: '电网基础设施', icon: 'Connection', bg: 'linear-gradient(135deg, #e65100, #ff9800)' },
  { label: '医疗应用', icon: 'FirstAidKit', bg: 'linear-gradient(135deg, #2e7d32, #66bb6a)' },
  { label: '新能源', icon: 'Sunny', bg: 'linear-gradient(135deg, #f9a825, #fdd835)' },
  { label: '汽车电子', icon: 'Van', bg: 'linear-gradient(135deg, #6a1b9a, #ab47bc)' },
  { label: '人工智能', icon: 'Cpu', bg: 'linear-gradient(135deg, #00838f, #26c6da)' },
  { label: '智能家居', icon: 'HomeFilled', bg: 'linear-gradient(135deg, #ad1457, #e91e63)' },
  { label: '仪器仪表', icon: 'Monitor', bg: 'linear-gradient(135deg, #37474f, #78909c)' },
]

function scrollLeft() {
  if (gridRef.value) {
    gridRef.value.scrollBy({ left: -240, behavior: 'smooth' })
  }
}
function scrollRight() {
  if (gridRef.value) {
    gridRef.value.scrollBy({ left: 240, behavior: 'smooth' })
  }
}
function updateScrollPos() {
  if (gridRef.value) {
    scrollPos.value = gridRef.value.scrollLeft
  }
}
</script>

<style scoped>
.industry-section {
  padding: 20px 0 50px;
}
.industry-container {
  max-width: var(--max-width);
  margin: 0 auto;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 0 15px;
  position: relative;
}
.industry-grid {
  display: flex;
  gap: 20px;
  overflow-x: auto;
  scroll-behavior: smooth;
  padding: 10px 0;
  flex: 1;
  -webkit-overflow-scrolling: touch;
}
.industry-grid::-webkit-scrollbar {
  display: none;
}
.industry-item {
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  transition: transform var(--transition-fast);
  padding: 10px 8px;
  min-width: 120px;
}
.industry-item:hover {
  transform: translateY(-4px);
}
.industry-icon {
  width: 80px;
  height: 80px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}
.industry-label {
  font-size: 14px;
  font-weight: 500;
  color: var(--color-dark);
}
.nav-arrow {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: 1px solid var(--color-gray-6);
  background: var(--color-white);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  flex-shrink: 0;
  transition: all var(--transition-fast);
  box-shadow: var(--shadow-sm);
}
.nav-arrow:hover:not(:disabled) {
  border-color: var(--color-primary);
  color: var(--color-primary);
}
.nav-arrow:disabled {
  opacity: 0.3;
  cursor: not-allowed;
}
</style>
