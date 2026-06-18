<template>
  <div class="hero-banner-wrapper" @mouseenter="pauseAutoPlay" @mouseleave="resumeAutoPlay">
    <div class="hero-banner-container">
      <!-- LEFT: empty spacing aligned with category menu -->
      <div class="hero-left-spacer"></div>

      <!-- CENTER: Carousel slider -->
      <div class="hero-carousel">
        <div class="carousel-track" :style="{ transform: `translateX(-${currentSlide * 100}%)` }">
          <div class="carousel-slide slide-1">
            <div class="slide-content">
              <div class="slide-brand">隆祺电子</div>
              <div class="slide-tagline">电子元器件采购网</div>
              <div class="slide-desc">原装正品 · 极速发货 · 一站式采购</div>
              <button class="slide-btn">立即选购</button>
            </div>
          </div>
          <div class="carousel-slide slide-2">
            <div class="slide-content">
              <div class="slide-brand">TI、ADI 热门现货</div>
              <div class="slide-tagline">德州仪器 / 亚德诺半导体</div>
              <div class="slide-desc">海量现货 · 当日发货 · 价格优势</div>
              <button class="slide-btn">查看库存</button>
            </div>
          </div>
          <div class="carousel-slide slide-3">
            <div class="slide-content">
              <div class="slide-brand">电容现货促销</div>
              <div class="slide-tagline">三星 / 村田 / 国巨</div>
              <div class="slide-desc">全系列MLCC电容 · 批量特惠价格</div>
              <button class="slide-btn">了解详情</button>
            </div>
          </div>
        </div>

        <!-- Dot indicators -->
        <div class="carousel-dots">
          <span
            v-for="(_, index) in 3"
            :key="index"
            :class="['dot', { active: currentSlide === index }]"
            @click="goToSlide(index)"
          ></span>
        </div>
      </div>

      <!-- RIGHT: Sidebar -->
      <div class="hero-sidebar">
        <!-- Welcome section -->
        <div class="sidebar-welcome">
          <div class="welcome-avatar">
            <svg viewBox="0 0 40 40" width="40" height="40">
              <circle cx="20" cy="20" r="20" fill="#e0e0e0"/>
              <circle cx="20" cy="14" r="6" fill="#bdbdbd"/>
              <ellipse cx="20" cy="30" rx="12" ry="10" fill="#bdbdbd"/>
            </svg>
          </div>
          <div class="welcome-text">HI~欢迎访问隆祺电子</div>
          <div class="welcome-actions">
            <button class="action-btn login-btn">登录</button>
            <button class="action-btn register-btn">免费注册</button>
          </div>
        </div>

        <!-- 万联快报 section -->
        <div class="sidebar-news">
          <div class="news-header">
            <span class="news-title">隆祺快报</span>
            <a href="#" class="news-more">更多 &gt;</a>
          </div>
          <ul class="news-list">
            <li class="news-item" v-for="(item, idx) in newsItems" :key="idx">
              <span class="news-tag">快报</span>
              <span class="news-text">{{ item }}</span>
            </li>
          </ul>
        </div>

        <!-- Quick entry icons -->
        <div class="sidebar-quick">
          <div class="quick-item" v-for="entry in quickEntries" :key="entry.label">
            <div class="quick-icon" :style="{ background: entry.bg }">
              <svg viewBox="0 0 24 24" width="20" height="20" fill="#fff">
                <path :d="entry.iconPath"/>
              </svg>
            </div>
            <span class="quick-label">{{ entry.label }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const currentSlide = ref(0)
let autoPlayTimer = null
const AUTO_PLAY_INTERVAL = 4000

const newsItems = [
  '芯闻 | TI推出新一代电源管理芯片',
  '库存 | 村田MLCC大量到货通知',
  '促销 | 国巨电阻全场8折特惠',
  '新品 | ADI发布高精度ADC系列',
  '活动 | 新用户注册即享满减优惠'
]

const quickEntries = [
  { label: '领券中心', bg: 'linear-gradient(135deg, #ff6b6b, #ee5a24)', iconPath: 'M4 4h16v4H4V4zm0 6h16v10H4V10zm3 2h2v6H7v-6zm6 0h2v6h-2v-6z' },
  { label: '呆料寄售', bg: 'linear-gradient(135deg, #667eea, #764ba2)', iconPath: 'M12 2l10 6v8l-10 6-10-6V8l10-6zm0 2.5L4.5 9l7.5 4.5L19.5 9 12 4.5z' },
  { label: '供应商登记', bg: 'linear-gradient(135deg, #f093fb, #f5576c)', iconPath: 'M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5s-3 1.34-3 3 1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z' },
  { label: '原厂直订', bg: 'linear-gradient(135deg, #4facfe, #00f2fe)', iconPath: 'M19 3H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.11 0 2-.9 2-2V5c0-1.1-.89-2-2-2zm-2 10h-4v4h-2v-4H7v-2h4V7h2v4h4v2z' }
]

function goToSlide(index) {
  currentSlide.value = index
}

function startAutoPlay() {
  stopAutoPlay()
  autoPlayTimer = setInterval(() => {
    currentSlide.value = (currentSlide.value + 1) % 3
  }, AUTO_PLAY_INTERVAL)
}

function stopAutoPlay() {
  if (autoPlayTimer) {
    clearInterval(autoPlayTimer)
    autoPlayTimer = null
  }
}

function pauseAutoPlay() {
  stopAutoPlay()
}

function resumeAutoPlay() {
  startAutoPlay()
}

onMounted(() => {
  startAutoPlay()
})

onBeforeUnmount(() => {
  stopAutoPlay()
})
</script>

<style scoped>
.hero-banner-wrapper {
  width: 100%;
  background: #f5f5f5;
}

.hero-banner-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  height: 380px;
}

