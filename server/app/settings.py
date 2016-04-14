"""
Configuration for Flask app

Important: Place your keys in the secret_keys.py module,
           which should be kept out of version control.
           secret_keys.py is generated by generate_keys.py.
"""

from app import secret_keys
from app.authenticator import GoogleAuthenticator, TestingAuthenticator

GOOGLE_AUTHENTICATOR = GoogleAuthenticator()
TESTING_AUTHENTICATOR = TestingAuthenticator()


class Config(object): #pylint: disable=R0903
    """
    Base config
    """
    # Set secret keys for CSRF protection
    SECRET_KEY = secret_keys.CSRF_SECRET_KEY
    CSRF_SESSION_KEY = secret_keys.SESSION_KEY
    # Flask-Cache settings
    CACHE_TYPE = 'gaememcached'
    AUTHENTICATOR = GOOGLE_AUTHENTICATOR
    GAE_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"
    CLIENT_VERSION = '1.0.6'


class Debug(Config): #pylint: disable=R0903
    """
    Development config
    """
    DEBUG = True
    TESTING = True
    CSRF_ENABLED = True
    AUTHENTICATOR = TESTING_AUTHENTICATOR


class Production(Config): #pylint: disable=R0903
    """
    Prod config
    """
    DEBUG = False
    CSRF_ENABLED = True