from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import requests
import os
import random
import string

BOT_TOKEN = os.getenv("8339241243:AAGXFCZYlgPgoR0Eag8RpeNQDqimc4EHK_E")

# memory storage (simple version)
file_db = {}

def gen_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.document or update.message.video or update.message.photo[-1]

    file_id = file.file_id
    uid = gen_id()

    file_db[uid] = file_id

    link = f"https://your-app-url.koyeb.app/file/{uid}"

    await update.message.reply_text(f"Download link:\n{link}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me any file, I will generate link.")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(MessageHandler(filters.Document.ALL | filters.VIDEO | filters.PHOTO, handle_file))
app.add_handler(MessageHandler(filters.COMMAND, start))

app.run_polling()
