<h2>Телеграм бот с функцией валидации и бьютифаера JSON</h2>

> **Статус проекта:**
>
> 🟢 Поддерживается (активный) 

## Цели и Задачи
Помочь тестировщику быстрее проверить JSON на нарушение синтаксиса

Этот бот при получении JSON:
* Проверяет на ошибки синтаксиса и показывает, где они
* Возвращает JSON в удобочитаемом формате

## 🖼 Скриншоты

Стартовое меню:

<img width="1191" height="1026" alt="Image" src="https://github.com/user-attachments/assets/b636abdb-4f65-4eca-ba1f-064d22834513" />

После отправки JSON c ошибкой:

<img width="1188" height="1033" alt="Image" src="https://github.com/user-attachments/assets/312eaf6d-71bb-4aa7-8003-bf2b798122d3" />

Пример работы beautifier:

<img width="1189" height="1029" alt="Image" src="https://github.com/user-attachments/assets/8f1ad52a-3645-4631-b189-3a430dfd4238" />


## 💻 Технологии

* Python
* Библиотека `telebot`

## ⏬ Установка на локальном компьютере

1. Скачать проект
   
2. Создать бота и через [@BotFather](https://t.me/BotFather) и вставить в проекте свой токен от бота

3. Создаём виртуальное окружение внутри папки проекта.
Далее команды для MacOS (для windows инуструкция [есть вот тут](https://realpython.com/python-virtual-environments-a-primer/#create-it))

``` markdown
python3 -m venv venv
```

``` markdown
source venv/bin/activate
```
4. Устанавливаем библиотеки

``` markdown
python3 -m pip install pyTelegramBotAPI
```


5. Запускаем
``` markdown
python3 json_bot.py
```

## Автор

Иван Депутатов ([Telegram](https://t.me/IvanD_QA), [Email](mailto:deputatovivan272@gmail.com))
