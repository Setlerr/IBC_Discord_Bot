# -*- coding: utf-8 -*-
import nextcord
import json
from funcs.role_check import check_for_admin
from nextcord.ext import commands
from pathlib import Path
intents = nextcord.Intents.all()


class Purge(commands.Cog):
    
    def __init__(self,client):
        self.client=client


    @commands.command(name='purge')
    async def purge(self, ctx):
        await ctx.message.delete()
        print("purge")                   
        channel_id = ctx.channel.id
        raw_data = Path("./data.json").read_text()
        Current_games = json.loads(raw_data)
        if check_for_admin(ctx) is True:
            print(Current_games[str(channel_id)])
            del Current_games[str(channel_id)]
            with open('data.json', 'w') as f:
                json.dump(Current_games, f)
        else:
            await ctx.channel.send("Potrzebujesz uprawnienia!",delete_after=5)
                    
        
def setup(client):
    client.add_cog(Purge(client))

