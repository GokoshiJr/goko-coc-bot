import telegram, handlers, keys
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters
from goko_bot import GokoBot, SLASH

if __name__ == "__main__": 
  # Initialize the bot
  bot = telegram.Bot(keys.BOT_TOKEN)  
  print(GokoBot(bot.get_me()))

  # Set bot rules
  bot.set_my_commands(commands=SLASH)

  # updater - to listen de user request 
  updater = Updater(token=keys.BOT_TOKEN, use_context=True)

  # get the dispatcher to register handlers
  dispatcher = updater.dispatcher

  # handlers
  dispatcher.add_handler(CommandHandler("start", handlers.start))
  dispatcher.add_handler(CommandHandler("commands", handlers.commands)) 
  dispatcher.add_handler(CommandHandler("dev", handlers.dev_social))
  dispatcher.add_handler(CommandHandler("cwl", handlers.cwl_rules))

  # conversations handlers - callbacks 
  dispatcher.add_handler(ConversationHandler(
    entry_points=[
      CommandHandler("balance", handlers.balance),
      CallbackQueryHandler(pattern="LatinosArmy", callback=handlers.callback_balance)],
    states={},
    fallbacks=[],
  ))
  dispatcher.add_handler(ConversationHandler(
    entry_points=[
      CommandHandler("war", handlers.war),
      CallbackQueryHandler(pattern="LatinosWar", callback=handlers.latinos_war),
      CallbackQueryHandler(pattern="VzlaWar", callback=handlers.vzla_war)],
    states={      
      # WAR_STATE:[MessageHandler(Filters.text, handlers.balance)]},
    },
    fallbacks=[],
  ))

  # start the Bot
  updater.start_polling() # verifica si esta recibiendo mensajes
  updater.idle() # terminar bot ctrl + c
