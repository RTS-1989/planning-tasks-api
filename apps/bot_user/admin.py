from django.contrib import admin

from apps.bot_user.models import BotUser


@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ['surname', 'first_name', 'patronymic', 'is_active', 'email', 'birthday']
    list_filter = ['is_active']
    search_fields = ['id', 'surname', 'first_name', 'patronymic', 'birthday']
