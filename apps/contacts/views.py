from django.http import HttpRequest
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions, BasePermission
from rest_framework import filters

from .models import Phone, Telegram
from .serializers import PhoneSerializer, TelegramSerializer
from .filters import PhonesFilterSet, TelegramFilterSet


class CanCreate(BasePermission):
    def has_permission(self, request: HttpRequest, view):
        return request.method == "POST"


class CanRead(BasePermission):
    def has_permission(self, request: HttpRequest, view):
        return request.method == "GET"


class PhoneViewSet(ModelViewSet):

    queryset = Phone.objects.select_related('bot_user').all()
    serializer_class = PhoneSerializer
    permission_classes = [CanRead]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = PhonesFilterSet
    search_fields = ['e164', 'raw_phone_number', 'international', 'is_active', 'bot_user__id', 'bot_user__first_name',
                     'bot_user__surname', 'bot_user__patronymic']


class TelegramViewSet(ModelViewSet):

    queryset = Telegram.objects.select_related('bot_user').all()
    serializer_class = TelegramSerializer
    permission_classes = [CanCreate | CanRead]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = TelegramFilterSet
    search_fields = ['bot_user', 'user_id', 'username', 'is_active']
