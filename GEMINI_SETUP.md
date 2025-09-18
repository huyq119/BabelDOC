# 🤖 BabelDOC Gemini API 配置指南

## 📋 概述

虽然BabelDOC主要支持OpenAI API，但您可以通过以下几种方式使用Gemini API进行PDF翻译。

## 🚀 推荐方法

### 方法1：使用LiteLLM代理（最推荐）

LiteLLM是一个统一的LLM API接口，可以将Gemini API转换为OpenAI兼容格式。

#### 1. 安装LiteLLM
```bash
uv add litellm
```

#### 2. 设置Gemini API密钥
```bash
export GEMINI_API_KEY="your-gemini-api-key-here"
```

#### 3. 启动LiteLLM代理
```bash
litellm --model gemini/gemini-pro --port 4000
```

#### 4. 使用BabelDOC
```bash
uv run babeldoc \
  --openai \
  --openai-base-url "http://localhost:4000" \
  --openai-api-key "your-key" \
  --files example.pdf
```

### 方法2：使用OpenAI兼容接口

许多服务提供OpenAI兼容的接口来访问Gemini。

#### 1. 设置环境变量
```bash
export GEMINI_API_KEY="your-gemini-api-key-here"
export OPENAI_BASE_URL="https://your-proxy.com/v1"
```

#### 2. 使用BabelDOC
```bash
uv run babeldoc \
  --openai \
  --openai-base-url "$OPENAI_BASE_URL" \
  --openai-api-key "$GEMINI_API_KEY" \
  --files example.pdf
```

### 方法3：使用配置文件

#### 1. 编辑配置文件
```bash
cp config_gemini.toml my_gemini_config.toml
# 编辑配置文件，设置正确的API密钥和Base URL
```

#### 2. 使用配置文件
```bash
uv run babeldoc --config my_gemini_config.toml --files example.pdf
```

## 🔧 快速设置

### 使用设置脚本
```bash
bash setup_gemini.sh
```

这个脚本会：
- ✅ 引导您选择配置方式
- ✅ 设置API密钥
- ✅ 提供使用示例

### 测试配置
```bash
uv run python test_gemini_api.py
```

## 📊 支持的Gemini模型

| 模型名称 | LiteLLM标识 | 描述 |
|----------|-------------|------|
| Gemini Pro | `gemini/gemini-pro` | 标准模型 |
| Gemini 1.5 Pro | `gemini/gemini-1.5-pro` | 最新版本 |
| Gemini 1.5 Flash | `gemini/gemini-1.5-flash` | 快速版本 |

## 🛠️ 详细配置步骤

### 步骤1：获取Gemini API密钥

1. 访问 [Google AI Studio](https://makersuite.google.com/app/apikey)
2. 创建新的API密钥
3. 复制密钥（格式：`AI...`）

### 步骤2：选择配置方式

#### 选项A：LiteLLM代理
```bash
# 安装依赖
uv add litellm

# 设置API密钥
export GEMINI_API_KEY="your-api-key"

# 启动代理
litellm --model gemini/gemini-pro --port 4000

# 在另一个终端使用BabelDOC
uv run babeldoc --openai --openai-base-url "http://localhost:4000" --openai-api-key "dummy" --files example.pdf
```

#### 选项B：直接配置
```bash
# 设置环境变量
export GEMINI_API_KEY="your-api-key"
export OPENAI_BASE_URL="https://your-proxy.com/v1"

# 使用BabelDOC
uv run babeldoc --openai --openai-base-url "$OPENAI_BASE_URL" --openai-api-key "$GEMINI_API_KEY" --files example.pdf
```

## 🧪 测试和验证

### 1. 基本功能测试
```bash
uv run python test_basic_functionality.py
```

### 2. Gemini API测试
```bash
uv run python test_gemini_api.py
```

### 3. 实际翻译测试
```bash
# 创建测试PDF
uv run python create_test_pdf.py

# 测试翻译
uv run babeldoc --openai --files test_document.pdf --output ./test_output
```

## 🔒 安全最佳实践

### 1. 环境变量（最安全）
```bash
export GEMINI_API_KEY="your-api-key"
```

### 2. 配置文件安全
- ⚠️ 确保配置文件不被提交到Git
- ⚠️ 设置适当的文件权限
- ⚠️ 定期轮换API密钥

### 3. 代理服务
- ✅ 使用可信的代理服务
- ✅ 检查代理服务的隐私政策
- ✅ 考虑自建代理服务

## 🐛 故障排除

### 问题1：API密钥无效
```
❌ Gemini连接失败: Invalid API key
```
**解决方案：**
- 检查API密钥是否正确
- 确认密钥格式（以`AI`开头）
- 检查Google AI Studio中的密钥状态

### 问题2：LiteLLM连接失败
```
❌ LiteLLM连接失败: Connection refused
```
**解决方案：**
- 确认LiteLLM代理正在运行
- 检查端口是否正确（默认4000）
- 检查防火墙设置

### 问题3：模型不支持
```
❌ Model not found: gemini/gemini-pro
```
**解决方案：**
- 检查模型名称是否正确
- 尝试其他Gemini模型
- 更新LiteLLM版本

## 📚 相关资源

- [Google AI Studio](https://makersuite.google.com/app/apikey) - 获取API密钥
- [LiteLLM文档](https://docs.litellm.ai/) - 统一LLM接口
- [Gemini API文档](https://ai.google.dev/docs) - 官方文档

## 🆘 获取帮助

如果遇到问题：
1. 运行测试脚本诊断问题
2. 检查Gemini API状态
3. 查看BabelDOC日志输出
4. 访问GitHub Issues获取支持

---

**注意**: 使用第三方代理服务时，请确保服务的安全性和可靠性。建议优先使用官方API或自建代理服务。
