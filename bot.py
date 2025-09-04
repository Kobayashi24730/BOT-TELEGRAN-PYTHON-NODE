import os
import sys
import logging
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

load_dotenv()
TOKEN = os.getenv("TELEGRAN_BOT_TOKEN")
PORT = int(os.getenv("PORT", 8443))  # Render define PORT automaticamente

async def start(update, context):
    await update.message.reply_text("🤖 Bot online via Webhook!")

async def ping(update, context):
    await update.message.reply_text("🏓 Pong!")

def main():
    if not TOKEN:
        logger.error("❌ BOT_TOKEN não encontrado!")
        sys.exit(1)

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ping", ping))

    # URL pública do Render (troque pelo seu domínio Render)
    render_url = os.getenv("RENDER_EXTERNAL_URL")  # Render injeta essa var
    webhook_url = f"{render_url}/webhook"

    logger.info(f"🚀 Iniciando webhook em {webhook_url}")
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=webhook_url,
    )

if __name__ == "__main__":
    main()
