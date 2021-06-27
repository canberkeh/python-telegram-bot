import telegram
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
    
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """/start"""
    update.message.reply_text('This is Rylai')

def help(update, context):
    """/help"""
    update.message.reply_text('Do you need help?')

def echo(update, context):
    """reply users message"""
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def callback_minute(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id='885261354',
                             text='Message every minute')

def main():
    """Start the bot."""
    # Post version 12 this will no longer be necessary
    token = "1636789127:AAH8WbQuof3fAFQm6cAkhRnVEFU0my-TE-s"
    updater = Updater(token, use_context=True)
    j = updater.job_queue
    job_minute = j.run_repeating(callback_minute, interval=60, first=10)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)
    # Start the Bot
    updater.start_polling()

    myuser_id = '885261354'

    updater.dispatcher.bot.send_message(chat_id=myuser_id, text='Lets start')

    # ctrl + c to stop
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()