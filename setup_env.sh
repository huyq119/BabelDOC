#!/bin/bash
# BabelDOC 环境变量设置脚本

echo "🔑 BabelDOC API密钥设置向导"
echo "================================"

# 检查是否已有API密钥
if [ -n "$OPENAI_API_KEY" ]; then
    echo "✅ 检测到已设置的OpenAI API密钥"
    echo "   当前密钥: ${OPENAI_API_KEY:0:8}..."
    read -p "是否要重新设置？(y/N): " reset_key
    if [[ ! $reset_key =~ ^[Yy]$ ]]; then
        echo "保持当前设置"
        exit 0
    fi
fi

# 获取API密钥
echo ""
echo "请输入您的OpenAI API密钥："
echo "（密钥格式通常以 'sk-' 开头）"
read -p "API密钥: " api_key

if [ -z "$api_key" ]; then
    echo "❌ 未输入API密钥，退出"
    exit 1
fi

# 验证密钥格式
if [[ ! $api_key =~ ^sk- ]]; then
    echo "⚠️  警告：API密钥格式可能不正确（通常以 'sk-' 开头）"
    read -p "是否继续？(y/N): " continue_anyway
    if [[ ! $continue_anyway =~ ^[Yy]$ ]]; then
        echo "取消设置"
        exit 1
    fi
fi

# 设置环境变量
export OPENAI_API_KEY="$api_key"

echo ""
echo "🔧 选择设置方式："
echo "1) 仅当前会话有效（临时）"
echo "2) 永久设置（添加到shell配置文件）"
read -p "请选择 (1/2): " choice

case $choice in
    1)
        echo "✅ API密钥已设置为当前会话有效"
        echo "   密钥: ${api_key:0:8}..."
        echo ""
        echo "💡 使用方法："
        echo "   uv run babeldoc --openai --files example.pdf"
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
        
        # 检查是否已存在设置
        if grep -q "OPENAI_API_KEY" "$config_file" 2>/dev/null; then
            echo "⚠️  检测到配置文件中已有OPENAI_API_KEY设置"
            read -p "是否要更新？(y/N): " update_config
            if [[ $update_config =~ ^[Yy]$ ]]; then
                # 删除旧的设置
                sed -i.bak '/export OPENAI_API_KEY/d' "$config_file"
            else
                echo "保持现有配置"
                exit 0
            fi
        fi
        
        # 添加新的设置
        echo "" >> "$config_file"
        echo "# BabelDOC OpenAI API配置" >> "$config_file"
        echo "export OPENAI_API_KEY=\"$api_key\"" >> "$config_file"
        
        echo "✅ API密钥已永久设置"
        echo "   配置文件: $config_file"
        echo "   密钥: ${api_key:0:8}..."
        echo ""
        echo "💡 请运行以下命令使配置生效："
        echo "   source $config_file"
        echo "   或者重新打开终端"
        ;;
    *)
        echo "❌ 无效选择"
        exit 1
        ;;
esac

echo ""
echo "🧪 测试API密钥设置："
echo "   echo \$OPENAI_API_KEY"

echo ""
echo "🚀 现在可以使用BabelDOC了："
echo "   uv run babeldoc --openai --files example.pdf"
