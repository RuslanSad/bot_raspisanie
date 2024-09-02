from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я буду вам скидывать расписание.')


async def raspisanie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    today = datetime.now()
    week_number = today.isocalendar()[1]
    if week_number % 2 == 0:
        week_description = "Красная"
    else:
        week_description = "Синяя"
    day_of_week = today.strftime("%A")
    schedule_text = ''
    if day_of_week == 'Monday':
        schedule_text = f"""Расписание на Вторник:\n{week_description} неделя
        1. -
        2. 10:15-11:50 | История России(лек) | <a href="https://yandex.ru/maps/-/CDwf785n">Хт-132</a>
        3. 10:15-11:50 | История России(лек) | <a href="https://yandex.ru/maps/-/CDwjAYM0">Хт-132</a>
        4. 10:15-11:50 | История России(лек) | Хт-132
        5. 10:15-11:50 | История России(лек) | Хт-132
        6. 10:15-11:50 | История России(лек) | Хт-132
        """
    elif day_of_week == 'Tuesday':
        schedule_text = f"""Расписание на Среду:\n{week_description} неделя
        1. -
        2. 10:15-11:50 | История России(лек) | Хт-132
        3. 10:15-11:50 | История России(лек) | Хт-132
        4. 10:15-11:50 | История России(лек) | Хт-132
        5. 10:15-11:50 | История России(лек) | Хт-132
        6. 10:15-11:50 | История России(лек) | Хт-132
        """
    elif day_of_week == 'Wednesday':
        schedule_text = f"""Расписание на Четверг:\n{week_description} неделя
        1. -
        2. 10:15-11:50 | История России(лек) | Хт-132
        3. 10:15-11:50 | История России(лек) | Хт-132
        4. 10:15-11:50 | История России(лек) | Хт-132
        5. 10:15-11:50 | История России(лек) | Хт-132
        6. 10:15-11:50 | История России(лек) | Хт-132
        """
    elif day_of_week == 'Thursday':
        schedule_text = f"""Расписание на Пятницу:\n{week_description} неделя
        1. -
        2. 10:15-11:50 | История России(лек) | Хт-132
        3. 10:15-11:50 | История России(лек) | Хт-132
        4. 10:15-11:50 | История России(лек) | Хт-132
        5. 10:15-11:50 | История России(лек) | Хт-132
        6. 10:15-11:50 | История России(лек) | Хт-132
        """
    else:
        schedule_text = f"""Расписание на Понедельник:\n{week_description} неделя
        1. -
        2. 10:15-11:50 | История России(лек) | Хт-132
        3. 10:15-11:50 | История России(лек) | Хт-132
        4. 10:15-11:50 | История России(лек) | Хт-132
        5. 10:15-11:50 | История России(лек) | Хт-132
        6. 10:15-11:50 | История России(лек) | Хт-132
        """
    await update.message.reply_text(schedule_text, parse_mode='HTML')


if __name__ == '__main__':
    application = ApplicationBuilder().token('7482905333:AAGxcbHnucIczwgSgBUid6Rb6FSlIrXaYJk').build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("raspisanie", raspisanie))  # Изменил имя команды на raspisanie
    application.run_polling()
