import logging
from .. import socketio, mqtt_wrapper


logger = logging.getLogger(__name__)


@socketio.on("move_axis")
def move_axis(json):
    logger.info(json)
    velocity = 10
    mqtt_wrapper.move_axis(json["axis"], json["value"], velocity)
