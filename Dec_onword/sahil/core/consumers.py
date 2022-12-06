from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import JsonWebsocketConsumer,AsyncJsonWebsocketConsumer
import json
from random import randint
from asyncio import sleep
import asyncio
from asgiref.sync import sync_to_async,async_to_sync
import time
from .models import Group,Chat

class asyWebsocket(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print("Websocket connect....")
        print("channel Layer",self.channel_layer)
        print("channel Name",self.channel_name)
        self.group_name = self.scope['url_route']['kwargs']['groupname']
        print("group Name:",self.group_name)

    #     await async_to_sync(self.channel_layer.group_add)(
    #     self.room_group_name,
    #     self.channel_name
    #     )

    #     await async_to_sync(self.channel_layer.group_discard)(
    #     self.room_group_name,
    #     self.channel_name
    # )

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()
        print("websocket connected")
        a=[self.group_name]
        print('this is group',a)
        # for i in range(1,10):
        #     # time.sleep(1)
        #     # asyncio.sleep(1)
        #     a=[i,self.group_name]
        #     print("this is a",a)
            # await self.channel_layer.group_send(
            # 'sahil',
            # {
            #     'type':'chat.message',
            #     'message':a
            # })

            # time.sleep(5)

            # await self.channel_layer.group_send(
            # 'khan',
            # {
            #     'type':'chat.message',
            #     'message':a
            # })
            # asyncio.sleep(1)
        # for i in range(20):
        #     time.sleep(1)
        #     print(i)
        #     time
        #     self.send_json({"message":str(i)})
        #     asyncio.sleep(1)  



    async def receive_json(self,content,**kwargs):
        print("message Received from client...",content)

        # group=sync_to_async(Group.objects.get(name=self.group_name))()
        # print("this is group",group)
        # chat=sync_to_async(Chat(content=content['msg'],group=group))()
        # print("this is ",Chat)
        # chat.save()

        # @sync_to_async
        # def get_all_users():
        #     # return User.objects.all()

        # # for user in await get_all_users():
        # #     print(user)

        # group=Group.objects.get(name=self.group_name)
        # print(group)
        #     chat=Chat(
        #     content=content['msg'],
        #     group=group
        #     )
        #     chat.save()

        # get_all_users()

        await self.channel_layer.group_send(self.group_name,
            {
                'type':'chat.message',
                'message':content['msg']
            }
        )

    async def chat_message(self,event):
        print("Event...",event['message'])
        await self.send_json({
            'message':event['message']
        })

        # for i in range(20):
        #     print(i)
        #     self.send_json({"message":str(i)})
        #     asyncio.sleep(1)
    
    async def disconnect(self,close_code):
        print("websocket Connected....",close_code)
        print("channel Layer",self.channel_layer)
        print("channel Name",self.channel_name)
        self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def send_notification(self,event):
        print("notification")
        print(event)
        print("this is notification function")


























# class jsonWebsocket(JsonWebsocketConsumer):
#     def connect(self):
#         print("Websocket connect....")
#         print("channel Layer",self.channel_layer)
#         print("channel Name",self.channel_name)
#         self.group_name = self.scope['url_route']['kwargs']['groupname']
#         print("group Name:",self.group_name)

#     #     await async_to_sync(self.channel_layer.group_add)(
#     #     self.room_group_name,
#     #     self.channel_name
#     #     )

#     #     await async_to_sync(self.channel_layer.group_discard)(
#     #     self.room_group_name,
#     #     self.channel_name
#     # )

#         self.channel_layer.group_add(
#             self.group_name,
#             self.channel_name
#         )
#         self.accept()
#         print(" json websocket connected")

#         # for i in range(1,10):
#         #     # time.sleep(1)
#         #     # asyncio.sleep(1)
#         #     a=[i,self.group_name]
#         #     print("this is a",a)
#             # await self.channel_layer.group_send(
#             # 'sahil',
#             # {
#             #     'type':'chat.message',
#             #     'message':a
#             # })

#             # time.sleep(5)

#             # await self.channel_layer.group_send(
#             # 'khan',
#             # {
#             #     'type':'chat.message',
#             #     'message':a
#             # })
#             # asyncio.sleep(1)
#         # for i in range(20):
#         #     time.sleep(1)
#         #     print(i)
#         #     time
#         #     self.send_json({"message":str(i)})
#         #     asyncio.sleep(1)  

#     def receive_json(self,content,**kwargs):
#         print("message Received from client json...",content)

#         # async_to_sync(self.channel_layer.group_send)(self.group_name,
#         #     {
#         #         'type':'chat.message',
#         #         'message':content['msg']
#         #     }
#         # )

#         async_to_sync(self.channel_layer.group_send)(
#             self.group_name,
#             {
#                 "type": "chat.message",
#                 'message':content['msg']
#             },
#         )

#     def chat_message(self,event):
#         print("Event...",event['message'])
#         self.send_json({
#             'message':event['message']
#         })

#         # for i in range(20):
#         #     print(i)
#         #     self.send_json({"message":str(i)})
#         #     asyncio.sleep(1)
    
#     def disconnect(self,close_code):
#         print("websocket Connected....",close_code)
#         print("channel Layer",self.channel_layer)
#         print("channel Name",self.channel_name)
#         self.channel_layer.group_discard(
#             self.group_name,
#             self.channel_name
#         )

#     def send_notification(self,event):
#         print("notification")
#         print(event)
#         print("this is notification function")









# class asyWebsocket1(AsyncJsonWebsocketConsumer):
#     async def connect(self):
#         print("websocket connected")
#         await self.accept()
#         for i in range(20):
#             print(i)
#             await self.send_json({"message":str(i)})
#             await asyncio.sleep(1)  

#     # async def receive_json(self,content,**kwargs):
#     #     print("message Received from client...",content)
#     #     for i in range(30):
#     #         print(i)
#     #         await self.send_json({"message":str(i)})
#     #         await asyncio.sleep(1)
    
#     async def disconnect(self,close_code):
#         print("websocket Connected....",close_code)










# class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
#     async def connect(self):
#         print("websocket connected")
#         await self.accept()
#         # for i in range(20):
#         #     print(i)
#         #     await self.send_json({"message":str(i)})
#         #     await asyncio.sleep(1)  

#     async def receive_json(self,content,**kwargs):
#         print("message Received from client...",content)
#         for i in range(20):
#             print(i)
#             await self.send_json({"message":str(i)})
#             await asyncio.sleep(1)
    
#     async def disconnect(self,close_code):
#         print("websocket Connected....",close_code)