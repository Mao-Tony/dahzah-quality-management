"""质量管理模块完整表结构迁移

Revision ID: quality_complete_001
Revises: ai_config_001
Create Date: 2026-06-17

此迁移文件创建完整的质量管理模块表，包括：
- quality.sop_rule (SOP规则表)
- quality.dev_task (偏差任务表)
- quality.report_template (报告模板表)
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'quality_complete_001'
down_revision = 'ai_config_001'
branch_labels = None
depends_on = None


def upgrade() -> None:
    """创建质量管理模块的完整表结构"""

    # ============================================================
    # 1. 创建 SOP 规则表 (quality.sop_rule)
    # ============================================================
    op.create_table(
        'sop_rule',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False, primary_key=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('NOW()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True, onupdate=sa.text('NOW()')),
        sa.Column('created_by', sa.String(length=100), nullable=True),
        sa.Column('updated_by', sa.String(length=100), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=False, server_default='false'),
        # SOP基本信息
        sa.Column('sop_code', sa.String(length=64), nullable=False, unique=True, comment='SOP编号'),
        sa.Column('sop_name', sa.String(length=255), nullable=False, comment='SOP名称'),
        sa.Column('sop_type', sa.String(length=50), nullable=False, comment='SOP类型'),
        sa.Column('version', sa.String(length=20), nullable=False, comment='版本号'),
        sa.Column('effective_date', sa.Date(), nullable=False, comment='生效日期'),
        sa.Column('expiry_date', sa.Date(), nullable=True, comment='失效日期'),
        # 适用范围
        sa.Column('applicable_departments', postgresql.JSONB(), nullable=True, comment='适用部门'),
        sa.Column('applicable_products', postgresql.JSONB(), nullable=True, comment='适用产品'),
        # 规则内容
        sa.Column('rule_content', postgresql.JSONB(), nullable=True, comment='规则内容（JSON格式）'),
        sa.Column('check_items', postgresql.JSONB(), nullable=True, comment='检查项目'),
        # 状态
        sa.Column('status', sa.String(length=20), nullable=False, server_default='draft', comment='状态'),
        sa.Column('attachments', postgresql.JSONB(), nullable=True, comment='附件'),
        schema='quality'
    )
    op.create_index('idx_sop_rule_code', 'sop_rule', ['sop_code'], unique=True, schema='quality')
    op.create_index('idx_sop_rule_type', 'sop_rule', ['sop_type'], schema='quality')
    op.create_index('idx_sop_rule_status', 'sop_rule', ['status'], schema='quality')

    # ============================================================
    # 2. 创建偏差任务表 (quality.dev_task)
    # ============================================================
    op.create_table(
        'dev_task',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False, primary_key=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('NOW()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True, onupdate=sa.text('NOW()')),
        sa.Column('created_by', sa.String(length=100), nullable=True),
        sa.Column('updated_by', sa.String(length=100), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=False, server_default='false'),
        # 关联偏差
        sa.Column('deviation_id', postgresql.UUID(as_uuid=True), nullable=False, comment='关联偏差ID'),
        sa.Column('deviation_no', sa.String(length=64), nullable=False, comment='偏差编号'),
        # 任务信息
        sa.Column('task_no', sa.String(length=64), nullable=False, unique=True, comment='任务编号'),
        sa.Column('task_type', sa.String(length=50), nullable=False, comment='任务类型'),
        sa.Column('task_title', sa.String(length=255), nullable=False, comment='任务标题'),
        sa.Column('task_description', sa.Text(), nullable=True, comment='任务描述'),
        # 责任人
        sa.Column('responsible_department', sa.String(length=100), nullable=True, comment='责任部门'),
        sa.Column('responsible_person', sa.String(length=100), nullable=True, comment='责任人'),
        sa.Column('assignee', sa.String(length=100), nullable=True, comment='指派人'),
        sa.Column('assignee_department', sa.String(length=100), nullable=True, comment='指派人部门'),
        # 时间节点
        sa.Column('plan_start_date', sa.DateTime(), nullable=True, comment='计划开始日期'),
        sa.Column('plan_end_date', sa.DateTime(), nullable=True, comment='计划完成日期'),
        sa.Column('actual_start_date', sa.DateTime(), nullable=True, comment='实际开始日期'),
        sa.Column('actual_end_date', sa.DateTime(), nullable=True, comment='实际完成日期'),
        # 进度和状态
        sa.Column('progress', sa.Integer(), nullable=False, server_default='0', comment='进度百分比'),
        sa.Column('priority', sa.String(length=20), nullable=False, server_default='normal', comment='优先级'),
        sa.Column('status', sa.String(length=20), nullable=False, server_default='pending', comment='状态'),
        # 结果
        sa.Column('result', sa.Text(), nullable=True, comment='任务结果'),
        sa.Column('attachments', postgresql.JSONB(), nullable=True, comment='附件'),
        sa.Column('completion_evidence', postgresql.JSONB(), nullable=True, comment='完成证据'),
        schema='quality'
    )
    op.create_index('idx_dev_task_no', 'dev_task', ['task_no'], unique=True, schema='quality')
    op.create_index('idx_dev_task_deviation', 'dev_task', ['deviation_id'], schema='quality')
    op.create_index('idx_dev_task_type', 'dev_task', ['task_type'], schema='quality')
    op.create_index('idx_dev_task_status', 'dev_task', ['status'], schema='quality')
    op.create_index('idx_dev_task_assignee', 'dev_task', ['assignee'], schema='quality')

    # ============================================================
    # 3. 创建报告模板表 (quality.report_template)
    # ============================================================
    op.create_table(
        'report_template',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False, primary_key=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('NOW()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True, onupdate=sa.text('NOW()')),
        sa.Column('created_by', sa.String(length=100), nullable=True),
        sa.Column('updated_by', sa.String(length=100), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=False, server_default='false'),
        # 模板基本信息
        sa.Column('template_code', sa.String(length=64), nullable=False, unique=True, comment='模板编码'),
        sa.Column('template_name', sa.String(length=255), nullable=False, comment='模板名称'),
        sa.Column('template_type', sa.String(length=50), nullable=False, comment='模板类型'),
        sa.Column('version', sa.String(length=20), nullable=False, comment='版本号'),
        # 模板内容
        sa.Column('template_content', postgresql.JSONB(), nullable=True, comment='模板内容（JSON格式）'),
        sa.Column('template_html', sa.Text(), nullable=True, comment='HTML模板内容'),
        sa.Column('template_css', sa.Text(), nullable=True, comment='CSS样式'),
        sa.Column('variables', postgresql.JSONB(), nullable=True, comment='变量定义'),
        # 适用范围
        sa.Column('applicable_modules', postgresql.JSONB(), nullable=True, comment='适用模块'),
        sa.Column('applicable_departments', postgresql.JSONB(), nullable=True, comment='适用部门'),
        # 状态
        sa.Column('is_default', sa.Boolean(), nullable=False, server_default='false', comment='是否默认模板'),
        sa.Column('status', sa.String(length=20), nullable=False, server_default='draft', comment='状态'),
        sa.Column('attachments', postgresql.JSONB(), nullable=True, comment='附件'),
        schema='quality'
    )
    op.create_index('idx_report_template_code', 'report_template', ['template_code'], unique=True, schema='quality')
    op.create_index('idx_report_template_type', 'report_template', ['template_type'], schema='quality')
    op.create_index('idx_report_template_status', 'report_template', ['status'], schema='quality')

    # ============================================================
    # 4. 添加外键约束
    # ============================================================
    # dev_task 到 quality_deviations 的外键
    op.create_foreign_key(
        'fk_dev_task_deviation',
        'dev_task', 'quality_deviations',
        ['deviation_id'], ['id'],
        source_schema='quality', referent_schema='quality'
    )


def downgrade() -> None:
    """删除质量管理模块的表结构"""

    # 删除外键约束
    op.drop_constraint('fk_dev_task_deviation', 'dev_task', 'foreignkey', schema='quality')

    # 删除表（按依赖顺序）
    op.drop_table('report_template', schema='quality')
    op.drop_table('dev_task', schema='quality')
    op.drop_table('sop_rule', schema='quality')
