<template>
  <div class="home">
    <TopBar />
    <Header />
    <NavBar />
    <HeroBanner />
    <WhyChoose />
    <BrandShowcase />
    <FindParts />
    <ServiceIndustries />
    <NewsCenter />
    <FeaturesBar />
    <Footer />
    <RightSidebar />
  </div>
</template>

<script setup>
import TopBar from '@/components/TopBar.vue'
import Header from '@/components/Header.vue'
import NavBar from '@/components/NavBar.vue'
import HeroBanner from '@/components/HeroBanner.vue'
import WhyChoose from '@/components/WhyChoose.vue'
import BrandShowcase from '@/components/BrandShowcase.vue'
import FindParts from '@/components/FindParts.vue'
import ServiceIndustries from '@/components/ServiceIndustries.vue'
import NewsCenter from '@/components/NewsCenter.vue'
import FeaturesBar from '@/components/FeaturesBar.vue'
import Footer from '@/components/Footer.vue'
import RightSidebar from '@/components/RightSidebar.vue'
</script>

<style scoped>
.home {
  min-height: 100vh;
  background: var(--color-gray-9);
}
</style>
