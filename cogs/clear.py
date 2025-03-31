# -*- coding: utf-8 -*-
import nextcord
import json

from nextcord.ext import commands
intents = nextcord.Intents.all()


class Clear(commands.Cog):
    
    def __init__(self,client):
        self.client=client
#remove
    @commands.command(name='clear',aliases=['clr'])
    async def clear(self, ctx, amount: int):
        await ctx.channel.send(f"Usuwanie {str(amount)} wiadomości",delete_after=5)
        mgs = []
        amount = amount + 1
        async for x in ctx.logs_from(ctx.message.channel, limit = amount):
            mgs.append(x)
        for message in mgs:
            await ctx.delete.message(message)


def setup(client):
    client.add_cog(Clear(client))

