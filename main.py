import telebot
import os

# توکن ربات رو از محیط می‌گیره (نه مستقیم داخل کد)
BOT_TOKEN = os.environ.get("6100374382:AAFT3TEx_eHfUfGONjq4wurUgZTeisrZ0EI")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.reply_to(message, "سلام! 👋\nربات شما با موفقیت روی Render فعال شده ✅")

print("🤖 ربات روشن است و منتظر پیام‌هاست...")
bot.infinity_polling()
