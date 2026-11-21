import os
import logging
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("No BOT_TOKEN found. Please set the BOT_TOKEN environment variable in Render.")

WEB_APP_URL = "https://whodabla.github.io/Casino-/"

CASINO_DESCRIPTION = """
👑 **WELCOME TO TREASURE HUB!** 💎

Your ultimate casino experience starts here! 🎰

Tap the button below to explore our games, access services and discover what Treasure Hub has to offer.

👇 **Click “OPEN MENU” to get started!**
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [[InlineKeyboardButton(text="🎰 Open Menu", web_app={"url": WEB_APP_URL})]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        CASINO_DESCRIPTION,
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

# --- Dummy Web Server for Render ---
def run_dummy_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), BaseHTTPRequestHandler)
    logging.info(f"Starting dummy web server on port {port}")
    server.serve_forever()

def main() -> None:
    # Start the dummy web server in a separate thread
    threading.Thread(target=run_dummy_server, daemon=True).start()
    
    # Start the bot
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()