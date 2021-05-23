from rest_framework import serializers

from .models import BotUser


class BaseBotUserSerializer(serializers.ModelSerializer):

    full_name = serializers.CharField()

    class Meta:
        model = BotUser
        fields = '__all__'


class BotUserSerializer(BaseBotUserSerializer):
    from apps.contacts.serializers import BaseTelegramSerializer, BasePhoneSerializer
    phone = BasePhoneSerializer(many=True)
    telegrams = BaseTelegramSerializer(many=True)


class BotUserTelegramSerializer(serializers.ModelSerializer):
    from apps.contacts.serializers import BaseTelegramSerializer
    telegrams = BaseTelegramSerializer(many=True)

    class Meta:
        model = BotUser
        fields = 'id', 'telegrams'
