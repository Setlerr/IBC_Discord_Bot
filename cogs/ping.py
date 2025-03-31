# -*- coding: utf-8 -*-
import nextcord

from nextcord.ext import commands

intents = nextcord.Intents.all()

class Ping(commands.Cog):
    
    def __init__(self,client):
        self.client=client
#Ping someone x times
    @commands.command()
    async def ping(self, ctx, arg1, arg2=1): #edit
        await ctx.message.delete()
        if ctx.author.guild_permissions.administrator or ctx.author.id == 276390407565344779:
            for n in range(int(arg2)):
                await ctx.channel.send(arg1,delete_after=5)
        else:
            await ctx.channel.send("Nie jesteś Administratorem!")


def setup(client):
    client.add_cog(Ping(client))
