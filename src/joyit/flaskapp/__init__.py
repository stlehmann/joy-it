from flask import Flask
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from .config import config
from ..mqtt import MQTTWrapper


socketio = SocketIO()
mqtt_client = Mqtt()
mqtt_wrapper = MQTTWrapper(mqtt_client.client, "joyit")
socketio = SocketIO()


def create_app(config_name: str = "default") -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    socketio.init_app(app)
    mqtt_client.init_app(app)
    socketio.init_app(app)

    # blueprints
    from . import main
    app.register_blueprint(main.bp)

    from . import websockets
    app.register_blueprint(websockets.bp)

    return app
