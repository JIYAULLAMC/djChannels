from django.shortcuts import render
from app.models import Chat, Group

# Create your views here.


def index(request, groupname):
    group = Group.objects.all().filter(name=groupname).first()
    chats = []
    if group :
        chats = Chat.objects.filter(group=group)
    else:
        group = Group(name=groupname)
        group.save()
    return render(request, 'app/index.html', {"groupname":groupname, 'chats':chats})