import nextcord
import nextcord.utils
import os
import subprocess
from nextcord.ext import commands

# import psutil

# NOT WORKING


intents = nextcord.Intents.all()
intents.members = True
intents.messages = True


class Stop(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_any_role("Moderator", "Admin", "Technik")
    async def stop(self, ctx):
        await ctx.message.delete()

        for proc in psutil.process_iter():
            if proc.name() == "arma3serverprofiling_x64":
                proc.kill()
                await ctx.message.channel.send(
                    "Serwer został wyłączony", delete_after=4
                )
            if proc.name() == "arma3server_x64.exe":
                proc.kill()
                await ctx.message.channel.send(
                    "Serwer został wyłączony", delete_after=4
                )


def setup(client):
    client.add_cog(Stop(client))
