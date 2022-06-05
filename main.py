from email import message
import nextcord
import os 
import asyncio

from nextcord.ext import tasks, commands
from nextcord.utils import get
from datetime import datetime
from time import gmtime, strftime

#import token from file
from apikeys import *
from settings import *

intents = nextcord.Intents.all()
intents.members = True
intents.messages = True

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

@client.command(pass_context = True)
async def re(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()#End of this


#check for word learning
@client.command()
async def edit(ctx, *, word: str):
    channel = client.get_channel(ctx.channel)
    messages = await ctx.channel.history(limit=200).flatten()

    for msg in messages:
        if "Event" in msg.content:
            print(msg.jump_url)
#TODO MAKE IT PRETTIER
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #print(message)
    channel = client.get_channel(logs_channel) #channel id where message will be sent  
    #all messege logs
    mess = "#" + str(message.channel) + " " + str(message.author) + " at " + str(message.created_at)[0:19] + "\n" + str(message.content)
    await channel.send(mess)
    #print(mess)
    #trying to take string after .re command
    mess = str(message.content)
    if mess.find(".re ") > -1:
        print("register")                   #debug
        role = mess[3:]
        if role.find("slot") == -1:
            await message.channel.send("Nie ma takiej roli")
            await asyncio.sleep(3)
            await message.delete()
            await message.channel.delete()
        elif role.find("slot") > -1:
            await message.delete()
            messages = await message.channel.history(limit=200).flatten()
            for event in messages:
                if "Event" in event.content:
                    mess = event.content
                    print(mess)
                    mess = mess.replace(role,(" @"+str(message.author)))
                    await event.edit(content=mess)
    #if mess.find(".rm ") > -1:
    #    print("register")                   #debug
    #    role = mess[3:]
    #    if role.find("slot") == -1:
    #        await asyncio.sleep(3)
    #        await message.channel.send("Nie ma takiej roli")
    #        await message.delete()
    #    await message.delete()
    #    messages = await message.channel.history(limit=200).flatten()
    #    for event in messages:
    #        if "Event" in event.content:
    #            mess = event.content
    #            mess.replace(role,str(message.author))
    #            await event.edit(content=mess)
    elif mess.find(".create ") > -1:
        print("Create")                     #Create
        text = "Event\n" + mess[8:]
        await message.delete()
        await message.channel.send(text)
    elif mess.find(".edit ") > -1:                
        print("Edit")
        text = mess[5:]
        await message.delete()                     #Edit
        messages = await message.channel.history(limit=200).flatten()
        for event in messages:
            if "Event" in event.content:
                await event.edit(content="Event\n"+ text + "\n Edited by: " + str(message.author))

client.run(TOKEN)