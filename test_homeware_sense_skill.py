"""
Homeware Sense 技能测试文件
"""
import unittest
import sys
import os
# 添加项目路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from homeware_sense_skill import HomewareSenseSkill


class TestHomewareSenseSkill(unittest.TestCase):
    """
    Homeware Sense 技能测试类
    """
    
    def setUp(self):
        """测试前准备"""
        self.skill = HomewareSenseSkill({'debug': True})
    
    def test_initialization(self):
        """测试初始化"""
        self.assertIsNotNone(self.skill)
        self.assertTrue(self.skill.config.debug)
    
    def test_get_environment_data(self):
        """测试获取环境数据"""
        result = self.skill.get_environment_data()
        self.assertTrue(result['success'])
        self.assertIsNotNone(result['data'])
        self.assertIsNone(result['error'])
        
        # 检查数据结构
        data = result['data']
        self.assertIn('environment_status', data)
        self.assertIn('readings', data)
        self.assertIn('alerts', data)
        self.assertIn('config', data)
    
    def test_set_thresholds(self):
        """测试设置阈值"""
        thresholds = {
            'temperature': [20, 25],
            'humidity': [40, 60]
        }
        result = self.skill.set_thresholds(thresholds)
        self.assertTrue(result['success'])
        self.assertIsNotNone(result['data'])
        self.assertIsNone(result['error'])
    
    def test_get_platform_status(self):
        """测试获取平台状态"""
        result = self.skill.get_platform_status()
        self.assertTrue(result['success'])
        self.assertIsNotNone(result['data'])
        self.assertIsNone(result['error'])
        
        # 检查数据结构
        data = result['data']
        self.assertIn('configured_platforms', data)
        self.assertIn('current_config', data)
        self.assertIn('timestamp', data)
    
    def test_quick_connect(self):
        """测试快速连接功能"""
        skill = HomewareSenseSkill.quick_connect('auto')
        self.assertIsNotNone(skill)
        
        result = skill.get_environment_data()
        self.assertTrue(result['success'])
    
    def test_from_env(self):
        """测试从环境变量加载功能"""
        skill = HomewareSenseSkill.from_env()
        self.assertIsNotNone(skill)
        
        result = skill.get_environment_data()
        self.assertTrue(result['success'])


if __name__ == '__main__':
    unittest.main()