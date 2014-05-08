import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = '12345'
    SQL_DRIVER = 'SQL Server Native Client 11.0'
    SQL_SERVER = 'WIN8\MSSQL2K12'
    SQL_DATABASE = 'LogMe'
    SQL_USER = 'LogMe'
    SQL_PASSWORD = 'password'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development' : DevelopmentConfig
}