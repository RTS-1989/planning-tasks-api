from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from .models import Task, TaskCategory
from .serializers import TaskSerializer
from services.tools.custom_permissions import CanRead, CanCreate


class PlansViewSet(ModelViewSet):

    queryset = Task.objects.select_related('bot_user').all()
    serializer_class = TaskSerializer
    permission_classes = [CanCreate | CanRead]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['task_name', 'category', 'countable_value', 'date', 'done', 'bot_user']

    # Дописать с celery
    # def create(self, *args, **kwargs):
    #     response = super(PlansViewSet, self).create(*args, **kwargs)
    #     identifier = response.data.get('id')
