from random import choice
from typing import Callable, List
from uuid import uuid4

from telegram import Update, InlineQueryResultCachedSticker, Sticker, Bot
from telegram.ext import CallbackContext
from cachetools.func import ttl_cache

from config import settings


def send_text_command_factory(text: str) -> Callable[[Update, CallbackContext], None]:
    def command(update: Update, context: CallbackContext) -> None:
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    return command


def send_random_sticker(update: Update, context: CallbackContext) -> None:
    stickers = []  # type: List[str]
    for sticker_set_name in settings.bot.packs:
        stickers += __get_sticker_set_stickers(context.bot, sticker_set_name)

    response = [InlineQueryResultCachedSticker(id=str(uuid4()), sticker_file_id=choice(stickers)) for _ in
                range(settings.bot.options)]

    update.inline_query.answer(response, cache_time=0)


@ttl_cache(maxsize=settings.cache.size, ttl=settings.cache.ttl)
def __get_sticker_set_stickers(bot: Bot, name: str) -> List[str]:
    return [sticker.file_id for sticker in bot.get_sticker_set(name).stickers]
