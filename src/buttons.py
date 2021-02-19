from telegram import InlineKeyboardMarkup, InlineKeyboardButton

# keyboard buttons
dev_telegram = InlineKeyboardButton(
  text="Telegram",
  url="telegram.me/GokoshiJr"
)
dev_twitter = InlineKeyboardButton(
  text="Twitter",
  url="https://twitter.com/GokoshiJr"
)
dev_whatsapp = InlineKeyboardButton(
  text="WhatsApp",
  url="wa.me/+584247300796"
)
dev_github = InlineKeyboardButton(
  text="GitHub",
  url="https://github.com/GokoshiJr"
)
miembros = InlineKeyboardButton(
  text="Miembros",
  callback_data="miembros"
)
ataques = InlineKeyboardButton(
  text="Ataques",
  callback_data="ataques"
)
stats = InlineKeyboardButton(
  text="Estadisticas",
  callback_data="stats"
)
salir = InlineKeyboardButton(
  text="Salir",
  callback_data="salir"
)

# markups
dev_social_markup = InlineKeyboardMarkup([
  [dev_whatsapp, dev_telegram],
  [dev_twitter, dev_github]
])
war_markup = InlineKeyboardMarkup([
  [miembros],
  [ataques],
  [salir]
])
miembros_markup = InlineKeyboardMarkup([
  [stats],
  [miembros],
  [salir]
])
ataques_markup = InlineKeyboardMarkup([
  [stats],
  [ataques],
  [salir]
])
