import json
from typing import Dict, Any
import redis
from paho.mqtt.client import Client, MQTTMessage


# typing
JsonDict = Dict[str, Any]


# set up redis client
redis_client = redis.Redis("localhost")

# set up mqtt client
mqtt_client = Client()
mqtt_client.connect("localhost")


keys = ["ax0", "ax1", "ax2", "ax3", "ax4", "ax5"]


def on_command_move(client: Client, userdata: Any, message: MQTTMessage) -> None:
    payload = message.payload
    data = json.loads(payload.decode())
    print(data)
    cmd = data["cmd"]
    ax, position, velocity = data["params"]
    redis_client.set(keys[ax], position)


mqtt_client.subscribe("joyit/command/#")
mqtt_client.message_callback_add("joyit/command/#", on_command_move)


while True:
    mqtt_client.loop(0.1)
