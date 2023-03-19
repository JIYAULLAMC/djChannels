from django.shortcuts import render

# Create your views here.


def index(request, groupname):
    return render(request, 'app/index.html', {"groupname":groupname})