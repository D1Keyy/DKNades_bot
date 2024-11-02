from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, \
    InlineKeyboardButton


async def generate_main_keyboard():
    markup = InlineKeyboardMarkup()
    mirage = InlineKeyboardButton(text='Mirage', callback_data='main_mirage')
    dust2 = InlineKeyboardButton(text='Dust2', callback_data='main_dust2')
    markup.add(mirage).add(dust2)
    return markup

# Функции для генерации клавиатур для разных карт
#Mirage
async def generate_mirage_keyboard():
    markup = InlineKeyboardMarkup()
    # Добавляем кнопки для Mirage
    mirage_a = InlineKeyboardButton(text='A', callback_data='mirage_a')
    mirage_b = InlineKeyboardButton(text='B', callback_data='mirage_b')
    markup.add(mirage_a).add(mirage_b)
    return markup

# Функция для создания вложенной клавиатуры для Точки A на карте Mirage
async def generate_mirage_a_keyboard():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('CT', callback_data='mirage_a_ct'))
    markup.add(InlineKeyboardButton('Stairs', callback_data='mirage_a_stairs'))
    markup.add(InlineKeyboardButton('Jungle', callback_data='mirage_a_jungle'))
    return markup

# Функция для создания вложенной клавиатуры для СT, Точки A на карте Mirage
async def generate_mirage_a_ct_keyboard():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Смотреть видео', callback_data='ct_watch_video'))
    markup.add(InlineKeyboardButton('Вернуться назад', callback_data='ct_back'))
    markup.add(InlineKeyboardButton('Смена карты', callback_data='ct_change_map'))
    return markup

#Inferno
async def generate_inferno_keyboard():
    markup = InlineKeyboardMarkup()
    # Добавьте кнопки для Inferno
    markup.add(InlineKeyboardButton('Точка A', callback_data='inferno_a'))
    markup.add(InlineKeyboardButton('Точка B', callback_data='inferno_b'))
    return markup

#Dust2
async def generate_dust2_keyboard():
    markup = InlineKeyboardMarkup()
    # Добавьте кнопки для Dust2
    markup.add(InlineKeyboardButton('Точка A', callback_data='dust2_a'))
    markup.add(InlineKeyboardButton('Точка B', callback_data='dust2_b'))
    return markup