import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from groq import Groq  # 👈 замість openai

# Завантаження змінних середовища
load_dotenv()

# Ключі
GROQ_API_KEY = "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"
TELEGRAM_BOT_TOKEN = "7353760084:AAEIJ928tS3XKafMruV6qrrmp9pMsUc7ePo"

# Клієнт Groq
client = Groq(api_key=GROQ_API_KEY)

# Функція отримання відповіді від ШІ
def get_gpt_response(prompt):
    print(f"[Groq GPT] Запит: {prompt}")
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",  # Або можна використати llama3-8b-8192
            messages=[{"role": "user", "content": prompt}]
        )
        reply = response.choices[0].message.content.strip()
        print(f"[Groq GPT] Відповідь: {reply}")
        return reply
    except Exception as e:
        print("[Помилка Groq]:", str(e))
        return "⚠️ Помилка при зверненні до Groq API. Спробуй пізніше."

# Обробка команди /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    print(f"[Start] Користувач {user.first_name} (@{user.username}) почав діалог.")
    welcome_text = (
        f"Привіт, {user.first_name}!\n\n"
        "Я — бот, підключений до штучного інтелекту Groq (Mixtral). Напиши мені будь-яке запитання — і я відповім 🤖"
    )
    await update.message.reply_text(welcome_text)

# Обробка звичайних повідомлень
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_text = update.message.text
    print(f"[Повідомлення] {user.first_name} (@{user.username}): {user_text}")

    response = get_gpt_response(user_text)
    await update.message.reply_text(response)

# Запуск бота
def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("[Бот] Бот запущено. Очікую повідомлення...")
    app.run_polling()

if __name__ == "__main__":
    main()
