class GokoBot(): 
  def __init__(self, bot):
    self.__bot = bot
    self.__id = bot.id
    self.__first_name = bot.first_name
    self.__is_bot = bot.is_bot
    self.__user_name = bot.username
    self.__can_join_groups = bot.can_join_groups
    self.__can_read_all_group_messages = bot.can_read_all_group_messages
    # self.__suprts_inline_queries = bot.suprts_inline_queries
  
  def get_id(self) -> int:
    return self.__id

  def get_first_name(self) -> str:
    return self.__first_name

  def is_bot(self) -> bool:
    return self.__is_bot

  def get_user_name(self) -> str:
    return self.__user_name

  def can_join_groups(self) -> bool:
    return self.__can_join_groups

  def can_read_all_group_messages(self) -> bool:
    return self.__can_read_all_group_messages

  def suprts_inline_queries(self) -> bool:
    """ return self.__suprts_inline_queries """
    pass

  def __str__(self) -> str:
    return f"El bot {self.__user_name} esta escuchando peticiones."
