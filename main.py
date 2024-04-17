import discord
import os
import responses
from keepAlive import keep_alive

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  response = responses.handle_message(message)
  if (response != None):
    await message.channel.send(response)

keep_alive()
client.run(os.environ['TOKEN'])