from telegram import ChatAction

def escribiendo(chat) -> None:
  chat.send_action(action=ChatAction.TYPING, timeout=None)

# Messages

START = f"\n\nSoy un bot y me encuentro en desarrollo \n\n" \
  f"Escribe /commands para ver el listado de comandos disponibles."
  
COMMANDS = f"Lista de comandos que puedes usar: \n\n/commands \n/dev \n/balance" \
  f"\n/war"

DEV = "Puedes contactar al desarrollador <b>Julio González</b> mediante:"