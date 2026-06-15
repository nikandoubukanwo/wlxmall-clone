<template>
  <div class="why-section section-gray">
    <div class="section-title">为什么选择万联芯城</div>
    <p class="section-subtitle">11年专注电子元器件供应链服务</p>
    <div class="cards-container">
      <div class="why-card" v-for="(card, i) in cards" :key="i">
        <div class="card-icon" :style="{ background: card.iconBg }">
          <el-icon :size="36" color="#fff">{{ card.icon }}</el-icon>
        </div>
        <h3 class="card-title">{{ card.title }}</h3>
        <ul class="card-list">
          <li v-for="(item, j) in card.items" :key="j">{{ item }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
const cards = [
  {
    icon: 'Medal',
    iconBg: 'linear-gradient(135deg, #c62828, #e53935)',
    title: '知名元器件供应链服务平台',
    items: [
      '11年服务10万注册用户',
      '深圳市电子商会副会长单位',
      '电子元器件行业"杰出电子商务平台""优秀电商平台"',
      '年流量超100万，位居行业前列',
    ],
  },
  {
    icon: 'Ship',
    iconBg: 'linear-gradient(135deg, #1565c0, #42a5f5)',
    title: '卓越的元器件供应服务',
    items: [
      '一站式服务：提供元器件现货采购、期货订购、BOM配单、紧缺物料、工厂呆料寄售等一站式服务',
      '全球化供应链：超600万SKU、300+商品类目、400+全球知名品牌、3000+全球化供应商',
      '品质可靠：严控渠道、品质可靠、5道验货流程、每一颗料均可追溯',
    ],
  },
  {
    icon: 'UserFilled',
    iconBg: 'linear-gradient(135deg, #e65100, #ff9800)',
    title: '"3位一体"全服务链团队',
    items: [
      '专业、快速响应的在线咨询、报价服务',
      '销售工程师团队提供一对一现场服务',
      '专业采销团队达100人、强大的采销服务能力',
    ],
  },
]
</script>

<style scoped>
.why-section {
  padding: 20px 0 50px;
}
.cards-container {
  max-width: var(--max-width);
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  padding: 0 15px;
}
.why-card {
  background: var(--color-white);
  border-radius: 8px;
  padding: 30px 24px;
  box-shadow: var(--shadow-sm);
  transition: all var(--transition-normal);
  text-align: center;
}
.why-card:hover {
  box-shadow: var(--shadow-lg);
  transform: translateY(-4px);
}
.card-icon {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 16px;
}
.card-title {
  font-size: var(--font-md);
  font-weight: 600;
  color: var(--color-dark);
  margin-bottom: 14px;
}
.card-list {
  list-style: none;
  padding: 0;
  text-align: left;
}
.card-list li {
  font-size: var(--font-sm);
  color: var(--color-gray-2);
  padding: 5px 0;
  padding-left: 14px;
  position: relative;
  line-height: 1.6;
}
.card-list li::before {
  content: '✓';
  position: absolute;
  left: 0;
  color: var(--color-primary);
  font-weight: 700;
}

@media (max-width: 768px) {
  .cards-container {
    grid-template-columns: 1fr;
  }
}
</style>
