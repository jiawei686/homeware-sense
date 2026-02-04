# 贡献指南

欢迎来到Homeware Sense项目！我们很高兴您有兴趣为这个开源项目做出贡献。

## 📋 目录
- [行为准则](#行为准则)
- [开始之前](#开始之前)
- [贡献方式](#贡献方式)
- [开发设置](#开发设置)
- [代码规范](#代码规范)
- [提交指南](#提交指南)
- [问题报告](#问题报告)
- [功能请求](#功能请求)

## 行为准则

请阅读并遵守我们的行为准则，确保社区友好和包容。

## 开始之前

### 项目概述
Homeware Sense是一个统一的环境感知技能，允许OpenClaw AI助手感知和响应物理环境的变化。该技能支持多种智能家居平台，包括HomeKit、Mi Home、MQTT、GPIO和模拟器。

### 技术栈
- Python 3.8+
- OpenClaw Skill Framework
- 可选：HAP-python (HomeKit), python-miio (Mi Home), paho-mqtt (MQTT)

## 贡献方式

### 🐛 报告Bug
- 在Issues中搜索是否已有相似问题
- 新建Issue并使用Bug报告模板
- 提供详细的复现步骤

### ✨ 提交功能
- 在Issues中讨论新功能的可行性
- 提交功能请求使用Feature Request模板
- 确保功能符合项目目标

### 📝 改进文档
- 修正拼写错误
- 改进现有文档
- 添加新的使用示例

### 🔧 提交代码
- Fork仓库
- 创建功能分支
- 提交PR

## 开发设置

### 环境准备
```bash
# 克隆仓库
git clone https://github.com/jiawei686/homeware-sense-skill.git
cd homeware-sense-skill

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或 venv\Scripts\activate  # Windows

# 安装开发依赖
pip install -e .
```

### 运行测试
```bash
python -m unittest discover -s test_homeware_sense_skill.py
```

### 运行技能
```bash
python -m homeware_sense_skill get_data
```

## 代码规范

### Python代码规范
- 遵循PEP 8风格指南
- 使用类型提示
- 编写有意义的提交信息
- 保持函数简洁

### 文件结构
```
homeware_sense_skill/
├── __init__.py
├── homeware_sense_skill.py    # 主技能实现
├── bridge.py                  # 与原实现桥接
├── api.py                     # API接口
├── config.py                  # 配置管理
├── SKILL.md                   # 技能文档
├── test_homeware_sense_skill.py  # 测试文件
└── README.md
```

### 提交信息格式
```
feat: 添加新功能
fix: 修复bug
docs: 更新文档
style: 代码样式调整
refactor: 重构代码
test: 添加测试
chore: 构建过程或辅助工具变动
```

## 提交指南

### 1. Fork仓库
点击GitHub上的"Fork"按钮创建仓库副本

### 2. 克隆仓库
```bash
git clone https://github.com/YOUR_USERNAME/homeware-sense-skill.git
cd homeware-sense-skill
```

### 3. 创建分支
```bash
git checkout -b feature/your-feature-name
```

### 4. 进行更改
- 遵循代码规范
- 添加测试（如适用）
- 更新文档（如适用）

### 5. 提交更改
```bash
git add .
git commit -m "feat: 添加新功能描述"
```

### 6. 推送更改
```bash
git push origin feature/your-feature-name
```

### 7. 创建PR
在GitHub上创建Pull Request

## 问题报告

### Bug报告
当报告Bug时，请包含以下信息：
- 问题描述
- 复现步骤
- 预期行为
- 实际行为
- 系统环境（操作系统、Python版本等）
- 相关错误日志

### 性能问题
- 问题描述
- 性能测试数据
- 环境配置信息

## 功能请求

提交功能请求时，请描述：
- 需求背景
- 期望的功能
- 使用场景
- 实现建议（可选）

## 平台支持贡献

### 添加新平台支持
Homeware Sense使用硬件抽象层来支持不同平台。要添加新平台支持：

1. 在`hardware/`目录下创建新的适配器
2. 继承基类`BaseSensor`
3. 实现必要的方法
4. 在配置中注册新平台类型
5. 添加相应的测试
6. 更新文档

### 示例适配器结构
```python
from .base_sensor import BaseSensor

class NewPlatformAdapter(BaseSensor):
    def __init__(self, config):
        super().__init__(config)
        # 初始化代码
    
    def read_sensor(self):
        # 传感器读取逻辑
        pass
    
    def validate_config(self):
        # 配置验证逻辑
        pass
```

## 测试要求

所有功能都需要相应的测试：
- 单元测试覆盖主要功能
- 集成测试验证整体功能
- 边界条件测试
- 错误处理测试

## 文档要求

- 为新功能添加文档
- 更新README.md（如需要）
- 为公共API添加docstrings
- 更新使用示例

## 联系方式

如有疑问，请：
- 在Issues中提问
- 查看现有讨论
- 联系项目维护者

## 感谢

感谢您花时间阅读这份贡献指南，我们期待您的贡献！