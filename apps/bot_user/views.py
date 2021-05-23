from django.http import HttpRequest
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions, BasePermission
from rest_framework import filters

from .models import BotUser
from .serializers import BotUserSerializer


class CanRead(BasePermission):
    def has_permission(self, request: HttpRequest, view):
        return request.method == "GET"


class BotUserViewSet(ModelViewSet):

    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer
    permission_classes = [CanRead]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = 'id', 'surname', 'first_name', 'patronymic', 'is_active', 'email', 'birthday'

    class Meta:
        model = BotUser
