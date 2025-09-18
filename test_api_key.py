#!/usr/bin/env python3
"""
BabelDOC API密钥测试脚本
测试OpenAI API密钥是否有效
"""

import os
import asyncio
from pathlib import Path

def check_api_key():
    """检查API密钥设置"""
    print("🔑 检查API密钥设置...")
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ 未找到OPENAI_API_KEY环境变量")
        print("   请设置API密钥：")
        print("   export OPENAI_API_KEY='your-api-key-here'")
        return False
    
    print(f"✅ 找到API密钥: {api_key[:8]}...")
    
    # 验证密钥格式
    if not api_key.startswith("sk-"):
        print("⚠️  警告：API密钥格式可能不正确（通常以 'sk-' 开头）")
    
    return True

async def test_openai_connection():
    """测试OpenAI连接"""
    print("\n🌐 测试OpenAI连接...")
    
    try:
        import openai
        from openai import AsyncOpenAI
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("❌ 未设置API密钥")
            return False
        
        # 创建客户端
        client = AsyncOpenAI(api_key=api_key)
        
        # 测试连接（简单的模型列表请求）
        print("   正在测试连接...")
        models = await client.models.list()
        
        print("✅ OpenAI连接成功！")
        print(f"   可用模型数量: {len(models.data)}")
        
        # 显示一些常用模型
        model_names = [model.id for model in models.data if 'gpt' in model.id.lower()]
        if model_names:
            print("   推荐模型:")
            for model in model_names[:5]:  # 显示前5个
                print(f"     - {model}")
        
        return True
        
    except Exception as e:
        print(f"❌ OpenAI连接失败: {e}")
        return False

def test_babeldoc_translator():
    """测试BabelDOC翻译器"""
    print("\n🔧 测试BabelDOC翻译器...")
    
    try:
        from babeldoc.translator.translator import OpenAITranslator
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("❌ 未设置API密钥")
            return False
        
        # 创建翻译器实例
        translator = OpenAITranslator(
            lang_in="en",
            lang_out="zh",
            model="gpt-4o-mini",
            api_key=api_key
        )
        
        print("✅ BabelDOC翻译器创建成功")
        print(f"   源语言: {translator.lang_in}")
        print(f"   目标语言: {translator.lang_out}")
        print(f"   模型: {translator.model}")
        
        return True
        
    except Exception as e:
        print(f"❌ BabelDOC翻译器测试失败: {e}")
        return False

async def test_simple_translation():
    """测试简单翻译"""
    print("\n📝 测试简单翻译...")
    
    try:
        from babeldoc.translator.translator import OpenAITranslator
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("❌ 未设置API密钥")
            return False
        
        translator = OpenAITranslator(
            lang_in="en",
            lang_out="zh",
            model="gpt-4o-mini",
            api_key=api_key
        )
        
        # 测试简单翻译
        test_text = "Hello, world!"
        print(f"   测试文本: {test_text}")
        print("   正在翻译...")
        
        result = await translator.translate_async(test_text)
        
        print(f"✅ 翻译成功: {result}")
        return True
        
    except Exception as e:
        print(f"❌ 翻译测试失败: {e}")
        return False

def show_usage_examples():
    """显示使用示例"""
    print("\n💡 使用示例:")
    print("=" * 50)
    
    print("1. 命令行翻译:")
    print("   uv run babeldoc --openai --files example.pdf")
    
    print("\n2. 使用配置文件:")
    print("   uv run babeldoc --config config_with_api.toml --files example.pdf")
    
    print("\n3. 指定特定页面:")
    print("   uv run babeldoc --openai --files example.pdf --pages 1,2,3")
    
    print("\n4. 调整翻译质量:")
    print("   uv run babeldoc --openai --files example.pdf --qps 2 --pool-max-workers 4")

async def main():
    """主测试函数"""
    print("🧪 BabelDOC API密钥测试")
    print("=" * 50)
    
    # 检查API密钥
    if not check_api_key():
        print("\n💡 设置API密钥的方法:")
        print("   1. 运行设置脚本: bash setup_env.sh")
        print("   2. 手动设置: export OPENAI_API_KEY='your-key'")
        print("   3. 在配置文件中设置: 编辑 config_with_api.toml")
        return False
    
    # 测试OpenAI连接
    if not await test_openai_connection():
        print("\n💡 可能的解决方案:")
        print("   1. 检查API密钥是否正确")
        print("   2. 检查网络连接")
        print("   3. 检查OpenAI账户余额")
        return False
    
    # 测试BabelDOC翻译器
    if not test_babeldoc_translator():
        return False
    
    # 测试简单翻译
    if not await test_simple_translation():
        print("\n💡 翻译测试失败，但API连接正常")
        print("   可能是模型权限或配额问题")
    
    # 显示使用示例
    show_usage_examples()
    
    print("\n🎉 API密钥配置完成！可以开始使用BabelDOC了。")
    return True

if __name__ == "__main__":
    success = asyncio.run(main())
    exit(0 if success else 1)
