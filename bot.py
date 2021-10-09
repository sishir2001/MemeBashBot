#bot.py

import os
import discord
from dotenv import load_dotenv
# dotenv library for parsing .env files 

# loads the environment variables from .env file into shell environment variable 
load_dotenv()
# Get the token from environment varible 
TOKEN = os.getenv('DISCORD_TOKEN')

# client - an object that represents the connection to discord 
client = discord.Client()

# an event handler , which handles the event when connected to discord
@client.event
async def on_ready():
    print(f"{client.user} has connected to discord!")

#run the client 
client.run(TOKEN) 


