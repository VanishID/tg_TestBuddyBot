# Для подключение библиотеки telebot нужно в google colab добавить: !pip install pyTelegramBotAPI
from telebot import TeleBot, types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup  # <-- новый импорт
import json

bot = TeleBot(token='Твой токен', parse_mode='html')  # подставь свой токен

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    
    bot.send_message(
        chat_id=message.chat.id,
        text='Привет! 👋'
    )

    # 👇 СОЗДАЁМ ДВЕ КНОПКИ-ССЫЛКИ
    keyboard = InlineKeyboardMarkup()
    btn_repo = InlineKeyboardButton(
        text='🔗 Мой репозиторий',
        url='https://github.com/твой-репозиторий'  
    )
    btn_tg = InlineKeyboardButton(
        text='💬 Написать мне в личку',
        url='https://t.me/твой_ник'               
    )
    keyboard.add(btn_repo, btn_tg)  # кнопки в один ряд
    # Или можно по одной в ряду:
    # keyboard.row(btn_repo)
    # keyboard.row(btn_tg)

    # 👇 ВТОРОЕ СООБЩЕНИЕ – С КНОПКАМИ
    bot.send_message(
        chat_id=message.chat.id,
        text='Я умею проверять JSON и форматировать его в красивый текст\nВведи JSON в виде строки!',
        reply_markup=keyboard   # <-- вот здесь добавляем клавиатуру
    )

# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    try:
        payload = json.loads(message.text)
    except json.JSONDecodeError as ex:
        bot.send_message(
            chat_id=message.chat.id,
            text=f'При обработке произошла ошибка:\n<code>{str(ex)}</code>'
        )
        return

    text = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'JSON:\n<code>{text}</code>'
    )

# главная функция программы
def main():
    bot.infinity_polling()

if __name__ == '__main__':
    main()