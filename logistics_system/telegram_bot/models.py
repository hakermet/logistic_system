from django.db import models
from django.conf import settings

class TelegramUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='telegram_user')
    chat_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Telegram User: {self.user.username}"
