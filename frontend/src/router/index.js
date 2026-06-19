import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import SearchResults from '@/views/SearchResults.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/search', name: 'Search', component: SearchResults },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
