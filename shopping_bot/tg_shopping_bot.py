import json
from aiogram import Dispatcher , types , Bot ,executor
import asyncio
from aiogram.dispatcher.filters import Text
from adidas_кроссовки import adidas_func
from megasport_кроссовки import megasport_func
from megasport_шорты import megasport_shorts
from megasport_футболки import megasport_tshirt
from puma_кроссовки import puma_sneakers
from puma_шорты import puma_shorts
from puma_футболки import puma_tshirts
from adidas_футболки import adidas_tshirt
from adidas_шорты import adidas_shorts_run
from aiogram.utils.markdown import hbold
from aiogram.utils.markdown import hlink , link
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from tg_info import *

token = token_info
channel_id = channel_id_info
storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot , storage=storage)

                                                        # """Формы"""



class Gender_Form(StatesGroup):
    Gender = State()


class Adidas_Form(StatesGroup):
    Adidas_Sneakers_Size = State()
    Adidas_Tshirt_Size = State()
    Adidas_Shorts_Size = State()


class Megasport_Form(StatesGroup):
    Megasport_Sneakers_Size = State()
    Megasport_Tshirt_Size = State()
    Megasport_Shorts_Size = State()


class Puma_Form(StatesGroup):
    Puma_Sneakers_Size = State()
    Puma_Tshirt_Size = State()
    Puma_Shorts_Size = State()





                                                        # """Основное"""

with open('size.json' , 'r') as f:
    size_json = json.load(f)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['Male' , 'Female']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer('Hi, choose a gender.' , reply_markup=keyboard)
    # await Gender_Form.Gender.set()



@dp.message_handler(Text(equals='Male') )
async def adidas(message: types.Message , state: FSMContext):
    async with state.proxy() as data:
        data['Gender'] = message.text
    start_buttons = ['adidas' , 'puma' , 'megasport']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer('Select a store' , reply_markup=keyboard)
    # await state.finish()
    # await Gender_Form.Gender.set()



@dp.message_handler(Text(equals='Female'))
async def adidas(message: types.Message , state: FSMContext):
    async with state.proxy() as data:
        data['Gender'] = message.text
    start_buttons = ['adidas' , 'puma' , 'megasport']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer('Select a store' , reply_markup=keyboard)




@dp.message_handler(Text(equals='adidas'))
async def adidas(message: types.Message):
    start_buttons = ['sneakers(adidas)', 'shorts(adidas)', 'tshirts(adidas)']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer('Choose which of these you are interested in' , reply_markup=keyboard)
    # await Gender_Form.next()




@dp.message_handler(Text(equals='puma'))
async def puma(message: types.Message):
    start_buttons = ['sneakers(puma)', 'tshirts(puma)', 'shorts(puma)']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer('Choose which of these you are interested in' , reply_markup=keyboard)




@dp.message_handler(Text(equals='megasport'))
async def megasport(message: types.Message):
    start_buttons = ['sneakers(megasport)', 'shorts(megasport)', 'tshirts(megasport)']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer('Choose which of these you are interested in' , reply_markup=keyboard)





                                                         # """Кросовки"""

@dp.message_handler(Text(equals='sneakers(adidas)'))
async def adidas_sneakers(message: types.Message):
    buttons = ['38','39','40','41','42','43','44','45','46','47','48','49']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=10)
    keyboard.add(*buttons)
    await Adidas_Form.Adidas_Sneakers_Size.set()
    await message.reply('Choose a size' , reply_markup=keyboard)





@dp.message_handler(Text(equals='sneakers(megasport)'))
async def megasport_sneakers(message: types.Message):
    buttons = ['35', '36', '36,5', '37', '37,5', '38', '38,5', '39', '40', '40,5', '41', '42', '42,5', '43', '44', '44,5', '45', '45,5', '46', '47']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=10)
    keyboard.add(*buttons)
    await Megasport_Form.Megasport_Sneakers_Size.set()
    await message.answer('Choose a size' , reply_markup=keyboard)







@dp.message_handler(Text(equals='sneakers(puma)'))
async def puma_sneakers_(message: types.Message):
    buttons = ['35,5', '36', '37', '37,5', '38', '38,5', '39', '40', '40,5', '41', '42', '42,5', '43', '44', '44,5', '45', '46', '47']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=10)
    keyboard.add(*buttons)
    await Puma_Form.Puma_Sneakers_Size.set()
    await message.answer('Choose a size' , reply_markup=keyboard)







                                                        # """Футболки"""
