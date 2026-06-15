<template>
  <footer class="footer">
    <!-- Top: Link Columns -->
    <div class="footer-top">
      <div class="footer-inner">
        <div class="footer-cols">
          <div class="footer-col" v-for="(col, i) in linkColumns" :key="i">
            <h4 class="col-title">{{ col.title }}</h4>
            <a class="col-link" v-for="(link, j) in col.links" :key="j" href="javascript:;">{{ link }}</a>
          </div>
        </div>
        <div class="footer-contact">
          <div class="qr-section">
            <div class="qr-placeholder">
              <el-icon :size="48" color="#999"><Camera /></el-icon>
            </div>
            <p class="qr-text">关注公众号，优惠活动早知道！</p>
          </div>
          <div class="hotline-section">
            <div class="hotline-title">4000-306-326</div>
            <p class="hotline-desc">周一至周五（9:00-18:30）采购热线</p>
            <a class="hotline-btn" href="https://wpa1.qq.com/ExeLLyG7?_type=wpa&qidian=true" target="_blank">
              <el-icon><ChatDotRound /></el-icon>
              人工服务
            </a>
          </div>
        </div>
      </div>
    </div>

    <!-- Middle: Friend Links -->
    <div class="footer-friend">
      <div class="footer-inner">
        <span class="friend-label">友情链接：</span>
        <a class="friend-link" v-for="(link, i) in friendLinks" :key="i" href="javascript:;">{{ link }}</a>
      </div>
    </div>

    <!-- Bottom: Copyright -->
    <div class="footer-bottom">
      <div class="footer-inner">
        <p>Copyright ©2023 wlxmall.com万联芯城版权所有 | 电信与信息服务业务经营许可证100798号 | 粤ICP备14012234号 | 投诉建议</p>
        <p>客服电话：4000-306-326 文明办网文明上网举报电话：010-82615762 违法不良信息举报中心</p>
        <p>粤公网安备 44030402002882号</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
const linkColumns = [
  {
    title: '新手入门',
    links: ['注册登录', '找回密码', '购物流程', '账号设置', '常见问题'],
  },
  {
    title: '购物指南',
    links: ['支付方式', '配送方式', '售后服务', '发票须知', '品牌目录', '商品目录'],
  },
  {
    title: '关于我们',
    links: ['企业简介', '企业文化', '加入我们', '联系我们'],
  },
  {
    title: '特色服务',
    links: ['选型手册', '期货订购', '海外代购', '原厂直订'],
  },
  {
    title: '政策声明',
    links: ['隐私保护政策', '网站免责声明', '注册用户协议', '特别申明'],
  },
]

const friendLinks = [
  '电子元器件网', '万通商务网', 'Marking丝印查询', '电子工程网',
  '拍明芯城元器件商城', '烜芯微二极管', '芯片商城', '深圳市电子商会',
  '电子元器件索引', '青岛仪器仪表', '全球半导体观察', '机电设备采购网',
]
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
.qr-placeholder {
  width: 100px;
  height: 100px;
  background: #444;
  border-radius: 6px;
  margin: 0 auto 8px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.qr-text {
  font-size: 11px;
  color: var(--color-gray-4);
  margin-bottom: 10px;
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

/* Friend Links */
.footer-friend {
  padding: 14px 0;
  border-bottom: 1px solid rgba(255,255,255,0.08);
}
.friend-label {
  color: var(--color-gray-3);
  margin-right: 6px;
}
.friend-link {
  color: var(--color-gray-4);
  margin: 0 6px;
  white-space: nowrap;
  transition: color var(--transition-fast);
  cursor: pointer;
}
.friend-link:hover {
  color: var(--color-primary-light);
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
