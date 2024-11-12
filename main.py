from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.types import InputFile
from aiogram.dispatcher.filters.state import State, StatesGroup
import config
from keyboards import (generate_language_keyboard,
    generate_maps_keyboard,
    generate_mirage_keyboard,
    generate_dust2_keyboard,
    generate_inferno_keyboard,
    generate_mirage_a_keyboard,
    generate_mirage_a_ct_keyboard)

bot = Bot(token=config.bot_token)
dp = Dispatcher(bot)


class UserState(StatesGroup):
    language = State()


@dp.message_handler(commands='start')
async def command_start(message: types.Message):
    try:
        await bot.send_photo(message.from_user.id, InputFile('photo/logo.png'), caption='Welcome! / Добро пожаловать!')
        await bot.send_message(message.from_user.id, "Please select your language / Пожалуйста, выберите язык",
                               reply_markup=await generate_language_keyboard()
        )
    except Exception as e:
        print(e)
        await bot.send_message(config.admin_id, 'Ошибка в боте: ' + str(e))


@dp.callback_query_handler(lambda x: x.data.startswith('lang'))
async def set_language(call: types.CallbackQuery, state: FSMContext):
    try:
        await call.answer()
        language = call.data.split('_')[1]
        await state.update_data(language=language)

        # Показать выбор карты после выбора языка
        reply_markup = await generate_maps_keyboard(language)  # Изменено на generate_maps_keyboard
        greeting = "Выберите карту" if language == 'ru' else "Choose a map"
        await bot.send_message(call.from_user.id, greeting, reply_markup=reply_markup)
    except Exception as e:
        print(e)
        await bot.send_message(config.admin_id, 'Ошибка в боте: ' + str(e))

    @dp.callback_query_handler(lambda x: str(x.data).startswith('main'))
    async def command_main(call: types.CallbackQuery, state: FSMContext):
        try:
            await call.answer()
            await bot.delete_message(call.from_user.id, call.message.message_id)
            data = await state.get_data()
            language = data.get('language', 'en')

            karta = call.data.split('_')[1]
            print(karta)

            if karta == 'mirage':
                text = f'Вы выбрали карту Mirage' if language == 'ru' else 'You selected Mirage'
                await bot.send_message(call.from_user.id, text, reply_markup=await generate_mirage_keyboard())
            elif karta == 'dust2':
                text = f'Вы выбрали карту Dust2' if language == 'ru' else 'You selected Dust2'
                await bot.send_message(call.from_user.id, text, reply_markup=await generate_dust2_keyboard())
            elif karta == 'inferno':
                text = f'Вы выбрали карту Inferno' if language == 'ru' else 'You selected Inferno'
                await bot.send_message(call.from_user.id, text, reply_markup=await generate_inferno_keyboard())
            else:
                text = 'Эта карта пока не поддерживается.' if language == 'ru' else 'This map is not supported yet.'
                await bot.send_message(call.from_user.id, text)
        except Exception as e:
            print(e)
            await bot.send_message(config.admin_id, 'Ошибка в боте: ' + str(e))


@dp.callback_query_handler(lambda x: x.data == 'mirage_a')
async def handle_mirage_a(call: types.CallbackQuery, state: FSMContext):
    try:
        await call.answer()
        data = await state.get_data()
        language = data.get('language', 'en')

        text = 'Вы выбрали точку A на карте Mirage. Выберите конкретное местоположение:' if language == 'ru' else 'You selected point A on Mirage. Choose a specific location:'
        await bot.send_message(call.from_user.id, text, reply_markup=await generate_mirage_a_keyboard())
    except Exception as e:
        print(e)
        await bot.send_message(config.admin_id, 'Ошибка в боте: ' + str(e))


@dp.callback_query_handler(lambda x: x.data == 'mirage_a_ct')
async def handle_mirage_a_ct(call: types.CallbackQuery, state: FSMContext):
    try:
        await call.answer()
        data = await state.get_data()
        language = data.get('language', 'en')

        photo = InputFile("photo/Mirage/a_CT.png")
        caption_text = "Вы выбрали CT на точке A (Mirage)" if language == 'ru' else "You selected CT on point A (Mirage)"

        await bot.send_photo(
            call.from_user.id,
            photo=photo,
            caption=caption_text,
            reply_markup=await generate_mirage_a_ct_keyboard()
        )
    except Exception as e:
        print(e)
        await bot.send_message(config.admin_id, 'Ошибка в боте: ' + str(e))


@dp.callback_query_handler(lambda x: x.data == 'ct_watch_video')
async def watch_video_ct(call: types.CallbackQuery, state: FSMContext):
    try:
        await call.answer()
        video = InputFile("video/mirage/mir_a_ct.mp4")
        data = await state.get_data()
        language = data.get('language', 'en')

        caption_text = "Видео для CT на точке A (Mirage)" if language == 'ru' else "Video for CT on point A (Mirage)"
        await bot.send_video(
            call.from_user.id,
            video=video,
            caption=caption_text
        )
    except Exception as e:
        print(e)
        await bot.send_message(config.admin_id, 'Ошибка в боте при отправке видео: ' + str(e))


@dp.callback_query_handler(lambda x: x.data in ['mir_a_back', 'stairs_back'])
async def go_back(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    data = await state.get_data()
    language = data.get('language', 'en')
    text = "Возвращаемся к выбору точки A (Mirage)" if language == 'ru' else "Returning to point A (Mirage)"

    await bot.send_message(
        call.from_user.id,
        text,
        reply_markup=await generate_mirage_a_keyboard()
    )


@dp.callback_query_handler(lambda x: x.data in ['ct_change_map', 'stairs_change_map'])
async def change_map(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    data = await state.get_data()
    language = data.get('language', 'en')
    text = "Выберите карту" if language == 'ru' else "Choose a map"

    await bot.send_message(
        call.from_user.id,
        text,
        reply_markup=await generate_maps_keyboard(language)
    )


executor.start_polling(dp, skip_updates=True)