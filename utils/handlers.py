import logging
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Logger
logger = logging.getLogger(__name__)


def start(update, context):
    """Starts the conversation"""
    user = update.message.from_user
    logger.info(f"User {user.full_name} started the conversation")
    update.message.reply_text(
        "Hi there! Are you ready to join our airdrop?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🚀 Join Airdrop", callback_data="proceed"),
                    InlineKeyboardButton("Cancel", callback_data="cancel"),
                ]
            ]
        ),
    )
    return PROCEED

def submit_details(update, context):
    """Captures user's details"""
    query = update.callback_query
    query.answer()
    user = query.from_user
    logger.info(f"User {user.full_name} submitted their details")
    query.edit_message_text(
        text="To proceed with the airdrop, please follow us on the following social media platforms:",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Telegram", callback_data="follow_telegram"),
                    InlineKeyboardButton("Twitter", callback_data="follow_twitter"),
                ],
                [
                    InlineKeyboardButton("Youtube", callback_data="follow_youtube"),
                    InlineKeyboardButton("Submit Details", callback_data="submit_details"),
                ],
            ]
        ),
    )
    return FOLLOW_TELEGRAM

def follow_telegram(update, context):
    text = (
        "To proceed, please follow our Telegram channel:\n"
        "https://t.me/example_channel\n"
        "Click on the 'Follow' button, then press the 'Submit Details' button."
    )
    update.message.reply_text(text)
    return FOLLOW_TELEGRAM


def follow_twitter(update, context):
    text = (
        "To proceed, please follow our Twitter account:\n"
        "https://twitter.com/example_account\n"
        "Click on the 'Follow' button, then press the 'Done' button."
    )
    update.message.reply_text(text)
    return FOLLOW_TWITTER


def follow_youtube(update, context):
    text = (
        "To proceed, please follow our Youtube channel:\n"
        "https://youtube.com/example_channel\n"
        "Click on the 'Follow' button, then press the 'Done' button."
    )
    update.message.reply_text(text)
    return FOLLOW_YOUTUBE


def submit_address(update, context):
    text = (
        "Please submit your Ethereum address where you would like to receive the tokens:\n"
        "Your Ethereum address should start with '0x...'"
    )
    update.message.reply_text(text)
    return SUBMIT_ADDRESS


def end_conversation(update, context):
    update.message.reply_text("Thank you for submitting your details. You will receive your tokens shortly.")
    return END_CONVERSATION


def loop_answer(update, context):
    update.message.reply_text("Invalid option, please try again.")
    return LOOP


def sure_want_to(update, context):
    if update.message.text.upper() == "YES":
        update.message.reply_text("Please enter the captcha:")
        return CAPTCHASTATE
    else:
        update.message.reply_text("Exiting, have a great day!")
        return END_CONVERSATION


def check_captcha(update, context):
    # Vérification du captcha envoyé par l'utilisateur
    captcha = update.message.text
    if captcha == "secret_captcha":
        # Si le captcha est correct, envoyer un message de confirmation
        update.message.reply_text("Captcha correct, accès autorisé.")
    else:
        # Si le captcha est incorrect, envoyer un message d'erreur
        update.message.reply_text("Captcha incorrect, accès refusé.")

def cancel_handler(update, context):
    # Annulation de la conversation en cours
    update.message.reply_text("Conversation annulée.")
    return ConversationHandler.END

def get_list(update, context):
    # Récupération de la liste d'articles
    articles = get_article_list()
    # Envoi de la liste d'articles à l'utilisateur
    update.message.reply_text("Liste des articles disponibles: \n\n" + "\n".join(articles))

def get_stats(update, context):
    # Récupération des statistiques
    stats = get_statistics()
    # Envoi des statistiques à l'utilisateur
    update.message.reply_text("Statistiques: \n\n" + stats)

def set_status(update, context):
    # Mise à jour du statut
    status = update.message.text
    set_article_status(status)
    # Envoi d'un message de confirmation
    update.message.reply_text("Statut mis à jour.")
