#!/usr/bin/env python3
"""
BabelDOC 基本功能测试
测试BabelDOC的核心功能，无需API密钥
"""

import asyncio
from pathlib import Path

def test_imports():
    """测试所有关键模块的导入"""
    print("🔍 测试模块导入...")
    
    try:
        import babeldoc
        print(f"   ✅ babeldoc (版本: {babeldoc.__version__})")
    except ImportError as e:
        print(f"   ❌ babeldoc: {e}")
        return False
    
    modules_to_test = [
        ("babeldoc.format.pdf.high_level", "高级PDF处理"),
        ("babeldoc.format.pdf.translation_config", "翻译配置"),
        ("babeldoc.translator.translator", "翻译器"),
        ("babeldoc.docvision.doclayout", "文档布局分析"),
        ("babeldoc.assets.assets", "资源管理"),
    ]
    
    all_imports_ok = True
    for module_name, description in modules_to_test:
        try:
            __import__(module_name)
            print(f"   ✅ {description}")
        except ImportError as e:
            print(f"   ❌ {description}: {e}")
            all_imports_ok = False
    
    return all_imports_ok

def test_assets():
    """测试资源管理功能"""
    print("\n📦 测试资源管理...")
    
    try:
        from babeldoc.const import CACHE_FOLDER
        cache_folder = CACHE_FOLDER
        print(f"   ✅ 缓存文件夹: {cache_folder}")
        
        # 检查缓存文件夹是否存在
        if cache_folder.exists():
            print(f"   ✅ 缓存文件夹已创建")
        else:
            print(f"   ⚠️  缓存文件夹不存在，将在首次使用时创建")
        
        return True
    except Exception as e:
        print(f"   ❌ 资源管理测试失败: {e}")
        return False

def test_config():
    """测试配置功能"""
    print("\n⚙️  测试配置功能...")
    
    try:
        from babeldoc.format.pdf.translation_config import TranslationConfig, WatermarkOutputMode
        
        # 测试枚举
        watermark_modes = [mode.value for mode in WatermarkOutputMode]
        print(f"   ✅ 水印模式: {watermark_modes}")
        
        # 测试配置创建（不包含翻译器）
        print("   ✅ 配置类导入成功")
        
        return True
    except Exception as e:
        print(f"   ❌ 配置测试失败: {e}")
        return False

def test_docvision():
    """测试文档视觉分析功能"""
    print("\n👁️  测试文档视觉分析...")
    
    try:
        from babeldoc.docvision.doclayout import DocLayoutModel
        
        # 检查是否可以加载模型
        print("   ✅ 文档布局模型类导入成功")
        
        # 注意：实际加载模型需要下载，这里只测试类导入
        return True
    except Exception as e:
        print(f"   ❌ 文档视觉分析测试失败: {e}")
        return False

def test_pdf_processing():
    """测试PDF处理功能"""
    print("\n📄 测试PDF处理功能...")
    
    try:
        import pymupdf
        
        # 测试PyMuPDF基本功能
        doc = pymupdf.open()
        page = doc.new_page()
        page.insert_text((100, 100), "Test PDF")
        
        # 保存到内存
        pdf_bytes = doc.write()
        doc.close()
        
        print(f"   ✅ PyMuPDF基本功能正常 (生成PDF大小: {len(pdf_bytes)} bytes)")
        
        return True
    except Exception as e:
        print(f"   ❌ PDF处理测试失败: {e}")
        return False

def test_async_functionality():
    """测试异步功能"""
    print("\n🔄 测试异步功能...")
    
    try:
        from babeldoc.asynchronize import AsyncCallback
        
        # 测试异步回调
        callback = AsyncCallback()
        print("   ✅ 异步回调类导入成功")
        
        return True
    except Exception as e:
        print(f"   ❌ 异步功能测试失败: {e}")
        return False

def test_example_files():
    """测试示例文件"""
    print("\n📁 测试示例文件...")
    
    example_files = [
        "examples/basic.xml",
        "examples/ci/test.pdf",
        "examples/code-figure.xml",
        "examples/complex.xml",
        "examples/formular.xml",
        "examples/table.xml"
    ]
    
    existing_files = []
    for file_path in example_files:
        if Path(file_path).exists():
            existing_files.append(file_path)
            print(f"   ✅ {file_path}")
        else:
            print(f"   ⚠️  {file_path} (不存在)")
    
    if existing_files:
        print(f"   📊 找到 {len(existing_files)} 个示例文件")
        return True
    else:
        print("   ❌ 没有找到示例文件")
        return False

def main():
    """主测试函数"""
    print("🧪 BabelDOC 基本功能测试")
    print("=" * 50)
    
    tests = [
        ("模块导入", test_imports),
        ("资源管理", test_assets),
        ("配置功能", test_config),
        ("文档视觉分析", test_docvision),
        ("PDF处理", test_pdf_processing),
        ("异步功能", test_async_functionality),
        ("示例文件", test_example_files),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"   ❌ {test_name}测试出现异常: {e}")
            results.append((test_name, False))
    
    # 汇总结果
    print("\n" + "=" * 50)
    print("📊 测试结果汇总:")
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"   {test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\n🎯 总体结果: {passed}/{total} 测试通过")
    
    if passed == total:
        print("🎉 所有测试通过！BabelDOC环境配置正确。")
        print("\n💡 下一步:")
        print("   1. 设置OpenAI API密钥: export OPENAI_API_KEY='your-key'")
        print("   2. 运行翻译测试: uv run babeldoc --openai --files examples/ci/test.pdf --openai-api-key $OPENAI_API_KEY")
    else:
        print("⚠️  部分测试失败，请检查环境配置。")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
