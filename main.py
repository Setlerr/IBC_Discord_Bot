import discord
import os 

from discord.ext import tasks, commands
from discord.utils import get

client = commands.Bot(command_prefix='`')

@client.event
async def on_ready():
    print("Bot is working")


@client.command() #define commands
async def hello(ctx):
    await ctx.send("Hello, I'm still working!")







client.run('TOKEN')