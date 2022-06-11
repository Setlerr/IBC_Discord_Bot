from email import message
import nextcord
import os 
import asyncio
import time

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

#edit event by creator
@client.command()
async def edit(ctx, *, word: str): #edit
    print("edit")
    messages = await ctx.channel.history(limit=200).flatten()
    for event in messages:
            if "Event" in event.content:
                #await ctx.delete()
                text = event.content
                check_position = text.find("Created by: ")
                check_text = text[check_position:]
                if check_text.find(str(ctx.author.mention)) > -1:
                    await event.edit(content="Event\n"+ word + "\nCreated by: " + str(ctx.author.mention))
                else:
                    await ctx.channel.send("Nie możesz edytować tej wiadomości!")

#register
@client.command()
async def re(ctx, arg: str): 
    if arg.find("slot") == -1:
        await ctx.channel.send("Nie ma takiej roli")
        await asyncio.sleep(3)
        #await ctx.delete()
        #await ctx.delete()
    elif arg.find("slot") > -1:
        #await ctx.delete()
        messages = await ctx.channel.history(limit=200).flatten()
        for event in messages:
            if "Event" in event.content:
                mess = event.content
                print(mess)
                mess = mess.replace(arg,(" "+str(ctx.author.mention)))
                await event.edit(content=mess)

#create
@client.command()
async def create(ctx, *, word: str):
    print("create")
    #await ctx.delete()
    await ctx.send(content="Event\n"+ word + "\nCreated by: " + str(ctx.author.mention))


#remove
@client.command()
async def rm(ctx,*,word: str):
        print("remove")                   
        #await ctx.delete()
        messages = await ctx.channel.history(limit=200).flatten()
        for event in messages:
            if "Event" in event.content:
                check_slot = event.content
                if word.find("slot") == -1:
                    #await ctx.delete()
                    await ctx.channel.send("Musisz nazwać slota z którego chcesz się wypisać np. slot5")
                    await asyncio.sleep(6)
                    #await ctx.delete()
                    break
                elif check_slot.find(word)>-1:
                    #await ctx.delete()
                    await ctx.channel.send("Taki slot już istnieje")
                    await asyncio.sleep(6)
                    #await ctx.delete()
                    break
                elif word.find("slot")>-1:
                    text = event.content
                    check_position = text.find("Created by: ")
                    check_text = text[check_position:]
                    text = text[:check_position]
                    text = text.replace(str(ctx.author.mention),word)
                    await event.edit(content=text+check_text)

                    

client.run(TOKEN)