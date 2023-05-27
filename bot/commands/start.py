"""/start command."""

from telegram import Update
from telegram.ext import CallbackContext
from telegram.constants import ParseMode

from bot.config import config
from . import constants
from . import help


class StartCommand:
    """Answers the `start` command."""

    async def __call__(self, update: Update, context: CallbackContext) -> None:
        if update.effective_user.username not in config.telegram.usernames:
            text = "Здравствуйте! Я - ИИ Sezin, психологический ассистент. \n" \
                   "Я здесь, чтобы помочь тебе с проблемами, " \
                   "связанными с психологическим здоровьем. \nЕсли у тебя есть какие-то вопросы или проблемы, " \
                   "я готов помочь. \n\nЧтобы начать диалог, просто задайте вопрос в этом чате.\n\n" \
                   'Если вы хотите, чтобы я запоминал контекст предыдущего сообщения, то поставьте перед своим ' \
                   'новым сообщением "+" '

            await update.message.reply_text(text)
            return

        text = text = "Здравствуйте! Я - ИИ Sezin, психологический ассистент. \n" \
                      "Я здесь, чтобы помочь тебе с проблемами, " \
                      "связанными с психологическим здоровьем. \nЕсли у тебя есть какие-то вопросы или проблемы, " \
                      "я готов помочь. \n\nЧтобы начать диалог, просто задайте вопрос в этом чате.\n\n" \
                      'Если вы хотите, чтобы я запоминал контекст предыдущего сообщения, то поставьте перед своим ' \
                      'новым сообщением "+" '
        text += help.generate_message(update.effective_user.username)
        if not context.bot.can_read_all_group_messages:
            text += f"\n\n{constants.PRIVACY_MESSAGE}"
        await update.message.reply_text(
            text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
        )
