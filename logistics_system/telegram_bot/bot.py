from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from .models import TelegramUser
from orders.models import Order
from routes.models import Route
import asyncio

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user = update.effective_user
    username = user.username or "Guest"

    TelegramUser.objects.get_or_create(chat_id=chat_id)

    await update.message.reply_text(f"Привіт, {username}! Тепер ви отримуватимете оновлення про замовлення.")

async def my_orders(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    try:
        telegram_user = TelegramUser.objects.get(chat_id=chat_id)
        orders = Order.objects.filter(user=telegram_user.user)

        if not orders:
            await update.message.reply_text("У вас немає замовлень.")
        else:
            message = "\n".join([f"Замовлення #{o.id}: {o.cargo_type}, {o.weight} кг" for o in orders])
            await update.message.reply_text(message)

    except TelegramUser.DoesNotExist:
        await update.message.reply_text("Вас не знайдено в системі.")

# Налаштування бота
def setup_bot():
    token = "7549191302:AAEvj8szv3giwaGpWAy9CTqXNAEVi7x9RGQ"
    app = ApplicationBuilder().token(token).build()

    try:
        asyncio.get_event_loop().run_until_complete(app.run_polling())
    except RuntimeError as e:
        if str(e) == "Event loop is closed":
            asyncio.set_event_loop(asyncio.new_event_loop())
            asyncio.get_event_loop().run_until_complete(app.run_polling())
