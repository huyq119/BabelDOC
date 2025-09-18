#!/usr/bin/env python3
"""
BabelDOC Gemini API 测试脚本
测试Gemini API密钥是否有效
"""

import os
import asyncio
from pathlib import Path

def check_gemini_api_key():
    """检查Gemini API密钥设置"""
    print("🤖 检查Gemini API密钥设置...")
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ 未找到GEMINI_API_KEY环境变量")
        print("   请设置API密钥：")
        print("   export GEMINI_API_KEY='your-gemini-api-key-here'")
        return False
    
    print(f"✅ 找到Gemini API密钥: {api_key[:8]}...")
    
    # 验证密钥格式
    if not api_key.startswith("AI"):
        print("⚠️  警告：Gemini API密钥格式可能不正确（通常以 'AI' 开头）")
    
    return True

async def test_gemini_connection():
    """测试Gemini连接"""
    print("\n🌐 测试Gemini连接...")
    
    try:
        import google.generativeai as genai
        
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("❌ 未设置Gemini API密钥")
            return False
        
        # 配置Gemini
        genai.configure(api_key=api_key)
        
        # 创建模型
        model = genai.GenerativeModel('gemini-pro')
        
        # 测试连接
        print("   正在测试连接...")
        response = await asyncio.to_thread(
            model.generate_content, 
            "Hello, this is a test message."
        )
        
        print("✅ Gemini连接成功！")
        print(f"   响应: {response.text[:100]}...")
        
        return True
        
    except ImportError:
        print("❌ 未安装google-generativeai包")
        print("   请运行: uv add google-generativeai")
        return False
    except Exception as e:
        print(f"❌ Gemini连接失败: {e}")
        return False

def test_litellm_option():
    """测试LiteLLM选项"""
    print("\n🔄 测试LiteLLM选项...")
    
    try:
        import litellm
        print("✅ LiteLLM已安装")
        
        # 检查可用的模型
        print("   可用的Gemini模型:")
        gemini_models = [
            "gemini/gemini-pro",
            "gemini/gemini-1.5-pro", 
            "gemini/gemini-1.5-flash"
        ]
        
        for model in gemini_models:
            print(f"     - {model}")
        
        return True
        
    except ImportError:
        print("❌ 未安装LiteLLM")
        print("   请运行: uv add litellm")
        return False
    except Exception as e:
        print(f"❌ LiteLLM测试失败: {e}")
        return False

def show_gemini_usage_examples():
    """显示Gemini使用示例"""
    print("\n💡 Gemini API使用示例:")
    print("=" * 50)
    
    print("1. 使用LiteLLM代理:")
    print("   # 启动代理")
    print("   litellm --model gemini/gemini-pro --port 4000")
    print("   # 使用BabelDOC")
    print("   uv run babeldoc --openai --openai-base-url 'http://localhost:4000' --openai-api-key 'your-key' --files example.pdf")
    
    print("\n2. 使用OpenAI兼容接口:")
    print("   uv run babeldoc --openai --openai-base-url 'https://your-proxy.com/v1' --openai-api-key 'your-gemini-key' --files example.pdf")
    
    print("\n3. 使用配置文件:")
    print("   uv run babeldoc --config config_gemini.toml --files example.pdf")

def create_gemini_config():
    """创建Gemini配置文件"""
    print("\n📝 创建Gemini配置文件...")
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ 未设置Gemini API密钥")
        return False
    
    config_content = f"""[babeldoc]
# Gemini API配置
openai = true
openai-model = "gemini-pro"
openai-base-url = "https://api.openai.com/v1"  # 替换为您的代理地址
openai-api-key = "{api_key}"

# 其他配置
lang-in = "en"
lang-out = "zh"
qps = 4
output = "./output"
"""
    
    config_file = "my_gemini_config.toml"
    with open(config_file, 'w') as f:
        f.write(config_content)
    
    print(f"✅ 配置文件已创建: {config_file}")
    return True

async def main():
    """主测试函数"""
    print("🧪 BabelDOC Gemini API测试")
    print("=" * 50)
    
    # 检查API密钥
    if not check_gemini_api_key():
        print("\n💡 设置Gemini API密钥的方法:")
        print("   1. 运行设置脚本: bash setup_gemini.sh")
        print("   2. 手动设置: export GEMINI_API_KEY='your-key'")
        print("   3. 在配置文件中设置: 编辑 config_gemini.toml")
        return False
    
    # 测试Gemini连接
    gemini_ok = await test_gemini_connection()
    
    # 测试LiteLLM选项
    litellm_ok = test_litellm_option()
    
    # 创建配置文件
    config_ok = create_gemini_config()
    
    # 显示使用示例
    show_gemini_usage_examples()
    
    if gemini_ok or litellm_ok:
        print("\n🎉 Gemini API配置完成！可以开始使用BabelDOC了。")
        return True
    else:
        print("\n⚠️  Gemini API配置有问题，请检查设置。")
        return False

if __name__ == "__main__":
    success = asyncio.run(main())
    exit(0 if success else 1)
