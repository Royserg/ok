#!/usr/bin/env python3
# To run:
# gunicorn -b 0.0.0.0:5000 wsgi:app
import os

from server import create_app, generate
from server.models import db, User

env = os.environ.get('OK_ENV', 'dev')
app = create_app('settings/%s.py' % env)


