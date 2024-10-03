class Config:
    SECRET_KEY = 'your-secret-key'
    UPLOAD_FOLDER = './app/uploads'
    PROCESSED_FOLDER = './app/processed'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

    # # 数据库配置（如果使用数据库）
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False