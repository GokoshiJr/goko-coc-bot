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
latinos_army_donaciones = InlineKeyboardButton(
  text="Latinos Army",
  callback_data="LatinosArmy",
)
latinos_army_actual_war = InlineKeyboardButton(
  text="Latinos Army",
  callback_data="LatinosWar",
)
otro_clan_actual_war = InlineKeyboardButton(
  text="Otro",
  callback_data="OtroWar",
)

# markup
dev_social_markup = InlineKeyboardMarkup([
  [dev_whatsapp, dev_telegram],
  [dev_twitter, dev_github]
])
donaciones_markup = InlineKeyboardMarkup([
  [latinos_army_donaciones],
])
war_markup = InlineKeyboardMarkup([
  [latinos_army_actual_war],
  [otro_clan_actual_war],
])