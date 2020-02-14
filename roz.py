#New Bot Розклад

import telebot
import parser

#main variables
TOKEN = "TOKEN"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'go', 's'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, я помощник /Th1rd-Player и могу сказать какой у тебя расклад занятий на сегодня!!!')
    bot.send_message(message.chat.id, 'Просто введи /help')
@bot.message_handler(commands=['Th1rd-Player', 'TP'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Решил осмотреть что это за команда а ты не такой и тупой как я думал я Каин создатель этого бота!!!')

@bot.message_handler(commands=['Monday', 'monday', 'mon'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Понеділок')
    bot.send_message(message.chat.id, '1)Україньська література - 23')
    bot.send_message(message.chat.id, '2)Україньська мова - 23')
    bot.send_message(message.chat.id, '3)Фізична культура- 29')
    bot.send_message(message.chat.id, '4)Алгебра - 8')
    bot.send_message(message.chat.id, '5)Географія, Історія україни - 5')
    bot.send_message(message.chat.id, '6)Інформатика - 26')
    bot.send_message(message.chat.id, '7)Всесвітня історія - 23')
@bot.message_handler(commands=['Tuesday', 'tuesday', 'tue'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Вівторок')
    bot.send_message(message.chat.id, '1)Фізика - 2')
    bot.send_message(message.chat.id, '2)Історія україни - 9')
    bot.send_message(message.chat.id, '3)Хімія - 12')
    bot.send_message(message.chat.id, '4)Англійська мова - 30')
    bot.send_message(message.chat.id, '5)Геометрія - 8')
    bot.send_message(message.chat.id, '6)Фізична культура - 29')
    bot.send_message(message.chat.id, '7)Інформатика - 26')

@bot.message_handler(commands=['Wednesday', 'wednesday', 'wed'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Середа')
    bot.send_message(message.chat.id, '1)Фізика - 2')
    bot.send_message(message.chat.id, '2)Біологія - 17')
    bot.send_message(message.chat.id, '3)Англійська мова - 27')
    bot.send_message(message.chat.id, '4)Право знавство - 4')
    bot.send_message(message.chat.id, '5)Основи здоров`я - 2')
    bot.send_message(message.chat.id, '6)Хімія - 10')

@bot.message_handler(commands=['Thursday', 'thursday', 'thu'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Четверг')
    bot.send_message(message.chat.id, '1)Англійська мова - 11')
    bot.send_message(message.chat.id, '2)Алгебра - 8')
    bot.send_message(message.chat.id, '3)Географія - 5')
    bot.send_message(message.chat.id, '4)Фізична культура - 29')
    bot.send_message(message.chat.id, '5)Фізика - 2')
    bot.send_message(message.chat.id, '6)Зарубіжна література - 4')
    bot.send_message(message.chat.id, '7)Праця - майстерня/9')

@bot.message_handler(commands=['Friday', 'friday', 'fri'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Пятниця')
    bot.send_message(message.chat.id, '1)Україньська - 12')
    bot.send_message(message.chat.id, '2)Україньська - 12')
    bot.send_message(message.chat.id, '3)Зарубіжна - 11')
    bot.send_message(message.chat.id, '4)Геометрія - 8')
    bot.send_message(message.chat.id, '5)Біологія - 17')
    bot.send_message(message.chat.id, '6)Мистецтво - 4')

@bot.message_handler(commands=['Saturday', 'saturday', 'sat'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Гуляй, страдай хернёй, если у тебя есть друзья зови их к себе проведи это время вместе с людьми с которыми тебе легко и весело! Вить знай есть люди у которых нету реальных друзей!! Но если ты хочешь быть успешным  и не жить как рядовой житель со дня в день ходить на роботу, готовить, а вечером засиживаться до позна за тупым сериалом  и повторять это каждый божий день то оставь хоть чуточку времени на саморазвития и нет домашня работа не саморазвитие. Саморазвивайся в ту сторону в которую ты хочешь учи не то что хотят твои родители а то что тебе нравиться и в один прекрасный день ты будешь вспоминать как ты проводил время с теми кто тебя любил кто не предал тебя до сих пор!!! ')
    bot.send_message(message.chat.id, 'Жизнь, как програмный код в какойто игре на первый взгляд всё идеально но в самый неожиданый момент случается баг который не пофиксить- Th1rd-Player')

@bot.message_handler(commands=['Sunday', 'sunday', 'sun'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Создатель проекта Th1rd-Player Каин и Алексей Марущак')

@bot.message_handler(commands=['Help', 'help', 'h'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Розклад занять!!!')
    bot.send_message(message.chat.id, 'Понеділок - /monday')
    bot.send_message(message.chat.id, 'Вівторок  - /tuesday')
    bot.send_message(message.chat.id, 'Середа    - /wednesday')
    bot.send_message(message.chat.id, 'Четверг   - /thursday')
    bot.send_message(message.chat.id, 'Пятниця   - /friday')


bot.polling()