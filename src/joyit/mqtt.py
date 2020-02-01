import logging
from typing import NamedTuple, Tuple

import json
from paho.mqtt.client import Client


logger = logging.getLogger(__name__)


def join_topics(*topics: str) -> str:
    """Join two topics."""
    if not topics:
        raise ValueError("Need to pass at least one topic")
    return "/".join(topics)


class MoveAxisParams(NamedTuple):
    """Parameters for moving a single axis."""
    axis: int
    position: int
    velocity: int


class MoveParams(NamedTuple):
    """Parameters for moving all axes."""
    ax0: int
    ax1: int
    ax2: int
    ax3: int
    ax4: int
    ax5: int
    velocity: int


commands = {
    "move_axis": MoveAxisParams,
    "move": MoveParams,
}


class MQTTWrapper:
    """Wrapper for MQTT communication."""

    def __init__(self, mqtt_client: Client, parent_topic: str) -> None:
        self._mqtt_client = mqtt_client
        self.parent_topic = parent_topic

    def send_command(self, command: str, params: Tuple) -> None:
        """Send a command via mqtt."""
        assert command in commands.keys()
        assert type(params) == commands[command]

        data = {
            "cmd": command,
            "params": params
        }

        topic = join_topics(self.parent_topic, "command")
        msg = json.dumps(data)
        qos = 2
        info = self._mqtt_client.publish(topic, msg, qos=qos)

        if info.rc < qos:
            logger.warning(f"Published to topic {topic} only with qos: {info.rc}, message: {msg}")
        elif info.rc == qos:
            logger.debug(f"Published to topic {topic}, message: {msg}")
        else:
            logger.error(f"Publishing to topic {topic} failed, message: {msg}")

    def move_axis(self, axis: int, position: int, velocity: int) -> None:
        params = MoveAxisParams(axis, position, velocity)
        return self.send_command("move_axis", params)

    def move(self, ax0: int, ax1: int, ax2: int, ax3: int, ax4: int, ax5: int, velocity: int) -> None:
        params = MoveParams(ax0, ax1, ax2, ax3, ax4, ax5, velocity)
        return self.send_command("move", params)
