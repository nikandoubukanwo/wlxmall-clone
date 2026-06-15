<template>
  <div class="navbar">
    <div class="navbar-inner">
      <!-- 全部分类 -->
      <div class="category-btn" @mouseenter="showCategory = true" @mouseleave="showCategory = false">
        <el-icon :size="18"><Operation /></el-icon>
        全部分类
        <el-icon :size="14"><ArrowDown /></el-icon>

        <!-- Category Dropdown -->
        <transition name="slide-down">
          <div v-show="showCategory" class="category-dropdown">
            <div class="category-column" v-for="(col, ci) in categories" :key="ci">
              <a
                class="category-group-link"
                v-for="(cat, si) in col"
                :key="si"
                href="javascript:;"
                @mouseenter="activeCat = cat.name"
              >
                <span class="cat-main">{{ cat.name }}</span>
                <span class="cat-sub">{{ cat.sub }}</span>
              </a>
            </div>
          </div>
        </transition>
      </div>

      <!-- Nav Links -->
      <div class="nav-links">
        <router-link to="/" class="nav-link active">首页</router-link>
        <a class="nav-link" href="javascript:;">品牌目录</a>
        <a class="nav-link hot" href="javascript:;">
          可议价
          <span class="nav-badge">HOT</span>
        </a>
        <a class="nav-link" href="javascript:;">超级爆款</a>
        <a class="nav-link" href="javascript:;">热门现货</a>
        <a class="nav-link" href="javascript:;">期货订购</a>
        <a class="nav-link" href="javascript:;">领券中心</a>
        <a class="nav-link" href="javascript:;">海外代购</a>
        <a class="nav-link" href="javascript:;">代理品牌</a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const showCategory = ref(false)
const activeCat = ref('')

const categories = [
  [
    { name: '微控制器', sub: 'MCU' },
    { name: '存储器', sub: 'Memory' },
    { name: '音视频', sub: 'Audio/Video' },
    { name: '电源管理', sub: 'Power' },
    { name: '数据转换', sub: 'ADC/DAC' },
    { name: '传感器', sub: 'Sensors' },
  ],
  [
    { name: '光电器件', sub: 'Opto' },
    { name: '滤波器', sub: 'Filter' },
    { name: '逻辑器件', sub: 'Logic' },
    { name: '接口', sub: 'Interface' },
    { name: '放大器', sub: 'Amplifier' },
    { name: '时钟', sub: 'Clock/Timing' },
  ],
  [
    { name: '二极管', sub: 'Diode' },
    { name: '晶体管', sub: 'Transistor' },
    { name: '电路保护', sub: 'Protection' },
    { name: '开关', sub: 'Switches' },
    { name: '继电器', sub: 'Relay' },
    { name: '晶振', sub: 'Crystal' },
  ],
  [
    { name: '电阻', sub: 'Resistor' },
    { name: '电容', sub: 'Capacitor' },
    { name: '电感', sub: 'Inductor' },
    { name: '连接器/接插件/端子', sub: 'Connector' },
    { name: '开发套件', sub: 'Dev Kit' },
    { name: '模块', sub: 'Module' },
  ],
  [
    { name: '测试与测量', sub: 'Test & Measure' },
    { name: '自动化', sub: 'Automation' },
    { name: '更多商品类别', sub: 'More >>' },
  ],
]
</script>

<style scoped>
.navbar {
  background: var(--color-primary);
  height: var(--navbar-height);
}
.navbar-inner {
  max-width: var(--max-width);
  margin: 0 auto;
  display: flex;
  align-items: center;
  height: 100%;
  position: relative;
}

/* Category Button */
.category-btn {
  width: var(--sidebar-width);
  height: 100%;
  background: rgba(0, 0, 0, 0.15);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  color: var(--color-white);
  font-size: 15px;
  font-weight: 500;
  cursor: pointer;
  position: relative;
  user-select: none;
  transition: background var(--transition-fast);
}
.category-btn:hover {
  background: rgba(0, 0, 0, 0.25);
}

/* Nav Links */
.nav-links {
  display: flex;
  align-items: center;
  height: 100%;
}
.nav-link {
  padding: 0 18px;
  color: var(--color-white);
  font-size: 14px;
  line-height: var(--navbar-height);
  transition: background var(--transition-fast);
  position: relative;
  white-space: nowrap;
}
.nav-link:hover,
.nav-link.active {
  background: rgba(0, 0, 0, 0.12);
}
.nav-badge {
  display: inline-block;
  background: #ff0;
  color: var(--color-primary);
  font-size: 10px;
  padding: 1px 4px;
  border-radius: 2px;
  margin-left: 3px;
  font-weight: 700;
  vertical-align: super;
}

/* Category Dropdown */
.category-dropdown {
  position: absolute;
  top: 100%;
  left: 0;
  width: var(--sidebar-width);
  background: var(--color-white);
  box-shadow: var(--shadow-popup);
  z-index: 1000;
  display: flex;
  flex-direction: column;
  padding: 6px 0;
}
.category-group-link {
  display: block;
  padding: 8px 14px;
  color: var(--color-dark);
  font-size: 13px;
  transition: background var(--transition-fast);
  border-bottom: 1px solid var(--color-gray-8);
}
.category-group-link:last-child {
  border-bottom: none;
}
.category-group-link:hover {
  background: #fff5f5;
  color: var(--color-primary);
}
.cat-main {
  display: block;
  font-weight: 500;
}
.cat-sub {
  display: block;
  font-size: 11px;
  color: var(--color-gray-4);
  margin-top: 1px;
}
</style>
