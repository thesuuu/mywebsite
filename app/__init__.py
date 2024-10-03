# import logging
from flask import Flask, Blueprint
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
import os
from config import Config

# db = SQLAlchemy()
# migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # db.init_app(app)
    # migrate.init_app(app, db)

    # # 配置日志
    # logging.basicConfig(level=logging.DEBUG,
    #                     format='%(asctime)s %(levelname)s: %(message)s',
    #                     datefmt='%Y-%m-%d %H:%M:%S')

    # 注册蓝图
    from app.routes import bp
    app.register_blueprint(bp)

    # 创建文件夹
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)

    return app

# 工厂模式创建应用实例
app = create_app()