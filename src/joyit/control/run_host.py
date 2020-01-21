import json

from paho.mqtt.client import Client
import Adafruit_PCA9685
import time


pwm = Adafruit_PCA9685.PCA9685(address=0x41)
mqtt_client = Client()
mqtt_client.connect("localhost")


# set min/max pulse width
servo_min = 150
servo_max = 600

servo_scale_x0 = 0
servo_scale_x1 = 100
servo_scale_y0 = 0.5
servo_scale_y1 = 2.5


keys = ["ax0", "ax1", "ax2", "ax3", "ax4", "ax5"]


def scale(x):
    m = (servo_scale_y1 - servo_scale_y0) / (servo_scale_x1 - servo_scale_x0)
    n = servo_scale_y0
    return m * x + n


def set_servo_pulse(channel, pulse):
    pulse_length = 1000000
    pulse_length /= 50
    pulse_length /= 4096
    pulse *= 1000
    pulse /= pulse_length
    pulse = round(pulse)
    pulse = int(pulse)
    pwm.set_pwm(channel, 0, pulse)


pwm.set_pwm_freq(50)


def on_command_move(client, userdata, message):
    payload = message.payload
    data = json.loads(payload.decode())
    print(data)
    set_servo_pulse(0, scale(data["params"][0]))


mqtt_client.subscribe("joyit/command/#")
mqtt_client.message_callback_add("joyit/command/#", on_command_move)


# set pwm frequency
while True:
    mqtt_client.loop(1.0)

