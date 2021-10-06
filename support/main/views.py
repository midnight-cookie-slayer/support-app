from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
from .models import Support


def index(request):
    users = User.objects.all()
    sups = Support.objects.all()
    return render(request, "index.html", {"users": users, "sups": sups})


def create(request):
    if request.method == "POST":
        user = User()
        user.name = request.POST.get("name")
        user.message = request.POST.get("message")
        user.save()
    return HttpResponseRedirect("/")