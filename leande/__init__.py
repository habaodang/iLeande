from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()
login_manager = LoginManager()
def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Abcd1234@localhost/leande?charset=utf8mb4'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'mysecretkey12345'
    db.init_app(app)
    login_manager.init_app(app)
    with app.app_context():
        db.create_all()
        print("Database và các bảng đã được khởi tạo!")
    # Đăng ký Blueprint
    from leande.routes import register_routes
    register_routes(app)

    return app