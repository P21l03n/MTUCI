import telebot
from telebot import types
import datetime
import psycopg2

conn = psycopg2.connect(database="timetable_db",
                        user="Polina2",
                        password="12345",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()

token = "2105189954:AAEW9fRlWC9jU-gnAcnzE6G0vYQQZ-W5X-E"

bot = telebot.TeleBot(token)

now = datetime.datetime.now()
month = now.month
n_day = now.day

month -= 9
days = (30 * month + (month // 2) + n_day)
if days % 7 != 0:
    week = days // 7 + 1
else:
    week = days // 7


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Понедельник", "Вторник")
    keyboard.row("Среда", "Четверг", "Пятница")
    keyboard.row("Расписание на текущую неделю")
    keyboard.row("Расписание на следующую неделю")
    bot.send_message(message.chat.id,
                     'Здравствуйте! Этот бот поможет вам узнать актуальное расписание. Напишите /help, чтобы узнать подробности.',
                     reply_markup=keyboard)


def days_timetable(n):
    n = str(n)
    a = []
    cursor.execute("SELECT day, subject, room_numb, start_time FROM timetable.timetable ")
    records = list(cursor.fetchall())
    for i in range(len(records)):
        if records[i][0] == n:
            a.append(records[i])
    message = '\n'
    for i in range(len(a)):
        cursor.execute("SELECT full_name, subject FROM timetable.teacher")
        records1 = list(cursor.fetchall())
        for j in range(len(records1)):
            if a[i][1] == records1[j][1]:
                line = str(i + 1) + '. ' + a[i][1] + ', ауд. ' + a[i][2] + ' <' + a[i][3] + '> ' + records1[j][0] + '\n'
                message += line
    if message == '\n':
        message += '$ CHILL $'
    return message


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'С помощью этого бота вы можете:\n'
                                      '/week - узнать четность текущей недели\n'
                                      '/mtuci - получить ссылку на официальный сайт МТУСИ\n'
                                      'Узнать расписание (с помощью кнопок на клавиатуре)')


@bot.message_handler(commands=['week'])
def week_(message):
    if week % 2 == 0:
        bot.send_message(message.chat.id, 'Сейчас нижняя неделя')
    else:
        bot.send_message(message.chat.id, 'Сейчас верхняя неделя')


@bot.message_handler(commands=['mtuci'])
def select_fairy(message):
    bot.send_message(message.chat.id, 'Официальный сайт МТУСИ - https://mtuci.ru/')


@bot.message_handler(content_types=['text'])
def timetable(message):
    if message.text == 'Понедельник':
        n_day = 'Понедельник'
        bot.send_message(message.chat.id, 'Понедельник ' + days_timetable(n_day))
    elif message.text == 'Вторник':
        if week % 2 == 0:
            n_day = 'Вторник_2'
        else:
            n_day = 'Вторник_1'
        bot.send_message(message.chat.id, 'Вторник ' + days_timetable(n_day))
    elif message.text == 'Среда':
        if week % 2 == 0:
            n_day = 'Среда_2'
        else:
            n_day = 'Среда_1'
        bot.send_message(message.chat.id, 'Среда ' + days_timetable(n_day))
    elif message.text == 'Четверг':
        if week % 2 == 0:
            n_day = 'Четверг_2'
        else:
            n_day = 'Четверг_1'
        bot.send_message(message.chat.id, 'Четверг ' + days_timetable(n_day))
    elif message.text == 'Пятница':
        n_day = 'Пятница'
        bot.send_message(message.chat.id, 'Пятница ' + days_timetable(n_day))
    elif message.text == 'Расписание на текущую неделю':
        bot.send_message(message.chat.id, 'Понедельник ' + days_timetable('Понедельник'))
        if week % 2 == 0:
            bot.send_message(message.chat.id, 'Вторник ' + days_timetable('Вторник_2'))
            bot.send_message(message.chat.id, 'Среда ' + days_timetable('Среда_2'))
            bot.send_message(message.chat.id, 'Четверг ' + days_timetable('Четверг_2'))
        else:
            bot.send_message(message.chat.id, 'Вторник ' + days_timetable('Вторник_1'))
            bot.send_message(message.chat.id, 'Среда ' + days_timetable('Среда_1'))
            bot.send_message(message.chat.id, 'Четверг ' + days_timetable('Четверг_1'))
        bot.send_message(message.chat.id, 'Пятница ' + days_timetable('Пятница'))
    elif message.text == 'Расписание на следующую неделю':
        bot.send_message(message.chat.id, 'Понедельник ' + days_timetable('Понедельник'))
        if week % 2 == 0:
            bot.send_message(message.chat.id, 'Вторник ' + days_timetable('Вторник_1'))
            bot.send_message(message.chat.id, 'Среда ' + days_timetable('Среда_1'))
            bot.send_message(message.chat.id, 'Четверг ' + days_timetable('Четверг_1'))
        else:
            bot.send_message(message.chat.id, 'Вторник ' + days_timetable('Вторник_2'))
            bot.send_message(message.chat.id, 'Среда ' + days_timetable('Среда_2'))
            bot.send_message(message.chat.id, 'Четверг ' + days_timetable('Четверг_2'))
        bot.send_message(message.chat.id, 'Пятница ' + days_timetable('Пятница'))
    elif message.text != 'Понедельник' and message.text != 'Вторник' and message.text != 'Среда' and message.text != 'Четверг' and message.text != 'Пятница' and message.text != 'Расписание на текущую неделю' and message.text != 'Расписание на следующую неделю' and message.text != '/start' and message.text != '/help' and message.text != '/week' and message.text != '/mtuci':
        bot.send_message(message.chat.id, 'Извините, я Вас не понял')


bot.polling()
