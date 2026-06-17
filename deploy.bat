@echo off
REM ==========================================
REM 一键部署脚本 (Windows)
REM ==========================================

echo ===========================================
echo 质量管理模块 - 一键部署脚本 (Windows)
echo ===========================================

REM 检查 Docker 是否安装
where docker >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo 错误: Docker 未安装，请先安装 Docker
    exit /b 1
)

where docker-compose >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo 错误: Docker Compose 未安装，请先安装 Docker Compose
    exit /b 1
)

REM 获取脚本所在目录
set SCRIPT_DIR=%~dp0
cd /d %SCRIPT_DIR%

REM 创建必要的目录
echo 创建必要目录...
if not exist backend\uploads mkdir backend\uploads
if not exist backend\logs mkdir backend\logs
if not exist frontend\uploads mkdir frontend\uploads

REM 复制环境配置文件
if not exist backend\.env (
    echo 复制环境配置文件...
    copy backend\.env.example backend\.env
    echo 请编辑 backend\.env 文件配置数据库和 API 密钥
)

if not exist frontend\.env.local (
    echo 复制前端环境配置文件...
    copy frontend\.env.example frontend\.env.local
)

REM 构建并启动服务
echo 构建并启动服务...
docker-compose down --remove-orphans
docker-compose build --no-cache
docker-compose up -d

REM 等待服务启动
echo 等待服务启动...
timeout /t 10 /nobreak >nul

REM 检查服务状态
echo 检查服务状态...
docker-compose ps

REM 运行数据库迁移
echo 运行数据库迁移...
docker-compose exec -T backend alembic upgrade head

echo ===========================================
echo 部署完成！
echo ===========================================
echo 前端地址: http://localhost:3000
echo 后端API: http://localhost:8000
echo API文档: http://localhost:8000/docs
echo ===========================================
pause
