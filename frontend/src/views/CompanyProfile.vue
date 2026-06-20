<template>
  <div class="about-page">
    <TopBar />
    <Header />

    <!-- Banner -->
    <div class="page-banner">
      <div class="banner-inner">
        <h1 class="banner-title">{{ $t('about.bannerTitle') }}</h1>
        <p class="banner-subtitle">{{ $t('about.bannerSubtitle') }}</p>
      </div>
    </div>

    <div class="container">
      <!-- Company Intro -->
      <section class="section intro-section">
        <div class="section-header">
          <h2 class="section-title">{{ $t('about.sectionTitle') }}</h2>
          <div class="section-divider"></div>
        </div>
        <div class="intro-content">
          <p>{{ $t('about.intro1') }}</p>
          <p>{{ $t('about.intro2') }}</p>
        </div>
      </section>

      <!-- Corporate Culture -->
      <section class="section culture-section">
        <div class="section-header">
          <h2 class="section-title">{{ $t('about.culture') }}</h2>
          <div class="section-divider"></div>
        </div>
        <div class="culture-grid">
          <div class="culture-card" v-for="(item, i) in cultureItems" :key="i">
            <div class="culture-icon">
              <el-icon :size="28"><component :is="item.icon" /></el-icon>
            </div>
            <h3 class="culture-label">{{ item.label }}</h3>
            <p class="culture-desc">{{ item.desc }}</p>
          </div>
        </div>
      </section>

      <!-- Contact -->
      <section id="contact" class="section contact-section">
        <div class="section-header">
          <h2 class="section-title">{{ $t('about.contactTitle') }}</h2>
          <div class="section-divider"></div>
        </div>
        <div class="contact-layout">
          <div class="contact-card">
            <div class="contact-row">
              <span class="contact-label">{{ $t('about.contactPerson') }}</span>
              <span class="contact-value">{{ $t('about.contactPersonValue') }}</span>
            </div>
            <div class="contact-row">
              <span class="contact-label">{{ $t('about.contactPhone') }}</span>
              <span class="contact-value">+8618823333285</span>
            </div>
            <div class="contact-row">
              <span class="contact-label">{{ $t('about.contactEmail') }}</span>
              <span class="contact-value">peilan@longkitech.com</span>
            </div>
            <div class="contact-row">
              <span class="contact-label">{{ $t('about.contactAddress') }}</span>
              <span class="contact-value">{{ $t('about.contactAddressValue') }}</span>
            </div>
          </div>
          <div class="contact-qrcode">
            <img src="/wechat.jpg" alt="微信二维码" />
            <span class="qrcode-label">扫一扫添加微信</span>
          </div>
        </div>
      </section>
    </div>

    <Footer />
    <RightSidebar />
  </div>
</template>

<script setup>
import { computed, onMounted, nextTick } from 'vue'
import { useI18n } from 'vue-i18n'
import { useRoute } from 'vue-router'
import TopBar from '@/components/TopBar.vue'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import RightSidebar from '@/components/RightSidebar.vue'

const { t } = useI18n()
const route = useRoute()

const cultureItems = computed(() => [
  { icon: 'Check', label: t('about.cultureCommitment'), desc: t('about.cultureCommitmentDesc') },
  { icon: 'TrendCharts', label: t('about.cultureGoal'), desc: t('about.cultureGoalDesc') },
  { icon: 'Service', label: t('about.cultureService'), desc: t('about.cultureServiceDesc') },
  { icon: 'Star', label: t('about.cultureValue'), desc: t('about.cultureValueDesc') },
])

onMounted(() => {
  if (route.hash === '#contact') {
    // 先等 Vue 渲染完成
    nextTick(() => {
      const el = document.getElementById('contact')
      if (el) el.scrollIntoView({ behavior: 'smooth' })
    })
    // 等页面所有资源（图片等）加载完再定位一次，防止布局偏移
    const onPageLoad = () => {
      const el = document.getElementById('contact')
      if (el) el.scrollIntoView({ behavior: 'smooth' })
    }
    if (document.readyState === 'complete') {
      onPageLoad()
    } else {
      window.addEventListener('load', onPageLoad, { once: true })
    }
  }
})
</script>

<style scoped>
.about-page {
  min-height: 100vh;
  background: var(--color-gray-9);
}

/* Banner */
.page-banner {
  background: linear-gradient(135deg, var(--color-primary) 0%, #003d85 100%);
  padding: 50px 0;
  text-align: center;
}
.banner-inner {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 15px;
}
.banner-title {
  font-size: 32px;
  font-weight: 700;
  color: var(--color-white);
  margin-bottom: 8px;
}
.banner-subtitle {
  font-size: 14px;
  color: rgba(255,255,255,0.7);
  letter-spacing: 2px;
}

/* Container */
.container {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 40px 15px;
}

/* Sections */
.section {
  background: var(--color-white);
  border-radius: 8px;
  padding: 36px 40px;
  box-shadow: var(--shadow-sm);
  margin-bottom: 24px;
}
.section-header {
  text-align: center;
  margin-bottom: 28px;
}
.section-title {
  font-size: 22px;
  font-weight: 700;
  color: var(--color-dark);
}
.section-divider {
  width: 50px;
  height: 3px;
  background: var(--color-primary);
  margin: 10px auto 0;
  border-radius: 2px;
}

/* Intro */
.intro-content p {
  font-size: 15px;
  line-height: 1.9;
  color: var(--color-gray-2);
  margin-bottom: 14px;
  text-indent: 2em;
}
.intro-content p:last-child {
  margin-bottom: 0;
}

/* Culture Grid */
.culture-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
}
.culture-card {
  text-align: center;
  padding: 28px 16px;
  border-radius: 8px;
  background: var(--color-gray-9);
  transition: transform var(--transition-fast), box-shadow var(--transition-fast);
}
.culture-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-popup);
}
.culture-icon {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: var(--color-primary);
  color: var(--color-white);
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 14px;
}
.culture-label {
  font-size: 16px;
  font-weight: 600;
  color: var(--color-dark);
  margin-bottom: 8px;
}
.culture-desc {
  font-size: 13px;
  line-height: 1.6;
  color: var(--color-gray-3);
}

/* Contact */
.contact-layout {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 50px;
}
.contact-card {
  max-width: 500px;
  flex: 1;
}
.contact-row {
  display: flex;
  padding: 12px 0;
  border-bottom: 1px solid var(--color-gray-8);
  font-size: 15px;
}
.contact-row:last-child {
  border-bottom: none;
}
.contact-label {
  width: 100px;
  color: var(--color-gray-3);
  flex-shrink: 0;
  font-weight: 500;
}
.contact-value {
  color: var(--color-dark);
  flex: 1;
}
.contact-qrcode {
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  padding: 16px;
  background: var(--color-gray-9);
  border-radius: 8px;
  border: 1px solid var(--color-gray-7);
}
.contact-qrcode img {
  width: 140px;
  height: 140px;
  display: block;
}
.qrcode-label {
  font-size: 13px;
  color: var(--color-gray-2);
}

@media (max-width: 768px) {
  .culture-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .contact-layout {
    flex-direction: column;
    gap: 24px;
  }
  .section {
    padding: 24px 18px;
  }
}
</style>
