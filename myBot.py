#aioBot.py

''' =====================IMPORTS================='''

import os
import discord
from dotenv import load_dotenv

'''======================IMPORTS================='''

#Create client connect to discord server
load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')
#GUILD = os.getenv('DISCORD_GUILD')
TOKEN = x
GUILD = 'test_bot'

client = discord.Client()
'''
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

    for guilds in Client.guilds:
        if(guild.name == GUILD):
            break
    print(f'{client.user} is connected to the following guild:{guild.name}(id: {guild.id})\n')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'{Guild Members: \n - {members}')
'''

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

client.run(TOKEN)
