# Homeware Sense - OpenClaw技能

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw Skill](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://github.com/openclaw/openclaw)

Homeware Sense是一个统一的环境感知技能，允许OpenClaw AI助手感知和响应物理环境的变化。该技能支持多种智能家居平台，包括HomeKit、Mi Home、MQTT、GPIO和模拟器。

## ✨ 功能特性

- **多平台支持**: HomeKit, Mi Home, MQTT, GPIO, 模拟器
- **统一接口**: 所有平台通过相同API访问
- **自动回退**: 硬件不可用时自动切换到模拟器
- **简化接入**: 最少代码量完成平台接入
- **实时监控**: 温度、湿度、光照、声音、运动、空气质量
- **阈值管理**: 可配置的警报阈值

## 🚀 快速开始

### 安装

将此技能文件夹复制到OpenClaw的skills目录：

```bash
git clone https://github.com/jiawei686/homeware-sense.git
cp -r homeware-sense ~/.openclaw/skills/
```

或者直接下载到您的OpenClaw技能目录：

```bash
cd ~/.openclaw/skills/
wget https://github.com/jiawei686/homeware-sense/archive/main.zip
unzip main.zip
mv homeware-sense-main homeware-sense
```

### Python API

```python
from homeware_sense_skill import HomewareSenseSkill

# 基本使用
skill = HomewareSenseSkill()
result = skill.get_environment_data()
print(result)

# 设置阈值
thresholds = {
    'temperature': [18, 26],
    'humidity': [30, 70]
}
result = skill.set_thresholds(thresholds)
```

### 简化接口

```python
from homeware_sense_skill import HomewareSenseSkill

# 自动检测所有平台
skill = HomewareSenseSkill.quick_connect('auto')
result = skill.get_environment_data()

# 指定平台连接
skill = HomewareSenseSkill.quick_connect('homekit')  # HomeKit
skill = HomewareSenseSkill.quick_connect('mihome')   # Mi Home
skill = HomewareSenseSkill.quick_connect('mqtt')     # MQTT
skill = HomewareSenseSkill.quick_connect('gpio')     # GPIO
```

### 环境变量配置

```python
from homeware_sense_skill import HomewareSenseSkill

# 从环境变量加载配置
skill = HomewareSenseSkill.from_env()
result = skill.get_environment_data()
```

## 🔧 配置选项

- `debug`: 调试模式
- `sensors_enabled`: 启用的传感器类型
- `hardware_config`: 硬件配置
- `polling_interval`: 轮询间隔（秒）
- `data_retention_days`: 数据保留天数

### 硬件配置示例

```json
{
  "hardware_config": {
    "temperature": {
      "enabled": true,
      "type": "homekit",
      "accessory_id": "com.example.temperature-sensor",
      "pin_code": "123-45-678",
      "sensor_type": "temperature",
      "location": "living_room"
    },
    "humidity": {
      "enabled": true,
      "type": "mihome",
      "device_ip": "192.168.1.100",
      "device_token": "your_mihome_device_token",
      "sensor_type": "air_monitor",
      "location": "bedroom"
    }
  }
}
```

## 📱 支持的平台

- **HomeKit**: Apple HomeKit兼容设备
- **Mi Home**: 小米米家生态系统
- **MQTT**: MQTT协议传感器
- **GPIO**: 树莓派GPIO传感器
- **模拟器**: 无需硬件的软件模拟

## 📚 API端点

- `GET /environment-data`: 获取环境数据
- `POST /thresholds`: 设置阈值
- `GET /platform-status`: 获取平台状态
- `GET /health`: 健康检查

## 🛠️ 可选依赖

根据您使用的硬件平台，可能需要安装额外的依赖：

```bash
# HomeKit支持
pip install HAP-python

# Mi Home支持
pip install python-miio

# MQTT支持
pip install paho-mqtt
```

## 🤝 贡献

欢迎提交Issue和Pull Request来改进Homeware Sense技能！

## 📄 许可证

MIT License - 查看 [LICENSE](LICENSE) 文件了解详情

## 🙏 致谢

感谢OpenClaw社区的支持和反馈。

---

⭐ 如果这个项目对您有帮助，请给个Star！