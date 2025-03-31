# -*- coding: utf-8 -*-
import nextcord
import json
import sys

from pathlib import Path
from nextcord.ext import commands

intents = nextcord.Intents.all()


class Export(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Export players from json file to activity channel
    @commands.command()
    @commands.has_any_role("Moderator", "Admin", "Technik", "Mission Maker")
    async def export(self, ctx):
        await ctx.message.delete()
        channel_id = ctx.channel.id
        raw_data = Path("./data.json").read_text()
        print(raw_data)
        Current_games = json.loads(raw_data)
        print("current_Games")
        print(Current_games)
        Channel_name = str(Current_games[str(channel_id)]["Channel_name"])
        Author_name = str(str(Current_games[str(channel_id)]["Author_name"]))
        Players = Current_games[str(channel_id)]["Players"]
        List_of_players = "**Gracze zapisani:**\n"
        for player in Players:
            List_of_players += f"<@{str(player)}>" + "\n"
        Message_content = f"**Nazwa kanału:** {Channel_name}\n\n**Autor zapisów/misji:** {Author_name}\n\n{List_of_players}\n\n"
        print(Message_content)
        channel = ctx.guild.get_thread(1008094444660203540)
        await channel.send(Message_content)


def setup(client):
    client.add_cog(Export(client))
