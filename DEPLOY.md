# 部署指南

## 首次部署（已完成）

项目已通过脚本部署到服务器 `120.76.143.219`。

## 日常更新流程 — Git + GitHub

### 前提

1. 在 GitHub 上创建一个仓库（如 `wlxmall-clone`）
2. 将本地代码推送到 GitHub

```bash
# 在本地项目目录
git remote add origin git@github.com:你的用户名/wlxmall-clone.git
git branch -M master
git push -u origin master
```

### 开发 → 部署步骤

**第 1 步：本地修改代码并提交**

```bash
git add .
git commit -m "做了哪些修改"
git push
```

**第 2 步：SSH 到服务器执行部署**

```bash
ssh root@120.76.143.219 "bash /opt/wlxmall/backend/deploy.sh"
```

或者在服务器上直接运行：

```bash
bash /opt/wlxmall/backend/deploy.sh
```

部署脚本会自动：
1. 从 GitHub 拉取最新代码
2. 安装后端 Python 依赖
3. 构建前端（npm install + build）
4. 部署前端文件到 Nginx 目录
5. 重启后端服务 + 重载 Nginx

### 服务器 Git 配置（首次部署时才需执行）

在服务器上执行一次：

```bash
cd /opt/wlxmall
git init
git remote add origin git@github.com:你的用户名/wlxmall-clone.git
git fetch origin master
git checkout master
```

> ⚠️ 需要给服务器添加 SSH deploy key，或者使用 `git remote set-url origin https://...` 加用户名密码的方式。

## 部署架构

```
GitHub <--push-- 本地开发环境
  |
  |--pull--> 云服务器 (120.76.143.219)
               ├── Nginx (443 HTTPS → 80 重定向)
               │   ├── /         → /var/www/wlxmall (前端静态文件)
               │   └── /api/*    → localhost:8000   (后端代理)
               └── systemd: wlxmall-api
                    └── uvicorn (FastAPI, port 8000)
```
