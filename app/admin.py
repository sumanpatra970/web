from django.contrib import admin

from .models import chat,group

@admin.register(chat)
class ChatAdmin(admin.ModelAdmin):
    list_display=['id','content','timestamp','group','person']

@admin.register(group)
class groupadmin(admin.ModelAdmin):
    list_display=['id','name']




