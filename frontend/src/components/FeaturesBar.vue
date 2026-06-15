<template>
  <div class="features-bar">
    <div class="features-container">
      <div class="feature-item" v-for="(item, i) in features" :key="i">
        <el-icon :size="36" color="#fff">{{ item.icon }}</el-icon>
        <span class="feature-text">{{ item.text }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
const features = [
  { icon: 'Box', text: '海量现货，种类齐全' },
  { icon: 'Lightning', text: '报价讯捷，闪电出货' },
  { icon: 'Shop', text: '原厂渠道，正品保证' },
  { icon: 'Money', text: '批量采购，支持议价' },
  { icon: 'Headset', text: '专属客服，一对一服务' },
]
</script>

<style scoped>
.features-bar {
  background: linear-gradient(135deg, #c62828, #e53935);
  padding: 24px 0;
}
.features-container {
  max-width: var(--max-width);
  margin: 0 auto;
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding: 0 15px;
}
.feature-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: 0 10px;
}
.feature-text {
  color: var(--color-white);
  font-size: 14px;
  font-weight: 500;
  white-space: nowrap;
}

@media (max-width: 768px) {
  .features-container {
    flex-wrap: wrap;
    gap: 16px;
  }
  .feature-item {
    width: 30%;
  }
}
</style>
