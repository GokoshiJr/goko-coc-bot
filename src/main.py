import telegram, handlers, keys
from telegram.ext import Updater, CommandHandler
from goko_bot import GokoBot

if __name__ == "__main__": 
  # Initialize the bot
  bot = telegram.Bot(keys.BOT_TOKEN)  
  print(GokoBot(bot.get_me()))

  # updater - to listen de user request 
  updater = Updater(token=keys.BOT_TOKEN, use_context=True)

  # get the dispatcher to register handlers
  dispatcher = updater.dispatcher

  # on different commands - answer in Telegram
  dispatcher.add_handler(CommandHandler("start", handlers.start))
  dispatcher.add_handler(CommandHandler("commands", handlers.commands)) 
  dispatcher.add_handler(CommandHandler("dev", handlers.dev_social)) 
  dispatcher.add_handler(CommandHandler("balance", handlers.balance))
  dispatcher.add_handler(CommandHandler("war", handlers.war))

  # start the Bot
  updater.start_polling() # verifica si esta recibiendo mensajes
  updater.idle() # terminar bot ctrl + c
