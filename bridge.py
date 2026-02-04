"""
Homeware Sense 到 EnvSense 的桥接模块
用于将技能接口映射到底层实现
"""
import sys
import os

# 确保能够导入原EnvSense模块
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'envsense-skill-release', 'src'))

# 尝试导入Homeware Sense实现
HAS_ENVSENSE = False
EnvSenseSkill = None
SensorHub = None

try:
    # 尝试从重命名后的包导入
    from homeware_sense import SensorHub as ImportedSensorHub
    SensorHub = ImportedSensorHub
    EnvSenseSkill = ImportedSensorHub  # 保持兼容性
    HAS_ENVSENSE = True
except ImportError:
    try:
        # 备选：从原始技能导入
        from skills.envsense import EnvSenseSkill as OriginalSkill
        EnvSenseSkill = OriginalSkill
        HAS_ENVSENSE = True
    except ImportError:
        try:
            # 最后的备选：从当前目录导入
            sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'envsense-skill-release', 'src'))
            from homeware_sense import SensorHub as ImportedSensorHub
            SensorHub = ImportedSensorHub
            EnvSenseSkill = ImportedSensorHub
            HAS_ENVSENSE = True
        except ImportError:
            HAS_ENVSENSE = False
            print("Warning: Could not find EnvSense/Homeware Sense implementation")


def create_sensor_hub(config=None):
    """
    创建传感器中心实例的工厂函数
    
    Args:
        config: 配置参数
        
    Returns:
        SensorHub实例
    """
    if HAS_ENVSENSE and SensorHub:
        if config:
            return SensorHub(config)
        else:
            return SensorHub()
    elif HAS_ENVSENSE and EnvSenseSkill:
        if config:
            from skills.envsense import EnvSenseSkill as ESS
            return ESS(config)
        else:
            from skills.envsense import EnvSenseSkill as ESS
            return ESS()
    else:
        raise RuntimeError("No EnvSense/Homeware Sense implementation available")


__all__ = ['create_sensor_hub', 'HAS_ENVSENSE', 'EnvSenseSkill', 'SensorHub']