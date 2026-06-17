# 质量管理模块 (dahzah-quality-management)

质量管理模块是 Dazah 系统的核心模块之一，提供完整的质量检验和偏差报告管理功能。

## 功能特性

### 1. 试剂/标准品管理
- 试剂/标准品台账管理
- AI 标签识别功能（自动识别试剂标签图片）
- Excel 导出功能
- 批量导入/导出

### 2. 偏差报告自动化
- 新建偏差报告任务
- 历史任务查询
- Word 文档解析
- AI 智能标准化处理
- 报告预览与编辑
- SOP 规则管理
- 报告模板管理

### 3. AI 配置与日志
- AI 配置设置（API Key、模型参数等）
- AI 交互日志查询
- 使用统计

## 技术栈

### 后端
- **框架**: FastAPI + Uvicorn
- **数据库**: PostgreSQL 16 + SQLAlchemy (异步)
- **ORM**: Alembic 数据库迁移
- **AI**: MiniMax API (支持文本和视觉识别)

### 前端
- **框架**: Next.js 15 (App Router)
- **UI**: Ant Design 6
- **状态管理**: React Hooks + Server Actions

## 目录结构

```
dahzah-quality-management/
├── backend/                    # 后端代码
│   ├── app/
│   │   ├── api/              # API 路由
│   │   ├── core/             # 核心配置
│   │   ├── modules/           # 业务模块
│   │   │   └── quality/       # 质量管理模块
│   │   ├── platform/          # 平台服务（AI、存储等）
│   │   └── shared/            # 共享代码
│   ├── alembic/               # 数据库迁移
│   │   └── versions/          # 迁移版本
│   ├── scripts/               # 脚本
│   ├── uploads/               # 上传文件目录
│   ├── pyproject.toml         # Python 依赖
│   ├── Dockerfile              # Docker 配置
│   └── .env.example           # 环境变量示例
├── frontend/                   # 前端代码
│   ├── src/
│   │   ├── app/              # Next.js App Router
│   │   ├── actions/           # Server Actions
│   │   ├── components/        # 组件
│   │   ├── lib/               # 工具库
│   │   └── types/             # TypeScript 类型
│   ├── package.json            # Node 依赖
│   ├── Dockerfile              # Docker 配置
│   └── .env.example            # 环境变量示例
├── docker-compose.yml          # Docker Compose 配置
├── deploy.sh                   # Linux/macOS 部署脚本
├── deploy.bat                  # Windows 部署脚本
└── README.md                   # 本文档
```

## 快速部署

### 环境要求

- Docker >= 20.10
- Docker Compose >= 2.0
- 内存 >= 4GB
- 磁盘 >= 20GB

### 一键部署（推荐）

```bash
# Linux/macOS
chmod +x deploy.sh
./deploy.sh

# Windows
deploy.bat
```

### 手动部署

```bash
# 1. 克隆或下载代码
git clone https://github.com/Mao-Tony/dahzah-quality-management.git
cd dahzah-quality-management

# 2. 配置环境变量
cp backend/.env.example backend/.env
# 编辑 backend/.env 配置数据库

cp frontend/.env.example frontend/.env.local
# 编辑 frontend/.env.local 配置 API 地址

# 3. 启动服务
docker-compose up -d

# 4. 运行数据库迁移
docker-compose exec backend alembic upgrade head

# 5. 初始化数据（可选）
docker-compose exec -T backend bash scripts/init_db.sh
```

### 访问地址

- 前端界面: http://localhost:3000
- 后端 API: http://localhost:8000
- API 文档: http://localhost:8000/docs

## 数据库表结构

### qms schema

| 表名 | 说明 |
|------|------|
| qms_ai_config | AI 配置表 |
| qms_ai_log | AI 交互日志表 |
| qms_reagent_quality | 试剂/标准品台账表 |

### quality schema

| 表名 | 说明 |
|------|------|
| quality_deviations | 偏差主表 |
| quality_deviation_investigations | 偏差调查表 |
| quality_deviation_corrections | 偏差整改表 |
| quality_deviation_closings | 偏差关闭表 |
| quality_deviation_approvals | 偏差审批记录表 |
| sop_rule | SOP 规则表 |
| dev_task | 偏差任务表 |
| report_template | 报告模板表 |

## API 接口

### AI 配置
- `GET /api/v1/config` - 获取 AI 配置
- `POST /api/v1/config` - 保存 AI 配置

