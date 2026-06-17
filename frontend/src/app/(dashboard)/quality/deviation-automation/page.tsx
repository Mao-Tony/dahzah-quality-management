'use client'

import { Card, Row, Col, Statistic, Button, Space, Typography } from 'antd'
import {
  PlusOutlined,
  FileTextOutlined,
  HistoryOutlined,
  SettingOutlined,
  AimOutlined,
  TemplateOutlined,
} from '@ant-design/icons'
import Link from 'next/link'

const { Title } = Typography

// 模拟统计数据，实际应从API获取
const statistics = {
  pendingTasks: 5,
  completedToday: 12,
  totalRules: 25,
  totalTemplates: 8,
}

export default function DeviationAutomationPage() {
  return (
    <div className="p-6">
      <Card
        title="偏差报告自动化"
        extra={
          <Link href="/quality/deviation-automation/create">
            <Button type="primary" icon={<PlusOutlined />}>
              新建偏差报告
            </Button>
          </Link>
        }
      >
        <Row gutter={16} className="mb-6">
          <Col span={6}>
            <Card bordered={false} hoverable>
              <Statistic
                title="待处理任务"
                value={statistics.pendingTasks}
                prefix={<AimOutlined />}
                valueStyle={{ color: '#faad14' }}
              />
              <div className="mt-4">
                <Link href="/quality/deviation-automation/history?status=1">
                  <Button type="link">查看详情</Button>
                </Link>
              </div>
            </Card>
          </Col>
          <Col span={6}>
            <Card bordered={false} hoverable>
              <Statistic
                title="今日完成"
                value={statistics.completedToday}
                prefix={<FileTextOutlined />}
                valueStyle={{ color: '#52c41a' }}
              />
              <div className="mt-4">
                <Link href="/quality/deviation-automation/history">
                  <Button type="link">查看详情</Button>
                </Link>
              </div>
            </Card>
          </Col>
          <Col span={6}>
            <Card bordered={false} hoverable>
              <Statistic
                title="SOP规则数"
                value={statistics.totalRules}
                prefix={<SettingOutlined />}
              />
              <div className="mt-4">
                <Link href="/quality/deviation-automation/sop">
                  <Button type="link">管理规则</Button>
                </Link>
              </div>
            </Card>
          </Col>
          <Col span={6}>
            <Card bordered={false} hoverable>
              <Statistic
                title="报告模板数"
                value={statistics.totalTemplates}
                prefix={<TemplateOutlined />}
              />
              <div className="mt-4">
                <Link href="/quality/deviation-automation/templates">
                  <Button type="link">管理模板</Button>
                </Link>
              </div>
            </Card>
          </Col>
        </Row>

        <Title level={5}>快速入口</Title>
        <Row gutter={16} className="mt-4">
          <Col span={6}>
            <Link href="/quality/deviation-automation/create">
              <Card hoverable className="text-center">
                <PlusOutlined style={{ fontSize: 32, color: '#1890ff' }} />
                <div className="mt-2">新建偏差报告</div>
                <div className="text-gray-500 text-sm">上传Word文档，AI自动标准化</div>
              </Card>
            </Link>
          </Col>
          <Col span={6}>
            <Link href="/quality/deviation-automation/history">
              <Card hoverable className="text-center">
                <HistoryOutlined style={{ fontSize: 32, color: '#52c41a' }} />
                <div className="mt-2">历史任务</div>
                <div className="text-gray-500 text-sm">查看所有偏差报告任务</div>
              </Card>
            </Link>
          </Col>
          <Col span={6}>
            <Link href="/quality/deviation-automation/sop">
              <Card hoverable className="text-center">
                <SettingOutlined style={{ fontSize: 32, color: '#722ed1' }} />
                <div className="mt-2">SOP规则管理</div>
                <div className="text-gray-500 text-sm">配置SOP规则和标准语句</div>
              </Card>
            </Link>
          </Col>
          <Col span={6}>
            <Link href="/quality/deviation-automation/templates">
              <Card hoverable className="text-center">
                <TemplateOutlined style={{ fontSize: 32, color: '#eb2f96' }} />
                <div className="mt-2">报告模板</div>
                <div className="text-gray-500 text-sm">管理报告模板文件</div>
              </Card>
            </Link>
          </Col>
        </Row>
      </Card>

      <Card title="功能说明" className="mt-4">
        <Space direction="vertical" style={{ width: '100%' }}>
          <div>
            <strong>偏差报告自动化</strong> - 将原始偏差报告文档通过AI技术自动转换为标准化格式。
          </div>
          <ul style={{ marginLeft: 20, color: '#666' }}>
            <li>上传原始Word偏差报告文档</li>
            <li>AI自动识别偏差内容并提取关键信息</li>
            <li>根据SOP规则进行内容标准化处理</li>
            <li>生成符合规范的标准化偏差报告</li>
            <li>支持报告预览、编辑和导出</li>
          </ul>
        </Space>
      </Card>
    </div>
  )
}