/* ---- LEFT SPACER ---- */
.hero-left-spacer {
  width: 220px;
  flex-shrink: 0;
}

/* ---- CAROUSEL ---- */
.hero-carousel {
  flex: 1;
  position: relative;
  overflow: hidden;
  min-width: 0;
}

.carousel-track {
  display: flex;
  height: 100%;
  transition: transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  will-change: transform;
}

.carousel-slide {
  min-width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}

.slide-1 {
  background: linear-gradient(135deg, #c62828 0%, #e53935 30%, #ef5350 60%, #ffcdd2 100%);
}

.slide-2 {
  background: linear-gradient(135deg, #0d47a1 0%, #1565c0 30%, #1976d2 60%, #bbdefb 100%);
}

.slide-3 {
  background: linear-gradient(135deg, #e65100 0%, #ef6c00 30%, #f57c00 60%, #ffe0b2 100%);
}

.slide-content {
  text-align: center;
  color: #fff;
  padding: 20px;
}

.slide-brand {
  font-size: 36px;
  font-weight: 700;
  letter-spacing: 2px;
  margin-bottom: 8px;
  text-shadow: 0 2px 8px rgba(0,0,0,0.2);
}

.slide-tagline {
  font-size: 20px;
  font-weight: 500;
  margin-bottom: 6px;
  opacity: 0.95;
}

.slide-desc {
  font-size: 14px;
  opacity: 0.8;
  margin-bottom: 20px;
}

.slide-btn {
  display: inline-block;
  padding: 10px 32px;
  border: 2px solid rgba(255,255,255,0.9);
  border-radius: 24px;
  background: transparent;
  color: #fff;
  font-size: 15px;
  cursor: pointer;
  transition: all 0.3s;
}

.slide-btn:hover {
  background: rgba(255,255,255,0.2);
  border-color: #fff;
  transform: scale(1.05);
}

/* Dots */
.carousel-dots {
  position: absolute;
  bottom: 16px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 10px;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: rgba(255,255,255,0.45);
  cursor: pointer;
  transition: all 0.3s;
}

.dot.active {
  background: #fff;
  transform: scale(1.25);
}

.dot:hover {
  background: rgba(255,255,255,0.8);
}

/* ---- SIDEBAR ---- */
.hero-sidebar {
  width: 230px;
  flex-shrink: 0;
  background: #fff;
  display: flex;
  flex-direction: column;
  border-left: 1px solid #eee;
}

/* Welcome */
.sidebar-welcome {
  padding: 18px 16px 14px;
  text-align: center;
  border-bottom: 1px solid #f0f0f0;
}

.welcome-avatar {
  margin-bottom: 6px;
}

.welcome-text {
  font-size: 13px;
  color: #333;
  margin-bottom: 10px;
  font-weight: 500;
}

.welcome-actions {
  display: flex;
  gap: 10px;
  justify-content: center;
}

.action-btn {
  flex: 1;
  padding: 6px 0;
  border: 1px solid #c62828;
  border-radius: 4px;
  font-size: 13px;
  cursor: pointer;
  transition: all 0.25s;
}

.login-btn {
  background: #c62828;
  color: #fff;
}

.login-btn:hover {
  background: #b71c1c;
}

.register-btn {
  background: #fff;
  color: #c62828;
}

.register-btn:hover {
  background: #fff5f5;
}

/* News */
.sidebar-news {
  padding: 12px 16px;
  border-bottom: 1px solid #f0f0f0;
  flex-shrink: 0;
}

.news-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.news-title {
  font-size: 14px;
  font-weight: 700;
  color: #333;
}

.news-more {
  font-size: 12px;
  color: #999;
  text-decoration: none;
}

.news-more:hover {
  color: #c62828;
}

.news-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.news-item {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 4px 0;
  font-size: 12px;
  color: #555;
  white-space: nowrap;
  overflow: hidden;
}

.news-tag {
  flex-shrink: 0;
  display: inline-block;
  padding: 1px 5px;
  background: #ff6d00;
  color: #fff;
  font-size: 11px;
  border-radius: 3px;
  font-weight: 600;
}

.news-text {
  overflow: hidden;
  text-overflow: ellipsis;
}

/* Quick entries */
.sidebar-quick {
  display: flex;
  gap: 0;
  padding: 14px 10px;
  justify-content: space-between;
}

.quick-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  cursor: pointer;
  transition: transform 0.2s;
}

.quick-item:hover {
  transform: translateY(-2px);
}

.quick-icon {
  width: 38px;
  height: 38px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.quick-label {
  font-size: 11px;
  color: #555;
  white-space: nowrap;
}
</style>
