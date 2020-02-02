import redis
import Adafruit_PCA9685
import time


pwm = Adafruit_PCA9685.PCA9685(address=0x41)
redis_client = redis.Redis("localhost")


# set min/max pulse width
servo_min = 150
servo_max = 600
servo_scale_x0 = 0
servo_scale_x1 = 100
servo_scale_y0 = 0.5
servo_scale_y1 = 2.5


keys = ["ax0", "ax1", "ax2", "ax3", "ax4", "ax5"]


def scale(x: int) -> float:
    m = (servo_scale_y1 - servo_scale_y0) / (servo_scale_x1 - servo_scale_x0)
    n = servo_scale_y0
    return m * x + n


def set_servo_pulse(channel: int, pulse: float) -> None:
    pulse_length = 1000000 / 50 / 4096
    pulse *= 1000
    pulse /= pulse_length
    pulse = round(pulse)
    pulse = int(pulse)
    pwm.set_pwm(channel, 0, pulse)


# set pwm frequency
pwm.set_pwm_freq(50)


while True:
    for ch, key in enumerate(keys):
        val = int(redis_client.get(key) or b"0")
        if val > 0:
            set_servo_pulse(ch, scale(val))

    time.sleep(0.001)
