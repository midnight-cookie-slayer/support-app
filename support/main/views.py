from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .models import Support


def index(request):
    return HttpResponse("<h4>Im working<h4>")