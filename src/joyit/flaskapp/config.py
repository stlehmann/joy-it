class Config:
    REDIS_URL = "redis://:password@localhost:6379/0"


class DevelopmentConfig(Config):
    TEMPLATES_AUTO_RELOAD = True
    REDIS_URL = "redis://@rpi2-joyit"


class ProductionConfig(Config):
    pass


config = dict(
    default=DevelopmentConfig(),
    development=DevelopmentConfig(),
    production=ProductionConfig(),
)