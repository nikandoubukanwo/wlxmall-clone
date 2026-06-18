---
name: server-sync
description: 检查万联芯城服务器部署状态、Git 同步代码、一键部署更新、服务运维
---

# server-sync

管理万联芯城 (`wlxmall`) 生产服务器的代码同步、部署和服务运维。服务器运行 Ubuntu + Nginx + FastAPI + Vue 3，代码托管在 GitHub。

所有操作通过 SSH 远程执行，不需要登录到服务器交互式终端。

## 服务器信息

| 项目 | 值 |
|------|-----|
| IP | `120.76.143.219` |
| 用户 | `root` |
| 项目根目录 | `/opt/wlxmall`（Git 仓库） |
| 后端服务 | `wlxmall-api`（systemd） |
| Web 服务 | `nginx`（systemd） |
| 前端静态文件 | `/var/www/wlxmall/` |

## 先决条件

- 本地已配置 SSH 密钥（免密码登录服务器）
- 本地有 GitHub 仓库的写权限
- 服务器 Git 已配置远程仓库（`origin`）

## 常用操作

### 1. 查看服务器 Git 状态

```bash
ssh root@120.76.143.219 "cd /opt/wlxmall && git status"
```

预期输出：
```
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

### 2. 查看提交历史

```bash
ssh root@120.76.143.219 "cd /opt/wlxmall && git log --oneline -10"
```

### 3. 检查服务和健康状态

```bash
# 查看所有服务状态
ssh root@120.76.143.219 "systemctl status wlxmall-api nginx --no-pager | grep Active"

# 预期:
#    Active: active (running)
#    Active: active (running)

# API 健康检查
ssh root@120.76.143.219 "curl -s https://localhost/health"
# 预期: {"status":"ok"}

# 检查前端是否正常响应
ssh root@120.76.143.219 "curl -sI https://localhost/ | head -1"
# 预期: HTTP/2 200
```

### 4. 拉取最新代码 + 部署

```bash
ssh root@120.76.143.219 "bash /opt/wlxmall/deploy.sh"
```

部署脚本自动执行以下步骤：
1. `git pull` 拉取最新代码
2. `pip install -r requirements.txt` 更新后端依赖
3. `npm install && npm run build` 构建前端
4. `cp -r dist/* /var/www/wlxmall/` 部署前端文件
5. `systemctl restart wlxmall-api && systemctl reload nginx` 重启服务

### 5. 单独更新代码（不执行完整部署）

```bash
ssh root@120.76.143.219 "cd /opt/wlxmall && git pull"
```

### 6. 查看后端日志

```bash
# 实时日志（按 Ctrl+C 退出）
ssh root@120.76.143.219 "journalctl -u wlxmall-api -f"

# 最近 50 行
ssh root@120.76.143.219 "journalctl -u wlxmall-api --no-pager -n 50"

# 查看今天的日志
ssh root@120.76.143.219 "journalctl -u wlxmall-api --since today --no-pager"
```

### 7. 查看 Nginx 访问日志

```bash
ssh root@120.76.143.219 "tail -20 /var/log/nginx/access.log"
```

### 8. 磁盘和数据库检查

```bash
# 磁盘使用情况
ssh root@120.76.143.219 "df -h /"
# 预期: 40G 总容量，约 30% 已用

# 数据库大小
ssh root@120.76.143.219 "ls -lh /opt/wlxmall/backend/wlxmall.db"

# 项目目录大小
ssh root@120.76.143.219 "du -sh /opt/wlxmall/{backend,frontend} /var/www/wlxmall"
```

### 9. 备份数据库

```bash
ssh root@120.76.143.219 "cp /opt/wlxmall/backend/wlxmall.db /root/wlxmall-backup-$(date +%Y%m%d).db && echo 'done'"
```

### 10. 重启服务

```bash
# 重启所有服务
ssh root@120.76.143.219 "systemctl restart wlxmall-api && systemctl reload nginx"

# 仅重启后端
ssh root@120.76.143.219 "systemctl restart wlxmall-api"

# 仅重载 Nginx
ssh root@120.76.143.219 "systemctl reload nginx"
```

## 完整部署流程示例

从本地修改代码到生产环境上线：

```bash
# 第 1 步：本地修改 → 提交 → 推送到 GitHub
cd /g/program/c_web_program/wlxmall-clone
git add .
git commit -m "feat: xxx"
git push

# 第 2 步：服务器拉取并部署
ssh root@120.76.143.219 "bash /opt/wlxmall/deploy.sh"

# 第 3 步：验证部署成功
ssh root@120.76.143.219 "curl -s https://localhost/health && echo ' OK' && curl -sI https://localhost/ | head -1"
```

## 故障排查

| 症状 | 可能原因 | 诊断命令 |
|------|----------|----------|
| `git pull` 失败 | 本地有未提交修改 | `git status` → `git stash` 暂存后重试 |
| `git pull` 报冲突 | 服务器文件被手动修改过 | `git stash` 或 `git reset --hard origin/master` |
| 部署后 API 返回 502 | 后端服务挂了 | `systemctl status wlxmall-api` + `journalctl -u wlxmall-api -n 20` |
| 部署后前端白屏 | 构建失败或静态文件未更新 | 检查 `npm run build` 输出；确认 `/var/www/wlxmall/` 下有文件 |
| HTTPS 访问超时 | 云安全组未放开 443 端口 | 登录云控制台检查安全组规则 |
| 磁盘空间满 | 日志或旧备份堆积 | `df -h` → 清理 `/var/log/` 或旧备份 |
| Python 依赖安装失败 | 版本不兼容 | `pip install --upgrade pip` 后重试 |
| `Permission denied (publickey)` | SSH 密钥失效 | 检查 `~/.ssh/id_*.pub` 是否在服务器 `~/.ssh/authorized_keys` 中 |

## 项目结构

```
/opt/wlxmall/                    ← Git 仓库根目录
├── deploy.sh                    ← 一键部署脚本
├── .gitignore
├── DEPLOY.md
├── OPS.md                       ← 运维文档
├── backend/
│   ├── app/                     ← FastAPI 源码
│   ├── venv/                    ← Python 虚拟环境
│   ├── requirements.txt
│   ├── seed.py                  ← 种子数据
│   └── wlxmall.db               ← SQLite 数据库
├── frontend/
│   ├── src/                     ← Vue 3 源码
│   ├── package.json
│   └── vite.config.js
└── .git/

/opt/wlxmall-api → /opt/wlxmall/backend  (软链接)
```
