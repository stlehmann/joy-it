from flask import Flask, Blueprint
from flask_redis import FlaskRedis
from .config import config


redis_client = FlaskRedis()


def create_app(config_name: str="default") -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    redis_client.init_app(app)

    from . import main, redis
    app.register_blueprint(main.bp)
    app.register_blueprint(redis.bp)

    return app

