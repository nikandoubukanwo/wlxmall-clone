import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useCartStore = defineStore('cart', () => {
  const items = ref([])
  const count = computed(() => items.value.reduce((s, i) => s + i.qty, 0))
  function addItem(product) {
    const existing = items.value.find(i => i.id === product.id)
    if (existing) existing.qty += (product.qty || 1)
    else items.value.push({ ...product, qty: product.qty || 1 })
  }
  function removeItem(id) { items.value = items.value.filter(i => i.id !== id) }
  function updateQty(id, qty) {
    const item = items.value.find(i => i.id === id)
    if (item) item.qty = qty
  }
  function clear() { items.value = [] }
  return { items, count, addItem, removeItem, updateQty, clear }
})

export const useInquiryStore = defineStore('inquiry', () => {
  const items = ref([])
  const count = computed(() => items.value.reduce((s, i) => s + i.qty, 0))
  function addItem(product) {
    const existing = items.value.find(i => i.id === product.id)
    if (existing) existing.qty += (product.qty || 1)
    else items.value.push({ ...product, qty: product.qty || 1 })
  }
  function removeItem(id) { items.value = items.value.filter(i => i.id !== id) }
  function clear() { items.value = [] }
  return { items, count, addItem, removeItem, clear }
})

export const useUserStore = defineStore('user', () => {
  const isLoggedIn = ref(false)
  const userInfo = ref(null)
  function login(info) {
    isLoggedIn.value = true
    userInfo.value = info
    localStorage.setItem('token', info.token)
  }
  function logout() {
    isLoggedIn.value = false
    userInfo.value = null
    localStorage.removeItem('token')
  }
  function checkLogin() {
    const token = localStorage.getItem('token')
    if (token) isLoggedIn.value = true
  }
  return { isLoggedIn, userInfo, login, logout, checkLogin }
})
