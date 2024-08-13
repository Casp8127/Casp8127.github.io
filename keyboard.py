from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from aiogram.types.web_app_info import WebAppInfo
import text

main_menu = [
    [InlineKeyboardButton(text='🕒 График работы', callback_data='schedule'),
    InlineKeyboardButton(text='Кто сегодня готовит для вас?', callback_data='working_personal_now')],
    [InlineKeyboardButton(text='🏷️ Акции', callback_data='discount'),
    InlineKeyboardButton(text='☕ Заказать кофе', web_app=WebAppInfo(url='https://casp8127.github.io/'))],
    [InlineKeyboardButton(text='📢 Оставить отзыв', url='https://yandex.ru/maps/org/sosedi/170378129106/reviews/?ll=37.598968%2C55.636738&z=16'),
    InlineKeyboardButton(text='❓ Сообщить о проблеме', callback_data='problem_requst')],
    [InlineKeyboardButton(text='🌟 Как заказать кофе с собой?', callback_data='order_info')],
]


menu = InlineKeyboardMarkup(inline_keyboard=main_menu)
back_menu_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                       one_time_keyboard=True)
back_menu_markup.add(KeyboardButton(text.kb_back_manu))

cancel_KB = InlineKeyboardMarkup(row_width=2) \
    .add(KeyboardButton("Не хочу оставлять отзыв 🚫", callback_data="cancel_feedback"))

