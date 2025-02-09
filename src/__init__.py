from datetime import timedelta

from flask import Flask
from flask_cors import CORS  # type: ignore
from flask_jwt_extended import JWTManager

from src.env import env
from src.routes.auth import auth_bp
from src.routes.health import health_bp
from src.routes.user import user_bp
from src.utils.jwt import register_jwt_handlers


def create_app():
    application = Flask("dstt", instance_relative_config=True)

    application.register_blueprint(auth_bp)
    application.register_blueprint(user_bp)
    application.register_blueprint(health_bp)

    application.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(
        minutes=env.JWT_ACCESS_TOKEN_EXPIRES
    )
    application.config["JWT_SECRET_KEY"] = env.SECRET_KEY

    jwt_manager = JWTManager(application)
    register_jwt_handlers(jwt_manager)

    CORS(application, expose_headers="Authorization", supports_credentials=True)

    return application
