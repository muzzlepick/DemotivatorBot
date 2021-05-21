from aiogram import Bot, Dispatcher, executor, types
import photo_editor

TOKEN = '1707165011:AAHHB-4FlY48-RpaVbjkovc2OsFKkuC-7vM'

try:
    bot = Bot(token= TOKEN)
    dp = Dispatcher(bot)

    @dp.message_handler(commands=['start'])
    async def start(message: types.Message):
        await bot.send_message(message.from_user.id, 'Отправь мне фото с подписью')

    @dp.message_handler(content_types=['photo'])
    async def photo(message):

        await message.photo[-1].download('pic/mem.jpg')      

        if message.caption:
            text = message.caption

            photo_editor.add_text(text)    
            await bot.send_photo(message.from_user.id, photo=open('pic/paste/ok.jpg', 'rb'))
        else:
            await bot.send_message(message.from_user.id, 'Ты забыл добавить подпись')

    if __name__ == '__main__':
        print('Бот успешно запущен')
        executor.start_polling(dp, skip_updates=True)
except:
    print('Вы забыли ввести токен\nЭто можно сделать в файле main.py')