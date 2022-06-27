from email import message
import numbers
import nextcord
import os
import linecache as lc

from nextcord.ext import tasks, commands
from nextcord.utils import get
from datetime import datetime
from time import gmtime, strftime
from array import array

#import token from file
from apikeys import TOKEN
from settings import logs_channel, join_leave_channel
intents = nextcord.Intents.all()
intents.members = True
intents.messages = True

def save_event(**event):
    print(event)

client = commands.Bot(command_prefix='.', intents=intents) #define prefix



@client.event
async def on_ready():
    await client.change_presence(activity=nextcord.Game("It's a bot what did you expect?"))

@client.command() #define commands
async def hello(ctx):
    await ctx.send("Hello, I'm still working!")

@client.event
async def on_member_join(member):
    channel = client.get_channel(join_leave_channel) #channel id where message will be sent
    await channel.send(f"Witaj {member}")    

@client.event
async def on_member_remove(member):
    channel = client.get_channel(join_leave_channel)
    await channel.send(f"Uciekł {member}")
############################################
#Learning Cogs
extensions = []
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        extensions.append("cogs." + filename[:-3])#to delete .py

if __name__== '__main__':
    for extension in extensions:
        client.load_extension(extension)

#edit/delete messages logs
@client.event
async def on_message_delete(message):
    print("deleted")
    embed = nextcord.Embed(title=f"{message.author.name} usunął wiadomość z kanału {message.channel}",description=f"{message.content}")
    channel = client.get_channel(logs_channel)
    await channel.send(embed=embed)

@client.event
async def on_message_edit(message_before,message_after):
    embed_message = nextcord.Embed(title=f"{message_before.author.name} edytował wiadomość na kanale {message_before.channel}")
    embed_message.add_field(name="Przed",value=f"{message_before.content}",inline=False)
    embed_message.add_field(name="Po",value=f"{message_after.content}",inline=False)
    channel = client.get_channel(logs_channel)
    await channel.send(embed=embed_message)


client.run(TOKEN)