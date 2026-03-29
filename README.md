# 基于大模型的个人智能生活助理系统

## 项目简介

本项目致力于用大语言模型和多模态AI技术，打造可个性化设置的智能生活助理。支持文本、语音、图片等多方式输入，实现日常事务管理、生活信息查询、智能提醒和简单智能家居控制。

## 技术栈

- 后端：Python 3.8+、FastAPI
- 前端：React（或 Vue/小程序，后续可扩展）
- 数据库：SQLite（开发测试）/MongoDB/PostgreSQL（生产环境）
- AI服务：OpenAI GPT-3.5/4，Qwen等
- 多模态：OCR（easyocr/PaddleOCR）、语音（Vosk/百度ASR）
- 智能家居：米家/Home Assistant（可拓展）

## 项目结构

```
.
├── backend/     # 后端代码
│   └── main.py
├── frontend/    # 前端代码（预留）
├── docs/        # 文档说明
└── README.md
```

## 起步

1. 克隆仓库，进入 backend 目录：
   ```bash
   cd backend
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```

2. 访问：http://localhost:8000/ 查看API服务。

## 基础功能计划

- [ ] 支持文本对话与问答
- [ ] 基础待办/提醒
- [ ] 天气/资讯推送
- [ ] 图片/票据OCR录入
- [ ] 智能家居设备控制API demo
