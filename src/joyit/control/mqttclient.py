import json

import redis
from paho.mqtt.client import Client
import Adafruit_PCA9685
import time


redis_client = redis.Redis("localhost")
mqtt_client = Client()
mqtt_client.connect("localhost")


keys = ["ax0", "ax1", "ax2", "ax3", "ax4", "ax5"]


def on_command_move(client, userdata, message):
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

