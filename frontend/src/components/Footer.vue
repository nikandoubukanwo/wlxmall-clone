<template>
  <footer class="footer">
    <!-- Top: Link Columns -->
    <div class="footer-top">
      <div class="footer-inner">
        <div class="footer-cols">
          <div class="footer-col" v-for="(col, i) in [aboutCol]" :key="i">
            <h4 class="col-title">{{ col.title }}</h4>
            <a class="col-link" v-for="(link, j) in col.links" :key="j" href="javascript:;">{{ link }}</a>
          </div>
        </div>
        <div class="footer-contact">
          <div class="hotline-section">
            <div class="hotline-title">0755-83233897</div>
            <p class="hotline-desc">周一至周五（9:00-18:30）采购热线</p>
            <a class="hotline-btn" href="https://wpa1.qq.com/ExeLLyG7?_type=wpa&qidian=true" target="_blank">
              <el-icon><ChatDotRound /></el-icon>
              人工服务
            </a>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom: Copyright -->
    <div class="footer-bottom">
      <div class="footer-inner">
        <p>Copyright ©2026 longkitech.com 版权所有 | 电信与信息服务业务经营许可证xxx号 | 粤ICP备xxx号 | 投诉建议</p>
        <p>客服电话：0755-83233897 文明办网文明上网举报电话：010-82615762 违法不良信息举报中心</p>
        <p>粤公网安备 xxx号</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
const aboutCol = {
  title: '关于我们',
  links: ['企业简介', '企业文化', '加入我们', '联系我们'],
}
</script>

<style scoped>
.footer {
  background: var(--color-dark);
  color: var(--color-gray-4);
  font-size: 12px;
}
.footer-inner {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 15px;
}

/* Top Section */
.footer-top {
  padding: 36px 0 24px;
  border-bottom: 1px solid rgba(255,255,255,0.08);
}
.footer-top .footer-inner {
  display: flex;
  gap: 30px;
}
.footer-cols {
  flex: 1;
  display: flex;
  gap: 30px;
}
.footer-col {
  flex: 1;
}
.col-title {
  color: var(--color-white);
  font-size: 14px;
  font-weight: 600;
  margin-bottom: 12px;
}
.col-link {
  display: block;
  color: var(--color-gray-4);
  padding: 4px 0;
  transition: color var(--transition-fast);
  cursor: pointer;
}
.col-link:hover {
  color: var(--color-primary-light);
}

/* Contact */
.footer-contact {
  width: 240px;
  flex-shrink: 0;
  text-align: center;
}
.hotline-title {
  font-size: 22px;
  font-weight: 700;
  color: var(--color-primary-light);
  margin-bottom: 4px;
}
.hotline-desc {
  font-size: 11px;
  color: var(--color-gray-4);
  margin-bottom: 10px;
}
.hotline-btn {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 6px 20px;
  background: var(--color-primary);
  color: var(--color-white);
  border-radius: 4px;
  font-size: 13px;
  cursor: pointer;
  transition: background var(--transition-fast);
}
.hotline-btn:hover {
  background: var(--color-primary-hover);
}

/* Bottom */
.footer-bottom {
  background: var(--color-darker);
  padding: 18px 0;
  text-align: center;
  line-height: 1.8;
}
.footer-bottom p {
  color: var(--color-gray-4);
  font-size: 11px;
}

@media (max-width: 768px) {
  .footer-top .footer-inner {
    flex-direction: column;
  }
  .footer-cols {
    flex-wrap: wrap;
  }
  .footer-col {
    min-width: 45%;
  }
}
</style>
