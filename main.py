from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InputFile
import config
from keyboards import (
    generate_main_keyboard,
    generate_mirage_keyboard,
    generate_dust2_keyboard,
    generate_inferno_keyboard,
    generate_mirage_a_keyboard,
    generate_mirage_a_ct_keyboard,
    generate_mirage_a_stairs_keyboard
)

bot = Bot(token=config.bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def command_start(message: types.Message):
    try:
        await bot.send_photo(message.from_user.id, InputFile('photo/logo.png'), caption='Подпись')
        await bot.send_message(message.from_user.id, config.hi_message, reply_markup=await generate_main_keyboard())
    except Exception as e:
        print(e)
        await bot.send_message(config.admin_id, 'Ошибка в боте: ' + str(e))

@dp.callback_query_handler(lambda x: str(x.data).startswith('main'))
async def command_main(call: types.CallbackQuery):
    try:
        await call.answer()
        karta = call.data.split('_')[1]
        print(karta)

        if karta == 'mirage':
            await bot.send_message(call.from_user.id, f'Вы выбрали карту {karta.capitalize()}', reply_markup=await generate_mirage_keyboard())
        elif karta == 'inferno':
            await bot.send_message(call.from_user.id, f'Вы выбрали карту {karta.capitalize()}', reply_markup=await generate_inferno_keyboard())
        elif karta == 'dust2':
            await bot.send_message(call.from_user.id, f'Вы выбрали карту {karta.capitalize()}', reply_markup=await generate_dust2_keyboard())
        else:
            await bot.send_message(call.from_user.id, 'Эта карта пока не поддерживается.')

    except Exception as e:
        print(e)
        await bot.send_message(config.admin_id, 'Ошибка в боте: ' + str(e))

@dp.callback_query_handler(lambda x: x.data == 'mirage_a')
async def handle_mirage_a(call: types.CallbackQuery):
    try:
        await call.answer()
        await bot.send_message(
            call.from_user.id,
            'Вы выбрали точку A на карте Mirage. Выберите конкретное местоположение:',
            reply_markup=await generate_mirage_a_keyboard()
        )
    except Exception as e:
        print(e)
        await bot.send_message(config.admin_id, 'Ошибка в боте: ' + str(e))

# Обработчик для кнопки CT на точке A
@dp.callback_query_handler(lambda x: x.data == 'mirage_a_ct')
async def handle_mirage_a_ct(call: types.CallbackQuery):
    try:
        await call.answer()
        photo = InputFile("photo/Mirage/a_CT.png")  # Картинка А, CT
        await bot.send_photo(
            call.from_user.id,
            photo=photo,
            caption="Вы выбрали CT на точке A (Mirage)",
            reply_markup=await generate_mirage_a_ct_keyboard()
        )
    except Exception as e:
        print(e)
        await bot.send_message(config.admin_id, 'Ошибка в боте: ' + str(e))

# Отправка видеофайла при выборе "Смотреть видео" для CT
@dp.callback_query_handler(lambda x: x.data == 'ct_watch_video')
async def watch_video_ct(call: types.CallbackQuery):
    try:
        await call.answer()
        video = InputFile("video/mirage/mir_a_ct.mp4")  # Видео дым CT
        await bot.send_video(
            call.from_user.id,
            video=video,
            caption="Видео для CT на точке A (Mirage)"
        )
    except Exception as e:
        print(e)
        await bot.send_message(config.admin_id, 'Ошибка в боте при отправке видео: ' + str(e))

# Обработчик для кнопки Stairs на точке A
@dp.callback_query_handler(lambda x: x.data == 'mirage_a_stairs')
async def handle_mirage_a_stairs(call: types.CallbackQuery):
    try:
        await call.answer()
        photo = InputFile("photo/Mirage/a_")  # Картинка для Stairs
        await bot.send_photo(
            call.from_user.id,
            photo=photo,
            caption="Вы выбрали Stairs на точке A (Mirage)",
            reply_markup=await generate_mirage_a_stairs_keyboard()
        )
    except Exception as e:
        print(e)
        await bot.send_message(config.admin_id, 'Ошибка в боте: ' + str(e))

# Отправка видеофайла при выборе "Смотреть видео" для Stairs
@dp.callback_query_handler(lambda x: x.data == 'stairs_watch_video')
async def watch_video_stairs(call: types.CallbackQuery):
    try:
        await call.answer()
        video = InputFile("video/mirage/a_stairs.mp4")  # Видео дым для Stairs
        await bot.send_video(
            call.from_user.id,
            video=video,
            caption="Дым на Stairs на точке A (Mirage)"
        )
    except Exception as e:
        print(e)
        await bot.send_message(config.admin_id, 'Ошибка в боте при отправке видео: ' + str(e))

# Возврат к выбору точки A (для CT и Stairs)
@dp.callback_query_handler(lambda x: x.data in ['mir_a_back', 'stairs_back'])
async def go_back(call: types.CallbackQuery):
    await call.answer()
    await bot.send_message(
        call.from_user.id,
        "Возвращаемся к выбору точки A (Mirage)",
        reply_markup=await generate_mirage_a_keyboard()
    )

# Смена карты (для CT и Stairs)
@dp.callback_query_handler(lambda x: x.data in ['ct_change_map', 'stairs_change_map'])
async def change_map(call: types.CallbackQuery):
    await call.answer()
    await bot.send_message(
        call.from_user.id,
        "Выберите карту",
        reply_markup=await generate_main_keyboard()
    )

executor.start_polling(dp, skip_updates=True)