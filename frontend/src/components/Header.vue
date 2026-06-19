<template>
  <div class="header">
    <div class="header-inner">
      <!-- Logo -->
      <div class="logo-area">
        <router-link to="/">
          <div class="logo">隆祺电子</div>
          <div class="logo-tag">电子元器件采购网</div>
        </router-link>
      </div>

      <!-- Search -->
      <div class="search-area">
        <div class="search-box">
          <input
            v-model="keyword"
            class="search-input"
            type="text"
            placeholder="请输入采购的型号！"
            @keyup.enter="handleSearch"
          />
          <div class="search-camera">
            <el-icon><Camera /></el-icon>
          </div>
          <button class="search-btn" @click="handleSearch">
            <el-icon><Search /></el-icon>
            搜索
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const keyword = ref('')

function handleSearch() {
  if (keyword.value.trim()) {
    router.push({ path: '/search', query: { keyword: keyword.value.trim() } })
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
.logo {
  font-size: 28px;
  font-weight: 700;
  color: var(--color-primary);
  line-height: 1.2;
}
.logo-tag {
  font-size: 12px;
  color: var(--color-gray-4);
  margin-top: 2px;
}

/* Search */
.search-area {
  flex: 1;
}
.search-box {
  display: flex;
  height: 42px;
}
.search-input {
  flex: 1;
  height: 100%;
  border: 2px solid var(--color-primary);
  border-right: none;
  border-radius: 4px 0 0 4px;
  padding: 0 16px;
  font-size: 14px;
  outline: none;
  color: var(--color-dark);
}
.search-input::placeholder {
  color: var(--color-gray-4);
}
.search-camera {
  display: flex;
  align-items: center;
  padding: 0 10px;
  border: 2px solid var(--color-primary);
  border-left: none;
  border-right: none;
  color: var(--color-gray-4);
  cursor: pointer;
  transition: color var(--transition-fast);
}
.search-camera:hover {
  color: var(--color-primary);
}
.search-btn {
  height: 100%;
  padding: 0 24px;
  background: var(--color-primary);
  color: var(--color-white);
  border: none;
  border-radius: 0 4px 4px 0;
  font-size: 16px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 4px;
  transition: background var(--transition-fast);
}
.search-btn:hover {
  background: var(--color-primary-hover);
}

</style>
