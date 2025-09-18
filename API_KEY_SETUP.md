# 🔑 BabelDOC OpenAI API密钥配置指南

## 📋 配置方法总览

| 方法 | 适用场景 | 安全性 | 推荐度 |
|------|----------|--------|--------|
| 环境变量 | 开发/生产 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 配置文件 | 个人使用 | ⭐⭐⭐ | ⭐⭐⭐ |
| 命令行参数 | 临时测试 | ⭐⭐ | ⭐⭐ |
| 设置脚本 | 新手用户 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

## 🚀 推荐方法：使用设置脚本

### 1. 运行交互式设置脚本
```bash
bash setup_env.sh
```

这个脚本会：
- ✅ 引导您输入API密钥
- ✅ 验证密钥格式
- ✅ 提供临时或永久设置选项
- ✅ 自动配置shell环境

### 2. 测试配置
```bash
uv run python test_api_key.py
```

## 🔧 手动配置方法

### 方法1：环境变量（推荐）

#### 临时设置（当前终端会话）
```bash
export OPENAI_API_KEY="sk-your-actual-api-key-here"
```

#### 永久设置
```bash
# 添加到shell配置文件
echo 'export OPENAI_API_KEY="sk-your-actual-api-key-here"' >> ~/.zshrc

# 重新加载配置
source ~/.zshrc
```

#### 验证设置
```bash
echo $OPENAI_API_KEY
```

### 方法2：配置文件

#### 编辑配置文件
```bash
# 复制配置模板
cp config_with_api.toml my_config.toml

# 编辑配置文件
nano my_config.toml
```

在配置文件中设置：
```toml
[babeldoc]
openai-api-key = "sk-your-actual-api-key-here"
```

#### 使用配置文件
```bash
uv run babeldoc --config my_config.toml --files example.pdf
```

### 方法3：命令行参数

```bash
uv run babeldoc \
  --openai \
  --openai-api-key "sk-your-actual-api-key-here" \
  --openai-model "gpt-4o-mini" \
  --files example.pdf
```

## 🧪 测试和验证

### 1. 基本功能测试
```bash
uv run python test_basic_functionality.py
```

### 2. API密钥测试
```bash
uv run python test_api_key.py
```

### 3. 实际翻译测试
```bash
# 使用示例PDF进行测试
uv run babeldoc \
  --openai \
  --files examples/ci/test.pdf \
  --output ./test_output
```

## 🔒 安全最佳实践

### 1. 环境变量（最安全）
- ✅ 不会保存在代码中
- ✅ 不会被意外提交到版本控制
- ✅ 可以轻松在不同环境间切换

### 2. 配置文件安全
- ⚠️ 确保配置文件不被提交到Git
- ⚠️ 设置适当的文件权限
- ⚠️ 定期轮换API密钥

### 3. 命令行参数
- ❌ 会出现在命令历史中
- ❌ 可能被其他进程看到
- ❌ 不推荐用于生产环境

## 🛠️ 故障排除

### 问题1：API密钥未设置
```
❌ 未找到OPENAI_API_KEY环境变量
```
**解决方案：**
```bash
export OPENAI_API_KEY="your-key"
# 或运行设置脚本
bash setup_env.sh
```

### 问题2：API密钥格式错误
```
⚠️ 警告：API密钥格式可能不正确（通常以 'sk-' 开头）
```
**解决方案：**
- 检查密钥是否以 `sk-` 开头
- 确认密钥完整且未截断
- 重新从OpenAI控制台复制密钥

### 问题3：API连接失败
```
❌ OpenAI连接失败: Invalid API key
```
**解决方案：**
- 验证API密钥是否正确
- 检查OpenAI账户余额
- 确认网络连接正常
- 检查API密钥权限

### 问题4：配额不足
```
❌ 翻译测试失败: Rate limit exceeded
```
**解决方案：**
- 检查OpenAI账户余额
- 降低QPS设置：`--qps 1`
- 等待配额重置

## 📊 不同配置方法对比

### 环境变量
```bash
# 优点：安全、灵活、易管理
export OPENAI_API_KEY="sk-..."
uv run babeldoc --openai --files example.pdf
```

### 配置文件
```toml
# 优点：集中管理、可版本控制（不含密钥）
[babeldoc]
openai = true
openai-model = "gpt-4o-mini"
# openai-api-key = "从环境变量读取"
```
```bash
uv run babeldoc --config my_config.toml --files example.pdf
```

### 命令行参数
```bash
# 优点：简单直接
# 缺点：不安全、不便于管理
uv run babeldoc --openai --openai-api-key "sk-..." --files example.pdf
```

## 🎯 推荐配置流程

1. **首次设置**：运行 `bash setup_env.sh`
2. **验证配置**：运行 `uv run python test_api_key.py`
3. **测试翻译**：使用示例PDF进行测试
4. **生产使用**：使用环境变量或配置文件

## 📚 相关文件

- `setup_env.sh` - 交互式设置脚本
- `test_api_key.py` - API密钥测试脚本
- `config_with_api.toml` - 配置文件模板
- `test_basic_functionality.py` - 基本功能测试
- `UV_SETUP_README.md` - 完整使用指南

## 🆘 获取帮助

如果遇到问题：
1. 运行测试脚本诊断问题
2. 检查OpenAI账户状态
3. 查看BabelDOC日志输出
4. 访问GitHub Issues获取支持
