from telegram import Update
from telegram.ext import ApplicationBuilder,CommandHandler,ContextTypes
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

TOKEN = os.getenv("TELEGRAN_BOT_TOKEN")

async def start (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ola,Mundo! EU sou um bot")