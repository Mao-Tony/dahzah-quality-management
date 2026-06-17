#!/bin/bash
# ===========================================
# 数据库初始化脚本
# ===========================================
# 用于初始化 PostgreSQL 数据库和运行迁移

set -e

echo "==========================================="
echo "质量管理模块 - 数据库初始化"
echo "==========================================="

# 等待 PostgreSQL 就绪
echo "等待 PostgreSQL 就绪..."
sleep 5

# 运行 Alembic 迁移
echo "运行数据库迁移..."
cd /app
alembic upgrade head

# 创建初始数据（如果需要）
echo "检查初始数据..."
python -c "
import asyncio
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

async def init_data():
    engine = create_async_engine('${DATABASE_URL}')
    async with engine.connect() as conn:
        # 检查是否已有 SOP 规则
        result = await conn.execute(text('SELECT COUNT(*) FROM quality.sop_rule'))
        count = result.scalar()
        if count == 0:
            print('创建初始 SOP 规则...')
            await conn.execute(text('''
                INSERT INTO quality.sop_rule (sop_code, sop_full_name, sop_version, business_tag, standard_limit, standard_sentence, status)
                VALUES
                ('SOP-QC-001', '偏差调查与处理管理规程', 'V1.0', '偏差管理', '偏差调查应在规定时限内完成', '按照偏差处理流程进行调查和分析', 1),
                ('SOP-QC-002', '纠正预防措施管理规程', 'V1.0', 'CAPA管理', 'CAPA应在规定时限内完成', '根据调查结论制定并执行纠正预防措施', 1)
            '''))
            await conn.commit()
            print('初始 SOP 规则创建完成')
        else:
            print(f'已有 {count} 条 SOP 规则，跳过初始化')
    await engine.dispose()

asyncio.run(init_data())
"

echo "==========================================="
echo "数据库初始化完成！"
echo "==========================================="
