from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from selenium.webdriver.common.by import By
from selenium import webdriver
import for_sql
import mysql.connector as mysql


storage = MemoryStorage()

bot = Bot(token="6047869714:AAHeLQi8_L2_gZSmWyfB7bo6dyTRiA4tRH8")
dp = Dispatcher(bot, storage=storage)


class FSMAdmin(StatesGroup):
    photo1 = State()
    number_all = State()
    name = State()
    name1 = State()
    price = State()

@dp.message_handler(commands="nimda", state=None)
async def admin_start(message: types.Message):
    await FSMAdmin.photo1.set()
    await message.reply("Download photo")

@dp.message_handler(commands=["123"])
async def command_start(message: types.message):
    db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Arsen121",
    database = "pordz2"
)

    cur = db.cursor()
    cur.execute("SELECT * FROM example1")
    print(cur.fetchall())
    await bot.send_message(message.from_user.id, "Ynreq filtr")


@dp.message_handler(content_types=["photo"], state=FSMAdmin.photo1)
async def load_photo(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data["photo1"] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply("Download number_all")

@dp.message_handler(state=FSMAdmin.number_all)
async def load_number_all(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["number_all"] = message.text
    await FSMAdmin.next()
    await message.reply("name")

@dp.message_handler(state=FSMAdmin.name)
async def load_taracq(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await FSMAdmin.next()
    await message.reply("name")

@dp.message_handler(state=FSMAdmin.name1)
async def load_taracq(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name1"] = message.text
    await FSMAdmin.next()
    await message.reply("price")


@dp.message_handler(state=FSMAdmin.price)
async def load_taracq(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["price"] = message.text
        for_sql.upload(data)
    await state.finish()
    await bot.send_message(message.from_user.id, "All is good! Product saved!")


@dp.message_handler()
async def example(message: types.Message):
    if message.text == "1":   
        browser = webdriver.Firefox()
        browser.get(f"https://list.am")
        date_code = browser.find_elements(By.XPATH,"/html/body/div[2]/div[2]/div/div[7]/a")
        date_code = f"{date_code[0].text}"
        print(date_code)
    else:
        pass



executor.start_polling(dp, skip_updates=True)