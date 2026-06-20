<template>
  <div class="find-parts-section section-gray">
    <div class="find-parts-container">
      <!-- Left: Search Form -->
      <div class="find-form-panel">
        <div class="form-title">{{ $t('home.findParts.title') }}</div>
        <div class="form-body">
          <div class="form-row">
            <label class="form-label">{{ $t('home.findParts.model') }}</label>
            <input v-model="keyword" class="input" :placeholder="$t('home.findParts.modelPlaceholder')" @keyup.enter="handleSearch" />
          </div>
          <div class="form-row">
            <label class="form-label">{{ $t('home.findParts.brand') }}</label>
            <input v-model="brand" class="input" :placeholder="$t('home.findParts.brandPlaceholder')" @keyup.enter="handleSearch" />
          </div>
          <div class="form-row">
            <label class="form-label">{{ $t('home.findParts.pkg') }}</label>
            <input v-model="pkg" class="input" :placeholder="$t('home.findParts.pkgPlaceholder')" @keyup.enter="handleSearch" />
          </div>
          <button class="submit-btn" @click="handleSearch">{{ $t('home.findParts.submit') }}</button>
        </div>
      </div>

      <!-- Right: Hot Products Table -->
      <div class="hot-products-panel">
        <div class="hot-title">{{ $t('home.findParts.hotTitle') }}</div>
        <div class="table-wrapper">
          <table class="table">
            <thead>
              <tr>
                <th>{{ $t('home.findParts.rank') }}</th>
                <th>{{ $t('home.findParts.productModel') }}</th>
                <th>{{ $t('home.findParts.brand') }}</th>
                <th>{{ $t('home.findParts.pkg') }}</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(item, i) in hotProducts" :key="item.id">
                <td class="rank-cell">{{ (hotPage - 1) * hotPageSize + i + 1 }}</td>
                <td>
                  <a class="link" href="javascript:;" @click="searchByModel(item.model)">{{ item.model }}</a>
                </td>
                <td>{{ item.brand }}</td>
                <td>{{ item.pkg }}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <!-- Hot products pagination -->
        <div class="hot-pagination" v-if="hotTotal > hotPageSize">
          <button class="page-btn" :disabled="hotPage <= 1" @click="loadHot(hotPage - 1)">‹</button>
          <span class="page-info">{{ hotPage }} / {{ hotTotalPages }}</span>
          <button class="page-btn" :disabled="hotPage >= hotTotalPages" @click="loadHot(hotPage + 1)">›</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { productAPI } from '@/api/index.js'

const router = useRouter()

// Search form state
const keyword = ref('')
const brand = ref('')
const pkg = ref('')

// Hot products state
const hotProducts = ref([])
const hotPage = ref(1)
const hotTotal = ref(0)
const hotPageSize = 10

const hotTotalPages = computed(() => Math.max(1, Math.ceil(hotTotal.value / hotPageSize)))

async function loadHot(page = 1) {
  try {
    const res = await productAPI.hotList({ page, page_size: hotPageSize })
    hotProducts.value = res.items || []
    hotTotal.value = res.total || 0
    hotPage.value = page
  } catch (e) {
    console.error('Failed to load hot products:', e)
  }
}

function handleSearch() {
  const query = {}
  if (keyword.value) query.keyword = keyword.value.trim()
  if (brand.value) query.brand = brand.value.trim()
  if (pkg.value) query.pkg = pkg.value.trim()
  router.push({ path: '/search', query })
}

function searchByModel(model) {
  router.push({ path: '/search', query: { keyword: model } })
}

onMounted(() => loadHot(1))
</script>

<style scoped>
.find-parts-section {
  padding: 30px 0;
}
.find-parts-container {
  max-width: var(--max-width);
  margin: 0 auto;
  display: flex;
  gap: 24px;
  padding: 0 15px;
}

/* Left Form */
.find-form-panel {
  width: 280px;
  flex-shrink: 0;
  background: var(--color-white);
  border-radius: 6px;
  box-shadow: var(--shadow-sm);
  overflow: hidden;
}
.form-title {
  background: var(--color-primary);
  color: var(--color-white);
  font-size: 16px;
  font-weight: 600;
  padding: 14px 20px;
  text-align: center;
}
.form-body {
  padding: 16px 18px;
}
.form-row {
  margin-bottom: 14px;
}
.form-label {
  display: block;
  font-size: 13px;
  color: var(--color-gray-2);
  margin-bottom: 5px;
  font-weight: 500;
}
.form-input-group {
  display: flex;
  gap: 8px;
}
.form-input-group .input {
  flex: 1;
}
.form-select {
  width: 80px;
  border: 1px solid var(--color-gray-6);
  border-radius: 4px;
  padding: 0 8px;
  font-size: 13px;
  color: var(--color-dark);
  outline: none;
}
.price-input {
  position: relative;
}
.price-prefix {
  position: absolute;
  left: 10px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--color-gray-4);
  font-size: 14px;
  z-index: 1;
}
.price-input .input {
  padding-left: 24px;
}
.submit-btn {
  width: 100%;
  height: 38px;
  background: var(--color-primary);
  color: var(--color-white);
  border: none;
  border-radius: 4px;
  font-size: 15px;
  font-weight: 500;
  cursor: pointer;
  transition: background var(--transition-fast);
  margin-top: 4px;
}
.submit-btn:hover {
  background: var(--color-primary-hover);
}

/* Right Table */
.hot-products-panel {
  flex: 1;
  min-width: 0;
}
.hot-title {
  font-size: 18px;
  font-weight: 600;
  color: var(--color-dark);
  margin-bottom: 14px;
  padding-left: 2px;
}
.hot-title::before {
  content: '';
  display: inline-block;
  width: 4px;
  height: 18px;
  background: var(--color-primary);
  margin-right: 8px;
  vertical-align: middle;
  border-radius: 2px;
}
.table-wrapper {
  max-height: 480px;
  overflow-y: auto;
  background: var(--color-white);
  border-radius: 6px;
  box-shadow: var(--shadow-sm);
}
.table th {
  position: sticky;
  top: 0;
  z-index: 1;
}
.rank-cell {
  color: var(--color-gray-4);
  font-size: 12px;
}
.link {
  color: var(--color-primary);
  text-decoration: none;
  font-weight: 500;
}
.link:hover {
  text-decoration: underline;
}
.hot-pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;
  margin-top: 10px;
}
.page-btn {
  padding: 4px 12px;
  border: 1px solid var(--color-gray-6);
  border-radius: 4px;
  background: var(--color-white);
  cursor: pointer;
  font-size: 14px;
  color: var(--color-gray-2);
}
.page-btn:hover:not(:disabled) {
  border-color: var(--color-primary);
  color: var(--color-primary);
}
.page-btn:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}
.page-info {
  font-size: 13px;
  color: var(--color-gray-4);
}
</style>
