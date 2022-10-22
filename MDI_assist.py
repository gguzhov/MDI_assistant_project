import telebot
from telebot import types
from telebot.types import ReplyKeyboardRemove


def check(message):
    ans = 0
    if message.text == "✍🏼 academic writing":
        ans = 0
    if message.text == "🖥 programming in Python":
        ans = 1
    if message.text == "🧮 financial & organizational accounting":
        ans = 2
    if message.text == "📊 probability theory & mathematical statistics":
        ans = 3
    if message.text == "🗣 business communications":
        ans = 4
    if message.text == "⌨ data management in database design":
        ans = 5
    return ans


if __name__ == "__main__":
    token = '5755529888:AAEiqE0ANV7JaiK7V_aycKE2KCnLMmzAhHM'

    ad_as = ["✍🏼 academic writing \n\
    length: 1st module \n\
    senior lecturer: Zaharova Anna Viktorovna \n\
    email: annazakharova@hse.ru\n\
    evaluation formula: (test)*0.25 + (hw)*0.25 + (self-study)*0.25 + (exam)*0.25\n\
    chat: no chat \n\
    course link: Academic Writing (2022/2023 modules: 1) — Smart LMS (https://smartedu.hse.ru/course/0/135618)\n\
    grades link: \n\
    MDI-211: https://docs.google.com/spreadsheets/d/1-JMtndPbL5VTA0vD1rPtkHgWdCO9j2ZplQpmqzTPiP4/edit#gid=0 (https://docs.google.com/spreadsheets/d/1-JMtndPbL5VTA0vD1rPtkHgWdCO9j2ZplQpmqzTPiP4/edit#gid=0%C2%A0) \n\
    MDI-212: https://docs.google.com/spreadsheets/d/13uusB-tnLbMVTD4VrhSmeei6i126eC6PWODZR36gH_Q/edit#gid=0 (https://docs.google.com/spreadsheets/d/13uusB-tnLbMVTD4VrhSmeei6i126eC6PWODZR36gH_Q/edit#gid=0%C2%A0) \n\
    MDI-213: https://docs.google.com/spreadsheets/d/1RnU4YLIEaxMGJPeaVWvtRWO76tNQy08qUZ2YcDv-O90/edit#gid=0",

             "🖥️ programming in Python \n\
           length: 1st module \n\
           lecturer 1: Bugaevskiy Vladimir Mikhailovich\n\
           email: vbugaevskiy@hse.ru\n\
           lecturer 2: Strakhov Alexander Mikhailovich\n\
           email: astrakhov@hse.ru\n\
           evaluation formula: (final exam)*0.3 + (workshop activity)*0.1 + (team project)*0.1 + (quiz)*0.3 + (hw)*0.2 \n\
           chat: https://vk.me/join/8vJ1hix49FyRh_ER9DQB8qiGG/UTwLSQ5T4= \n\
           course link: https://www.hse.ru/ba/digital/courses",

             "🧮 financial & organizational accounting \n\
           length: 1st, 2nd modules\n\
           senior lecturer 1: Kondrahina Olesya Sergeevna \n\
           email: okondrahina@hse.ru\n\
           senior lecturer 2: Shurchkova Tatiana Sergeevna \n\
           email: tshurchkova@hse.ru\n\
           evaluation formula: (test)*0.05 + (hw)*0.15 + (class participation)*0.05 + (midterm exam)*0.25 + (winter exam)*0.4+(case study)*0.1 \n\
           chat: https://t.me/+xpIKYg9VJ1s4NjE6\n\
           course link: Financial and Organizational Accounting (2022/2023 modules: 1,2) — Smart LMS (https://smartedu.hse.ru/course/0/122926)",

             "📊 probability theory & mathematical statistics \n\
           length: 1st module \n\
           lecturer: Gladkova Margarita Anatolievna \n\
           email: mgladkova@hse.ru\n\
           seminar professor: Karpov Gleb Alexandrovich \n\
           email: gkarpov@hse.ru\n\
           evaluation formula: (exam)*0.5 + (hw)*0.25 + (test)*0.15 + (quizzes)*0.1 \n\
           course link: Probability Theory and Mathematical Statistics (2022/2023 modules: 1) — Smart LMS (https://smartedu.hse.ru/course/0/120672)\n\
           grades link: https://docs.google.com/spreadsheets/d/1BHXxWMpAEyYfeYyGmWMaNuVViIvNW3kc/edit#gid=568922885",

             "🗣️ business communications\n\
           length: 1st module\n\
           lecturer: Shahrour Madi Farrukhovich\n\
           tg: @shakhrur \n\
           evaluation formula: (exam)*0.8 + (individual assignment)*0.2 \n\
           chat: no chat \n\
           course link: Business Communications (2022/2023 modules: 1) — Smart LMS (https://smartedu.hse.ru/course/0/128840)",

             "⌨️ data management in database design \n\
           length: 1st module\n\
           lecturer 1: Neklyudov Dmitriy Yurievich\n\
           email: dyuneklyudov@hse.ru\n\
           lecturer 2:  Volpe Mikhail Borisovich \n\
           email: mbvolpe@hse.ru\n\
           lecturer 3: Gomenyuk Kirill Sergeevich \n\
           email: kgomenyuk@hse.ru\n\
           evaluation formula: (activity)*0.3 + (hw)*0.4 + (exam)*0.3 \n\
           course link: Database design 2Y MDI (https://canvas.instructure.com/courses/5225007) "]

    bot = telebot.TeleBot(token)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    stop_b = types.KeyboardButton('/Stop')
    but1 = types.KeyboardButton("✍🏼 academic writing")
    but2 = types.KeyboardButton("🖥️ programming in Python")
    markup.row(but1, but2)
    but3 = types.KeyboardButton("🧮 financial & organizational accounting")
    but4 = types.KeyboardButton("📊 probability theory & mathematical statistics")
    markup.add(but3, but4)
    but5 = types.KeyboardButton("🗣️ business communications")
    but6 = types.KeyboardButton("⌨️ data management in database design")
    markup.add(but5, but6)
    markup.add(stop_b)


    @bot.message_handler(commands=['start'])
    def button_message(message):
        bot.send_message(message.chat.id,
                         'HI, dear MDI student 👩🏼‍🎓👨🏼‍🎓 I’m your personal assistant\n'
                         'Write /disciplines to see information about the subject')


    @bot.message_handler(commands=['Stop'])
    def button_message(message):
        bot.send_message(message.chat.id, 'Have a nice day, to return write "/start"',
                         reply_markup=ReplyKeyboardRemove())


    @bot.message_handler(content_types='text')
    def message_reply(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        stop_b = types.KeyboardButton('/Stop')
        but1 = types.KeyboardButton("✍🏼 academic writing")
        but2 = types.KeyboardButton("🖥️ programming in Python")
        markup.row(but1, but2)
        but3 = types.KeyboardButton("🧮 financial & organizational accounting")
        but4 = types.KeyboardButton("📊 probability theory & mathematical statistics")
        markup.add(but3, but4)
        but5 = types.KeyboardButton("🗣️ business communications")
        but6 = types.KeyboardButton("⌨️ data management in database design")
        markup.add(but5, but6)
        markup.add(stop_b)
        if message.text != "/disciplines":
            bot.send_message(message.chat.id, ad_as[check(message)])
        bot.send_message(message.chat.id, 'Please, choose a discipline', reply_markup=markup)

    bot.polling(none_stop=True)
