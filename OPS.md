---
name: longkitech-ops
description: 隆祺电子 服务器运维 - 服务管理、部署流程、SSL证书、故障排查
---

# longkitech-ops

隆祺电子 电商平台部署在阿里云 ECS，基于 **Nginx + FastAPI + Vue 3** 架构。通过 SSH + Git 实现代码更新部署。

## 服务器信息

| 项目 | 值 |
|------|-----|
| IP | `120.76.143.219` |
| 系统 | Ubuntu (Linux 7.0.0-15-generic x86_64) |
| 主机名 | `iZwz91xao1tbfxjbc8avfmZ` |
| 用户 | `root` |
| Python | 3.14.4 |
| Node.js | 22.22.1 |
| Nginx | 1.28.3 |

## 部署架构

```
用户 → 防火墙(云安全组)
       ├── 443 (HTTPS) → Nginx
       │   ├── /      → /var/www/longkitech/ (静态文件，SPA fallback)
       │   └── /api/* → proxy_pass → localhost:8000 (uvicorn)
       └── 80 (HTTP)  → Nginx → 301 redirect → HTTPS
```

## 服务管理

### 后端 API 服务 (`longkitech-api`)

```bash
# 查看状态
systemctl status longkitech-api

# 启动 / 停止 / 重启
systemctl start longkitech-api
systemctl stop longkitech-api
systemctl restart longkitech-api

# 查看实时日志
journalctl -u longkitech-api -f

# 查看最近日志
journalctl -u longkitech-api --no-pager -n 50
```

### Nginx

```bash
# 查看状态
systemctl status nginx

# 重载配置（不中断连接）
systemctl reload nginx

# 测试配置文件
nginx -t

# 重启
systemctl restart nginx
```

## 目录结构

```
/opt/longkitech/                    ← Git 仓库根目录
├── .git/
├── deploy.sh                    ← 一键部署脚本
├── .gitignore
├── DEPLOY.md
├── backend/
│   ├── app/
│   │   ├── main.py              ← FastAPI 入口
│   │   ├── config.py            ← 配置（数据库、密钥）
│   │   ├── database.py          ← 数据库连接
│   │   ├── models/              ← SQLAlchemy 模型
│   │   ├── routes/              ← API 路由
│   │   └── schemas/             ← Pydantic 校验模型
│   ├── venv/                    ← Python 虚拟环境
│   ├── requirements.txt
│   ├── seed.py                  ← 种子数据
│   └── longkitech.db               ← SQLite 数据库
└── frontend/
    ├── src/                     ← Vue 3 源码
    ├── index.html
    ├── package.json
    └── vite.config.js

/var/www/longkitech/                ← Nginx 前端静态文件（由部署脚本自动更新）

/etc/nginx/
├── nginx.conf
└── sites-enabled/
    └── longkitech                  ← 站点配置（SSL + 反向代理）

/etc/nginx/ssl/
├── www.longkitech.com.pem       ← SSL 证书
└── www.longkitech.com.key       ← SSL 私钥

/opt/longkitech-api → /opt/longkitech/backend  (软链接，兼容 systemd)
```

## SSL 证书

- 证书文件: `/etc/nginx/ssl/www.longkitech.com.pem`
- 私钥文件: `/etc/nginx/ssl/www.longkitech.com.key`
- 私钥权限: `600` (仅 root 可读)
- 协议: TLSv1.2 + TLSv1.3
- HTTP 自动 301 跳转 HTTPS

### 证书续期

```bash
# 替换证书文件后重载 Nginx
scp /本地路径/新证书.pem root@120.76.143.219:/etc/nginx/ssl/www.longkitech.com.pem
scp /本地路径/新私钥.key root@120.76.143.219:/etc/nginx/ssl/www.longkitech.com.key
ssh root@120.76.143.219 "chmod 600 /etc/nginx/ssl/*.key && systemctl reload nginx"
```

## 部署流程

### 首次部署（已完成）

1. 手动上传证书和代码
2. 安装依赖（Python venv + Node.js npm）
3. 构建前端 → 部署到 Nginx 目录
4. 配置 systemd 服务
5. 验证 HTTPS + API

### 日常更新

```bash
# 本地：修改代码 → 提交 → 推送到 GitHub
git add .
git commit -m "修改内容"
git push

# 服务器：一键拉取 + 构建 + 重启
ssh root@120.76.143.219 "bash /opt/longkitech/deploy.sh"
```

### 部署脚本说明

脚本路径: `/opt/longkitech/deploy.sh`

执行过程：

| 步骤 | 操作 |
|------|------|
| 1/5 | `git pull` 拉取最新代码 |
| 2/5 | `pip install -r requirements.txt` 安装后端依赖 |
| 3/5 | `npm install && npm run build` 构建前端 |
| 4/5 | `cp -r dist/* /var/www/longkitech/` 部署静态文件 |
| 5/5 | `systemctl restart longkitech-api && systemctl reload nginx` 重启服务 |

## 数据库

- 类型: SQLite
- 路径: `/opt/longkitech/backend/longkitech.db`
- 备份:

```bash
cp /opt/longkitech/backend/longkitech.db /root/longkitech-backup-$(date +%Y%m%d).db
```

- 重置数据: `cd /opt/longkitech/backend && source venv/bin/activate && python3 seed.py`

## 健康检查

```bash
# API 健康检查
curl -s https://localhost/health
# 预期: {"status":"ok"}

# 前端是否正常
curl -sI https://localhost/ | head -1
# 预期: HTTP/2 200
```

## 故障排查

| 问题 | 排查步骤 |
|------|----------|
| HTTPS 无法访问 | 检查云安全组是否开放 443 端口；`systemctl status nginx`；`nginx -t` |
| API 返回 502 | `systemctl restart longkitech-api`；`journalctl -u longkitech-api -n 20` 看日志 |
| 前端白屏 | 检查 `/var/www/longkitech/` 是否有文件；浏览器 F12 看网络请求 |
| 部署脚本报错 | 检查 `git pull` 是否有冲突；查看脚本执行到哪一步 |
| 磁盘空间不足 | `df -h`；清理旧备份和日志 |
| Python 依赖安装失败 | 检查 `venv/bin/activate` 后 pip 版本；`pip install --upgrade pip` |
| Git pull 失败 | `git status` 检查是否有未提交修改；`git stash` 暂存后重试 |

## 快捷命令

```bash
# 一键登录
ssh root@120.76.143.219

# 查看全部服务状态
ssh root@120.76.143.219 "systemctl status longkitech-api nginx --no-pager | grep Active"

# 查看实时日志
ssh root@120.76.143.219 "journalctl -u longkitech-api -f"

# 重启所有服务
ssh root@120.76.143.219 "systemctl restart longkitech-api && systemctl reload nginx"

# 检查磁盘
ssh root@120.76.143.219 "df -h && echo '---' && du -sh /opt /var/www /root/.cache"

# 完整部署
ssh root@120.76.143.219 "bash /opt/longkitech/deploy.sh"
```
