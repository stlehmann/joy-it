class Config:
    MQTT_BROKER_URL = "rpi2-joyit.local"


class DevelopmentConfig(Config):
    TEMPLATES_AUTO_RELOAD = True


class ProductionConfig(Config):
    pass


config = dict(
    default=DevelopmentConfig(),
    development=DevelopmentConfig(),
    production=ProductionConfig(),
)
