from leande.routes import main_route

def register_routes(app):
    app.register_blueprint(main_route.main, url_prefix='/')