@dp.message_handler(Text(equals='tshirts(megasport)'))
async def megasport_tsirts(message: types.Message):
    button = ['XS','S','M','L','XL','XXL']
    keybord = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=10)
    keybord.add(*button)
    await Megasport_Form.Megasport_Tshirt_Size.set()
    await message.answer('Choose a size' , reply_markup=keybord)








@dp.message_handler(Text(equals='tshirts(puma)'))
async def puma_tsirts_(message: types.Message):
    button = ['XS','S','M','L','XL','XXL']
    keybord = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=10)
    keybord.add(*button)
    await Puma_Form.Puma_Tshirt_Size.set()
    await message.answer('Choose a size' , reply_markup=keybord)





@dp.message_handler(Text(equals='tshirts(adidas)'))
async def adidas_tsirts(message: types.Message):
    button = ['XS','S','M','L','XL','XXL']
    keybord = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=10)
    keybord.add(*button)
    await Adidas_Form.Adidas_Tshirt_Size.set()
    await message.answer('Choose a size' , reply_markup=keybord)






                                                            # """Шорты"""

@dp.message_handler(Text(equals='shorts(megasport)'))
async def megasport_shorts_(message: types.Message):
    button = ['XS','S','M','L','XL','XXL']
    keybord = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=10)
    keybord.add(*button)
    await Megasport_Form.Megasport_Shorts_Size.set()
    await message.answer('Choose a size' , reply_markup=keybord)






@dp.message_handler(Text(equals='shorts(puma)'))
async def puma_shorts_(message: types.Message):
    button = ['XS','S','M','L','XL','XXL']
    keybord = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=10)
    keybord.add(*button)
    await Puma_Form.Puma_Shorts_Size.set()
    await message.answer('Choose a size' , reply_markup=keybord)






@dp.message_handler(Text(equals='shorts(adidas)'))
async def adidas_shorts(message: types.Message):
    button = ['XS','S','M','L','XL','XXL']
    keybord = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=10)
    keybord.add(*button)
    await Adidas_Form.Adidas_Shorts_Size.set()
    await message.answer('Choose a size' , reply_markup=keybord)



                                                        # """Запускаем все с форм"""



