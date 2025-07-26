import telebot
import os

# توکن ربات رو از محیط می‌گیره (نه مستقیم داخل کد)
BOT_TOKEN = os.environ.get("8105590498:AAE2m5zyazHzn41MmCHK9uajasOq30eWbcI")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.reply_to(message, "سلام! 👋\nربات شما با موفقیت روی Render فعال شده ✅")

print("🤖 ربات روشن است و منتظر پیام‌هاست...")
bot.infinity_polling()
