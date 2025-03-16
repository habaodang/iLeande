from flask import Flask

def create_app():
    app = Flask(__name__)

    # Đăng ký Blueprint
    from leande.routes import register_routes
    register_routes(app)

    return app