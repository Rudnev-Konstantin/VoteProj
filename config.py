import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_super_secret_key'
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    EXPLAIN_TEMPLATE_LOADING = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class ProductionConfig(Config):
    PREFERRED_URL_SCHEME = 'https'


config = {
    'default': Config,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
