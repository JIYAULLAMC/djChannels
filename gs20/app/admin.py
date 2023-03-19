from django.contrib import admin

# Register your models here.

from .models import Chat, Group


class ChatAdmin(admin.ModelAdmin):
    list_display = ["id", "content", "time", "group"]

admin.site.register(Chat, ChatAdmin)

 

class GroupAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

admin.site.register(Group, GroupAdmin)