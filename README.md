# MedIG website

## 项目概述

这是一个用于展示实验室算法功能的网站。

## 项目信息

- **项目名称**: 项目名称
- **创建日期**: 2024-09-07
- **作者**: Thesuuu
- **版本**: v1.0.0
- **状态**: 测试中

## 实现功能
    v1.0.0: 上传图片，实现对应的处理并返回下载连接

## 项目技术栈

前端：
  - **HTML + CSS**: 用于构建静态网页结构和样式。
  - **JavaScript**: 用于实现前端的动态交互功能。
后端：
  - **FLask**：轻量级的Python Web框架，用于处理HTTP请求和响应。

## 文件结构
flask_app/
│
├── app/                      # 主应用目录
│   ├── __init__.py           # 初始化 Flask 应用
│   ├── routes.py             # 路由处理
│   ├── static/               # 静态文件目录
│   │   ├── css/              # CSS 文件
│   │   │   └── style.css     # 样式文件
│   │   ├── js/               # JavaScript 文件
│   │   └── images/           # 图片文件
│   ├── templates/            # 模板文件目录
│   │   └── index.html        # 主页模板
│
├── config.py                 # 配置文件
├── requirements.txt          # 依赖文件
├── run.py                    # 启动脚本
└── README.md                 # 项目说明文档

## 文件功能
- config.py:
    - 定义了应用的基本配置，包括密钥、上传文件夹路径、数据库配置等。
- __init__.py:
    - 初始化Flask应用，并注册蓝图。
    - 配置数据库和其他扩展。
    - 创建必要的文件夹。
- routes.py:
    - 定义了路由和处理逻辑。
    - 处理图像上传、处理和下载。
- run.py:
    - 启动Flask应用。