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
Latinos_Army = InlineKeyboardButton(
  text="Latinos Army",
  callback_data="LatinosArmy",
)
Venezuela = InlineKeyboardButton(
  text="Venezuela (Armil)",
  callback_data="VzlaWar",
)
Latinos_War = InlineKeyboardButton(
  text="Latinos Army",
  callback_data="LatinosWar",
)

# markup
dev_social_markup = InlineKeyboardMarkup([
  [dev_whatsapp, dev_telegram],
  [dev_twitter, dev_github]
])
donaciones_markup = InlineKeyboardMarkup([
  [Latinos_Army],
])
war_markup = InlineKeyboardMarkup([
  [Latinos_War],
  [Venezuela]
])