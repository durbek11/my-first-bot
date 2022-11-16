import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5663234765:AAEmtX9IV0lfxI8s1OxYDOV9Skpq4gC-i1w'
wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Wikipedia Botiga Xush Kelibsiz! Biz Oraqali O`zinggiz Uchun Kerakli Ma`lumotlarni Olishingiz Mumkun. Bizni Tanlaganingizdan hursand Bo`lib Qolamiz😊!")



@dp.message_handler()
async def Wikipedia(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await  message.answer("Afsuski Bu Mavzuga Aloqador Xech Narsa Topilmadi🙁. Berilgan Malumotni Qaytadan Tekshirib Ko`ring. ")    

    


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)