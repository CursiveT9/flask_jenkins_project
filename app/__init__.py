from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['DEBUG'] = True

    with app.app_context():
        from .routes import main_blueprint
        app.register_blueprint(main_blueprint)

    return app
