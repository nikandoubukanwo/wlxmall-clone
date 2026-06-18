---
name: git-sync
description: git 提交、推送、拉取等操作（使用 GitHub API Token 认证）
---

# git-sync

将本地代码通过 git 提交并推送到 GitHub 仓库（`nikandoubukanwo/longkitech`），使用 GitHub Personal Access Token 进行 HTTPS 认证。

## 配置

GitHub Token 需作为 `GIT_TOKEN` 环境变量传入，或者在调用时作为参数提供。Token 需要 `repo` 权限。

远程仓库地址：`https://github.com/nikandoubukanwo/longkitech.git`

## 用法

### 快速提交并推送

在 `longkitech` 目录下执行：

```bash
# 设置 token（每次 session 只需一次）
export GIT_TOKEN="ghp_你的token"

# 查看状态
git status

# 添加所有修改
git add -A

# 提交
git commit -m "修改内容说明"

# 推送（自动处理认证）
git push https://$GIT_TOKEN@github.com/nikandoubukanwo/longkitech.git --all
```

### 一键提交+推送（全流程）

```bash
cd /g/program/c_web_program/longkitech && \
export GIT_TOKEN="ghp_你的token" && \
git add -A && \
git commit -m "更新内容" && \
git push https://$GIT_TOKEN@github.com/nikandoubukanwo/longkitech.git --all
```

### 拉取最新代码

```bash
cd /g/program/c_web_program/longkitech && \
export GIT_TOKEN="ghp_你的token" && \
git pull https://$GIT_TOKEN@github.com/nikandoubukanwo/longkitech.git
```

### 查看提交历史

```bash
git log --oneline -10
```

## 注意事项

- Token 不要写在代码或提交消息中，用环境变量传入
- 如果 token 泄露，立即到 GitHub Settings → Developer settings → Personal access tokens 撤销
- 第一次使用前确保 git 已配置 user.name 和 user.email：
  ```bash
  git config user.name "yourname"
  git config user.email "your@email.com"
  ```
- 服务器部署走 `/opt/longkitech/deploy.sh`，不依赖本地 git push
