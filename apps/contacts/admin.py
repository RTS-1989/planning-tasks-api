from django.contrib import admin

from apps.contacts.models import Phone, Telegram


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['bot_user', 'international', 'local_format', 'e164', 'is_active']
    list_filter = ['is_active']
    readonly_fields = ['international', 'local_format', "e164"]
    search_fields = 'e164', 'international', 'local_format', 'raw_phone_number'


@admin.register(Telegram)
class TelegramAdmin(admin.ModelAdmin):
    list_display = ['username', 'user_id', 'bot_user', 'is_active']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
