import os
import logging
from threading import Thread
from flask import Flask

from telegram import Update
from telegram.ext import Application, ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("bot")

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
BASE_URL = os.getenv("BASE_URL")  # set after you get the Render URL
PORT = int(os.getenv("PORT", 3000))  # Render provides this

# ---- simple keep-alive web server (for polling mode so Render sees a port) ----
def start_keepalive():
    app = Flask(__name__)

    @app.get("/")
    def home():
        return "OK"

    app.run(host="0.0.0.0", port=PORT)

# ---- bot handlers ----
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I’m alive. Try /help")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Commands:\n/start\n/help\n/echo <text>")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

def build_app() -> Application:
    if not TOKEN:
        raise RuntimeError("Set TELEGRAM_BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    return app

if __name__ == "__main__":
    app = build_app()

    if BASE_URL:
        # ---- Webhook mode (production) ----
        path = TOKEN  # a simple secret path
        webhook_url = f"{BASE_URL.rstrip('/')}/{path}"
        log.info(f"Starting webhook on 0.0.0.0:{PORT} -> {webhook_url}")
        app.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=path,
            webhook_url=webhook_url,
            drop_pending_updates=True,
        )
    else:
        # ---- Polling mode (first deploy) + keepalive web server ----
        log.info(f"BASE_URL not set. Running POLLING and keep-alive server on :{PORT}")
        Thread(target=start_keepalive, daemon=True).start()
        app.run_polling(drop_pending_updates=True, allowed_updates=Update.ALL_TYPES)
