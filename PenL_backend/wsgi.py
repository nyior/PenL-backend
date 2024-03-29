"""
WSGI config for PenL_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PenL_backend.settings')

import socketio
from django.core.wsgi import get_wsgi_application

django_app = get_wsgi_application()
from apps.game_room.api.views import sio

application = socketio.WSGIApp(sio, django_app)
