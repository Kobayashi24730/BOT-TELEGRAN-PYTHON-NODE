import os
import sys
import logging
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler

# ------------------------------
# LOGGING (mostra tudo nos logs do Render)
# ------------------------------
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    stream=sys.stdout
)

logger = logging.getLogger(__name__)

# ------------------------------
# Carregar token
# ------------------------------
load_dotenv()
TOKEN = os.getenv("TELEGRAN_BOT_TOKEN")

if not TOKEN:
    logger.error("❌ BOT_TOKEN não encontrado! Configure nas variáveis do Render.")
    sys.exit(1)  # força erro e fecha o app

# ------------------------------
# Comandos básicos
# ------------------------------
async def start(update, context):
    await update.message.reply_text("🤖 Bot online! Digite /ping")

async def ping(update, context):
    await update.message.reply_text("🏓 Pong!")

# ------------------------------
# Main
# ------------------------------
def main():
    try:
        app = Application.builder().token(TOKEN).build()

        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("ping", ping))

        logger.info("🚀 Bot iniciado com sucesso!")
        app.run_polling()
    except Exception as e:
        logger.exception("💥 Erro fatal no bot:")
        sys.exit(1)

if __name__ == "__main__":
    main()
