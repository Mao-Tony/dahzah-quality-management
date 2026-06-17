#!/bin/bash
# ===========================================
# 一键部署脚本
# ===========================================
# 用于在服务器上一键部署质量管理模块

set -e

echo "==========================================="
echo "质量管理模块 - 一键部署脚本"
echo "==========================================="

# 检查 Docker 是否安装
if ! command -v docker &> /dev/null; then
    echo "错误: Docker 未安装，请先安装 Docker"
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "错误: Docker Compose 未安装，请先安装 Docker Compose"
    exit 1
fi

# 获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# 创建必要的目录
echo "创建必要目录..."
mkdir -p backend/uploads backend/logs frontend/uploads

# 复制环境配置文件
if [ ! -f "backend/.env" ]; then
    echo "复制环境配置文件..."
    cp backend/.env.example backend/.env
    echo "请编辑 backend/.env 文件配置数据库和 API 密钥"
fi

if [ ! -f "frontend/.env.local" ]; then
    echo "复制前端环境配置文件..."
    cp frontend/.env.example frontend/.env.local
fi

# 拉取最新代码（如果有远程仓库）
if [ -d ".git" ]; then
    echo "拉取最新代码..."
    git pull origin main
fi

# 构建并启动服务
echo "构建并启动服务..."
docker-compose down --remove-orphans
docker-compose build --no-cache
docker-compose up -d

# 等待服务启动
echo "等待服务启动..."
sleep 10

# 检查服务状态
echo "检查服务状态..."
docker-compose ps

# 运行数据库迁移
echo "运行数据库迁移..."
docker-compose exec -T backend alembic upgrade head || echo "迁移可能已执行或需要手动处理"

echo "==========================================="
echo "部署完成！"
echo "==========================================="
echo "前端地址: http://localhost:3000"
echo "后端API: http://localhost:8000"
echo "API文档: http://localhost:8000/docs"
echo "==========================================="
