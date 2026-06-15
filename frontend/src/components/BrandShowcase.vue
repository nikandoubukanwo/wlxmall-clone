<template>
  <div class="brand-section section-white">
    <div class="section-title">知名品牌</div>
    <p class="section-subtitle">400+全球知名品牌，原厂渠道正品保障</p>
    <div class="brand-container">
      <div class="brand-tabs">
        <span
          :class="['tab-item', { active: activeTab === 'global' }]"
          @click="activeTab = 'global'"
        >知名品牌</span>
        <span
          :class="['tab-item', { active: activeTab === 'domestic' }]"
          @click="activeTab = 'domestic'"
        >国产器件</span>
      </div>
      <div class="brand-grid">
        <div
          class="brand-cell"
          v-for="(brand, i) in (activeTab === 'global' ? globalBrands : domesticBrands)"
          :key="i"
          @click="handleBrandClick(brand)"
        >
          <div class="brand-logo">{{ brand.name }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const activeTab = ref('global')

const globalBrands = [
  { name: 'TI', full: 'Texas Instruments' },
  { name: 'ADI', full: 'Analog Devices' },
  { name: 'ST', full: 'STMicroelectronics' },
  { name: 'NXP', full: 'NXP Semiconductors' },
  { name: 'ON', full: 'ON Semiconductor' },
  { name: 'Microchip', full: 'Microchip Technology' },
  { name: 'Infineon', full: 'Infineon Technologies' },
  { name: 'Renesas', full: 'Renesas Electronics' },
  { name: 'Samsung', full: 'Samsung Electro-Mechanics' },
  { name: 'Murata', full: 'Murata Manufacturing' },
  { name: 'Yageo', full: 'Yageo Corporation' },
  { name: 'TE', full: 'TE Connectivity' },
  { name: 'Molex', full: 'Molex' },
  { name: 'Xilinx', full: 'Xilinx (AMD)' },
  { name: 'Altera', full: 'Altera (Intel)' },
  { name: 'Vishay', full: 'Vishay Intertechnology' },
  { name: 'Diodes', full: 'Diodes Incorporated' },
  { name: 'Maxim', full: 'Maxim Integrated' },
]

const domesticBrands = [
  { name: '兆易创新', full: 'GigaDevice' },
  { name: '紫光展锐', full: 'Unisoc' },
  { name: '全志科技', full: 'Allwinner' },
  { name: '芯朋微', full: 'ChipON' },
  { name: '国民技术', full: 'Nations Technologies' },
  { name: '上海贝岭', full: 'Belling' },
  { name: '华大半导体', full: 'HDSC' },
  { name: '中科蓝讯', full: 'Bluetrum' },
  { name: '博通集成', full: 'Beken' },
  { name: '乐鑫科技', full: 'Espressif' },
  { name: '汇顶科技', full: 'Goodix' },
  { name: '圣邦微', full: 'SG Micro' },
  { name: '思瑞浦', full: '3PEAK' },
  { name: '纳芯微', full: 'NOVOSENSE' },
  { name: '晶晨股份', full: 'Amlogic' },
  { name: '北京君正', full: 'Ingenic' },
  { name: '复旦微电', full: 'Fudan Micro' },
  { name: '比亚迪半导体', full: 'BYD Semi' },
]

function handleBrandClick(brand) {
  alert(`查看${brand.name}(${brand.full})产品`)
}
</script>

<style scoped>
.brand-section {
  padding: 20px 0 50px;
}
.brand-container {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 15px;
}
.brand-tabs {
  display: flex;
  justify-content: center;
  gap: 4px;
  margin-bottom: 24px;
}
.tab-item {
  padding: 8px 32px;
  font-size: 15px;
  cursor: pointer;
  border: 1px solid var(--color-gray-6);
  border-radius: 4px;
  color: var(--color-gray-2);
  transition: all var(--transition-fast);
}
.tab-item.active {
  background: var(--color-primary);
  color: var(--color-white);
  border-color: var(--color-primary);
}
.tab-item:hover:not(.active) {
  border-color: var(--color-primary);
  color: var(--color-primary);
}

.brand-grid {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 12px;
}
.brand-cell {
  background: var(--color-white);
  border: 1px solid var(--color-gray-7);
  border-radius: 6px;
  padding: 16px 8px;
  text-align: center;
  cursor: pointer;
  transition: all var(--transition-fast);
}
.brand-cell:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
  border-color: var(--color-primary);
}
.brand-logo {
  font-size: 13px;
  font-weight: 600;
  color: var(--color-dark);
  letter-spacing: 0.5px;
}

@media (max-width: 768px) {
  .brand-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
</style>
