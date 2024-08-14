import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage


import text
import keyboard
import schedule_script
import day_of_week_skript

admin_chat = -1002182287942
bot_token = "6381087353:AAHABLHLI-hpIX8qH3Qkd3dtIXvFwfFkw9A"

class FeedbackState(StatesGroup):
    waiting_for_feedback = State()

bot = Bot(token=bot_token)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.message):
    await message.answer(text.start_phrase.format(name=message.from_user.full_name), reply_markup=keyboard.menu)


@dp.callback_query_handler(func=None)
async def answer_handler(call: types.CallbackQuery):
    if call.data == 'working_personal_now':
        if day_of_week_skript.day_now <= 2:
            await call.message.answer(text=text.Kirill_personal, reply_markup=keyboard.back_menu_markup)
        elif day_of_week_skript.day_now > 2 and day_of_week_skript.day_now <= 5:
            await call.message.answer(text=text.Alisher_personal, reply_markup=keyboard.back_menu_markup)
        else:
            await call.message.answer(text=text.Kenan_personal, reply_markup=keyboard.back_menu_markup)



    if call.data == 'schedule':
        if schedule_script.hour_is_now >= 9 and schedule_script.hour_is_now < 22:
            await call.message.answer(text.coffee_store_open, reply_markup=keyboard.back_menu_markup)
        else:
            await call.message.answer(text.coffee_store_close, reply_markup=keyboard.back_menu_markup)


    if call.data == 'discount':
        await call.message.answer(text.discount_message,
                                  reply_markup=keyboard.back_menu_markup,
                                  parse_mode='MarkdownV2')

    if call.data == 'order_info':
        await call.message.answer(text.order_info_answer_msg,
                                  reply_markup=keyboard.back_menu_markup,
                                  parse_mode='MarkdownV2')
    if call.data == 'problem_requst':
        await call.message.answer("Опешите проблему в текстовом формате ✏️")
        await FeedbackState.waiting_for_feedback.set()

@dp.message_handler(state=FeedbackState.waiting_for_feedback)
async def handle_feedback_message(message: types.Message, state: FSMContext):
    await bot.send_message(admin_chat, f"Новый отзыв от пользователя с ID {message.from_user.id}:\n{message.text}")
    await message.answer("Спасибо за вклад в развитие бота!" "\n" 
                         "Ваше сообщение было передано администратору 👨‍💻""\n"
                         "Мы постараемся решить проблему в ближайшее время")
    await state.finish()

@dp.message_handler(func=None)
async def answer_back_menu_handler(message: types.message):
   await message.answer(text='Главное меню:', reply_markup=keyboard.menu)



@dp.callback_query_handler(state='*', text="cancel_feedback")
async def cancel_feedback(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Отменено! Если найдёте ошибку в работе бота, сообщите нам! - отправьте команду /start')
    await state.finish()


@dp.message_handler(state='*', content_types=['document', 'photo', 'video', 'video_note', 'sticker', 'voice'])
async def answer_on_media(message: types.Message):
    await message.answer("Я принимаю только текстовые сообщения", reply_markup=keyboard.cancel_KB)


if __name__ == '__main__':
    logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                        level=logging.INFO)
    executor.start_polling(dp)