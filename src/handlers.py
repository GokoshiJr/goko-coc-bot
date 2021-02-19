import logging, actions, buttons, clash, coc, os 
from user import User 
from boto.s3.connection import S3Connection
API_EMAIL = S3Connection(os.environ["API_EMAIL"])
API_PASSWORD = S3Connection(os.environ["API_PASSWORD"])
LA_TAG = S3Connection(os.environ["LA_TAG"])
client = coc.login(API_EMAIL, API_PASSWORD)

# Enable logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__ + ".py")

def start(update, context) -> None:
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("ha iniciado el bot."))
  
  update.message.reply_text(
    text=f"¡Bienvenido <b>{user.get_name()}!</b>" + actions.START,
    parse_mode="HTML"
  ) 
    
def list_commands(update, context) -> None:
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("solicitó los comandos."))
  
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
  msg = client.loop.run_until_complete(clash.donaciones(client, LA_TAG, -2000))
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("solicitó el balance negativo de donaciones."))
  
  update.message.reply_text(
    text=msg,    
    parse_mode="HTML"
  )

def war(update, context) -> None:
  msg = client.loop.run_until_complete(clash.actual_war(client, LA_TAG))
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("solicitó ver el status de la guerra actual."))
  
  update.message.reply_text(
    text=msg,
    parse_mode="HTML",
    reply_markup=buttons.war_markup
  )

def cwl_rules(update, context) -> None:   
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("solicitó ver las reglas de cwl del clan."))
  
  update.message.reply_text(
    text=actions.CWL_RULES,
    parse_mode="HTML"
  )

def cb_war(update, context):
  msg = client.loop.run_until_complete(clash.actual_war(client, LA_TAG))
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("solicitó ver el status de la guerra actual."))
  query = update.callback_query
  query.answer()  
  query.edit_message_text(
    text=msg,
    parse_mode="HTML",
    reply_markup=buttons.war_markup
  )

def cb_war_members(update, context) -> None:
  msg = client.loop.run_until_complete(clash.members_in_war(client, LA_TAG))
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("solicitó ver los miembros de la guerra del clan."))
  query = update.callback_query
  query.answer()  
  query.edit_message_text(
    text=msg,
    parse_mode="HTML",
    reply_markup=buttons.ataques_markup
  )

def cb_war_attacks(update, context) -> None:
  msg = client.loop.run_until_complete(clash.attacks_in_war(client, LA_TAG))
  data = update.effective_user
  user = User(data.first_name, data.last_name, data.username)
  logger.info(user.log("solicitó ver los ataques de la guerra del clan."))
  query = update.callback_query
  query.answer()
  query.edit_message_text(
    text=msg,
    parse_mode="HTML",
    reply_markup=buttons.miembros_markup
  )

def cb_salir(update, context) -> None:
  query = update.callback_query
  query.answer()
  query.edit_message_text(text="Fin del mensaje.")
