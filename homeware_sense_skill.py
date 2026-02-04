"""
Homeware Sense - OpenClaw技能实现
统一的环境感知和智能家居集成框架
"""
import json
import os
from typing import Dict, Any, Optional

# 导入桥接模块
try:
    from .bridge import create_sensor_hub, HAS_ENVSENSE, EnvSenseSkill, SensorHub
except ImportError:
    # 处理直接运行的情况
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
    from bridge import create_sensor_hub, HAS_ENVSENSE, EnvSenseSkill, SensorHub


class HomewareSenseSkill:
    """
    Homeware Sense OpenClaw技能类
    统一的环境感知和智能家居集成框架
    """
    
    def __init__(self, config: Optional[Dict] = None):
        """
        初始化技能
        
        Args:
            config: 配置参数
        """
        if not HAS_ENVSENSE:
            raise RuntimeError("Homeware Sense requires EnvSense implementation to be available")
        
        # 使用桥接模块创建底层实现
        self.hub = create_sensor_hub(config)
        self.config = self.hub.config
    
    def get_environment_data(self) -> Dict[str, Any]:
        """
        获取当前环境数据
        
        Returns:
            环境数据
        """
        return self.hub.get_environment_data()
    
    def set_thresholds(self, thresholds: Dict[str, float]) -> Dict[str, Any]:
        """
        设置环境阈值
        
        Args:
            thresholds: 阈值设置
            
        Returns:
            操作结果
        """
        return self.hub.set_thresholds(thresholds)
    
    @classmethod
    def quick_connect(cls, platform: str = 'auto'):
        """
        最简化的智能家居平台连接方法
        
        Args:
            platform: 平台类型 ('homekit', 'mihome', 'mqtt', 'gpio', 'auto')
                     'auto' 会尝试自动检测可用平台
                     默认使用模拟器（无需硬件）
        
        Returns:
            HomewareSenseSkill 实例
        """
        if not HAS_ENVSENSE:
            raise RuntimeError("Homeware Sense requires EnvSense implementation to be available")
        
        hub = SensorHub.quick_connect(platform)
        skill = cls.__new__(cls)
        skill.hub = hub
        skill.config = hub.config
        return skill
    
    @classmethod
    def from_env(cls):
        """
        从环境变量创建实例，自动配置所有启用的平台
        
        Returns:
            HomewareSenseSkill 实例
        """
        hub = SensorHub.from_env()
        skill = cls.__new__(cls)
        skill.hub = hub
        skill.config = hub.config
        return skill
    
    def get_platform_status(self) -> Dict[str, Any]:
        """
        获取各平台连接状态
        
        Returns:
            平台状态信息
        """
        # 返回当前配置和状态信息
        return {
            "success": True,
            "data": {
                "configured_platforms": self._get_configured_platforms(),
                "current_config": self.config.to_dict(),
                "timestamp": self._get_timestamp()
            },
            "error": None,
            "meta": {
                "timestamp": self._get_timestamp(),
                "version": self.config.version
            }
        }
    
    def _get_configured_platforms(self) -> Dict[str, bool]:
        """获取已配置的平台列表"""
        hardware_config = getattr(self.config, 'hardware_config', {})
        platforms = {}
        for sensor_type, config in hardware_config.items():
            if config.get('enabled', False):
                platform_type = config.get('type', 'mock')
                platforms[f"{sensor_type}_{platform_type}"] = True
        return platforms
    
    def _get_timestamp(self) -> str:
        """获取当前时间戳"""
        import datetime
        return datetime.datetime.utcnow().isoformat() + "Z"


def main():
    """命令行入口"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Homeware Sense - OpenClaw环境感知技能')
    parser.add_argument('command', help='要执行的命令 (get_data, set_thresholds, get_status)')
    parser.add_argument('--config', help='配置文件路径')
    parser.add_argument('--thresholds', help='阈值配置文件路径')
    parser.add_argument('--output', help='输出文件路径')
    
    args = parser.parse_args()
    
    # 加载配置
    config = None
    if args.config:
        with open(args.config, 'r') as f:
            config = json.load(f)
    
    # 创建技能实例
    skill = HomewareSenseSkill(config)
    
    # 执行命令
    if args.command == 'get_data':
        result = skill.get_environment_data()
    elif args.command == 'set_thresholds':
        thresholds = {}
        if args.thresholds:
            with open(args.thresholds, 'r') as f:
                thresholds = json.load(f)
        result = skill.set_thresholds(thresholds)
    elif args.command == 'get_status':
        result = skill.get_platform_status()
    else:
        result = {
            "success": False,
            "data": None,
            "error": f"Unknown command: {args.command}",
            "meta": {"timestamp": "error", "version": "1.0.0"}
        }
    
    # 输出结果
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(result, f, indent=2)
        print(f"结果已保存至 {args.output}")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()