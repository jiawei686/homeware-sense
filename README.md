# Homeware Sense - OpenClaw技能

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw Skill](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://github.com/openclaw/openclaw)
[![Smart Home](https://img.shields.io/badge/Smart-Home-orange)](https://github.com/topics/smart-home)
[![IoT](https://img.shields.io/badge/IoT-Device-green)](https://github.com/topics/iot)

<p align="center">
  <img src="https://placehold.co/800x200/4a6cf7/ffffff?text=Homeware+Sense+-+Unified+Home+Automation" alt="Homeware Sense Banner">
</p>

> 🏠 统一的环境感知和智能家居集成框架 - 让AI助手感知物理世界

Homeware Sense是一个统一的环境感知技能，允许OpenClaw AI助手感知和响应物理环境的变化。该技能支持多种智能家居平台，包括HomeKit、Mi Home、MQTT、GPIO和模拟器。

## ✨ 核心特性

### 🌍 多平台统一支持
- **Apple HomeKit**: 原生支持HomeKit兼容设备
- **小米米家**: 集成小米生态链设备
- **MQTT协议**: 支持通用MQTT传感器
- **GPIO接口**: 支持树莓派GPIO传感器
- **智能模拟**: 无需硬件即可开发测试

### ⚡ 简化集成
- **统一API**: 所有平台使用相同的调用接口
- **自动发现**: 自动检测可用的硬件平台
- **故障回退**: 硬件不可用时自动切换到模拟器
- **最少代码**: 仅需几行代码完成平台集成

### 🛡️ 智能监控
- **实时监测**: 温度、湿度、光照、声音、运动、空气质量
- **智能警报**: 超出阈值时自动通知
- **数据聚合**: 综合多传感器数据进行分析

## 🚀 快速开始

### 安装

#### 方法1: Git Clone
```bash
cd ~/.openclaw/skills/
git clone https://github.com/jiawei686/homeware-sense-skill.git
```

#### 方法2: 直接下载
```bash
cd ~/.openclaw/skills/
curl -L https://github.com/jiawei686/homeware-sense-skill/archive/main.zip -o homeware-sense-skill.zip
unzip homeware-sense-skill.zip
mv homeware-sense-skill-main homeware-sense-skill
```

### 基础使用

#### 简化接口（推荐）
```python
from homeware_sense_skill import HomewareSenseSkill

# 自动连接所有可用平台
skill = HomewareSenseSkill.quick_connect('auto')
data = skill.get_environment_data()
print(data)
```

#### 指定平台连接
```python
from homeware_sense_skill import HomewareSenseSkill

# 连接特定平台
skill = HomewareSenseSkill.quick_connect('homekit')  # HomeKit
skill = HomewareSenseSkill.quick_connect('mihome')   # Mi Home
skill = HomewareSenseSkill.quick_connect('mqtt')     # MQTT
skill = HomewareSenseSkill.quick_connect('gpio')     # GPIO
```

#### 高级配置
```python
from homeware_sense_skill import HomewareSenseSkill

# 自定义配置
config = {
    'debug': True,
    'sensors_enabled': {
        'temperature': True,
        'humidity': True,
        'light': True
    },
    'hardware_config': {
        'temperature': {
            'enabled': True,
            'type': 'homekit',  # 或 'mihome', 'mqtt', 'gpio', 'mock'
            'accessory_id': 'com.example.sensor',
            'pin_code': '123-45-678',
            'sensor_type': 'temperature',
            'location': 'living_room'
        }
    }
}

skill = HomewareSenseSkill(config)
data = skill.get_environment_data()
```

## 📋 支持的传感器类型

| 传感器类型 | 描述 | 单位 |
|-----------|------|------|
| temperature | 温度 | °C |
| humidity | 湿度 | % |
| light | 光照强度 | lux |
| sound | 声音等级 | dB |
| motion | 运动检测 | boolean |
| air_quality | 空气质量 | AQI |

## 📚 API参考

### 主要方法

#### `get_environment_data()`
获取当前环境数据

```python
result = skill.get_environment_data()
# 返回: {
#   'success': bool,
#   'data': {...},
#   'error': str | None,
#   'meta': {...}
# }
```

#### `set_thresholds(thresholds)`
设置传感器阈值

```python
thresholds = {
    'temperature': [18, 26],  # [min, max]
    'humidity': [30, 70]
}
result = skill.set_thresholds(thresholds)
```

#### `get_platform_status()`
获取平台连接状态

```python
status = skill.get_platform_status()
```

#### `quick_connect(platform)`
快速连接指定平台

```python
skill = HomewareSenseSkill.quick_connect('auto')
```

## 🔧 配置选项

### 全局配置
- `debug`: 启用调试模式
- `sensors_enabled`: 控制启用的传感器类型
- `polling_interval`: 数据轮询间隔（秒）
- `data_retention_days`: 数据保留天数

### 硬件配置示例

#### HomeKit配置
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
    }
  }
}
```

#### Mi Home配置
```json
{
  "hardware_config": {
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

#### MQTT配置
```json
{
  "hardware_config": {
    "light": {
      "enabled": true,
      "type": "mqtt",
      "host": "localhost",
      "port": 1883,
      "topic": "sensors/light",
      "location": "kitchen"
    }
  }
}
```

## 🛠️ 可选依赖

根据使用的硬件平台，可能需要安装额外依赖：

```bash
# HomeKit支持
pip install HAP-python

# Mi Home支持
pip install python-miio

# MQTT支持
pip install paho-mqtt

# Flask用于API接口（可选）
pip install flask
```

## 📖 使用场景

### 场景1: 智能温控
```python
from homeware_sense_skill import HomewareSenseSkill

skill = HomewareSenseSkill.quick_connect('auto')
data = skill.get_environment_data()

temp = data['data']['environment_status']['temperature']
if temp > 26:
    print("温度过高，建议开启空调")
elif temp < 18:
    print("温度过低，建议开启暖气")
```

### 场景2: 智能照明
```python
from homeware_sense_skill import HomewareSenseSkill

skill = HomewareSenseSkill.quick_connect('auto')
data = skill.get_environment_data()

light = data['data']['environment_status']['light_level']
if light < 100:  # 黑暗环境
    print("建议开启室内照明")
```

### 场景3: 环境警报
```python
from homeware_sense_skill import HomewareSenseSkill

skill = HomewareSenseSkill.quick_connect('auto')
thresholds = {
    'temperature': [15, 30],
    'humidity': [30, 70],
    'air_quality': [0, 100]
}
skill.set_thresholds(thresholds)

data = skill.get_environment_data()
alerts = data['data']['alerts']
if alerts:
    for alert in alerts:
        print(f"警报: {alert['message']}")
```

## 🤝 贡献

欢迎提交Issue和Pull Request来改进Homeware Sense技能！

### 开发设置
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
python -m unittest discover -s ./test_homeware_sense_skill.py
```

## 📄 许可证

MIT License - 查看 [LICENSE](LICENSE) 文件了解详情

## 🙏 致谢

感谢OpenClaw社区的支持和反馈。

---

⭐ 如果这个项目对您有帮助，请给个Star！