from os import environ

SECRET_KEY = 'adkjfgkasdjfvbkadfvbkaldjfvbkjadfv'

DEBUG = True
SQLALCHEMY_DATABASE_URL = environ.get('DATABASE')
SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True
