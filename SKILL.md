# Homeware Sense - OpenClaw技能

## 技能描述
Homeware Sense是一个统一的环境感知技能，允许OpenClaw AI助手感知和响应物理环境的变化。该技能支持多种智能家居平台，包括HomeKit、Mi Home、MQTT、GPIO和模拟器，通过统一的接口收集环境数据，并根据这些数据提供建议或执行操作。

## 核心功能
- 实时环境监测（温度、湿度、光照、声音、运动、空气质量）
- 异常检测和警报
- 智能环境建议
- 可配置的阈值管理
- 多种硬件支持（模拟器、MQTT、GPIO、HomeKit、米家）
- 智能家居平台集成（Apple HomeKit、小米米家）
- 故障恢复机制（硬件不可用时自动回退到模拟器）

## 使用方法

### Python API
```python
from homeware_sense_skill import HomewareSenseSkill

# 初始化技能
skill = HomewareSenseSkill(config={'debug': True})

# 获取当前环境数据
result = skill.get_environment_data()
print(result)

# 设置环境阈值
thresholds = {
    'temperature': [18, 26],
    'humidity': [30, 70]
}
result = skill.set_thresholds(thresholds)
print(result)

# 获取平台状态
status = skill.get_platform_status()
print(status)
```

### 简化接口
```python
from homeware_sense_skill import HomewareSenseSkill

# 最简化的使用方式
skill = HomewareSenseSkill.quick_connect('auto')  # 自动检测所有平台
result = skill.get_environment_data()
print(result)

# 指定平台连接
skill = HomewareSenseSkill.quick_connect('homekit')  # 连接HomeKit
skill = HomewareSenseSkill.quick_connect('mihome')   # 连接Mi Home
skill = HomewareSenseSkill.quick_connect('mqtt')     # 连接MQTT
skill = HomewareSenseSkill.quick_connect('gpio')     # 连接GPIO
```

### 环境变量配置
```python
from homeware_sense_skill import HomewareSenseSkill

# 从环境变量加载配置
skill = HomewareSenseSkill.from_env()
result = skill.get_environment_data()
```

### 命令行
```bash
# 获取环境数据
python -m homeware_sense_skill get_data --output result.json

# 设置阈值
python -m homeware_sense_skill set_thresholds --thresholds thresholds.json --output result.json

# 获取平台状态
python -m homeware_sense_skill get_status --output status.json
```

## 配置选项

- `debug`: 是否启用调试模式 (默认: false)
- `sensors_enabled`: 启用的传感器类型 (默认: 全部启用)
- `hardware_config`: 硬件配置 (默认: 全部使用模拟器)
- `polling_interval`: 数据轮询间隔（秒）(默认: 30)
- `data_retention_days`: 数据保留天数 (默认: 7)

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

## 支持的硬件类型

- **模拟器 (mock)**: 软件模拟，无需实际硬件
- **MQTT传感器**: 通过MQTT协议连接的传感器
- **GPIO传感器**: 连接到树莓派GPIO引脚的传感器
- **HomeKit传感器**: Apple HomeKit兼容的传感器
- **米家传感器**: 小米米家生态系统传感器

## API接口

### GET /environment-data
获取当前环境数据

### POST /thresholds
设置环境阈值

### GET /platform-status
获取平台连接状态

## 输入数据格式

### 设置阈值
```json
{
  "temperature": [18, 26],
  "humidity": [30, 70],
  "light": [100, 10000],
  "sound": [20, 60],
  "air_quality": [0, 100]
}
```

## 输出结果格式

```json
{
  "success": true,
  "data": {
    "environment_status": {
      "temperature": 23.5,
      "humidity": 45.2,
      "light_level": 1200.5,
      "sound_level": 42.3,
      "motion_detected": false,
      "air_quality": 45.6,
      "timestamp": "2023-01-01T00:00:00Z",
      "location": null
    },
    "readings": {
      "temperature": {
        "sensor_type": "temperature",
        "value": 23.5,
        "unit": "°C",
        "timestamp": "2023-01-01T00:00:00Z",
        "location": "default",
        "device_id": null
      }
    },
    "alerts": [],
    "config": {
      "version": "1.0.0",
      "debug": false,
      "sensors_enabled": {
        "temperature": true,
        "humidity": true,
        "light": true,
        "sound": true,
        "motion": true,
        "air_quality": true
      },
      "hardware_config": {
        "temperature": {"enabled": false, "type": "mock"},
        "humidity": {"enabled": false, "type": "mock"},
        "light": {"enabled": false, "type": "mock"},
        "sound": {"enabled": false, "type": "mock"},
        "motion": {"enabled": false, "type": "mock"},
        "air_quality": {"enabled": false, "type": "mock"}
      },
      "polling_interval": 30,
      "data_retention_days": 7
    }
  },
  "error": null,
  "meta": {
    "timestamp": "2023-01-01T00:00:00Z",
    "version": "1.0.0"
  }
}
```

## 错误码

- `200`: 成功
- `400`: 请求参数错误
- `500`: 服务器内部错误

## 技能优势

1. **情境感知**: 让AI助手能够感知物理环境
2. **智能提醒**: 基于环境数据提供智能建议
3. **可配置**: 支持自定义阈值和传感器配置
4. **硬件兼容**: 支持多种真实硬件传感器和模拟器
5. **易于集成**: 简单的API接口，易于与其他系统集成
6. **故障恢复**: 硬件不可用时自动切换到模拟器
7. **多平台支持**: 统一接口支持HomeKit、Mi Home等多种智能家居平台
8. **最小化编码**: 提供简化的快速接入接口