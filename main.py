import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import tron

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text("Bonjour! Je suis un bot d'airdrop de TRON. Abonnez-vous à notre canal pour recevoir votre récompense en jetons TRON.")

def airdrop(update, context):
    user_id = update.message.from_user.id
    channel_username = "YOUR_CHANNEL_USERNAME"
    try:
        if context.bot.get_chat_member(channel_username, user_id).status in ["left", "kicked"]:
            update.message.reply_text("Vous n'êtes pas abonné à notre canal. Veuillez vous abonner pour recevoir votre récompense en jetons TRON.")
        else:
            tron.send_tron(user_id, amount=100) # Send 100 TRX to the user
            update.message.reply_text("Félicitations! Vous avez reçu 100 TRX pour vous être abonné à notre canal.")
    except Exception as e:
        update.message.reply_text("Une erreur s'est produite lors de la récompense en jetons TRON. Veuillez réessayer plus tard.")
        logger.error(e)

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    token = "YOUR_TELEGRAM_BOT_TOKEN"

    updater = Updater(token, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("airdrop", airdrop))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
