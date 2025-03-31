# -*- coding: utf-8 -*-
import nextcord
import json
from pathlib import Path
from nextcord.ext import commands
from funcs.role_check import check_for_admin

intents = nextcord.Intents.all()


class Edit(commands.Cog):
    def __init__(self, client):
        self.client = client

    # edit event by creator
    @commands.command()
    async def edit(self, ctx, *, word: str):  # edit
        channel_id = ctx.channel.id
        raw_data = Path("./data.json").read_text()
        print(raw_data)
        Current_games = json.loads(raw_data)
        print("current_Games")
        print(Current_games)
        message_id = Current_games[str(channel_id)]["message_id"]
        author_id = Current_games[str(channel_id)]["Author_name"]
        print(message_id)
        msg = await ctx.fetch_message(message_id)
        print(msg)
        await ctx.message.delete()
        if author_id == ctx.author.name or check_for_admin(ctx) is True:
            await msg.edit(content=word)
        else:
            await ctx.channel.send(
                "Nie możesz edytować tej wiadomości!", delete_after=5
            )


def setup(client):
    client.add_cog(Edit(client))
