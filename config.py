# config.py

import os

class Development(object):
    """Development environment configuration"""

    DEBUG = True
    TESTING = False

    # might not need these key *** MAYBE DELETE ME ***
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

class Production(object):
    """Production environment configurations"""

    DEBUG = False
    TESTING = False

    # might not need these key *** MAYBE DELETE ME ***
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

app_config = {
    "development": Development,
    "production": Production,
}