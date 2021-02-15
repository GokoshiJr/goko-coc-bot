import coc

async def donaciones(client, clan_tag, negativas):
  try:
    miembros = await client.get_members(clan_tag)
    desbalanceados = "Los siguientes jugadores presentan un balance nagativo de donaciones: \n\n"
    for miembro in miembros:
      balance = miembro.received - miembro.donations
      if (balance <= negativas):
        desbalanceados += f"{miembro.name} {balance}\n"
    result = desbalanceados
  except:
    result = "Disculpe, hubo un error en la peticion"
  return result  

async def war(client, clan_tag) -> str:
  try:
    war = await client.get_clan_war(clan_tag)
    result = f"{war.clan.name} vs {war.opponent.name} ({war.type}) \nTamaño: {war.team_size} \nEstatus: {war.state} {war.status} \nMiembros:"
  except coc.PrivateWarLog:
    result = "El clan posee el registro de guerras privado"
  return result
