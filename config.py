class Config(object):

    SECRET_KEY = 'Ritesh Gupta'

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None

class DevelopmentConfig(Config):
    DEBUG = True