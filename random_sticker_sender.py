import logging

from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters

from config import settings
from handlers import send_text_command_factory, send_random_sticker

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def main() -> None:
    updater = Updater(settings.bot.token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("help", send_text_command_factory(settings.messages.help)))
    dispatcher.add_handler(CommandHandler("start", send_text_command_factory(settings.messages.start)))
    dispatcher.add_handler(CommandHandler("privacy", send_text_command_factory(settings.messages.privacy)))
    dispatcher.add_handler(MessageHandler(Filters.command, send_text_command_factory(settings.messages.unknown)))
    dispatcher.add_handler(InlineQueryHandler(send_random_sticker))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
