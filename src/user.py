class User():
  # constructor
  def __init__(self, name, last_name, user_name):
    self.__name = name
    self.__last_name = last_name
    self.__user_name = user_name 

  def get_name(self):
    return self.__name

  def get_last_name(self):
    return self.__last_name

  def get_user_name(self):
    return self.__user_name

  def log(self, action):
    result = ""
    if (self.__last_name != None):
      result = f"El usuario {self.__user_name} ({self.__name} {self.__last_name}) {action}"
    else:
      result = f"El usuario {self.__user_name} ({self.__name}) {action}"
    return result

  def __str__(self):
    return f"User(username={self.__user_name}, name={self.__name}, last_name={self.__last_name})"
  