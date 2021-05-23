from django_filters.rest_framework import FilterSet, BooleanFilter

from apps.contacts.models import Phone, Telegram


class PhonesFilterSet(FilterSet):
    employee_is_active = BooleanFilter("botuser__is_active")

    class Meta:
        model = Phone
        fields = "bot_user_id", "e164", "employee_is_active"


class TelegramFilterSet(FilterSet):
    class Meta:
        model = Telegram
        fields = "bot_user_id", "username", "user_id", "is_active"
