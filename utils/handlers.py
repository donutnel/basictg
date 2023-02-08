import logging
from telegram import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackQueryHandler,
)

logger = logging.getLogger(__name__)

# Define constants for the states in the conversation handler
PROCEED, FOLLOW_TELEGRAM, FOLLOW_TWITTER, FOLLOW_YOUTUBE, SUBMIT_ADDRESS, END_CONVERSATION, LOOP, SUREWANTTO, CAPTCHASTATE = range(9)

# Define the conversation handler's entry point
def start(update, context):
    """Start the conversation and display the initial message."""
    message = "Bonjour! Voulez-vous rejoindre notre airdrop?"
    buttons = [
        [InlineKeyboardButton("Oui, je veux rejoindre!", callback_data="proceed")],
        [InlineKeyboardButton("Non, merci", callback_data="cancel")],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    update.message.reply_text(message, reply_markup=reply_markup)
    return PROCEED

# Define the handler for the `proceed` state
def submit_details(update, context):
    """Prompt the user to follow our Telegram, Twitter, and YouTube accounts."""
    message = "Merci de nous suivre sur Telegram, Twitter et YouTube pour recevoir votre jeton gratuit!"
    buttons = [
        [InlineKeyboardButton("Suivez-nous sur Telegram", callback_data="follow_telegram")],
        [InlineKeyboardButton("Suivez-nous sur Twitter", callback_data="follow_twitter")],
        [InlineKeyboardButton("Suivez-nous sur YouTube", callback_data="follow_youtube")],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    update.message.reply_text(message, reply_markup=reply_markup)
    return FOLLOW_TELEGRAM

    # Define the handler for the `follow_telegram` state
    def follow_telegram(update, context):
      """Prompt the user to confirm that they have followed us on Telegram."""
      message = "Avez-vous suivi notre compte Telegram?"
      buttons = [
        [InlineKeyboardButton("Oui, je l'ai suivi!", callback_data="followed_telegram")],
        [InlineKeyboardButton("Non, pas encore", callback_data="not_followed_telegram")],
      ]
      reply_markup = InlineKeyboardMarkup(buttons)
      update.message.reply_text(
      message, reply_markup=reply_markup, parse_mode=ParseMode.MARKDOWN
      )
      return FOLLOW_TELEGRAM

    #Define the handler for the follow_twitter state
    def follow_twitter(update, context):
      """Prompt the user to confirm that they have followed us on Twitter."""
      message = "Avez-vous suivi notre compte Twitter?"
      buttons = [
        [InlineKeyboardButton("Oui, je l'ai suivi!", callback_data="followed_twitter")],
        [InlineKeyboardButton("Non, pas encore", callback_data="not_followed_twitter")],
      ]
      reply_markup = InlineKeyboardMarkup(buttons)
      update.message.reply_text(
      message, reply_markup=reply_markup, parse_mode=ParseMode.MARKDOWN
      )
      return FOLLOW_TWITTER

    #Define the handler for the follow_youtube state
    def follow_youtube(update, context):
      """Prompt the user to confirm that they have followed us on YouTube."""
      message = "Avez-vous suivi notre chaîne YouTube?"
      buttons = [
        [InlineKeyboardButton("Oui, je l'ai suivi!", callback_data="followed_youtube")],
        [InlineKeyboardButton("Non, pas encore", callback_data="not_followed_youtube")],
      ]
      reply_markup = InlineKeyboardMarkup(buttons)
      update.message.reply_text(
      message, reply_markup=reply_markup, parse_mode=ParseMode.MARKDOWN
      )
      return FOLLOW_YOUTUBE

    #Define the handler for the submit_address state
    def submit_address(update, context):
      """Prompt the user to submit their Ethereum address."""
      message = "Veuillez soumettre votre adresse Ethereum."
      update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)
      return SUBMIT_ADDRESS
    
    
