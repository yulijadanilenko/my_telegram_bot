import json
import telebot
from apscheduler.schedulers.blocking import BlockingScheduler

# Читаем config.json
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

bot_token = config['bot_token']
groups = config['groups']
messages = config['messages']

bot = telebot.TeleBot(bot_token)
scheduler = BlockingScheduler()

def send_daily_tip():
    for group in groups:
        for message in messages:
            bot.send_message(group["id"], message["content"])

# Расписание — каждый день в 9:00
scheduler.add_job(send_daily_tip, 'cron', hour=9, minute=0)

print("Бот работает по расписанию...")
scheduler.start()
