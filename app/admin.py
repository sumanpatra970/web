from django.contrib import admin

from .models import chat,group,Feedback,ipbook

@admin.register(chat)
class ChatAdmin(admin.ModelAdmin):
    list_display=['id','content','timestamp','group','person']

@admin.register(group)
class groupadmin(admin.ModelAdmin):
    list_display=['id','name']

@admin.register(Feedback)  
class feedback(admin.ModelAdmin):
    list_display = ['Name','Query']

@admin.register(ipbook)  
class ipdata(admin.ModelAdmin):
    list_display = ['hostname','ip']



