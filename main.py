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

############################################
#Learning Cogs
extensions = []
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        extensions.append("cogs." + filename[:-3])#to delete .py

if __name__== '__main__':
    for extension in extensions:
        client.load_extension(extension)


@client.command()
async def reload(ctx):
    await ctx.message.delete()
    extensions = []
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            extensions.append("cogs." + filename[:-3])#to delete .py
    if __name__== '__main__':
        for extension in extensions:
            client.unload_extension(extension)
    if __name__== '__main__':
        for extension in extensions:
            client.load_extension(extension)
            await ctx.send(f'{extension} reloaded',delete_after=5)


@client.event
async def on_message_delete(message):
    async for entry in message.guild.audit_logs(limit=1,action=nextcord.AuditLogAction.message_delete):
        deleter = entry.user
    if deleter != message.author.name:
        embed = nextcord.Embed(title=f"{deleter.name} usunął wiadomość {message.author.name} z kanału {message.channel}",description=f"{message.content}")
    else:
        embed = nextcord.Embed(title=f"{message.author.name} usunął wiadomość {message.author.name} z kanału {message.channel}",description=f"{message.content}")
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