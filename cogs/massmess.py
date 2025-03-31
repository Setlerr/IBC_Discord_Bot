# -*- coding: utf-8 -*-
from queue import Empty
import nextcord
import json
from nextcord.ext import commands
from pathlib import Path


class MASSMESS(commands.Cog):
    def __init__(self,client):
        self.client=client


    @commands.command(name="massmess",aliases=["allmess"])
    @commands.has_permissions(administrator=True)
    async def massmess(self, ctx, role: nextcord.Role, *, message: str):
        members_sent = 0
        members_failed = 0
        for member in ctx.guild.members:
            if role in member.roles:
                try:
                    await member.send(message)
                    members_sent += 1
                except:
                    members_failed += 1
        await ctx.send(f'Wysłano wiadomość do {members_sent} członków. Nie udało się wysłać do {members_failed} członków.')
               

def setup(client):
    client.add_cog(MASSMESS(client))

