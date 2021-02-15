from telegram import ChatAction

def escribiendo(chat) -> None:
  chat.send_action(action=ChatAction.TYPING, timeout=None)

# Messages

START = f"\n\nSoy un bot y me encuentro en desarrollo \n\n" \
  f"Escribe /commands para ver el listado de comandos disponibles."
  
COMMANDS = f"Lista de comandos que puedes usar: \n\n/commands \n/dev \n/balance" \
  f"\n/war"

DEV = "Puedes contactar al desarrollador <b>Julio González</b> mediante:"

RULES = ""

CWL_RULES = f"Sanciones y reglas de liga: \n\n" \
f"1-. Atacar en sentido contrario al Th y hacer fail no participa más en toda la liga. \n\n" \
f"2-. No hacer un ataque en liga, no participa más en toda la liga. \n\n" \
f"3-. Hacer un fail 1 guerra, hacer dos fail no participa más en toda la liga. \n\n" \
f"4-. Decirle al mismo jugador que ataque en reiteradas ocasiones o que no le dé importancia a la liga, " \
f"no participa hasta que el jugador se manifieste. \n\n" \
f"5-. Prohibido hablar mal de algún jugador, si un jugador comete un fail, en vez de atacarlo," \
f"lo ideal es realizarle una crítica constructiva para que este pueda corregir la falla. \n\n" \
f"6-. Si algún castillo no está completo 2 hora antes que empiece la guerra se sanciona" \
f"el jugador al que le corresponda donar. (1G) \n\n" \
f"Cualquier duda o inquietud preguntar sin pena."
