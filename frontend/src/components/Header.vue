<template>
  <div class="header">
    <div class="header-inner">
      <!-- Logo -->
      <div class="logo-area">
        <router-link to="/" class="logo-link">
          <img class="logo-img" src="/logo.png" alt="隆祺科技" />
          <div>
            <div class="logo">隆祺科技</div>
            <div class="logo-tag">Longkitech</div>
          </div>
        </router-link>
      </div>

      <!-- Nav Links -->
      <div class="header-nav">
        <router-link to="/" class="header-nav-link">{{ $t('nav.home') }}</router-link>
        <router-link to="/about" class="header-nav-link">{{ $t('nav.about') }}</router-link>
        <a class="header-nav-link" href="javascript:;" @click="goStock">{{ $t('nav.stock') }}</a>
        <a class="header-nav-link" href="javascript:;" @click="goContact">{{ $t('nav.contact') }}</a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

function goContact() {
  if (route.path === '/about') {
    if (route.hash === '#contact') {
      document.getElementById('contact')?.scrollIntoView({ behavior: 'smooth' })
    } else {
      router.push('/about#contact')
    }
  } else {
    router.push('/about#contact')
  }
}

function goStock() {
  if (route.path === '/') {
    document.getElementById('ic-stock')?.scrollIntoView({ behavior: 'smooth' })
  } else {
    router.push('/#ic-stock')
  }
}
</script>

<style scoped>
.header {
  background: var(--color-white);
  border-bottom: 1px solid var(--color-gray-7);
}
.header-inner {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 18px 15px;
  display: flex;
  align-items: center;
  gap: 30px;
}

/* Logo */
.logo-area {
  flex-shrink: 0;
}
.logo-link {
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
}
.logo-img {
  height: 66px;
  width: auto;
}
.logo {
  font-size: 34px;
  font-weight: 700;
  color: var(--color-primary);
  line-height: 1.0;
}
.logo-tag {
  font-weight: 500;
  font-size: 24px; color: var(--color-primary);

  margin-top: 2px;
}

/* Header Nav */
.header-nav {
  flex: 1;
  display: flex;
  align-items: center;
  gap: 4px;
  padding-left: 30px;
}
.header-nav-link {
  padding: 0 18px;
  color: var(--color-dark);
  font-size: 15px;
  font-weight: 500;
  line-height: 42px;
  text-decoration: none;
  border-radius: 4px;
  transition: all var(--transition-fast);
  white-space: nowrap;
}
.header-nav-link:hover {
  background: var(--color-gray-8);
  color: var(--color-primary);
}
.header-nav-link.router-link-active {
  color: var(--color-primary);
  font-weight: 600;
}

</style>
