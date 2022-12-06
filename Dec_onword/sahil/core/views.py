from django.shortcuts import render,HttpResponse
from channels.layers import get_channel_layer
from asgiref.sync import sync_to_async,async_to_sync
from .models import Chat,Group
# Create your views here.

def index(request,group_name):
    group=Group.objects.filter(name=group_name).first()
    if group:
        pass
    else:
        group=Group(name=group_name)
        group.save()

    return render(request,'index.html',{"groupname":group_name})


# async def sahil(request):
#             await channel_layer.group_send(
#             'sahil',
#             {
#                 'type':'chat.message',
#                 'message':'sahil khan'
#             }
#         )

