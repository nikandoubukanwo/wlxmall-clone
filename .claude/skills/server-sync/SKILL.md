---
name: server-sync
description: 检查万联芯城服务器部署状态、Git 同步代码、一键部署更新、服务运维
---

# server-sync

管理万联芯城生产服务器（`120.76.143.219`）的代码同步和部署。

## 非显而易见的事

| 事项 | 说明 |
|------|------|
| **一键部署脚本** | `/opt/wlxmall/deploy.sh` — pull → pip → npm build → 复制前端 → 重启服务 |
| **systemd 软链接** | `/opt/wlxmall-api → /opt/wlxmall/backend`，服务的 WorkingDirectory 实际是 `backend/` 目录 |
| **前端部署路径** | 源码在 `/opt/wlxmall/frontend`，构建后输出到 `/var/www/wlxmall/`（Nginx root） |
| **API 健康检查** | `curl -s https://localhost/health` → `{"status":"ok"}` |
| **GitHub 仓库** | `nikandoubukanwo/wlxmall-clone`，服务器 remote 已配置 |
| **SSL 证书** | `/etc/nginx/ssl/www.longkitech.com.{pem,key}`，需一起备份 |

## 部署流程

```bash
# 本地：提交并推送
cd /g/program/c_web_program/wlxmall-clone
git add . && git commit -m "xxx" && git push

# 服务器：一键部署
ssh root@120.76.143.219 "bash /opt/wlxmall/deploy.sh"

# 验证
ssh root@120.76.143.219 "curl -s https://localhost/health"
```

## 注意事项

- 部署脚本里的 `git pull` 如果报错，服务器上可能有未提交的修改 → `git stash` 后再跑
- 数据库是 SQLite 单文件 `/opt/wlxmall/backend/wlxmall.db`，部署不会覆盖它，但保险起见先备份
- 前端 `.claude/skills/` 目录在项目根目录的 `.claude` 下（不是 wlxmall-clone 里面）
