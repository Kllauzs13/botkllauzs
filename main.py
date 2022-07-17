import telebot
from functions import main_request, results

# Creating bot 
TOKEN = '5594306116:AAHqWyrgnw95qFNAb_ZNHLfrXKf6PhoO_6Q'
bot = telebot.TeleBot(TOKEN, parse_mode=None)



@bot.message_handler(commands=['resultado'])
def send_stats(message):
    a = results()
    string = f'''Wins: {a['wins']} \nErros: {a['losses']} \nPrimeira tentativa: {a['prim_tent']} \nPrimeira gale: {a['prim_gale']} \nSegunda gale: {a['seg_gale']} \nWinrate: {a['porcentagem']}'''
    bot.reply_to(message, text=string)

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message('894633998', '\U0001f4c8 \U0001f4c8 LIGANDO ROBO DO KLLAUZS \U0001f4c8 \U0001f4c8')
    main_request(bot)

bot.infinity_polling()
