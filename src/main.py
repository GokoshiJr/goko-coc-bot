import telegram, handlers, os
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters
from actions import SLASH
from goko_bot import GokoBot

BOT_TOKEN = os.environ["BOT_TOKEN"]

if __name__ == "__main__":
  # Initialize the bot
  bot = telegram.Bot(BOT_TOKEN)
  print(GokoBot(bot.get_me()))

  # Set bot rules
  bot.set_my_commands(commands=SLASH)

  # updater - to listen de user request
  updater = Updater(token=BOT_TOKEN, use_context=True)

  # get the dispatcher to register handlers
  dispatcher = updater.dispatcher

  # handlers
  dispatcher.add_handler(CommandHandler("start", handlers.start))
  dispatcher.add_handler(CommandHandler("commands", handlers.list_commands))
  dispatcher.add_handler(CommandHandler("dev", handlers.dev_social))
  dispatcher.add_handler(CommandHandler("cwl", handlers.cwl_rules))
  dispatcher.add_handler(CommandHandler("balance", handlers.balance))
  dispatcher.add_handler(ConversationHandler(
    entry_points=[
      CommandHandler("war", handlers.war),
      CallbackQueryHandler(pattern="miembros", callback=handlers.cb_war_members),
      CallbackQueryHandler(pattern="ataques", callback=handlers.cb_war_attacks),
      CallbackQueryHandler(pattern="stats", callback=handlers.cb_war),
      CallbackQueryHandler(pattern="salir", callback=handlers.cb_salir)
    ],
    states={}, fallbacks=[]
  ))
  
  # start the Bot
  updater.start_polling() # verifica si esta recibiendo mensajes
  updater.idle() # terminar bot ctrl + c
