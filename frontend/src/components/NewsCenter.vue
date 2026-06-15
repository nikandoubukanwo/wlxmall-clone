<template>
  <div class="news-section section-gray">
    <div class="section-title">资讯中心</div>
    <p class="section-subtitle">了解最新行业动态与技术前沿</p>
    <div class="news-container">
      <!-- Column 1: Brand News -->
      <div class="news-column">
        <div class="col-header">
          <span>品牌资讯</span>
          <a class="col-more" href="javascript:;">更多&gt;</a>
        </div>
        <div class="featured-article">
          <div class="featured-img brand-img">
            <span>ADI</span>
          </div>
          <div class="featured-title">一文读懂亚德诺半导体（ADI）公司、核心产品、运用领域</div>
          <p class="featured-desc">亚德诺半导体是全球领先的高性能模拟、混合信号和数字信号处理集成电路设计、制造和营销厂商...</p>
        </div>
        <ul class="article-list">
          <li v-for="(item, i) in brandNews" :key="i">
            <span class="article-date">{{ item.date }}</span>
            <a class="article-link" href="javascript:;">{{ item.title }}</a>
            <span class="article-views">{{ item.views }}次</span>
          </li>
        </ul>
      </div>

      <!-- Column 2: Industry News -->
      <div class="news-column">
        <div class="col-header">
          <span>行业资讯</span>
          <a class="col-more" href="javascript:;">更多&gt;</a>
        </div>
        <div class="featured-article">
          <div class="featured-img industry-img">
            <span>光模块</span>
          </div>
          <div class="featured-title">一文读懂什么是光模块、内部结构、所用器件、用途？</div>
          <p class="featured-desc">光模块，全称光收发一体模块，是光纤通信系统中的核心器件。它的作用简单来说就是完成光电转换...</p>
        </div>
        <ul class="article-list">
          <li v-for="(item, i) in industryNews" :key="i">
            <span class="article-date">{{ item.date }}</span>
            <a class="article-link" href="javascript:;">{{ item.title }}</a>
            <span class="article-views">{{ item.views }}次</span>
          </li>
        </ul>
      </div>

      <!-- Column 3: Product News -->
      <div class="news-column">
        <div class="col-header">
          <span>产品资讯</span>
          <a class="col-more" href="javascript:;">更多&gt;</a>
        </div>
        <ul class="article-list full-list">
          <li v-for="(item, i) in productNews" :key="i">
            <span class="article-date">{{ item.date }}</span>
            <a class="article-link" href="javascript:;">{{ item.title }}</a>
            <span class="article-views">{{ item.views }}次</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
const brandNews = [
  { date: '2025-10-21', title: 'MDD辰达半导体推出低内阻、高开关频率MOS管，解决车载', views: 243 },
  { date: '2025-10-21', title: '国产替代正当时：MDD辰达芯推出逻辑IC产品全系列', views: 1262 },
  { date: '2025-10-21', title: 'Anlogic安路科技简介、核心产品、优势、运用', views: 1485 },
  { date: '2025-10-09', title: '一文读懂思佳讯Skyworks公司、产品、优势、运用', views: 581 },
]

const industryNews = [
  { date: '2025-10-10', title: '一文读懂卫星通信器件种类、功能、厂商、发展趋势', views: 2439 },
  { date: '2025-09-28', title: '国产FPGA公司、核心产品、应用介绍', views: 4499 },
  { date: '2025-08-21', title: '一文读懂数字隔离器芯片的原理、运用、品牌、选型要点', views: 568 },
  { date: '2025-06-19', title: '一文读懂DRAM工作原理、分类、主要厂商', views: 1990 },
]

const productNews = [
  { date: '2026-05-25', title: 'MDD辰达半导体推出大功率高防护TVS系列 专为小型BMS设计', views: 20 },
  { date: '2026-04-21', title: '芯伯乐高效3A降压方案：XBL2596 PCB设计指南', views: 179 },
  { date: '2026-04-21', title: '芯伯乐高效灵活降压方案：XBL1509B PCB设计指南', views: 109 },
  { date: '2026-04-21', title: '【应用】基于XBLW LM2596的DCDC转换器模块设计', views: 529 },
  { date: '2026-04-21', title: '【应用】宽压输入，高效稳压：XBL1509 DCDC降压方案', views: 59 },
  { date: '2026-04-16', title: 'MDD辰达半导体功率TVS新升级：封装不变，功率倍增', views: 99 },
  { date: '2026-04-14', title: 'Infineon英飞凌 IMW65R010M2H 产品介绍', views: 377 },
  { date: '2026-04-14', title: 'Infineon英飞凌 AIMBG75R050M2H 产品介绍', views: 499 },
]
</script>

<style scoped>
.news-section {
  padding: 20px 0 50px;
}
.news-container {
  max-width: var(--max-width);
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 20px;
  padding: 0 15px;
}
.news-column {
  background: var(--color-white);
  border-radius: 6px;
  padding: 20px;
  box-shadow: var(--shadow-sm);
}
.col-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
  padding-bottom: 10px;
  border-bottom: 2px solid var(--color-primary);
}
.col-header span {
  font-size: 16px;
  font-weight: 600;
  color: var(--color-dark);
}
.col-more {
  font-size: 12px;
  color: var(--color-gray-4);
  transition: color var(--transition-fast);
}
.col-more:hover {
  color: var(--color-primary);
}

/* Featured Article */
.featured-article {
  margin-bottom: 14px;
  cursor: pointer;
}
.featured-img {
  height: 100px;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  font-weight: 700;
  color: var(--color-white);
  margin-bottom: 10px;
}
.brand-img {
  background: linear-gradient(135deg, #1a237e, #283593);
}
.industry-img {
  background: linear-gradient(135deg, #004d40, #00695c);
}
.featured-title {
  font-size: 14px;
  font-weight: 500;
  color: var(--color-dark);
  margin-bottom: 6px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  line-height: 1.4;
}
.featured-title:hover {
  color: var(--color-primary);
}
.featured-desc {
  font-size: 12px;
  color: var(--color-gray-4);
  line-height: 1.6;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Article List */
.article-list {
  list-style: none;
  padding: 0;
  margin: 0;
}
.article-list li {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 7px 0;
  border-bottom: 1px dashed var(--color-gray-7);
  font-size: 13px;
}
.article-list li:last-child {
  border-bottom: none;
}
.article-date {
  flex-shrink: 0;
  color: var(--color-gray-4);
  font-size: 12px;
}
.article-link {
  flex: 1;
  color: var(--color-gray-2);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  transition: color var(--transition-fast);
}
.article-link:hover {
  color: var(--color-primary);
}
.article-views {
  flex-shrink: 0;
  color: var(--color-gray-4);
  font-size: 11px;
}
.full-list {
  max-height: 520px;
  overflow-y: auto;
}

@media (max-width: 900px) {
  .news-container {
    grid-template-columns: 1fr;
  }
}
</style>
