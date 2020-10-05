import os
class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI ="postgresql+psycopg2://mf839:bmth1327@localhost/movielist"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', None)
