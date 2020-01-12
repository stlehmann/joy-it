from flask import Flask
from flask_mqtt import Mqtt
from .config import config


mqtt_client = Mqtt()


def create_app(config_name: str = "default") -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    mqtt_client.init_app(app)

    from . import main

    app.register_blueprint(main.bp)

    return app
