"""
Configuration for Flask app

Important: Place your keys in the secret_keys.py module,
           which should be kept out of version control.
           secret_keys.py is generated by generate_keys.py.
"""

from app import secret_keys
from app.authenticator import GoogleAuthenticator

GOOGLE_AUTHENTICATOR = GoogleAuthenticator()

class Config: #pylint: disable=R0903
    """
    Base config
    """
    # Set secret keys for CSRF protection
    SECRET_KEY = secret_keys.CSRF_SECRET_KEY
    CSRF_SESSION_KEY = secret_keys.SESSION_KEY
    # Flask-Cache settings
    CACHE_TYPE = 'gaememcached'
    AUTHENTICATOR = GOOGLE_AUTHENTICATOR

class Development(Config): #pylint: disable=R0903
    """
    Development config
    """
    DEBUG = True
    CSRF_ENABLED = True

class Testing(Config): #pylint: disable=R0903
    """
    Testing config
    """
    TESTING = True
    DEBUG = True
    CSRF_ENABLED = True

class Production(Config): #pylint: disable=R0903
    """
    Prod config
    """
    DEBUG = False
    CSRF_ENABLED = True
