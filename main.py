import discord
import os 

from discord.ext import tasks, commands
from discord.utils import get

#import token from file
from apikeys import *

intents = discord.Intents.default()
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix='.', intents=intents) #define prefix



@client.command() #define commands
async def hello(ctx):
    await ctx.send("Hello, I'm still working!")

@client.event
async def on_member_join(member):
    channel = client.get_channel(982713233758634004) #channel id where message will be sent
    await channel.send(f"Witaj {member}")    

@client.event
async def on_member_remove(member):
    channel = client.get_channel(982713233758634004)
    await channel.send(f"Spierdolił {member}")

@client.command(pass_context=True)
async def join(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("Wejdź na kanał głosowy!")

#guild is basiclly your server so, go to guild > voice channel > leave
#Learning how joining works
@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()#End of this

#check for word learning

#all messege logs
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    channel = client.get_channel(982746762303402014) #channel id where message will be sent    
    mess = "#" + str(message.channel) + " " + str(message.author) + " at " + str(message.created_at)[0:19] + "\n" + str(message.content)
    await channel.send(mess)
    print(mess)



client.run(TOKEN)