"""planning_tasks_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from rest_framework.routers import DefaultRouter

from apps.tasks_planning.views import PlansViewSet
from apps.bot_user.views import BotUserViewSet
from apps.contacts.views import PhoneViewSet, TelegramViewSet

api = DefaultRouter()
api.register('plans', PlansViewSet)
api.register('phones', PhoneViewSet)
api.register('telegrams', TelegramViewSet)
api.register('bot_users', BotUserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api.urls)),
]
