from django.shortcuts import render
from . models import Group, Chat
# Create your views here.


def index(request, group_name):
    present_group = Group.objects.filter(name=group_name).first()
    chats = []
    if present_group:
        pass
        chats = Chat.objects.filter(group=present_group)
    else:
        group = Group(name=group_name)
        group.save()
    return render(request, "app/index.html", {'groupname':group_name, 'chats':chats})