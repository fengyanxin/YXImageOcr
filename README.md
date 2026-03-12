# YXImageOcr - 图片文字识别

基于 Tesseract.js 的纯前端 OCR 文字识别应用。

## 功能特点

- ✨ **纯前端实现** - 无需后端服务器，可直接部署到静态托管平台
- 🌐 **多语言支持** - 简体中文、繁体中文、英文、日文
- 🎯 **智能识别** - 自动图像增强 + 多模式识别，自动选择最佳结果
- 📱 **响应式设计** - 支持桌面和移动设备
- 🚀 **一键部署** - 支持 Netlify、Vercel、GitHub Pages 等平台

## 在线体验

- 拖拽或点击上传图片
- 支持本地图片和网络图片 URL
- 自动识别并提取文字内容
- 支持复制、保存为 TXT 文件

## 快速开始

### 本地运行

直接用浏览器打开 `index.html` 即可使用。

或使用本地服务器：

```bash
# Python 3
python3 -m http.server 8000

# Node.js
npx serve .

# 然后访问 http://localhost:8000
```

### 部署到 Netlify

**方式一：拖放部署**
1. 登录 [Netlify](https://netlify.com)
2. 将 `index.html` 文件拖放到部署区域

**方式二：Git 部署**
1. 推送代码到 GitHub
2. 在 Netlify 导入项目
3. 构建设置留空，直接部署

**方式三：CLI 部署**
```bash
npm install -g netlify-cli
netlify deploy --prod
```

### 部署到其他平台

| 平台 | 说明 |
|------|------|
| Vercel | 拖放 `index.html` 或连接 Git 仓库 |
| GitHub Pages | 推送到 gh-pages 分支 |
| Cloudflare Pages | 连接 Git 仓库自动部署 |

## 技术栈

- **前端**: HTML5, CSS3, Vanilla JavaScript
- **OCR 引擎**: [Tesseract.js](https://github.com/naptha/tesseract.js) v5.1.0
- **CDN**: unpkg.com

## 项目结构

```
YXImageOcr/
├── index.html          # 主应用文件（可直接部署）
├── test-ocr.html       # 测试页面
├── README.md           # 项目说明
├── server.py           # 本地开发服务器（Python Flask）
├── requirements.txt    # Python 依赖
├── start.sh           # 启动脚本
└── venv/              # Python 虚拟环境（本地开发）
```

## 本地开发（Python 后端）

如果需要使用 Python 后端进行本地开发：

### 安装依赖

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

### 安装 Tesseract OCR

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

### 启动服务

```bash
# 使用启动脚本
./start.sh

# 或直接运行
python server.py
```

访问 http://localhost:5001

## 注意事项

### 首次加载

- 首次使用需要下载 Tesseract 核心文件和语言包（约 20-40MB）
- 下载完成后会被浏览器缓存，后续访问更快
- 网络图片需要支持 CORS 跨域访问

### 识别准确率

- 印刷体文字准确率较高
- 手写文字识别效果一般
- 建议使用清晰、端正的图片
- 复杂背景可能影响识别效果

### 浏览器兼容性

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## 常见问题

**Q: 识别速度慢？**
A: 首次使用需要下载语言包，之后会快很多。图片越大识别越慢。

**Q: 识别不准确？**
A: 确保图片清晰、文字端正。可以尝试裁剪图片只保留文字区域。

**Q: 网络图片无法识别？**
A: 网络图片需要支持 CORS 跨域，建议下载后本地上传。

**Q: 移动端能用吗？**
A: 可以，但首次加载较慢，建议在 WiFi 环境下使用。

## 开源协议

MIT License

## 更新日志

### v1.0.0 (2025-03-12)
- 纯前端实现，无需后端
- 支持多语言识别
- 自动图像增强
- 多模式智能识别
- 响应式设计