@dp.message_handler(state=Adidas_Form.Adidas_Shorts_Size)
async def adidas_shorts(message: types.Message , state:FSMContext):
    async with state.proxy() as data:
        data['Adidas_Shorts_Size'] = message.text
    size = data['Adidas_Shorts_Size']
    print(data['Gender'])
    for k,v in size_json['adidas_shorts_tshirts'].items():
        if size == k:
            size=v
            print(size)
    await message.answer('Please waiting...')
    if data['Gender'] == 'Male':
        gender = 'choloviki'
        await adidas_shorts_run(size , gender)
    elif data['Gender'] == 'Female':
        gender = 'zhinki'
        await adidas_shorts_run(size , gender)
    with open('result_adidas_shorts.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for i in data:
        # card = f"{hlink(i.get('Модель') , i.get('Ссылка'))}\n" \
        #        f"{hbold('Прайс')}:{i.get('Цена')}\n" \
        #        f"{hbold('Прайс со скидкой')}:{i.get('Цена со скидкой')}"
        card = f'<b><a href="{i["Ссылка"]}">{i["Модель"]}</a></b>\n' \
               f'<b>Price:</b>{i["Цена"]}\n' \
               f'<b>Discounted price:</b>{i["Цена со скидкой"]}\n'
        await message.answer(card , parse_mode='HTML')
        await asyncio.sleep(1)
    await state.finish()

@dp.message_handler(state=Adidas_Form.Adidas_Sneakers_Size)
async def adidas_sneackers(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Adidas_Sneakers_Size'] = message.text
    size = data['Adidas_Sneakers_Size']
    for k,v in size_json['adidas_sneakers'].items():
        if size == k:
            size=v
            print(size)
    await message.answer('Please waiting...')
    if data['Gender'] == 'Male':
        gender = 'choloviki'
        await adidas_func(size, gender)
    elif data['Gender'] == 'Female':
        gender = 'zhinki'
        await adidas_func(size, gender)
    with open('result_adidas_sneakers.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for i in data:
        card = f'<b><a href="{i["Ссылка"]}">{i["Модель"]}</a></b>\n' \
               f'<b>Price:</b>{i["Цена"]}\n' \
               f'<b>Discounted price:</b>{i["Цена со скидкой"]}\n'
        await message.answer(card , parse_mode='HTML')
        await asyncio.sleep(1)
    await state.finish()



@dp.message_handler(state=Adidas_Form.Adidas_Tshirt_Size)
async def adidas_tshirts(message: types.Message , state:FSMContext):
    async with state.proxy() as data:
        data['Adidas_Sneakers_Size'] = message.text
    size = data['Adidas_Sneakers_Size']
    for k,v in size_json['adidas_shorts_tshirts'].items():
        if size == k:
            size=v
            print(size)
    await message.answer('Please waiting...')
    if data['Gender'] == 'Male':
        gender = 'choloviki'
        await adidas_tshirt(size, gender)
    elif data['Gender'] == 'Female':
        gender = 'zhinki'
        await adidas_tshirt(size, gender)
    with open('result_adidas_tshirt.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for i in data:
        card = f'<b><a href="{i["Ссылка"]}">{i["Модель"]}</a></b>\n' \
               f'<b>Price:</b>{i["Цена"]}\n' \
               f'<b>Discounted price:</b>{i["Цена со скидкой"]}\n'
        await message.answer(card, parse_mode='HTML')
        await asyncio.sleep(1)
    await state.finish()




@dp.message_handler(state=Megasport_Form.Megasport_Sneakers_Size)
async def megasport_sneakers(message : types.Message , state : FSMContext):
    async with state.proxy() as data:
        data['Megasport_Sneakers_Size'] = message.text
    size = data['Megasport_Sneakers_Size']
    for k,v in size_json['megasport_sneakers'].items():
        if size == k:
            size=v
            print(size)
    await message.answer('Please waiting...')
    if data['Gender'] == 'Male':
        gender = 'male'
        await megasport_func(size , gender)
    elif data['Gender'] == 'Female':
        gender = 'female'
        await megasport_func(size , gender)
    with open('result_megasport_sneakers.json.', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for i in data:
        card = f'<b><a href="{i["url"]}">{i["title"]}</a></b>\n' \
               f'<b>Price:</b>{i["sale_price"]}\n' \
               f'<b>Discounted price:</b>{i["price"]}\n'
        await message.answer(card, parse_mode='HTML')
        await asyncio.sleep(1)
    await state.finish()



@dp.message_handler(state=Megasport_Form.Megasport_Tshirt_Size)
async def megasport_tshirts(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Megasport_Tshirt_Size'] = message.text
    size = data['Megasport_Tshirt_Size']
    await message.answer('Please waiting...')
    if data['Gender'] == 'Male':
        gender = 'male'
        await megasport_tshirt(size , gender)
    elif data['Gender'] == 'Female':
        gender = 'female'
        await megasport_tshirt(size , gender)
    with open('result_megasport_tshirt.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for i in data:
        card = f'<b><a href="{i["Ссылка"]}">{i["Модель"]}</a></b>\n' \
               f'<b>Price:</b>{i["Цена"]}\n' \
               f'<b>Discounted price:</b>{i["Цена со скидкой"]}\n'
        await message.answer(card, parse_mode='HTML')
        await asyncio.sleep(1)
    await state.finish()



@dp.message_handler(state=Megasport_Form.Megasport_Shorts_Size)
async def megasport_short(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Megasport_Shorts_Size'] = message.text
    size = data['Megasport_Shorts_Size']
    await message.answer('Please waiting...')
    if data['Gender'] == 'Male':
        gender = 'male'
        await megasport_shorts(size , gender)
    elif data['Gender'] == 'Female':
        gender = 'female'
        await megasport_shorts(size , gender)
    with open('result_megasport_shorts.json.', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for i in data:
        card = f'<b><a href="{i["Ссылка"]}">{i["Модель"]}</a></b>\n' \
               f'<b>Price:</b>{i["Цена"]}\n' \
               f'<b>Discounted price:</b>{i["Цена со скидкой"]}\n'
        await message.answer(card, parse_mode='HTML')
        await asyncio.sleep(1)
    await state.finish()


@dp.message_handler(state=Puma_Form.Puma_Shorts_Size)
async def pumaa_shorts(message : types.Message , state : FSMContext):
    async with state.proxy() as data:
        data['Puma_Shorts_Size'] = message.text
    size = data['Puma_Shorts_Size']
    for k,v in size_json['puma_shorts_tshirts'].items():
        if size == k:
            size=v
            print(size)
    await message.answer('Please waiting...')
    if data['Gender'] == 'Male':
        gender = 'sportivnye-tovary-dlja-muzhchin'
        await puma_shorts(size , gender)
    elif data['Gender'] == 'Female':
        gender = 'sportivnye-tovary-dlja-zhenshhin'
        await puma_shorts(size , gender)
    with open('result_puma_shorts.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for i in data:
        if i['Цена'] != '':
            card = f'<b><a href="{i["Ссылка"]}">{i["Модель"]}</a></b>\n' \
                   f'<b>Price:</b>{i["Цена"]}\n' \
                   f'<b>Discounted price:</b>{i["Цена со скидкой"]}\n'
        # card = f"Модель:{i.get('Модель')}" \
        #        f"Прайс:{i.get('Цена')}" \
        #        f"Прайс со скидкой:{i.get('Цена со скидкой')}" \
        #        f"Ссылка:{i.get('Ссылка')}"
            await message.answer(card, parse_mode='HTML')
            await asyncio.sleep(1)
    await state.finish()

@dp.message_handler(state=Puma_Form.Puma_Sneakers_Size)
async def pumaa_sneakers(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Puma_Sneakers_Size'] = message.text
    size = data['Puma_Sneakers_Size']
    for k,v in size_json['puma_sneakers'].items():
        if size == k:
            size=v
            print(size)
    await message.answer('Please waiting...')
    if data['Gender'] == 'Male':
        gender = 'sportivnye-tovary-dlja-muzhchin'
        await puma_sneakers(size , gender)
    elif data['Gender'] == 'Female':
        gender = 'sportivnye-tovary-dlja-zhenshhin'
        await puma_sneakers(size , gender)
    with open('result_puma_sneakers.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for i in data:
        if i['Цена'] != '':
            card = f'<b><a href="{i["Ссылка"]}">{i["Модель"]}</a></b>\n' \
                   f'<b>Price:</b>{i["Цена"]}\n' \
                   f'<b>Discounted price:</b>{i["Цена со скидкой"]}\n'
            # card = f"Модель:{i.get('Модель')}" \
            #        f"Прайс:{i.get('Цена')}" \
            #        f"Прайс со скидкой:{i.get('Цена со скидкой')}" \
            #        f"Ссылка:{i.get('Ссылка')}"
            await message.answer(card, parse_mode='HTML')
            await asyncio.sleep(1)
    await state.finish()



@dp.message_handler(state=Puma_Form.Puma_Tshirt_Size)
async def pumaa_tshirts(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Puma_Tshirt_Size'] = message.text
    size = data['Puma_Tshirt_Size']
    for k,v in size_json['puma_shorts_tshirts'].items():
        if size == k:
            size=v
            print(size)
    await message.answer('Please waiting...')
    if data['Gender'] == 'Male':
        gender = 'sportivnye-tovary-dlja-muzhchin'
        await puma_tshirts(size , gender)
    elif data['Gender'] == 'Female':
        gender = 'sportivnye-tovary-dlja-zhenshhin'
        await puma_tshirts(size , gender)
    with open('result_puma_tshirts.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for i in data:
        if i['Цена'] != '':
            card = f'<b><a href="{i["Ссылка"]}">{i["Модель"]}</a></b>\n' \
                   f'<b>Price:</b>{i["Цена"]}\n' \
                   f'<b>Discounted price:</b>{i["Цена со скидкой"]}\n'
        # card = f"Модель:{i.get('Модель')}" \
        #        f"Прайс:{i.get('Цена')}" \
        #        f"Прайс со скидкой:{i.get('Цена со скидкой')}" \
        #        f"Ссылка:{i.get('Ссылка')}"
            await message.answer(card, parse_mode='HTML')
            await asyncio.sleep(1)
    await state.finish()


                                                        # """Запуск телеграмм бота"""

def main():
    executor.start_polling(dp , skip_updates=True)


if __name__ == '__main__':
    main()

