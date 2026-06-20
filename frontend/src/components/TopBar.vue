<template>
  <div class="topbar">
    <div class="topbar-inner">
      <div class="topbar-left">
        <span class="contact-info">
          <el-icon><Phone /></el-icon>
          {{ $t('topbar.phone') }}
        </span>
      </div>
      <div class="topbar-right">
        <div class="lang-switcher">
          <span
            class="lang-option"
            :class="{ active: currentLang === 'zh' }"
            @click="switchLang('zh')"
          >{{ $t('language.zh') }}</span>
          <span class="lang-sep">/</span>
          <span
            class="lang-option"
            :class="{ active: currentLang === 'en' }"
            @click="switchLang('en')"
          >{{ $t('language.en') }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useI18n } from 'vue-i18n'
import zhCn from 'element-plus/dist/locale/zh-cn.mjs'
import en from 'element-plus/dist/locale/en.mjs'

const { locale } = useI18n()
const currentLang = ref(localStorage.getItem('lang') || 'zh')

function switchLang(lang) {
  currentLang.value = lang
  locale.value = lang
  localStorage.setItem('lang', lang)
  window.location.reload()
}
</script>

<style scoped>
.topbar {
  height: var(--topbar-height);
  background-color: var(--color-dark);
  color: var(--color-gray-4);
  font-size: var(--font-xs);
  line-height: var(--topbar-height);
}
.topbar-inner {
  max-width: var(--max-width);
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 100%;
  padding: 0 15px;
}
.topbar-left,
.topbar-right {
  display: flex;
  align-items: center;
  gap: 8px;
}
.welcome {
  color: var(--color-gray-4);
}
.username {
  color: var(--color-primary-light);
  font-weight: 500;
}
.topbar-link {
  color: var(--color-gray-4);
  transition: color var(--transition-fast);
  cursor: pointer;
}
.topbar-link:hover {
  color: var(--color-primary-light);
}
.separator {
  color: var(--color-gray-1);
  margin: 0 2px;
}
.contact-info {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  color: var(--color-primary-light);
  font-weight: 500;
}
.qq-link {
  display: inline-flex;
  align-items: center;
  gap: 3px;
}
.lang-switcher {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  margin-left: 2px;
}
.lang-option {
  color: var(--color-gray-4);
  cursor: pointer;
  transition: color var(--transition-fast);
  font-size: 12px;
}
.lang-option:hover {
  color: var(--color-primary-light);
}
.lang-option.active {
  color: var(--color-primary-light);
  font-weight: 600;
}
.lang-sep {
  color: var(--color-gray-1);
}
</style>
