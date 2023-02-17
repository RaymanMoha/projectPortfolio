import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Flask configuration
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(BASE_DIR / 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Application factory function
def create_app():
    from flask import Flask

    app = Flask(__name__)
    app.config.from_object(Config)

    # Database setup
    from flask_sqlalchemy import SQLAlchemy
    db = SQLAlchemy(app)

    # Register blueprints
    from yourapp import yourapp_bp
    app.register_blueprint(yourapp_bp)

    return app
