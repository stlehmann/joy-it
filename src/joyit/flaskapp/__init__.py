from flask import Flask
from flask_mqtt import Mqtt
from .config import config
from ..mqtt import MQTTWrapper


mqtt_client = Mqtt()
mqtt_wrapper = MQTTWrapper(mqtt_client.client, "joyit")


def create_app(config_name: str = "default") -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    mqtt_client.init_app(app)

    # blueprints
    from . import main
    app.register_blueprint(main.bp)

    return app
