from flask import Flask
from config import Config


def init_app(app_config=Config):
    app = Flask(__name__)
    app.config.from_object(app_config)


    with app.app_context():
        
        from .errors import bp as errors_bp

        app.register_blueprint(errors_bp)
        from .main import bp as main_bp

        app.register_blueprint(main_bp)
        return app
