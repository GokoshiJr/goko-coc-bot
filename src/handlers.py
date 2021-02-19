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
  actions.escribiendo(update.message.chat)
  update.message.reply_text(
    text=f"¡Bienvenido <b>{user.get_name()}!</b>" + actions.START,
    parse_mode="HTML"
  ) 
    
def list_commands(update, context) -> None:
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("solicitó los comandos."))
  actions.escribiendo(update.message.chat)
  update.message.reply_text(
    text=actions.COMMANDS,
    parse_mode="HTML"
  )

def dev_social(update, context) -> None:
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("solicitó el contacto con el desarrollador."))
  update.message.reply_text(    
    text=actions.DEV, 
    reply_markup=buttons.dev_social_markup,
    parse_mode="HTML"
  )

def balance(update, context) -> None:
  msg = client.loop.run_until_complete(clash.donaciones(client, keys.LA_TAG, -2000))
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("solicitó el balance negativo de donaciones."))
  actions.escribiendo(update.message.chat)
  update.message.reply_text(
    text=msg,    
    parse_mode="HTML"
  )

def war(update, context) -> None:
  msg = client.loop.run_until_complete(clash.actual_war(client, keys.LA_TAG))
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("solicitó ver el status de la guerra actual."))
  actions.escribiendo(update.message.chat)
  update.message.reply_text(
    text=msg,
    parse_mode="HTML"
  )

def cwl_rules(update, context) -> None:   
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("solicitó ver las reglas de cwl del clan."))
  actions.escribiendo(update.message.chat)
  update.message.reply_text(
    text=actions.CWL_RULES,
    parse_mode="HTML"
  )
