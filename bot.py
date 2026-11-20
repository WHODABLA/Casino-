import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Replace with your actual Bot Token
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Replace with your actual Web App URL (Must be HTTPS)
WEB_APP_URL = "https://whodabla.github.io/Casino-/"

CASINO_DESCRIPTION = """
👑 **WELCOME TO TREASURE HUB!** 💎

Your ultimate casino experience starts here! 🎰

Tap the button below to explore our games, access services and discover what Treasure Hub has to offer.

👇 **Click “OPEN MENU” to get started!**
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send casino description and an Inline 'Open' button when /start is issued."""
    
    # Create the inline button
    keyboard = [
        [
            InlineKeyboardButton(
                text="🎰 Open Menu", 
                web_app={"url": WEB_APP_URL}
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send the message with the inline button
    await update.message.reply_text(
        CASINO_DESCRIPTION,
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

def main() -> None:
    """Start the bot."""
    application = Application.builder().token(BOT_TOKEN).build()

    # Register the /start command
    application.add_handler(CommandHandler("start", start))

    # Run the bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()