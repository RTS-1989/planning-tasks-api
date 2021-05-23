from rest_framework import serializers

from .models import TaskCategory, Task
from apps.bot_user.models import BotUser
from apps.bot_user.serializers import BaseBotUserSerializer
from tools.serializers import PrimaryKeyRelatedFieldID


class TaskCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCategory
        fields = 'category_name'


class TaskSerializer(serializers.ModelSerializer):

    bot_user = BaseBotUserSerializer(read_only=True)
    bot_user_id = PrimaryKeyRelatedFieldID(queryset=BotUser.objects.all())

    class Meta:
        model = Task
        fields = '__all__'
