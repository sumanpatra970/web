# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    path('wa/sc/<str:grpname>',consumer.MySync.as_asgi()),
    path('wa/ac/<str:grpname>',consumer.MyAsync.as_asgi())
]