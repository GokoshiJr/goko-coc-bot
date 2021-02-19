import coc

async def donaciones(client, clan_tag, negativas):
  try:
    miembros = await client.get_members(clan_tag)
    desbalanceados = "Los siguientes jugadores presentan un <b>balance negativo</b> de donaciones: \n\n"
    for miembro in miembros:
      balance = miembro.received - miembro.donations
      if (balance <= negativas):
        desbalanceados += f"{miembro.name} {balance}\n"
    result = desbalanceados
  except:
    result = "Disculpe, hubo un error en la peticion"
  return result  

async def actual_war(client, clan_tag) -> str:
  result = ""
  try:
    war = await client.get_clan_war(clan_tag)    
    result = \
    f"{war.clan.name} vs {war.opponent.name} ({war.type})" \
    f"\nTamaño: {war.team_size} \nEstatus: {war.state} {war.status} " \
    f"\nMiembros en guerra: \n" \
    f"{war_time(war)}"   
  except coc.PrivateWarLog:
    result = "El clan posee el registro de guerras privado."  
  return result

async def members_in_war(client, clan_tag) -> str:
  result = ""
  try:
    war = await client.get_clan_war(clan_tag)
    members = war.members
    for member in members:
      if not(member.is_opponent):
        result += f"{member.map_position}. {member.name} TH {member.town_hall} \n" 
  except:
    result = "Hubo un error en la peticion." 
  return result

def war_time(war) -> str:
  time_to_start = str(war.start_time.time - war.end_time.now)
  time_to_end = war.end_time.time - war.end_time.now
  result = ""  
  if (time_to_end.days == 1):
    result = \
    f"Tiempo para que inicie: {time_to_start[0:2]} horas" \
    f"{time_to_start[3:5]} minutos. \n\n {time_to_end}"
  else:    
    time_to_end = str(time_to_end)
    result = \
    f"Tiempo para que finalice: {time_to_end[0:2]} horas" \
    f"{time_to_end[3:5]} minutos. \n\n {time_to_end}"
  return result
