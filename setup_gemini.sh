#!/bin/bash
# BabelDOC Gemini API 设置脚本

echo "🤖 BabelDOC Gemini API 配置向导"
echo "================================"

# 检查是否已有API密钥
if [ -n "$GEMINI_API_KEY" ]; then
    echo "✅ 检测到已设置的Gemini API密钥"
    echo "   当前密钥: ${GEMINI_API_KEY:0:8}..."
    read -p "是否要重新设置？(y/N): " reset_key
    if [[ ! $reset_key =~ ^[Yy]$ ]]; then
        echo "保持当前设置"
        exit 0
    fi
fi

echo ""
echo "🔧 选择Gemini API配置方式："
echo "1) 使用LiteLLM代理（推荐）"
echo "2) 使用OpenAI兼容接口"
echo "3) 使用环境变量直接配置"
read -p "请选择 (1/2/3): " choice

case $choice in
    1)
        echo ""
        echo "📦 安装LiteLLM..."
        uv add litellm
        
        echo ""
        echo "请输入您的Gemini API密钥："
        read -p "API密钥: " api_key
        
        if [ -z "$api_key" ]; then
            echo "❌ 未输入API密钥，退出"
            exit 1
        fi
        
        # 设置环境变量
        export GEMINI_API_KEY="$api_key"
        
        echo ""
        echo "🔧 选择设置方式："
        echo "1) 仅当前会话有效（临时）"
        echo "2) 永久设置（添加到shell配置文件）"
        read -p "请选择 (1/2): " setup_choice
        
        case $setup_choice in
            1)
                echo "✅ Gemini API密钥已设置为当前会话有效"
                echo "   密钥: ${api_key:0:8}..."
                echo ""
                echo "💡 使用方法："
                echo "   uv run babeldoc --openai --openai-base-url 'http://localhost:4000' --openai-api-key 'your-key' --files example.pdf"
                ;;
            2)
                # 检测shell类型
                if [ -n "$ZSH_VERSION" ]; then
                    config_file="$HOME/.zshrc"
                elif [ -n "$BASH_VERSION" ]; then
                    config_file="$HOME/.bashrc"
                else
                    config_file="$HOME/.profile"
                fi
                
                # 添加新的设置
                echo "" >> "$config_file"
                echo "# BabelDOC Gemini API配置" >> "$config_file"
                echo "export GEMINI_API_KEY=\"$api_key\"" >> "$config_file"
                
                echo "✅ Gemini API密钥已永久设置"
                echo "   配置文件: $config_file"
                echo "   密钥: ${api_key:0:8}..."
                echo ""
                echo "💡 请运行以下命令使配置生效："
                echo "   source $config_file"
                ;;
        esac
        
        echo ""
        echo "🚀 启动LiteLLM代理："
        echo "   litellm --model gemini/gemini-pro --port 4000"
        ;;
        
    2)
        echo ""
        echo "请输入您的Gemini API密钥："
        read -p "API密钥: " api_key
        
        if [ -z "$api_key" ]; then
            echo "❌ 未输入API密钥，退出"
            exit 1
        fi
        
        echo ""
        echo "请输入OpenAI兼容接口的Base URL："
        echo "（例如：https://api.openai.com/v1 或自定义代理地址）"
        read -p "Base URL: " base_url
        
        # 设置环境变量
        export GEMINI_API_KEY="$api_key"
        export OPENAI_BASE_URL="$base_url"
        
        echo ""
        echo "✅ 配置完成"
        echo "   API密钥: ${api_key:0:8}..."
        echo "   Base URL: $base_url"
        echo ""
        echo "💡 使用方法："
        echo "   uv run babeldoc --openai --openai-base-url '$base_url' --openai-api-key '$api_key' --files example.pdf"
        ;;
        
    3)
        echo ""
        echo "请输入您的Gemini API密钥："
        read -p "API密钥: " api_key
        
        if [ -z "$api_key" ]; then
            echo "❌ 未输入API密钥，退出"
            exit 1
        fi
        
        # 设置环境变量
        export GEMINI_API_KEY="$api_key"
        
        echo ""
        echo "🔧 选择设置方式："
        echo "1) 仅当前会话有效（临时）"
        echo "2) 永久设置（添加到shell配置文件）"
        read -p "请选择 (1/2): " setup_choice
        
        case $setup_choice in
            1)
                echo "✅ Gemini API密钥已设置为当前会话有效"
                echo "   密钥: ${api_key:0:8}..."
                ;;
            2)
                # 检测shell类型
                if [ -n "$ZSH_VERSION" ]; then
                    config_file="$HOME/.zshrc"
                elif [ -n "$BASH_VERSION" ]; then
                    config_file="$HOME/.bashrc"
                else
                    config_file="$HOME/.profile"
                fi
                
                # 添加新的设置
                echo "" >> "$config_file"
                echo "# BabelDOC Gemini API配置" >> "$config_file"
                echo "export GEMINI_API_KEY=\"$api_key\"" >> "$config_file"
                
                echo "✅ Gemini API密钥已永久设置"
                echo "   配置文件: $config_file"
                echo "   密钥: ${api_key:0:8}..."
                echo ""
                echo "💡 请运行以下命令使配置生效："
                echo "   source $config_file"
                ;;
        esac
        ;;
        
    *)
        echo "❌ 无效选择"
        exit 1
        ;;
esac

echo ""
echo "🧪 测试Gemini API配置："
echo "   uv run python test_gemini_api.py"

echo ""
echo "🚀 现在可以使用Gemini API进行翻译了！"