### AI 日志
- `GET /api/v1/ai/logs` - 获取 AI 交互日志列表
- `GET /api/v1/ai/logs/{id}` - 获取日志详情

### 试剂管理
- `GET /api/v1/quality/reagent/list` - 试剂列表
- `POST /api/v1/quality/reagent` - 创建试剂记录
- `PUT /api/v1/quality/reagent/{id}` - 更新试剂记录
- `DELETE /api/v1/quality/reagent/{id}` - 删除试剂记录
- `POST /api/v1/quality/reagent/recognize` - AI 识别标签

### 偏差报告自动化
- `GET /api/v1/quality/deviation-automation/sop-rules` - SOP 规则列表
- `POST /api/v1/quality/deviation-automation/sop-rules` - 创建 SOP 规则
- `PUT /api/v1/quality/deviation-automation/sop-rules/{id}` - 更新 SOP 规则
- `DELETE /api/v1/quality/deviation-automation/sop-rules/{id}` - 删除 SOP 规则
- `GET /api/v1/quality/deviation-automation/tasks` - 任务列表
- `POST /api/v1/quality/deviation-automation/tasks` - 创建任务
- `POST /api/v1/quality/deviation-automation/upload` - 上传并解析 Word 文件
- `GET /api/v1/quality/deviation-automation/templates` - 模板列表
- `POST /api/v1/quality/deviation-automation/templates` - 创建模板

## 前端页面

| 路由 | 功能 |
|------|------|
| /quality | 质量管理主页 |
| /quality/reagent | 试剂/标准品管理 |
| /quality/deviation-automation/create | 新建偏差报告 |
| /quality/deviation-automation/history | 历史任务查询 |
| /quality/deviation-automation/preview/[id] | 报告预览 |
| /quality/deviation-automation/sop | SOP 规则管理 |
| /quality/deviation-automation/templates | 报告模板管理 |
| /quality/ai-config | AI 配置设置 |
| /quality/ai-log | AI 交互日志 |

## AI 功能配置

### MiniMax API

1. 访问 [MiniMax开放平台](https://platform.minimaxi.com/) 注册账号
2. 获取 API Key
3. 在前端 `/quality/ai-config` 页面配置 API Key
4. 可选配置：
   - Base URL: 默认 `https://api.minimaxi.com/v1`
   - 模型: 默认 `MiniMax-M3` (视觉), `MiniMax-M2.7` (文本)
   - Temperature: 默认 0.7
   - Max Tokens: 默认 1024

## 开发指南

### 后端开发

```bash
cd backend

# 安装依赖
uv sync

# 运行开发服务器
uv run uvicorn app.main:app --reload --port 8000

# 运行迁移
uv run alembic upgrade head

# 创建新迁移
uv run alembic revision --autogenerate -m "描述"
```

### 前端开发

```bash
cd frontend

# 安装依赖
pnpm install

# 运行开发服务器
pnpm dev

# 构建生产版本
pnpm build
```

## Docker 部署细节

### 环境变量

**后端 (backend/.env)**
```env
APP_NAME=dazah-quality-backend
APP_ENV=production
DEBUG=false
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql+asyncpg://postgres:postgres@postgres:5432/dazah_quality
REDIS_URL=redis://redis:6379/0
API_V1_PREFIX=/api/v1
```

**前端 (frontend/.env.local)**
```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
NEXT_PUBLIC_APP_NAME=质量管理模块
```

### 端口映射

| 服务 | 容器端口 | 主机端口 |
|------|----------|----------|
| PostgreSQL | 5432 | 5432 |
| Redis | 6379 | 6379 |
| Backend | 8000 | 8000 |
| Frontend | 3000 | 3000 |

## 故障排除

### 数据库连接失败
```bash
# 检查 PostgreSQL 日志
docker-compose logs postgres

# 手动连接测试
docker-compose exec postgres psql -U postgres
```

### 迁移失败
```bash
# 查看当前迁移状态
docker-compose exec backend alembic current

# 回滚到上一个版本
docker-compose exec backend alembic downgrade -1

# 重新运行迁移
docker-compose exec backend alembic upgrade head
```

### 前端无法连接后端
1. 检查后端是否正常运行: `docker-compose ps`
2. 检查环境变量 `NEXT_PUBLIC_API_URL` 是否正确
3. 检查后端 CORS 配置

## License

MIT License
