import os
import sys

#we must set env variable before importing any part of the django.
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

#to make us able to imort from our directory
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
