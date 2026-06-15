<template>
  <div class="find-parts-section section-gray">
    <div class="find-parts-container">
      <!-- Left: Find Parts Form -->
      <div class="find-form-panel">
        <div class="form-title">我要找料</div>
        <div class="form-body">
          <div class="form-row">
            <label class="form-label required">型号</label>
            <input v-model="form.model" class="input" placeholder="请输入型号" />
          </div>
          <div class="form-row">
            <label class="form-label required">数量</label>
            <div class="form-input-group">
              <input v-model="form.qty" class="input" placeholder="请输入数量" />
              <select v-model="form.unit" class="form-select">
                <option value="pcs">pcs</option>
                <option value="个">个</option>
              </select>
            </div>
          </div>
          <div class="form-row">
            <label class="form-label">品牌</label>
            <input v-model="form.brand" class="input" placeholder="品牌（选填）" />
          </div>
          <div class="form-row">
            <label class="form-label">目标单价</label>
            <div class="price-input">
              <span class="price-prefix">¥</span>
              <input v-model="form.price" class="input" placeholder="目标单价" />
            </div>
          </div>
          <div class="form-row">
            <label class="form-label">备注</label>
            <input v-model="form.remark" class="input" placeholder="备注（选填）" />
          </div>
          <button class="submit-btn" @click="handleSubmit">提交</button>
        </div>
      </div>

      <!-- Right: Hot Products Table -->
      <div class="hot-products-panel">
        <div class="hot-title">最新热卖型号</div>
        <div class="table-wrapper">
          <table class="table">
            <thead>
              <tr>
                <th>商品名称</th>
                <th>商品型号</th>
                <th>品牌</th>
                <th>价格</th>
                <th>库存</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(item, i) in hotProducts" :key="i">
                <td>{{ item.category }}</td>
                <td><a class="link" href="javascript:;" @click="viewDetail(item)">{{ item.model }}</a></td>
                <td>{{ item.brand }}</td>
                <td>{{ item.price }}</td>
                <td>{{ item.stock }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue'

const form = reactive({
  model: '',
  qty: '',
  unit: 'pcs',
  brand: '',
  price: '',
  remark: '',
})

const hotProducts = [
  { category: 'IGBT管/模块', model: 'FGW75XS120C', brand: 'FUJI(富士电机)', price: '¥16.90500', stock: '7200个' },
  { category: 'IGBT管/模块', model: 'FGW50XS65C', brand: 'FUJI(富士电机)', price: '¥8.19950', stock: '12000个' },
  { category: 'IGBT管/模块', model: 'FGW75XS65D', brand: 'FUJI(富士电机)', price: '¥13.83450', stock: '1200个' },
  { category: 'IGBT管/模块', model: 'FGW75XS65C', brand: 'FUJI(富士电机)', price: '¥10.60300', stock: '4800个' },
  { category: 'IGBT管/模块', model: 'FGW40XS120C', brand: 'FUJI(富士电机)', price: '¥10.15450', stock: '2400个' },
  { category: 'IGBT管/模块', model: 'FGW40N120HD', brand: 'FUJI(富士电机)', price: '¥19.09000', stock: '4800个' },
  { category: 'IGBT管/模块', model: 'FGZ75XS120C', brand: 'FUJI(富士电机)', price: '¥27.48500', stock: '200个' },
  { category: 'IGBT管/模块', model: '2MBI600VN-120-50', brand: 'FUJI(富士电机)', price: '¥603.75000', stock: '78个' },
  { category: 'IGBT管/模块', model: 'FGW40N120WD', brand: 'FUJI(富士电机)', price: '¥14.03000', stock: '4800个' },
  { category: '场效应管(MOSFET)', model: 'FMW60N027S2FDHF', brand: 'FUJI(富士电机)', price: '¥34.76450', stock: '1800个' },
]

function handleSubmit() {
  if (!form.model) {
    alert('请输入型号')
    return
  }
  if (!form.qty) {
    alert('请输入数量')
    return
  }
  alert(`询价提交成功！型号: ${form.model}, 数量: ${form.qty}${form.unit}`)
}

function viewDetail(item) {
  alert(`查看详情: ${item.model}`)
}
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
.form-label.required::before {
  content: '*';
  color: var(--color-primary);
  margin-right: 2px;
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
</style>
