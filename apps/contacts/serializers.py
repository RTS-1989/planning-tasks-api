from rest_framework import serializers

from apps.contacts.models import Phone, Telegram
from apps.bot_user.models import BotUser
from apps.bot_user.serializers import BaseBotUserSerializer
from tools.serializers import PrimaryKeyRelatedFieldID


class BasePhoneSerializer(serializers.ModelSerializer):

    bot_user_id = PrimaryKeyRelatedFieldID(queryset=BotUser.objects.all())

    class Meta:
        model = Phone
        fields = '__all__'


class PhoneSerializer(BasePhoneSerializer):
    bot_user = BaseBotUserSerializer()


class BaseTelegramSerializer(serializers.ModelSerializer):

    bot_user_id = PrimaryKeyRelatedFieldID(queryset=BotUser.objects.all())

    class Meta:
        model = Telegram
        fields = '__all__'


class TelegramSerializer(BaseTelegramSerializer):
    bot_user = BaseBotUserSerializer(read_only=True)
