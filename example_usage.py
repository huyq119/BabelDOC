#!/usr/bin/env python3
"""
BabelDOC 使用示例
演示如何使用uv虚拟环境中的BabelDOC进行PDF翻译
"""

import asyncio
import os
from pathlib import Path

# 注意：这个示例需要OpenAI API密钥
# 请设置环境变量 OPENAI_API_KEY="your-api-key-here"

async def example_translation():
    """示例：使用BabelDOC进行PDF翻译"""
    
    # 检查是否有API密钥
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ 请设置环境变量 OPENAI_API_KEY")
        print("   export OPENAI_API_KEY='your-api-key-here'")
        return
    
    print("✅ 找到OpenAI API密钥")
    
    # 导入BabelDOC模块
    try:
        from babeldoc.format.pdf.high_level import async_translate
        from babeldoc.format.pdf.translation_config import TranslationConfig
        from babeldoc.translator.translator import OpenAITranslator
        print("✅ 成功导入BabelDOC模块")
    except ImportError as e:
        print(f"❌ 导入BabelDOC模块失败: {e}")
        return
    
    # 检查示例PDF文件
    example_pdf = Path("examples/ci/test.pdf")
    if not example_pdf.exists():
        print(f"❌ 示例PDF文件不存在: {example_pdf}")
        print("   请确保在BabelDOC项目根目录下运行此脚本")
        return
    
    print(f"✅ 找到示例PDF文件: {example_pdf}")
    
    # 创建翻译器
    translator = OpenAITranslator(
        lang_in="en",
        lang_out="zh",
        model="gpt-4o-mini",
        api_key=api_key
    )
    
    # 创建输出目录
    output_dir = Path("./output")
    output_dir.mkdir(exist_ok=True)
    
    # 创建翻译配置
    config = TranslationConfig(
        input_file=str(example_pdf),
        translator=translator,
        output_dir=str(output_dir),
        debug=False,
        qps=2,  # 降低QPS以避免API限制
        min_text_length=3
    )
    
    print("🚀 开始翻译...")
    print("   这可能需要几分钟时间，请耐心等待...")
    
    try:
        # 执行异步翻译
        async for event in async_translate(config):
            if event["type"] == "progress_update":
                progress = event["overall_progress"]
                stage = event["stage"]
                current = event["stage_current"]
                total = event["stage_total"]
                print(f"📊 进度: {progress:.1f}% - {stage} ({current}/{total})")
                
            elif event["type"] == "finish":
                result = event["translate_result"]
                print("✅ 翻译完成！")
                print(f"   原文: {result.original_pdf_path}")
                if result.dual_pdf_path:
                    print(f"   双语: {result.dual_pdf_path}")
                if result.mono_pdf_path:
                    print(f"   译文: {result.mono_pdf_path}")
                break
                
            elif event["type"] == "error":
                print(f"❌ 翻译出错: {event['error']}")
                break
                
    except KeyboardInterrupt:
        print("\n⏹️  翻译被用户中断")
    except Exception as e:
        print(f"❌ 翻译过程中出现错误: {e}")

def show_environment_info():
    """显示环境信息"""
    print("🔧 BabelDOC 环境信息")
    print("=" * 50)
    
    # 检查虚拟环境
    venv_path = Path(".venv")
    if venv_path.exists():
        print(f"✅ 虚拟环境: {venv_path.absolute()}")
    else:
        print("❌ 虚拟环境不存在")
    
    # 检查Python版本
    import sys
    print(f"✅ Python版本: {sys.version}")
    
    # 检查BabelDOC版本
    try:
        import babeldoc
        print(f"✅ BabelDOC版本: {babeldoc.__version__}")
    except ImportError:
        print("❌ BabelDOC未安装")
    
    # 检查关键依赖
    dependencies = [
        "pymupdf", "onnxruntime", "openai", "numpy", 
        "cv2", "rich", "httpx"
    ]
    
    print("\n📦 关键依赖检查:")
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"   ✅ {dep}")
        except ImportError:
            print(f"   ❌ {dep}")
    
    print("=" * 50)

if __name__ == "__main__":
    print("🎯 BabelDOC 使用示例")
    print()
    
    # 显示环境信息
    show_environment_info()
    print()
    
    # 运行翻译示例
    print("📝 运行翻译示例...")
    asyncio.run(example_translation())
