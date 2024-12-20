from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, \
    InlineKeyboardButton

# Функциz для локализации
async def generate_language_keyboard():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Русский', callback_data='lang_ru'))
    markup.add(InlineKeyboardButton('English', callback_data='lang_en'))
    return markup

# Функции для генерации клавиатур для разных карт
async def generate_maps_keyboard(language):  # Переименовано
    markup = InlineKeyboardMarkup()
    if language == 'ru':
        markup.add(InlineKeyboardButton('Mirage', callback_data='maps_mirage'))
        markup.add(InlineKeyboardButton('Dust2', callback_data='main_dust2'))
        markup.add(InlineKeyboardButton('Inferno', callback_data='main_inferno'))
    elif language == 'en':
        markup.add(InlineKeyboardButton('Mirage', callback_data='main_mirage'))
        markup.add(InlineKeyboardButton('Dust2', callback_data='main_dust2'))
        markup.add(InlineKeyboardButton('Inferno', callback_data='main_inferno'))
    return markup

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
async def generate_mirage_a_ct_keyboard(language):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Смотреть видео', callback_data='ct_watch_video'))
    markup.add(InlineKeyboardButton('Вернуться назад', callback_data='mir_a_back'))
    markup.add(InlineKeyboardButton('Смена карты', callback_data='ct_change_map'))
    return markup

# Функция для создания вложенной клавиатуры для stairs, Точки A на карте Mirage
async def generate_mirage_a_stairs_keyboard():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Смотреть видео', callback_data='stairs_watch_video'))
    markup.add(InlineKeyboardButton('Вернуться назад', callback_data='stairs_back'))
    markup.add(InlineKeyboardButton('Смена карты', callback_data='stairs_change_map'))
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