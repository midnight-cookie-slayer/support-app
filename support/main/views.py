"""from django.shortcuts import render                       # остатки фронта
from django.http import HttpResponse, HttpResponseRedirect"""

from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer, UserISUpdateSerializer, SupportSerializer

from .models import User, Support


# Для чего это нужно ищите в комментариях support/urls.py . Туда я привязывал все эти классы.

# Users:


class UserViewList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewCreate(CreateAPIView):
    serializer_class = UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewISUpdate(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserISUpdateSerializer


# Supports:


class SupportViewList(ListAPIView):
    queryset = Support.objects.all()
    serializer_class = SupportSerializer


class SupportViewCreate(CreateAPIView):
    serializer_class = SupportSerializer


class SupportViewSet(ModelViewSet):
    queryset = Support.objects.all()
    serializer_class = SupportSerializer
"""
############################################################################           остатки от работы с фронтом
def index(request):
    users = User.objects.all()
    supports = Support.objects.all()
    return render(request, "index.html", {"users": users, "supps": supports})


def user(request):
    users = User.objects.all()
    supports = Support.objects.all()
    return render(request, "is_user.html", {"users": users, "supps": supports})


def support(request):
    users = User.objects.all()
    supports = Support.objects.all()
    return render(request, "is_supp.html", {"users": users, "supps": supports})
############################################################################


def create_user(request):
    if request.method == "POST":
        user = User()
        user.name = request.POST.get("name")
        user.message = request.POST.get("message")
        user.save()
    return HttpResponseRedirect("/")


def create_support(request):
    if request.method == "POST":
        support = Support()
        user = User()
        support.name = request.POST.get("name")
        support.user_name = request.POST.get("user_name")
        support.message = request.POST.get("message")
        if user.name == support.user_name:                          # Саппорт решает решен ли тикет / замораживает тикет
            user.is_done = request.POST.get("is_done")
            user.is_frozen = request.POST.get("is_frozen")
        user.save()
        support.save()
    return HttpResponseRedirect("/")"""