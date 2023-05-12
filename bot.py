import logging

from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from buttons import *

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Tilni Tanlang!", reply_markup=til)


@dp.message_handler(text="🇺🇿 O'zbekcha")
async def echo(message: types.Message):
    await message.answer("Telefon raqamingizni yuboring...", reply_markup=raqam)


@dp.message_handler(content_types='contact')
async def echo(message: types.Message):
    await message.answer("Joylashuvni yuboring...", reply_markup=joylashuv)


@dp.message_handler(content_types='location')
async def echo(message: types.Message):
    await message.answer("Siz ro'yxatdan o'tdingiz\n\nKategoriyalardan birini tanlang!", reply_markup=pastki_menu)


@dp.message_handler(text="Buyurtma berish")
async def echo(message: types.Message):
    await message.answer("Marhamat menu: ", reply_markup=bosh_menu)


# inline function
@dp.callback_query_handler(text='lavash')
async def my_fuck(call: types.CallbackQuery):
    await call.message.answer('✅Marxamat lavashlar menusi!!!', reply_markup=lavash_menu)


# mol gushti uchun menu
@dp.callback_query_handler(text='molgush')
async def my_fuck(call: types.CallbackQuery):
    await call.message.answer('✅Kategoriyalardan birini tanlang!!!', reply_markup=lavash_menu_mini_class)


@dp.callback_query_handler(text='min')
async def my_fuck(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("img/lavash_mini.jpg", 'rb'),
        caption="""Narxi:18000 ming so'm 
Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup=lavash_menu_mini_class_raqamlar)




# ===========================================================================
# lavash back1
@dp.callback_query_handler(text='back1')
async def my_fuck(call: types.CallbackQuery):
   await call.message.answer("Marhamat menu: ", 
                             reply_markup=bosh_menu)
   

# lavash mol gushti back2
@dp.callback_query_handler(text='back2')
async def my_fuck(call: types.CallbackQuery):
   await call.message.answer('✅Marxamat lavashlar menusi!!!', 
                             reply_markup=lavash_menu)

# =================================================================================

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
