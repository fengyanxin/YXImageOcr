#!/bin/bash

# 启动 OCR 服务

echo "启动 OCR 服务..."

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "错误: 未找到 python3"
    exit 1
fi

# 检查虚拟环境
if [ ! -d "venv" ]; then
    echo "创建虚拟环境..."
    python3 -m venv venv
fi

# 激活虚拟环境
source venv/bin/activate

# 检查依赖
if ! python -c "import flask" &> /dev/null; then
    echo "安装依赖..."
    pip install -r requirements.txt
fi

# 检查 Tesseract
if ! command -v tesseract &> /dev/null; then
    echo "警告: 未安装 tesseract，请运行: brew install tesseract tesseract-lang"
fi

# 启动服务
echo "启动服务在 http://localhost:5001"
python server.py
