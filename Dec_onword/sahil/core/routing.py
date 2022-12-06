from django.urls import path
from .consumers import *

ws_urlpatterns = [
path("ws/jwc/<str:groupname>/",asyWebsocket.as_asgi()),
# path("ws/jwc/<str:groupname>/",jsonWebsocket.as_asgi()),
    
]