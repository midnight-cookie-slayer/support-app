"""support URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import SimpleRouter
from main.views import UserViewSet, UserViewCreate, SupportViewSet, SupportViewCreate, UserViewISUpdate, UserViewList, \
    SupportViewList, UserViewUpdate

router = SimpleRouter()
router.register('api/user', UserViewSet)                                       # /api/user/?format=json
router.register('api/support', SupportViewSet)                                 # /api/support/?format=json

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UserViewCreate.as_view()),                                # создание пользователя с главной страницы
    path('user/list', UserViewList.as_view()),                         # список пользователей: id, name и message
    path('user/create', UserViewCreate.as_view()),                     # создание пользователя и его сообщения
    path('user/update/<int:pk>', UserViewUpdate.as_view()),            # изменение и удаление сообщения пользователя
    path('support/list', SupportViewList.as_view()),                   # список сапортов и их ответов
    path('support/create', SupportViewCreate.as_view()),               # создание сопорта и его ответа пользователю
    path('support/is_update/<int:pk>', UserViewISUpdate.as_view()),    # обновление is_done, is_frozen у пользователя
]

urlpatterns += router.urls