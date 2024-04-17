from replit import db

def TryGetValue(key, default):
  try:
    return db[key]
  except KeyError:
    return default

countingGameNumber = TryGetValue("countingGameNumber", 1)
highscore = TryGetValue("highscore", 0)
saidHighscore = False

def handle_message(message):
  global countingGameNumber, playingCountingGame, highscore, saidHighscore
  message.content = message.content.lower()
  if (message.content.isdigit()):
    if (int(message.content) == countingGameNumber):
      countingGameNumber += 1
      db["countingGameNumber"] = countingGameNumber
      if (countingGameNumber - 1 > highscore):
        highscore = countingGameNumber - 1
        db["highscore"] = highscore
        if (saidHighscore is False):
          saidHighscore = True
          return ("Congradulations, you now have a new high score!")
      return
    else:
      countingGameNumber = 1
      saidHighscore = False
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