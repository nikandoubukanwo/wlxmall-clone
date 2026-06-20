<template>
  <div class="brand-section section-white">
    <div class="section-title">{{ $t('home.brandTitle') }}</div>
    <p class="section-subtitle">{{ $t('home.brandSubtitle') }}</p>
    <div class="brand-container">
      <div class="brand-grid">
        <div
          class="brand-cell"
          v-for="(brand, i) in globalBrands"
          :key="i"
          @click="handleBrandClick(brand)"
          :title="brand.full"
        >
          <img
            v-if="brand.image"
            class="brand-logo-img"
            :src="brand.image"
            :alt="brand.name"
            loading="lazy"
          />
          <div v-else class="brand-logo-text">{{ brand.name }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const globalBrands = [
  { name: 'NVIDIA', full: 'NVIDIA', image: '/brands/nvidia.jpg' },
  { name: 'LINEAR', full: 'Linear Technology', image: '/brands/linear.png' },
  { name: 'Renesas', full: 'Renesas Electronics', image: '/brands/renesas.png' },
  { name: 'Freescale', full: 'Freescale Semiconductor', image: '/brands/freescale.png' },
  { name: 'Broadcom', full: 'Broadcom Inc.', image: '/brands/broadcom.png' },
  { name: 'Vishay', full: 'Vishay Intertechnology', image: '/brands/vishay.jpg' },
  { name: 'EXAR', full: 'EXAR Corporation', image: '/brands/exar.jpg' },
  { name: 'Diodes', full: 'Diodes Incorporated', image: '/brands/diodes.jpg' },
  { name: 'Avago', full: 'Avago Technologies', image: '/brands/avago.jpg' },
  { name: 'Atmel', full: 'Atmel Corporation', image: '/brands/atmel.jpg' },
  { name: 'Actel', full: 'Actel Corporation', image: '/brands/actel.jpg' },
  { name: 'Lattice', full: 'Lattice Semiconductor', image: '/brands/lattice.jpg' },
  { name: 'ADI', full: 'Analog Devices', image: '/brands/adi.jpg' },
  { name: 'TI', full: 'Texas Instruments', image: '/brands/ti.jpg' },
  { name: 'Maxim', full: 'Maxim Integrated', image: '/brands/maxim.jpg' },
  { name: 'SK Hynix', full: 'SK Hynix Inc.', image: '/brands/sk-hynix.jpg' },
  { name: 'Marvell', full: 'Marvell Technology', image: '/brands/marvell.jpg' },
  { name: 'Infineon', full: 'Infineon Technologies', image: '/brands/infineon.jpg' },
  { name: 'Toshiba', full: 'Toshiba Corporation', image: '/brands/toshiba.jpg' },
  { name: 'IOR', full: 'International Rectifier', image: '/brands/ior.jpg' },
  { name: 'ST', full: 'STMicroelectronics', image: '/brands/st.jpg' },
  { name: 'ON', full: 'ON Semiconductor', image: '/brands/on.jpg' },
  { name: 'NXP', full: 'NXP Semiconductors', image: '/brands/nxp.jpg' },
  { name: 'ISSI', full: 'Integrated Silicon Solution', image: '/brands/issi.jpg' },
  { name: 'Micron', full: 'Micron Technology', image: '/brands/micron.png' },
  { name: 'Xilinx', full: 'Xilinx (AMD)', image: '/brands/xilinx.jpg' },
  { name: 'Altera', full: 'Altera (Intel)', image: '/brands/altera.jpg' },
  { name: 'Samsung', full: 'Samsung Electronics', image: '/brands/samsung.jpg' },
  { name: 'Intel', full: 'Intel Corporation', image: '/brands/intel.jpg' },
]

function handleBrandClick(brand) {
  router.push({ path: '/search', query: { brand: brand.name } })
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
.brand-grid {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 12px;
}
.brand-cell {
  background: var(--color-white);
  border: 1px solid var(--color-gray-7);
  border-radius: 6px;
  padding: 12px 8px;
  text-align: center;
  cursor: pointer;
  transition: all var(--transition-fast);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 64px;
}
.brand-cell:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
  border-color: var(--color-primary);
}
.brand-logo-img {
  max-width: 100%;
  max-height: 48px;
  object-fit: contain;
  display: block;
}
.brand-logo-text {
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
