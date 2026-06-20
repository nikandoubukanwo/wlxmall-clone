<template>
  <div class="search-page">
    <!-- TopBar -->
    <TopBar />

    <!-- Header with search -->
    <div class="search-header-bar">
      <div class="header-inner">
        <router-link to="/" class="search-logo">
          <img class="logo-img" src="/logo.png" alt="隆祺科技" />
          <div>
            <div class="logo">隆祺科技</div>
            <div class="logo-tag">Longkitech</div>
          </div>
        </router-link>
        <div class="search-box-area">
          <div class="search-box">
            <input
              v-model="searchKeyword"
              class="search-input"
              type="text"
              :placeholder="$t('search.placeholder')"
              @keyup.enter="doSearch"
            />
            <button class="search-btn" @click="doSearch">
              <el-icon><Search /></el-icon>
              {{ $t('search.submit') }}
            </button>
          </div>
        </div>
      </div>
    </div>

    <div class="container">
      <!-- Filter bar -->
      <div class="filter-bar">
        <div class="filter-row">
          <div class="filter-item">
            <label class="filter-label">{{ $t('search.filterModel') }}</label>
            <input v-model="filterKeyword" class="filter-input" :placeholder="$t('search.filterModelPlaceholder')" @keyup.enter="doSearch" />
          </div>
          <div class="filter-item">
            <label class="filter-label">{{ $t('search.filterBrand') }}</label>
            <input v-model="filterBrand" class="filter-input" :placeholder="$t('search.filterBrandPlaceholder')" @keyup.enter="doSearch" />
          </div>
          <div class="filter-item">
            <label class="filter-label">{{ $t('search.filterPkg') }}</label>
            <input v-model="filterPkg" class="filter-input" :placeholder="$t('search.filterPkgPlaceholder')" @keyup.enter="doSearch" />
          </div>
          <button class="filter-btn" @click="doSearch">
            <el-icon><Search /></el-icon>
            {{ $t('search.submit') }}
          </button>
          <button class="reset-btn" @click="resetFilters">{{ $t('search.reset') }}</button>
        </div>
      </div>

      <!-- Result summary -->
      <div class="result-header">
        <div class="result-summary">
          {{ $t('search.resultLabel') }} <span class="total-hint">{{ $t('search.totalRecords', { count: total }) }}</span>
        </div>
      </div>

      <!-- Results table -->
      <div class="table-wrapper">
        <el-table
          :data="items"
          v-loading="loading"
          stripe
          :empty-text="$t('search.emptyText')"
          style="width: 100%"
        >
          <el-table-column :label="$t('search.index')" type="index" width="70" />
          <el-table-column :label="$t('search.productModel')" prop="model" min-width="200">
            <template #default="{ row }">
              <a class="model-link" href="javascript:;" @click="searchByModel(row.model)">
                {{ row.model }}
              </a>
            </template>
          </el-table-column>
          <el-table-column :label="$t('search.filterBrand')" prop="brand" min-width="180">
            <template #default="{ row }">
              <a class="brand-link" href="javascript:;" @click="searchByBrand(row.brand)">
                {{ row.brand }}
              </a>
            </template>
          </el-table-column>
          <el-table-column :label="$t('search.filterPkg')" prop="pkg" min-width="160" />
        </el-table>
      </div>

      <!-- Pagination -->
      <div class="pagination-wrap" v-if="total > pageSize">
        <el-pagination
          v-model:current-page="currentPage"
          :page-size="pageSize"
          :total="total"
          layout="prev, pager, next"
          @current-change="onPageChange"
        />
      </div>
    </div>

    <!-- Footer -->
    <Footer />
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { productAPI } from '@/api/index.js'
import TopBar from '@/components/TopBar.vue'
import Footer from '@/components/Footer.vue'

const route = useRoute()
const router = useRouter()

const loading = ref(false)
const items = ref([])
const total = ref(0)
const currentPage = ref(1)
const pageSize = 20

// Search box at top
const searchKeyword = ref('')

// Filter inputs
const filterKeyword = ref('')
const filterBrand = ref('')
const filterPkg = ref('')

// Sync from route on mount
function syncFromRoute() {
  searchKeyword.value = route.query.keyword || ''
  filterKeyword.value = route.query.keyword || ''
  filterBrand.value = route.query.brand || ''
  filterPkg.value = route.query.pkg || ''
  currentPage.value = Number(route.query.page) || 1
}

async function fetchData(page = 1) {
  loading.value = true
  try {
    const params = { page, page_size: pageSize }
    if (filterKeyword.value) params.keyword = filterKeyword.value
    if (filterBrand.value) params.brand = filterBrand.value
    if (filterPkg.value) params.pkg = filterPkg.value
    const res = await productAPI.search(params)
    items.value = res.items || []
    total.value = res.total || 0
  } catch (e) {
    console.error('Search error:', e)
    items.value = []
    total.value = 0
  } finally {
    loading.value = false
  }
}

