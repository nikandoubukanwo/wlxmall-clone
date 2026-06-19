<template>
  <div class="home">
    <TopBar />
    <Header />
    <NavBar />
    <BrandShowcase />
    <FindParts />
    <Footer />
    <RightSidebar />
  </div>
</template>

<script setup>
import TopBar from '@/components/TopBar.vue'
import Header from '@/components/Header.vue'
import NavBar from '@/components/NavBar.vue'
import BrandShowcase from '@/components/BrandShowcase.vue'
import FindParts from '@/components/FindParts.vue'
import Footer from '@/components/Footer.vue'
import RightSidebar from '@/components/RightSidebar.vue'
</script>

<style scoped>
.home {
  min-height: 100vh;
  background: var(--color-gray-9);
}
</style>
