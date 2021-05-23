import phonenumbers

from django.db import models

from apps.bot_user.models import BotUser


class Phone(models.Model):
    raw_phone_number = models.CharField(verbose_name="Сырой номер", max_length=50, null=True, blank=True)
    e164 = models.CharField(verbose_name="Формат E164", max_length=50, editable=False)
    international = models.CharField(verbose_name="Интернациональный формат", max_length=50, editable=False)
    local_format = models.CharField(verbose_name="Локальный формат", max_length=50, editable=False)
    bot_user = models.ForeignKey("bot_user.BotUser", verbose_name="Пользователь бота", on_delete=models.RESTRICT)
    is_active = models.BooleanField(verbose_name="Активен", default=True)

    class Meta:
        verbose_name = "Телефон"
        verbose_name_plural = "Телефоны"

    def save(self, *args, **kwargs):
        _phone = phonenumbers.parse(self.raw_phone_number)
        self.e164 = phonenumbers.format_number(_phone, phonenumbers.PhoneNumberFormat.E164)
        self.international = phonenumbers.format_number(_phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        self.local_format = phonenumbers.format_number(_phone, phonenumbers.PhoneNumberFormat.NATIONAL)
        return super(Phone, self).save(*args, **kwargs)

    def __str__(self):
        return self.international


class Telegram(models.Model):
    username = models.CharField(verbose_name="Имя пользователя", blank=True, null=True, max_length=255, unique=True)
    user_id = models.BigIntegerField(verbose_name="ID пользователя", unique=True)

    bot_user = models.ForeignKey(BotUser, verbose_name="Пользователь бота", on_delete=models.RESTRICT,
                                 related_name="telegrams")
    is_active = models.BooleanField(verbose_name="Активен", default=True)

    class Meta:
        verbose_name = "Telegram"
        verbose_name_plural = "Telegram"

    def __str__(self):
        if self.username:
            return self.username

        return f'{self.user_id}'
