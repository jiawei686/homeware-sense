"""
Homeware Sense 技能API接口
"""
from flask import Flask, jsonify, request
import json
from .homeware_sense_skill import HomewareSenseSkill


def create_skill_app(config_dict=None):
    """
    创建技能的Flask应用
    
    Args:
        config_dict: 配置字典
        
    Returns:
        Flask应用实例
    """
    app = Flask(__name__)
    skill = HomewareSenseSkill(config_dict)
    
    @app.route('/health', methods=['GET'])
    def health():
        """健康检查端点"""
        return jsonify({
            "status": "healthy",
            "skill": "homeware_sense",
            "version": skill.config.version
        })
    
    @app.route('/environment-data', methods=['GET'])
    def get_environment_data():
        """获取环境数据端点"""
        try:
            result = skill.get_environment_data()
            return jsonify(result)
        
        except Exception as e:
            return jsonify({
                "success": False,
                "data": None,
                "error": str(e),
                "meta": {"timestamp": "error", "version": skill.config.version}
            }), 500
    
    @app.route('/thresholds', methods=['POST'])
    def set_thresholds():
        """设置阈值端点"""
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "No JSON data provided"}), 400
            
            result = skill.set_thresholds(data)
            return jsonify(result)
        
        except Exception as e:
            return jsonify({
                "success": False,
                "data": None,
                "error": str(e),
                "meta": {"timestamp": "error", "version": skill.config.version}
            }), 500
    
    @app.route('/platform-status', methods=['GET'])
    def get_platform_status():
        """获取平台状态端点"""
        try:
            result = skill.get_platform_status()
            return jsonify(result)
        
        except Exception as e:
            return jsonify({
                "success": False,
                "data": None,
                "error": str(e),
                "meta": {"timestamp": "error", "version": skill.config.version}
            }), 500
    
    return app


if __name__ == '__main__':
    import os
    app = create_skill_app()
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)