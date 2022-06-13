from email import message
import numbers
import nextcord
import os 
import asyncio
import time
import linecache as lc

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

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

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
@client.command(pass_context=True)
async def edit(ctx, *, word: str): #edit
    print("edit")
    messages = await ctx.channel.history(limit=200).flatten()
    for event in messages:
            if "Event" in event.content:
                await ctx.message.delete()
                text = event.content
                check_position = text.find("Created by: ")
                check_text = text[check_position:]
                if check_text.find(str(ctx.author.mention)) > -1:
                    await event.edit(content="Event\n"+ word + "\nCreated by: " + str(ctx.author.mention))
                else:
                    await ctx.channel.send("Nie możesz edytować tej wiadomości!",delete_after=5)


#register
@client.command()
async def re(ctx, arg: str): 
    if arg.find("slot") == -1:
        await ctx.message.delete()
        await ctx.channel.send("Nie ma takiej roli",delete_after=5)
    elif arg.find("slot") > -1:
        if has_numbers(arg)==True:
            await ctx.message.delete()
            messages = await ctx.channel.history(limit=200).flatten()
            for event in messages:
                if "Event" in event.content:
                    mess = event.content
                    print(mess)
                    mess = mess.replace(arg,(" "+str(ctx.author.mention)),1)
                    await event.edit(content=mess)
        else:
            await ctx.message.delete()
            await ctx.channel.send("Podaj numer slota",delete_after=5)
#create
@client.command()
async def create(ctx, *, word: str):
    marker = 0
    print("create")
    messages = await ctx.channel.history(limit=200).flatten()
    await ctx.message.delete()
    for event in messages:
        if event.content.find("Event")>-1:
            print("1")
            marker = 1
            await ctx.channel.send("Już jest wydarzenie na tym kanale.",delete_after=5)
            break
    if marker==0:
        await ctx.send(content="Event\n"+ word + "\nCreated by: " + str(ctx.author.mention))
    

#remove
@client.command()
async def rm(ctx,*,word: str):
        print("remove")                   
        messages = await ctx.channel.history(limit=200).flatten()
        for event in messages:
            if "Event" in event.content:
                check_slot = event.content
                if word.find("slot") == -1:
                    
                    await ctx.channel.send("Musisz nazwać slota z którego chcesz się wypisać np. slot5",delete_after=5)
                    break
                elif check_slot.find(word)>-1:
                    await ctx.channel.send("Taki slot już istnieje",delete_after=5)
                    break
                elif word.find("slot")>-1:
                    text = event.content
                    check_position = text.find("Created by: ")
                    check_text = text[check_position:]
                    text = text[:check_position]
                    text = text.replace(str(ctx.author.mention),word,1)
                    await event.edit(content=text+check_text)
        await ctx.message.delete()

client.run(TOKEN)