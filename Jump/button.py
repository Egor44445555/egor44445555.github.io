from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext

TOKEN = "8132996734:AAFhwnXyj1wtLRYH-gUk7u-k2t3EEUuvt-s"
WEB_APP_URL = "https://egor44445555.github.io/Jump/"

async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("🎮 Играть в игру", web_app={"url": WEB_APP_URL})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Нажми кнопку, чтобы начать игру!", reply_markup=reply_markup)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()