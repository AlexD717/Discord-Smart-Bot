from replit import db

def TryGetValue(key, default):
  try:
    return db[key]
  except KeyError:
    return default

def handle_message(message):
  countingGameNumber = TryGetValue("countingGameNumber" + str(message.channel.id), 1)
  highscore = TryGetValue("highscore" + str(message.channel.id), 0)
  saidHighscore = TryGetValue("saidHighscore" + str(message.channel.id), False)
  message.content = message.content.lower()
  if (message.content.isdigit()):
    if (int(message.content) == countingGameNumber):
      countingGameNumber += 1
      db["countingGameNumber" + str(message.channel.id)] = countingGameNumber
      if (countingGameNumber - 1 > highscore):
        highscore = countingGameNumber - 1
        db["highscore" + str(message.channel.id)] = highscore
        if (saidHighscore is False):
          saidHighscore = True
          db["saidHighscore" + str(message.channel.id)] = saidHighscore
          return ("Congradulations, you now have a new high score!")
      return
    else:
      countingGameNumber = 1
      db["countingGameNumber" + str(message.channel.id)] = countingGameNumber
      saidHighscore = False
      db["saidHighscore" + str(message.channel.id)] = saidHighscore
      return "Incorrect!, Your count is restarting. Your highscore is " + str(highscore)
  if (message.content.startswith("!") is False):
    return
  message.content = message.content[1:]
  if (message.content == "hello"):
    return "Hello!"
  if (message.content == "number game"):
    return "Type numbers each increasing by one, and if you mess up then you start all the way back at 1"
  if (message.content == "highscore"):
    return highscore