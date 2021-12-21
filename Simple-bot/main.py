import telebot
from telebot import types


token = "2120913911:AAHQtWZffrnKmL7oiDIbsSrjsnhEajkHpLA"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/MTUCI", "/help","/Факультеты", "/Адреса", "/Творчество")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я расскажу тебе всю главную информацию О МТУСИ. Выбери о чем ты хочешь узнать.')


@bot.message_handler(commands=['MTUCI'])
def answer1(message):
    bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')

@bot.message_handler(commands=['Факультеты'])
def answer2(message):
    bot.send_message(message.chat.id, 'Напиши название факультета, о котором ты хочешь узнать')

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if message.text == "Сети и Системы Связи" or message.text == "СиСС":
            bot.send_message(message.from_user.id, "Декан - Мироноав Юрий Борисович")
            bot.send_message(message.from_user.id, "Тел. 8(495)957-79-22")
            bot.send_message(message.from_user.id, "Почта: mes@mtuci.ru")
            bot.send_message(message.from_user.id, "https://mtuci.ru/about_the_university/departments/306/")

        if message.text == "Цифровая Экономика и Массовые Коммуникации" or message.text == "ЦЭиМК":
            bot.send_message(message.from_user.id, "Декан - Кухаренко Елена Геннадьевна")
            bot.send_message(message.from_user.id, "Тел. 8(499)192-86-57, 8(499)192-85-00")
            bot.send_message(message.from_user.id, "Почта: feu@mtuci.ru")
            bot.send_message(message.from_user.id, "https://mtuci.ru/about_the_university/departments/307/")

        if message.text == "Информационные технологии" or message.text == "ИТ":
            bot.send_message(message.from_user.id, "Декан - Городничев Михаил Геннадьевич")
            bot.send_message(message.from_user.id, "Тел. 8(495)957-78-13, 8(495)957-78-20")
            bot.send_message(message.from_user.id, "Почта: it@mtuci.ru")
            bot.send_message(message.from_user.id, "https://mtuci.ru/about_the_university/departments/304/")

        if message.text == "Кибернетика и Информационная безопасность" or message.text == "КиИБ":
            bot.send_message(message.from_user.id, "Декан - Иевлев Олег Павлович")
            bot.send_message(message.from_user.id, "Тел. 8(495)957-78-13, 8(495)957-78-20")
            bot.send_message(message.from_user.id, "Почта: kib@mtuci.ru")
            bot.send_message(message.from_user.id, "https://mtuci.ru/about_the_university/departments/2444/")

        if message.text == "Радио и Телевидение" or message.text == "РиТ":
            bot.send_message(message.from_user.id, "Декан - Тауфик Бен Режеб")
            bot.send_message(message.from_user.id, "Тел. 8(495)957-79-27")
            bot.send_message(message.from_user.id, "Почта: rit@mtuci.ru")
            bot.send_message(message.from_user.id, "https://mtuci.ru/about_the_university/departments/306/")

@bot.message_handler(commands=['Адреса'])
def answer3(message):
    bot.send_message(message.chat.id, 'Напиши название отдела, о котором ты хочешь узнать. У нас есть:')
    bot.send_message(message.chat.id, 'Жилищно-коммунальный отдел')
    bot.send_message(message.chat.id, 'Отдел по воспитательной работе(ОВР)')
    bot.send_message(message.chat.id, 'Отдел кадров')
    bot.send_message(message.chat.id, 'Профком')

    @bot.message_handler(content_types=['text'])
    def get_text_messages2(message):
        if message.text == "Жилищно-коммунальный отдел":
            bot.send_message(message.from_user.id, "Адрес: ул.Авиамоторная 8А, А-303")
            bot.send_message(message.from_user.id, "Тел. 8(495)957-77-29")
            bot.send_message(message.from_user.id, "Почта: t.a.novikova@mtuci.ru")

        if message.text == "Отдел по воспитательной работе" or message.text == "ОВР":
            bot.send_message(message.from_user.id, "Адрес: ул.Авиамоторная 8А, А-233")
            bot.send_message(message.from_user.id, "Тел. 8(495)957-78-94")
            bot.send_message(message.from_user.id, "Почта: ovr@mtuci.ru")

        if message.text == "Отдел кадров":
            bot.send_message(message.from_user.id, "Адрес: ул.Авиамоторная 8А, А-265")
            bot.send_message(message.from_user.id, "Тел. 8(495)957-79-34")
            bot.send_message(message.from_user.id, "Почта: d.a.kalinina@mtuci.ru")
            bot.send_message(message.from_user.id, "Приемные дни: понедельник и среда")

        if message.text == "Профком":
            bot.send_message(message.from_user.id, "Декан - Иевлев Олег Павлович")
            bot.send_message(message.from_user.id, "Тел. 8(495)957-79-05")
            bot.send_message(message.from_user.id, "Почта: profkom@mtuci.ru")


@bot.message_handler(commands=['Творчество'])
def answer4(message):
    bot.send_message(message.chat.id, 'В нашем университете много творческих студий!'
                                      'И можешь стать их участником!')
    bot.send_message(message.chat.id, '-Территория творчества – руководитель Анна Анохина')
    bot.send_message(message.chat.id, '-Вокальная студия – руководитель Ирина Епифанова')
    bot.send_message(message.chat.id, '-Хореографическая студия – руководитель Мария Львова')
    bot.send_message(message.chat.id, '-Студенческая лига КВН “На связи МТУСИ” – редактор Святослав Скворцов')

bot.polling()