import logging, actions, buttons, clash, coc, keys 
from user import User 

client = coc.login(keys.API_EMAIL, keys.API_PASSWORD)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__+ ".py")

def start(update, context) -> None:
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("ha iniciado el bot."))
  actions.escribiendo(update.message.chat) # el bot esta escribiendo
  update.message.reply_text(f"¡Bienvenido {user.get_name()}!" + actions.START) 
    
def commands(update, context) -> None:
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("solicitó los comandos."))
  actions.escribiendo(update.message.chat)
  update.message.reply_text(actions.COMMANDS)

def dev_social(update, context) -> None:
  update.message.reply_text(parse_mode="HTML",text=actions.DEV, 
  reply_markup=buttons.dev_social_markup)

def balance(update, context) -> None:
  msg = client.loop.run_until_complete(clash.donaciones(client, keys.LA_TAG, -2000))
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("solicitó el balance de las donaciones."))
  actions.escribiendo(update.message.chat)
  update.message.reply_text(msg)

def war(update, context) -> None:
  msg = client.loop.run_until_complete(clash.war(client, keys.VZLA_TAG))  
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("solicitó ver el status de guerra del clan."))
  actions.escribiendo(update.message.chat)
  update.message.reply_text(msg)
