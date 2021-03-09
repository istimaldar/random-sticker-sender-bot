from random import choice
from typing import Callable, List
from uuid import uuid4

from telegram import Update, InlineQueryResultCachedSticker, Sticker
from telegram.ext import CallbackContext

from config import settings


def send_text_command_factory(text: str) -> Callable[[Update, CallbackContext], None]:
    def command(update: Update, context: CallbackContext) -> None:
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    return command


def send_random_sticker(update: Update, context: CallbackContext) -> None:
    stickers = []  # type: List[Sticker]
    for sticker_set_name in settings.bot.packs:
        stickers += context.bot.get_sticker_set(sticker_set_name).stickers

    response = [InlineQueryResultCachedSticker(id=str(uuid4()), sticker_file_id=choice(stickers).file_id) for _ in
                range(settings.bot.options)]

    update.inline_query.answer(response, cache_time=0)
