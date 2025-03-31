# -*- coding: utf-8 -*-
from nextcord.ext import commands

class Template(commands.Cog):
    
    def __init__(self,client):
        self.client=client
    #template - creates a template for x players
    @commands.command()
    async def template(self, ctx,amount: int):
        mess = "**Zapisy**\n"
        for number in range(amount):
            mess += f"{number+1}. slot{number+1} -\n"
        await ctx.author.send(mess)
        await ctx.message.delete()


def setup(client):
    client.add_cog(Template(client))

