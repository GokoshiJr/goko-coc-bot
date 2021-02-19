import coc

async def donaciones(client, clan_tag, negativas) -> str:
  result = ""
  try:
    miembros = await client.get_members(clan_tag)
    desbalanceados = "Los siguientes jugadores presentan un <b>balance negativo</b> de donaciones: \n\n"
    for miembro in miembros:
      balance = miembro.received - miembro.donations
      if (balance <= negativas):
        desbalanceados += f"{miembro.name} {balance}\n"
    result = desbalanceados
  except coc.Maintenance:
    result = "Los servidores se encuentran en mantenimiento"
  except:
    result = "Disculpe, hubo un error en la peticion"
  return result  

async def actual_war(client, clan_tag) -> str:
  result = ""  
  try:
    war = await client.get_clan_war(clan_tag)    
    result = \
    f"{war.clan.name} vs {war.opponent.name} \n" \
    f"Tipo: {war.type}\nTamaño: {war.team_size}" \
    f" \nEstatus: {war.state} {war.status} " \
    f"\n{war_time(war)} \nAtaques restantes: {ataques_restantes(war)}"
  except coc.PrivateWarLog:
    result = "El clan posee el registro de guerras privado."
  except coc.Maintenance:
    result = "Los servidores se encuentran en mantenimiento."
  except:
    result = "Disculpe, hubo un error en la petición."
  return result

async def members_in_war(client, clan_tag) -> str:
  result = ""  
  try:
    war = await client.get_clan_war(clan_tag)
    members = war.members
    result = "<b>Miembros en la guerra actual:</b>\n"
    for member in members:
      if not(member.is_opponent):
        result += f"{member.map_position}. {member.name} TH {member.town_hall} \n"
  except coc.Maintenance:
    result = "Los servidores se encuentran en mantenimiento" 
  except:
    result = "Disculpe, hubo un error en la petición." 
  return result

async def attacks_in_war(client, clan_tag) -> str:
  result = ""
  try:
    war = await client.get_clan_war(clan_tag)
    members = war.members
    for member in members:
      if not(member.is_opponent):
        ataques = member.attacks
        if (len(ataques) == 0):
          result += f"{member.name} \nAtaque1: No realizado \nAtaque2: No realizado\n\n"
        elif (len(ataques) == 1):
          result += f"{member.name} \nAtaque1: {ataques[0].destruction}% ({ataques[0].stars} stars)" \
            f"\nAtaque2: No realizado\n\n"
        else:
          result += f"{member.name} \nAtaque1: {ataques[0].destruction}% ({ataques[0].stars} stars)" \
            f"\nAtaque2: {ataques[1].destruction}% ({ataques[1].stars} stars)\n\n"
  except coc.PrivateWarLog:
    result = "El clan posee el registro de guerras privado."
  except coc.Maintenance:
    result = "Los servidores se encuentran en mantenimiento"
  except:
    result = "Disculpe, hubo un error en la petición"
  return result

def war_time(war) -> str:
  time_to_start = str(war.start_time.time - war.end_time.now)
  time_to_end = war.end_time.time - war.end_time.now
  result = ""  
  if (time_to_end.days == 1):
    if(len(str(time_to_start)) == 14):
      result = \
      f"Inicio de guerra: {time_to_start[0:1]} horas " \
      f"{time_to_start[2:4]} minutos"
    else:
      result = \
      f"Inicio de guerra: {time_to_start[0:2]} horas " \
      f"{time_to_start[3:5]} minutos"
  else:
    time_to_end = str(time_to_end)
    if(len(time_to_end) == 14):
      result = \
      f"Final de guerra: {time_to_end[0:1]} horas " \
      f"{time_to_end[2:4]} minutos"
    else:
      result = \
      f"Final guerra: {time_to_end[0:2]} horas " \
      f"{time_to_end[3:5]} minutos"
  return result

def ataques_restantes(war) -> int:
  result = 0
  members = war.members
  for member in members:
    if not(member.is_opponent):
      ataques = member.attacks
      if (len(ataques) == 0):
        result += 2
      elif (len(ataques) == 1):
        result += 1
  return result
