# BabelDOC UV 虚拟环境设置指南

## 🎉 环境设置完成！

您的BabelDOC项目已经成功配置了uv虚拟环境，所有依赖都已安装完成。

## 📁 环境结构

```
BabelDOC/
├── .venv/                    # uv虚拟环境目录
├── uv.lock                   # 依赖锁定文件
├── pyproject.toml           # 项目配置
├── example_usage.py         # 使用示例脚本
├── config_example.toml      # 配置文件示例
└── UV_SETUP_README.md       # 本文件
```

## 🚀 快速开始

### 1. 激活虚拟环境

```bash
# 使用uv运行命令（推荐）
uv run babeldoc --help

# 或者激活虚拟环境
source .venv/bin/activate  # Linux/macOS
# 或
.venv\Scripts\activate     # Windows
```

### 2. 验证安装

```bash
# 检查版本
uv run babeldoc --version

# 运行环境检查脚本
uv run python test_basic_functionality.py
```

### 3. 配置OpenAI API密钥

#### 方法1：使用设置脚本（推荐）
```bash
# 运行交互式设置脚本
bash setup_env.sh
```

#### 方法2：手动设置环境变量
```bash
# 临时设置（当前会话）
export OPENAI_API_KEY="your-api-key-here"

# 永久设置（添加到shell配置）
echo 'export OPENAI_API_KEY="your-api-key-here"' >> ~/.zshrc
source ~/.zshrc
```

#### 方法3：使用配置文件
```bash
# 编辑配置文件
cp config_with_api.toml my_config.toml
# 在my_config.toml中设置openai-api-key
```

### 4. 测试API密钥
```bash
# 测试API密钥是否有效
uv run python test_api_key.py
```

### 5. 下载资源（首次使用）

```bash
# 下载所需的模型和字体
uv run babeldoc --warmup
```

## 📝 使用示例

### 命令行使用

```bash
# 基本翻译（需要OpenAI API密钥）
uv run babeldoc \
  --openai \
  --openai-model "gpt-4o-mini" \
  --openai-api-key "your-api-key" \
  --files example.pdf

# 使用配置文件
uv run babeldoc --config config_example.toml --files example.pdf

# 多文件翻译
uv run babeldoc \
  --openai \
  --openai-api-key "your-api-key" \
  --files file1.pdf --files file2.pdf
```

### Python API使用

```python
import asyncio
from babeldoc.format.pdf.high_level import async_translate
from babeldoc.format.pdf.translation_config import TranslationConfig
from babeldoc.translator.translator import OpenAITranslator

async def translate_pdf():
    translator = OpenAITranslator(
        lang_in="en",
        lang_out="zh", 
        model="gpt-4o-mini",
        api_key="your-api-key"
    )
    
    config = TranslationConfig(
        input_file="example.pdf",
        translator=translator,
        output_dir="./output"
    )
    
    async for event in async_translate(config):
        if event["type"] == "finish":
            print("翻译完成！")
            break

asyncio.run(translate_pdf())
```

## ⚙️ 配置选项

### 环境变量

```bash
# 设置OpenAI API密钥
export OPENAI_API_KEY="your-api-key-here"
export OPENAI_BASE_URL="https://api.openai.com/v1"
export OPENAI_MODEL="gpt-4o-mini"
```

### 配置文件

使用 `config_example.toml` 作为模板，根据需要修改配置：

```toml
[babeldoc]
lang-in = "en"
lang-out = "zh"
qps = 4
openai = true
openai-model = "gpt-4o-mini"
# ... 其他配置
```

## 🔧 常用命令

### 开发相关

```bash
# 安装开发依赖
uv sync --group dev

# 运行测试
uv run pytest

# 代码格式化
uv run ruff format

# 代码检查
uv run ruff check

# 运行预提交钩子
uv run pre-commit run --all-files
```

### 资源管理

```bash
# 生成离线资产包
uv run babeldoc --generate-offline-assets ./offline_assets

# 恢复离线资产包
uv run babeldoc --restore-offline-assets ./offline_assets/offline_assets_*.zip
```

## 📊 性能优化

### 硬件要求

- **CPU**: 多核处理器（推荐8核以上）
- **内存**: 8GB以上（推荐16GB）
- **存储**: SSD硬盘，至少10GB可用空间

### 性能调优

```bash
# 调整并发数
--pool-max-workers 8

# 调整QPS限制
--qps 10

# 大文档分片处理
--max-pages-per-part 50

# 跳过扫描检测（已知非扫描文档）
--skip-scanned-detection
```

## 🐛 故障排除

### 常见问题

1. **依赖安装失败**
   ```bash
   # 清理并重新安装
   rm -rf .venv
   uv sync
   ```

2. **内存不足**
   ```bash
   # 减少并发数
   --pool-max-workers 4
   ```

3. **网络问题**
   ```bash
   # 使用离线资产包
   uv run babeldoc --restore-offline-assets /path/to/assets.zip
   ```

### 调试模式

```bash
# 启用调试日志
uv run babeldoc --debug --files example.pdf
```

## 📚 更多资源

- [BabelDOC官方文档](https://funstory-ai.github.io/BabelDOC/)
- [PDFMathTranslate 2.0](https://github.com/PDFMathTranslate/PDFMathTranslate-next) - 自部署方案
- [Immersive Translate](https://app.immersivetranslate.com/babel-doc/) - 在线服务

## 🆘 获取帮助

- GitHub Issues: https://github.com/funstory-ai/BabelDOC/issues
- Telegram群组: https://t.me/+Z9_SgnxmsmA5NzBl

---

**注意**: 首次使用需要下载模型和字体文件，请确保网络连接正常。如果遇到网络问题，可以使用离线资产包功能。
