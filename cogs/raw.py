# -*- coding: utf-8 -*-
from queue import Empty
import nextcord
import json
from nextcord.ext import commands
from pathlib import Path
intents = nextcord.Intents.all()

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

class RAW(commands.Cog):
    
    def __init__(self,client):
        self.client=client
#register
    @commands.command(name='raw',aliases=['debug'])
    async def raw(self, ctx): 
        await ctx.message.delete()
        channel_id = ctx.channel.id
        raw_data = Path("./data.json").read_text()
        print(raw_data)
        Current_games = json.loads(raw_data)
        print("current_Games")
        print(Current_games)
        message_id = Current_games[str(channel_id)]["message_id"]
        print(message_id)
        msg = await ctx.fetch_message(message_id)
        mess = msg.content
        mess = "```\n"+mess+"\n```"
        await ctx.author.send(mess)
               

def setup(client):
    client.add_cog(RAW(client))

