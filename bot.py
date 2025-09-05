import os
import logging
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler

# --------------------------
# Configuração de logs
# --------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("❌ BOT_TOKEN não configurado!")

# --------------------------
# Telegram Bot Application
# --------------------------
application = Application.builder().token(TOKEN).build()

# Comando /start
async def start(update: Update, context):
    await update.message.reply_text("🤖 Bot ativo com Webhook!")

# Registrar handlers
application.add_handler(CommandHandler("start", start))

# --------------------------
# Flask app para Webhook
# --------------------------
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot online ✅", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        update = Update.de_json(request.get_json(force=True), application.bot)
        application.update_queue.put_nowait(update)
    except Exception as e:
        logger.error(f"Erro no webhook: {e}")
        return "erro", 500
    return "ok", 200

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=PORT)
