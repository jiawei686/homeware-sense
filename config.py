"""
Homeware Sense 技能配置
"""
from skills.envsense.config import Config as BaseConfig


class SkillConfig(BaseConfig):
    """
    Homeware Sense 技能配置类
    继承自基础配置并添加技能特定配置
    """
    
    def __init__(self, config_dict: Optional[Dict[str, Any]] = None):
        """
        初始化技能配置
        
        Args:
            config_dict: 配置字典
        """
        super().__init__(config_dict)
        
        # 技能特定配置
        self.skill_name = "homeware_sense"
        self.skill_version = "1.0.0"
        
        # 应用传入的配置
        if config_dict:
            self._apply_config(config_dict)
        
        # 从环境变量覆盖配置
        self._apply_env_vars()
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        base_dict = super().to_dict()
        base_dict.update({
            'skill_name': self.skill_name,
            'skill_version': self.skill_version
        })
        return base_dict