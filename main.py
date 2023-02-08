import logging
import telegram
from telegram.ext import Updater, CommandHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello")

def main():
    # Get the bot token from the environment variable
    TOKEN = '5852766319:AAFJLw-NKobFaE2Qq12CDRxeAuu000jZTjE'

    # Create the Updater and pass it the bot token
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add the start command handler
    dp.add_handler(CommandHandler('start', start))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
