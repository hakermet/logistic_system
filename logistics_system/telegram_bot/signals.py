from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from telegram_bot.models import TelegramUser
from telegram import Bot

@receiver(post_save, sender=Order)
def notify_order_creation(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        try:
            telegram_user = TelegramUser.objects.get(user=user)
            chat_id = telegram_user.chat_id
            bot = Bot(token="7549191302:AAEvj8szv3giwaGpWAy9CTqXNAEVi7x9RGQ")
            bot.send_message(chat_id=chat_id, text=f"Ваше замовлення #{instance.id} створено!")
        except TelegramUser.DoesNotExist:
            pass
