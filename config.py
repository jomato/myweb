# coding:utf-8
import os
connection_string_dev = 'mysql://root:cross123@localhost:3306/dev_db'
connection_string_tes = 'mysql://root:cross123@localhost:3306/tes_db'
connection_string_pro = 'mysql://root:cross123@localhost:3306/pro_db'


class Config:
    '''
    功能：定义配置基类

    '''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[JH-Bolg]'
    FLASKY_MAIL_SENDER = '<sender email>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    FLASKY_POSTS_PER_PAGE = 8
    FLASKY_FOLLOWERS_PER_PAGE = 50
    FLASKY_COMMENTS_PER_PAGE = 30

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    '''
    功能：开发模式配置类

    '''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = connection_string_dev


class TestingConfig(Config):
    '''
    功能：测试模式配置类

    '''
    TESTING = True
    SQLALCHEMY_DATABASE_URI = connection_string_tes


class ProductionConfig(Config):
    '''
    功能：生产模式配置类

    '''
    SQLALCHEMY_DATABASE_URI = connection_string_pro


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}#类型字典
