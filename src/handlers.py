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
  update.message.reply_text(f"¡Bienvenido {user.get_name()}!" + actions.START) 
    
def list_commands(update, context) -> None:
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("solicitó los comandos."))
  actions.escribiendo(update.message.chat)
  update.message.reply_text(actions.COMMANDS)

def dev_social(update, context) -> None:
  update.message.reply_text(
    parse_mode="HTML",
    text=actions.DEV, 
    reply_markup=buttons.dev_social_markup
  )

def balance(update, context) -> None:
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("solicitó el balance negativo de donaciones."))
  actions.escribiendo(update.message.chat)
  update.message.reply_text(
    text="Verifica el balance de donaciones de",
    reply_markup=buttons.donaciones_markup
  )

def callback_balance(update, context) -> None:
  msg = client.loop.run_until_complete(clash.donaciones(client, keys.LA_TAG, -2000))
  query = update.callback_query
  query.answer()
  query.edit_message_text(
    text=msg,
    parse_mode="HTML"
  )  

def war(update, context) -> None:
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("solicitó ver el status de guerra del clan."))
  actions.escribiendo(update.message.chat)
  update.message.reply_text(
    text="Verifica las guerras actuales de",
    reply_markup=buttons.war_markup,
    parse_mode="HTML"
  )

def cb_latinos_war(update, context) -> None:
  msg, _ = client.loop.run_until_complete(clash.actual_war(client, keys.LA_TAG))
  query = update.callback_query
  query.answer()
  query.edit_message_text(
    text=msg
  )

def cb_otro_clan_war(update, context) -> None:
  query = update.callback_query
  query.answer()
  query.edit_message_text(
    text="Indique el tag del clan"
  )
  return 0

def filter_otro_clan_war(update, context) -> None:
  chat = update.message.chat
  text = update.message.text
  msg, state = client.loop.run_until_complete(clash.actual_war(client, text))
  if text == "salir":
    return -1
  else:
    actions.escribiendo(chat)
    update.message.reply_text(
    text=msg,
    parse_mode="HTML"
    )
    return state

def cwl_rules(update, context) -> None:   
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("solicitó ver las reglas de cwl del clan."))
  actions.escribiendo(update.message.chat)
  update.message.reply_text(actions.CWL_RULES)
