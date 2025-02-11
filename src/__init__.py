from datetime import timedelta

from flask import Flask
from flask_cors import CORS  # type: ignore
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from src.env import env
from src.routes.auth import auth_bp
from src.routes.health import health_bp
from src.routes.user import user_bp
from src.utils.jwt import register_jwt_handlers


def create_app():
    application = Flask("dstt", instance_relative_config=True)

    limiter = Limiter(
        get_remote_address,
        app=application,
        default_limits=["200 per day", "50 per hour"],
        storage_uri=str(env.REDIS_URL),
        storage_options={"socket_connect_timeout": 30},
        strategy="fixed-window",
    )

    application.register_blueprint(auth_bp)
    application.register_blueprint(user_bp)
    application.register_blueprint(health_bp)

    application.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(
        minutes=env.JWT_ACCESS_TOKEN_EXPIRES
    )
    application.config["JWT_SECRET_KEY"] = str(env.SECRET_KEY)

    jwt_manager = JWTManager(application)
    register_jwt_handlers(jwt_manager)

    CORS(application, expose_headers="Authorization", supports_credentials=True)

    return application
