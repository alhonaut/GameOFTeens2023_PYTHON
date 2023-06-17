import telebot
from telebot import types
import time

bot = telebot.TeleBot('6089567927:AAEEzAPFp-p56rrf936GZLZqGVaCUyqB6Rk')

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='ТАК🤩', callback_data='yes')
    button2 = types.InlineKeyboardButton(text='ні🤮', callback_data='no')
    markup.add(button1, button2)
    bot.send_message(message.chat.id, '*Привіт представник(-ця) Homosapiens!*\n\n'
                                      'Я ваш особистий цифровоий помічник. '
                                      'Моє завдання служити вам і зробити все, '
                                      'щоб ви знайшли для себе найкращий тариф🔥\n\n'
                                      'Ну що ж *готові*?',
                     reply_markup=markup,
                     parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: True)
def messages(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, 'Щоб знайти той самий тариф, які б підійшов вам, '
                                       'нам треба задати вам декілька питань')
        time.sleep(1)
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='ОДИН', callback_data='one')
        button2 = types.InlineKeyboardButton(text='ДЕКІЛЬКА', callback_data='many')
        markup.add(button1, button2)
        bot.send_message(call.message.chat.id, 'Ви шукаєте тариф для особистого користування на один пристрій, '
                                       'чи у вас декілька пристроїв, кожен з яких має бути з Інтернетом?📱',
                         reply_markup=markup)

    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'Жаль😥\n\n'
                                               'Надіюсь, що ви передумаєте і вернетесь до нас!')

    if call.data == 'one':
        markup2 = types.InlineKeyboardMarkup()
        button12 = types.InlineKeyboardButton(text='ТАК✔️', callback_data='yes1')
        button22 = types.InlineKeyboardButton(text='НІ❌', callback_data='no1')
        markup2.add(button12, button22)
        bot.send_message(call.message.chat.id, "Любите багато часу сидіти в мережі і завжди бути з друзями на зв'язку?📞",
                         reply_markup=markup2)

    elif call.data == 'many':
        markup2 = types.InlineKeyboardMarkup()
        button12 = types.InlineKeyboardButton(text='ПЕРЕЙТИ ДО ТАРИФУ', url='https://www.lifecell.ua/uk/mobilnij-zvyazok/gadget-series/')
        markup2.add(button12)
        bot.send_message(call.message.chat.id,
                         'Я думаю вам підійде цей тариф\n\n📱*Ґаджет*📱\n\nЦіна - *90 грн* / 12 тижні\n'
                         'Інтернет - від *150 МБ* до *безліміт*\n'
                         'Дзвінки - від *15 хв* до *50 хв*',
                         reply_markup=markup2,
                         parse_mode='Markdown')
        time.sleep(0.7)
        bot.send_message(call.message.chat.id,
                         'Надіюсь я зміг вам допомогти, і ви знайшли для себе ідеальний тариф.\n\n'
                         'Якщо вам треба буде знов вибрати тариф, то не переживайте, я завжди тут😉\n\n'
                         'Почати все заново - /start')

    if call.data == 'yes1':
        markup2 = types.InlineKeyboardMarkup()
        button12 = types.InlineKeyboardButton(text='ТАК✔️', callback_data='yes2')
        button22 = types.InlineKeyboardButton(text='НІ❌', callback_data='no2')
        markup2.add(button12, button22)
        bot.send_message(call.message.chat.id,
                         "Ви школяр або студент і не хочете, щоб мама не переживала про те, чи надагли ви шапку сьогодні чи ні, і хочете завжди бути з нею на зв'язку?",
                         reply_markup=markup2)

    elif call.data == 'no1':
        markup2 = types.InlineKeyboardMarkup()
        button12 = types.InlineKeyboardButton(text='ПЕРЕЙТИ ДО ТАРИФУ', url='http://pc.lifecell.ua/pc/perClickSso?locale=ua&accessKeyCode=20&serviceCode=IND_PRE_SIMPLE_2021&partnerCode=13&priceType=1&returnUrl=https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/prosto-life-2021/&type=TARIFF&signature=G39VN6Ua41L%2Fcnt3prssJdoJWuU%3D&_ga=2.7843890.1294304924.1686920698-1075078131.1686920698')
        markup2.add(button12)
        bot.send_message(call.message.chat.id,
                         'Я думаю вам підійде цей тариф\n\n🤙*Просто Лайф*🤙\n\nЦіна - *90 грн* / 4 тижні\n'
                         'Інтернет - *8 ГБ*\n'
                         'Дзвінки - *300 хв*',
                         reply_markup=markup2,
                         parse_mode='Markdown')
        time.sleep(0.7)
        bot.send_message(call.message.chat.id,
                         'Надіюсь я зміг вам допомогти, і ви знайшли для себе ідеальний тариф.\n\n'
                         'Якщо вам треба буде знов вибрати тариф, то не переживайте, я завжди тут😉\n\n'
                         'Почати все заново - /start')

    if call.data == 'yes2':
        markup2 = types.InlineKeyboardMarkup()
        button12 = types.InlineKeyboardButton(text='ПЕРЕЙТИ ДО ТАРИФУ',
                                              url='http://pc.lifecell.ua/pc/perClickSso?locale=ua&accessKeyCode=20&serviceCode=IND_PRE_SCHOOL&partnerCode=13&priceType=1&returnUrl=https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/shkilniy/&type=TARIFF&signature=lp0xsuJxxcD2GyXVO02FD0CTr5g%3D&_ga=2.110990085.1294304924.1686920698-1075078131.1686920698')
        markup2.add(button12)
        bot.send_message(call.message.chat.id,
                         'Я думаю вам підійде цей тариф\n\n💎*Шкільний Лайф*💎\n\nЦіна - *250 грн* / 4 тижні\n'
                         'Інтернет - *безліміт*\n'
                         'Дзвінки - *3000 хв*',
                         reply_markup=markup2,
                         parse_mode='Markdown')
        time.sleep(0.7)
        bot.send_message(call.message.chat.id,
                         'Надіюсь я зміг вам допомогти, і ви знайшли для себе ідеальний тариф.\n\n'
                         'Якщо вам треба буде знов вибрати тариф, то не переживайте, я завжди тут😉\n\n'
                         'Почати все заново - /start')

    elif call.data == 'no2':
        markup2 = types.InlineKeyboardMarkup()
        button12 = types.InlineKeyboardButton(text='ТАК✔️', callback_data='yes3')
        button22 = types.InlineKeyboardButton(text='НІ❌', callback_data='yes2') # ми повертаємся до шкільного тарифу, бо клієнт не закінчив школу
        markup2.add(button12, button22)
        bot.send_message(call.message.chat.id,
                         "Ви закінчили школу/бурсу/універ і тепер вам потрібен зв'язок для ваших справ?",
                         reply_markup=markup2)

    if call.data == 'yes3':
        markup2 = types.InlineKeyboardMarkup()
        button12 = types.InlineKeyboardButton(text='ТАК✔️', callback_data='yes4')
        button22 = types.InlineKeyboardButton(text='НІ❌', callback_data='no4')
        markup2.add(button12, button22)
        bot.send_message(call.message.chat.id,
                         "Ви вже обзавелись сім'єю і вам треба тримати зв'язок з ними?👨‍👩‍👦",
                         reply_markup=markup2)

    if call.data == 'yes4':
        markup2 = types.InlineKeyboardMarkup()
        button12 = types.InlineKeyboardButton(text='ПЕРЕЙТИ ДО ТАРИФУ',
                                              url='https://www.lifecell.ua/uk/mobilnij-zvyazok/smart-simya-series/')
        markup2.add(button12)
        bot.send_message(call.message.chat.id,
                         "Я думаю вам підійде цей тариф\n\n💎*Смарт Сім'я*💎\n\nЦіна - *375 грн* / 4 тижні\n"
                         'Інтернет - від *20 ГБ* до *50 ГБ*\n'
                         'Дзвінки - від *500 хв* до *1500 хв*',
                         reply_markup=markup2,
                         parse_mode='Markdown')
        time.sleep(0.7)
        bot.send_message(call.message.chat.id,
                         'Надіюсь я зміг вам допомогти, і ви знайшли для себе ідеальний тариф.\n\n'
                         'Якщо вам треба буде знов вибрати тариф, то не переживайте, я завжди тут😉\n\n'
                         'Почати все заново - /start')

    elif call.data == 'no4':
        markup2 = types.InlineKeyboardMarkup()
        button12 = types.InlineKeyboardButton(text='ТАК✔️', callback_data='yes5')
        button22 = types.InlineKeyboardButton(text='НІ❌', callback_data='no5')
        markup2.add(button12, button22)
        bot.send_message(call.message.chat.id,
                         'Ви не переймаєтесь за своє фінансове становище і бажаєте для себе тільки найкращого?🤑',
                         reply_markup=markup2)

    if call.data == 'yes5':
        markup2 = types.InlineKeyboardMarkup()
        button12 = types.InlineKeyboardButton(text='ПЕРЕЙТИ ДО ТАРИФУ',
                                              url='http://pc.lifecell.ua/pc/perClickSso?locale=ua&accessKeyCode=20&serviceCode=IND_PRE_PLATINUM_2021&partnerCode=13&priceType=1&returnUrl=https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/platinum-life-2021/&type=TARIFF&signature=ZGx4r10p8z44IY%2BRVpJmqLWRz88%3D&_ga=2.11497652.1294304924.1686920698-1075078131.1686920698')
        markup2.add(button12)
        bot.send_message(call.message.chat.id,
                         'Я думаю вам підійде цей тариф\n\n💎*Platinum Лайф*💎\n\nЦіна - *250 грн* / 4 тижні\n'
                         'Інтернет - *безліміт*\n'
                         'Дзвінки - *3000 хв*',
                         reply_markup=markup2,
                         parse_mode='Markdown')
        time.sleep(0.7)
        bot.send_message(call.message.chat.id,
                         'Надіюсь я зміг вам допомогти, і ви знайшли для себе ідеальний тариф.\n\n'
                         'Якщо вам треба буде знов вибрати тариф, то не переживайте, я завжди тут😉\n\n'
                         'Почати все заново - /start')

    elif call.data == 'no5':
        markup2 = types.InlineKeyboardMarkup()
        button12 = types.InlineKeyboardButton(text='ПЕРЕЙТИ ДО ТАРИФУ',
                                              url='http://pc.lifecell.ua/pc/perClickSso?locale=ua&accessKeyCode=20&serviceCode=IND_PRE_FREE_2021&partnerCode=13&priceType=1&returnUrl=https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-2021/&type=TARIFF&signature=2hQ%2BT4txRO8%2FIOZaE8QMaeYk%2FxY%3D&_ga=2.103717632.1294304924.1686920698-1075078131.1686920698')
        markup2.add(button12)
        bot.send_message(call.message.chat.id,
                         'Я думаю вам підійде цей тариф\n\n💎*Вільний Лайф*💎\n\nЦіна - *180 грн* / 4 тижні\n'
                         'Інтернет - *безліміт*\n'
                         'Дзвінки - *1600 хв*',
                         reply_markup=markup2,
                         parse_mode='Markdown')
        time.sleep(0.7)
        bot.send_message(call.message.chat.id,
                         'Надіюсь я зміг вам допомогти, і ви знайшли для себе ідеальний тариф.\n\n'
                         'Якщо вам треба буде знов вибрати тариф, то не переживайте, я завжди тут😉\n\n'
                         'Почати все заново - /start')

bot.polling(none_stop = True, interval = 0)