function doSearch() {
  const query = {}
  const kw = searchKeyword.value || filterKeyword.value
  if (kw) query.keyword = kw.trim()
  if (filterBrand.value) query.brand = filterBrand.value.trim()
  if (filterPkg.value) query.pkg = filterPkg.value.trim()
  router.push({ path: '/search', query })
}

function resetFilters() {
  filterKeyword.value = ''
  filterBrand.value = ''
  filterPkg.value = ''
  searchKeyword.value = ''
  router.push({ path: '/search' })
}

function onPageChange(page) {
  currentPage.value = page
  const query = { ...route.query, page }
  router.replace({ path: '/search', query })
}

function searchByModel(model) {
  router.push({ path: '/search', query: { keyword: model } })
}

function searchByBrand(brandName) {
  router.push({ path: '/search', query: { ...route.query, brand: brandName, page: undefined } })
}

watch(
  () => [route.query.keyword, route.query.brand, route.query.pkg, route.query.page],
  () => {
    syncFromRoute()
    fetchData(currentPage.value)
  },
  { immediate: true }
)

onMounted(syncFromRoute)
</script>

<style scoped>
.search-page {
  min-height: 100vh;
  background: var(--color-gray-9);
}

/* Header */
.search-header-bar {
  background: var(--color-white);
  border-bottom: 1px solid var(--color-gray-7);
}
.header-inner {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 14px 15px;
  display: flex;
  align-items: center;
  gap: 30px;
}
.search-logo {
  flex-shrink: 0;
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 10px;
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
.search-box-area {
  flex: 1;
}
.search-box {
  display: flex;
  height: 50px;
  max-width: 600px;
}
.search-input {
  flex: 1;
  height: 100%;
  border: 2px solid var(--color-primary);
  border-right: none;
  border-radius: 4px 0 0 4px;
  padding: 0 14px;
  font-size: 14px;
  outline: none;
  color: var(--color-dark);
}
.search-input::placeholder {
  color: var(--color-gray-4);
}
.search-btn {
  height: 100%;
  padding: 0 22px;
  background: var(--color-primary);
  color: var(--color-white);
  border: none;
  border-radius: 0 4px 4px 0;
  font-size: 15px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 4px;
  transition: background var(--transition-fast);
}
.search-btn:hover {
  background: var(--color-primary-hover);
}

/* Container */
.container {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 16px 15px;
}

/* Filter bar */
.filter-bar {
  background: var(--color-white);
  border-radius: 6px;
  padding: 16px 20px;
  box-shadow: var(--shadow-sm);
  margin-bottom: 16px;
}
.filter-row {
  display: flex;
  align-items: flex-end;
  gap: 14px;
  flex-wrap: wrap;
}
.filter-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.filter-label {
  font-size: 13px;
  color: var(--color-gray-2);
  font-weight: 500;
}
.filter-input {
  width: 150px;
  height: 36px;
  border: 1px solid var(--color-gray-6);
  border-radius: 4px;
  padding: 0 10px;
  font-size: 13px;
  outline: none;
  color: var(--color-dark);
  transition: border-color var(--transition-fast);
}
.filter-input:focus {
  border-color: var(--color-primary);
}
.filter-btn {
  height: 36px;
  padding: 0 20px;
  background: var(--color-primary);
  color: var(--color-white);
  border: none;
  border-radius: 4px;
  font-size: 14px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 4px;
  transition: background var(--transition-fast);
}
.filter-btn:hover {
  background: var(--color-primary-hover);
}
.reset-btn {
  height: 36px;
  padding: 0 16px;
  background: var(--color-white);
  color: var(--color-gray-2);
  border: 1px solid var(--color-gray-6);
  border-radius: 4px;
  font-size: 13px;
  cursor: pointer;
  transition: all var(--transition-fast);
}
.reset-btn:hover {
  border-color: var(--color-primary);
  color: var(--color-primary);
}

/* Result header */
.result-header {
  margin-bottom: 12px;
}
.result-summary {
  font-size: 15px;
  color: var(--color-gray-2);
}
.total-hint {
  margin-left: 10px;
  color: var(--color-primary);
  font-weight: 500;
}

/* Table */
.table-wrapper {
  background: var(--color-white);
  border-radius: 6px;
  box-shadow: var(--shadow-sm);
}
.model-link {
  color: var(--color-primary);
  text-decoration: none;
  font-weight: 500;
}
.model-link:hover {
  text-decoration: underline;
}
.brand-link {
  color: var(--color-dark);
  text-decoration: none;
}
.brand-link:hover {
  color: var(--color-primary);
}
.pagination-wrap {
  display: flex;
  justify-content: center;
  margin-top: 20px;
  padding: 10px;
}
</style>
