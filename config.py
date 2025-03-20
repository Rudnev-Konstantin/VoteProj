import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    EXPLAIN_TEMPLATE_LOADING = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    DEBUG = False
    PREFERRED_URL_SCHEME = 'https'


config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
