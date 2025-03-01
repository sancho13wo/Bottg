from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Твой токен
TOKEN = "7998000897:AAHLhUFMi8FgFtNQVn8e50TlX7LY3ITjIf0"

# База данных фильмов (ключ — код, значение — ссылка)
FILMS = {
    "1234": "https://example.com/film1",
    "5678": "https://example.com/film2",
    "0000": "https://example.com/secret-movie"
}

# Функция для команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Введи 4-значный код фильма:")

# Функция обработки кода фильма
async def get_film(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = update.message.text.strip()

    if code in FILMS:
        await update.message.reply_text(f"Фильм найден! Вот ссылка: {FILMS[code]}")
    else:
        await update.message.reply_text("Фильм с таким кодом не найден.")

# Создаём бота
app = Application.builder().token(TOKEN).build()
app.run_polling(poll_interval=0.5)
# Добавляем обработчики команд и сообщений
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_film))

# Запускаем бота
print("Бот запущен!")
app.run_polling()