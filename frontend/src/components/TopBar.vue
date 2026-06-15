<template>
  <div class="topbar">
    <div class="topbar-inner">
      <div class="topbar-left">
        <template v-if="!userStore.isLoggedIn">
          <span class="welcome">您好，</span>
          <a class="topbar-link" href="javascript:;" @click="handleLogin">请登录</a>
          <span class="separator">|</span>
          <a class="topbar-link" href="javascript:;" @click="handleRegister">免费注册</a>
        </template>
        <template v-else>
          <span class="welcome">您好，</span>
          <span class="username">{{ userStore.userInfo?.username || '用户' }}</span>
          <a class="topbar-link" href="javascript:;" @click="handleLogout">退出</a>
        </template>
      </div>
      <div class="topbar-right">
        <a class="topbar-link" href="javascript:;">我的订单</a>
        <span class="separator">|</span>
        <a class="topbar-link" href="javascript:;">会员中心</a>
        <span class="separator">|</span>
        <span class="contact-info">
          <el-icon><Phone /></el-icon>
          4000-306-326
        </span>
        <span class="separator">|</span>
        <a class="topbar-link qq-link" href="https://wpa1.qq.com/ExeLLyG7?_type=wpa&qidian=true" target="_blank">
          <el-icon><ChatDotSquare /></el-icon>
          4000306326
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from '@/store'

const userStore = useUserStore()

function handleLogin() {
  alert('登录功能开发中')
}

function handleRegister() {
  alert('注册功能开发中')
}

function handleLogout() {
  userStore.logout()
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
</style>
