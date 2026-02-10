# Homeware Sense - OpenClaw Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw Skill](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://github.com/openclaw/openclaw)
[![Smart Home](https://img.shields.io/badge/Smart-Home-orange)](https://github.com/topics/smart-home)
[![IoT](https://img.shields.io/badge/IoT-Device-green)](https://github.com/topics/iot)

<p align="center">
  <img src="https://placehold.co/800x200/4a6cf7/ffffff?text=Homeware+Sense+-+Unified+Home+Automation" alt="Homeware Sense Banner">
</p>

> 🏠 Unified environmental sensing and smart home integration framework - enabling AI assistants to perceive the physical world

Homeware Sense is a unified environmental sensing skill that allows the OpenClaw AI assistant to perceive and respond to physical environment changes. This skill supports multiple smart home platforms including HomeKit, Mi Home, MQTT, GPIO, and simulators.

## ✨ Core Features

### 🌍 Multi-Platform Unified Support
- **Apple HomeKit**: Native support for HomeKit compatible devices
- **Xiaomi Mi Home**: Integration with Xiaomi ecosystem devices
- **MQTT Protocol**: Support for generic MQTT sensors
- **GPIO Interface**: Support for Raspberry Pi GPIO sensors
- **Smart Simulation**: Develop and test without hardware

### ⚡ Simplified Integration
- **Unified API**: Same interface for all platforms
- **Auto Discovery**: Automatically detect available hardware platforms
- **Fallback**: Automatically switch to simulator when hardware is unavailable
- **Minimal Code**: Integrate platforms with just a few lines of code

### 🛡️ Smart Monitoring
- **Real-time Monitoring**: Temperature, humidity, light, sound, motion, air quality
- **Smart Alerts**: Automatic notifications when thresholds are exceeded
- **Data Aggregation**: Analyze data from multiple sensors

## 🚀 Quick Start

### Installation

#### Method 1: Git Clone
```bash
cd ~/.openclaw/skills/
git clone https://github.com/jiawei686/homeware-sense-skill.git
```

#### Method 2: Direct Download
```bash
cd ~/.openclaw/skills/
curl -L https://github.com/jiawei686/homeware-sense-skill/archive/main.zip -o homeware-sense-skill.zip
unzip homeware-sense-skill.zip
mv homeware-sense-skill-main homeware-sense-skill
```

### Basic Usage

#### Simplified Interface (Recommended)
```python
from homeware_sense_skill import HomewareSenseSkill

# Auto-connect to all available platforms
skill = HomewareSenseSkill.quick_connect('auto')
data = skill.get_environment_data()
print(data)
```

#### Specified Platform Connection
```python
from homeware_sense_skill import HomewareSenseSkill

# Connect to specific platform
skill = HomewareSenseSkill.quick_connect('homekit')  # HomeKit
skill = HomewareSenseSkill.quick_connect('mihome')   # Mi Home
skill = HomewareSenseSkill.quick_connect('mqtt')     # MQTT
skill = HomewareSenseSkill.quick_connect('gpio')     # GPIO
```

#### Advanced Configuration
```python
from homeware_sense_skill import HomewareSenseSkill

# Custom configuration
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
            'type': 'homekit',  # or 'mihome', 'mqtt', 'gpio', 'mock'
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

## 📋 Supported Sensor Types

| Sensor Type | Description | Unit |
|------------|-------------|------|
| temperature | Temperature | °C |
| humidity | Humidity | % |
| light | Light intensity | lux |
| sound | Sound level | dB |
| motion | Motion detection | boolean |
| air_quality | Air quality | AQI |

## 📚 API Reference

### Main Methods

#### `get_environment_data()`
Get current environment data

```python
result = skill.get_environment_data()
# Returns: {
#   'success': bool,
#   'data': {...},
#   'error': str | None,
#   'meta': {...}
# }
```

#### `set_thresholds(thresholds)`
Set sensor thresholds

```python
thresholds = {
    'temperature': [18, 26],  # [min, max]
    'humidity': [30, 70]
}
result = skill.set_thresholds(thresholds)
```

#### `get_platform_status()`
Get platform connection status

```python
status = skill.get_platform_status()
```

#### `quick_connect(platform)`
Quickly connect to specified platform

```python
skill = HomewareSenseSkill.quick_connect('auto')
```

## 🔧 Configuration Options

### Global Configuration
- `debug`: Enable debug mode
- `sensors_enabled`: Control enabled sensor types
- `polling_interval`: Data polling interval (seconds)
- `data_retention_days`: Data retention days

### Hardware Configuration Examples

#### HomeKit Configuration
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

#### Mi Home Configuration
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

#### MQTT Configuration
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

## 🛠️ Optional Dependencies

Depending on the hardware platform used, additional dependencies may be required:

```bash
# HomeKit Support
pip install HAP-python

# Mi Home Support
pip install python-miio

# MQTT Support
pip install paho-mqtt

# Flask for API interface (optional)
pip install flask
```

## 📖 Usage Scenarios

### Scenario 1: Smart Temperature Control
```python
from homeware_sense_skill import HomewareSenseSkill

skill = HomewareSenseSkill.quick_connect('auto')
data = skill.get_environment_data()

temp = data['data']['environment_status']['temperature']
if temp > 26:
    print("Temperature too high, suggest turning on AC")
elif temp < 18:
    print("Temperature too low, suggest turning on heater")
```

### Scenario 2: Smart Lighting
```python
from homeware_sense_skill import HomewareSenseSkill

skill = HomewareSenseSkill.quick_connect('auto')
data = skill.get_environment_data()

light = data['data']['environment_status']['light_level']
if light < 100:  # Dark environment
    print("Suggest turning on indoor lighting")
```

### Scenario 3: Environmental Alerts
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
        print(f"Alert: {alert['message']}")
```

## 🤝 Contributing

Issues and Pull Requests are welcome to improve the Homeware Sense skill!

### Development Setup
```bash
# Clone the repository
git clone https://github.com/jiawei686/homeware-sense-skill.git
cd homeware-sense-skill

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or venv\Scripts\activate  # Windows

# Install development dependencies
pip install -e .
```

### Run Tests
```bash
python -m unittest discover -s ./test_homeware_sense_skill.py
```

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details

## 🙏 Acknowledgments

Thanks to the OpenClaw community for support and feedback.

---

⭐ If this project helps you, please give it a Star!
