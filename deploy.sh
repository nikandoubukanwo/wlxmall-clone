#!/bin/bash
# ============================================
# 万联芯城 - 自动部署脚本
# 在服务器上运行: bash /opt/wlxmall/backend/deploy.sh
# ============================================
set -e

BACKEND_DIR="/opt/wlxmall/backend"
FRONTEND_SRC_DIR="/opt/wlxmall/frontend"
FRONTEND_DIST_DIR="/var/www/wlxmall"
SERVICE_NAME="wlxmall-api"
BRANCH="master"

echo "========================================="
echo "  万联芯城部署脚本"
echo "  时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo "========================================="

# 1. 拉取最新代码
echo ""
echo "[1/5] 拉取最新代码..."
if [ -d "$BACKEND_DIR/.git" ]; then
    cd "$BACKEND_DIR"
    git stash
    git checkout $BRANCH
    git pull origin $BRANCH
    echo "  ✅ 代码已更新"
else
    echo "  ⚠️ 未检测到 Git 仓库，跳过拉取"
    echo "  请先在服务器配置 Git："
    echo "    cd /opt/wlxmall"
    echo "    git init"
    echo "    git remote add origin <你的GitHub仓库URL>"
    echo "    git pull origin $BRANCH"
fi

# 2. 安装后端依赖
echo ""
echo "[2/5] 安装后端依赖..."
cd "$BACKEND_DIR"
source venv/bin/activate
pip install -r requirements.txt -q
echo "  ✅ 依赖安装完成"

# 3. 构建前端
echo ""
echo "[3/5] 构建前端..."
cd "$FRONTEND_SRC_DIR"
if [ -f package.json ]; then
    npm install --silent
    npm run build
    echo "  ✅ 前端构建完成"
else
    echo "  ⚠️ 前端源码不存在，跳过后端构建"
fi

# 4. 部署前端静态文件
echo ""
echo "[4/5] 部署前端文件到 Nginx..."
if [ -d dist ]; then
    rm -rf "$FRONTEND_DIST_DIR"/*
    cp -r dist/* "$FRONTEND_DIST_DIR/"
    echo "  ✅ 前端文件已部署"
else
    echo "  ⚠️ dist 目录不存在"
fi

# 5. 重启服务
echo ""
echo "[5/5] 重启服务..."
systemctl restart $SERVICE_NAME
systemctl reload nginx
echo "  ✅ 后端服务已重启"
echo "  ✅ Nginx 已重载"

echo ""
echo "========================================="
echo "  ✅ 部署完成!"
echo "  https://www.longkitech.com"
echo "========================================="
