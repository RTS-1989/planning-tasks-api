from typing import Optional

from django.conf import settings
from telegram import Message
from telegram.ext import Updater


class TelegramClient:

    def __init__(self):
        self.bot = Updater(settings.TELEGRAM_BOT_TOKEN).bot

    def send_message(self, chat_id: int, text: str) -> Optional[Message]:
        return self.bot.send_message(chat_id=chat_id, text=text)
