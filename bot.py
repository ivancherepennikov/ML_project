import telebot
from telebot import types
from main import main
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['photo'])
def score(message: types.Message):
    file_id = message.photo[-1].file_id 
    file_info = bot.get_file(file_id)
    downloaded = bot.download_file(file_info.file_path)

    input_photo_path = "input.jpg"
    with open(input_photo_path, "wb") as new_file:
        new_file.write(downloaded)

    result = main(input_photo_path)

    bot.send_message(message.chat.id, f"Результат: {result}")


if __name__ == "__main__":
    bot.polling(non_stop=True)

