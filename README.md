# OCR 文字识别

基于 Tesseract 的本地 OCR 服务

## 部署步骤

### 1. 安装依赖

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate  # macOS/Linux
# 或
venv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt
```

### 2. 安装 Tesseract OCR

**macOS:**
```bash
brew install tesseract tesseract-lang
```

**Ubuntu/Debian:**
```bash
sudo apt-get install tesseract-ocr tesseract-ocr-chi-sim
```

**Windows:**
下载安装: https://github.com/UB-Mannheim/tesseract/wiki

### 3. 启动服务

```bash
python server.py
```

服务启动后访问: http://localhost:5001

## 项目结构

```
ocr-文字识别/
├── index.html       # 前端页面
├── server.py        # Flask 后端服务
├── requirements.txt # Python 依赖
└── venv/           # 虚拟环境（可选）
```
