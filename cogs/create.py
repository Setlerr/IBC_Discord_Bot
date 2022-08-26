from http import server
from venv import create
import json
import nextcord
import os.path

from pathlib import Path
from nextcord.ext import commands

def create_event(channel_id,message_id,channel_name,author_id,author_name):
    if os.path.exists("./data.json") is True:
        raw_data = Path("./data.json").read_text()
        print(raw_data)
        Current_games = json.loads(raw_data)
    else:
        Current_games = {}
    Current_games[str(channel_id)] = {'message_id' : str(message_id),'Channel_name': str(channel_name) ,'Author': str(author_id),'Author_name': author_name, 'Players': []}
    with open('data.json', 'w') as f:
        json.dump(Current_games, f)
        f.close

intents = nextcord.Intents.all()


class Create(commands.Cog):
    
    def __init__(self,client):
        self.client=client
#remove
    @commands.command()
    async def create(self, ctx, *, word: str):
        marker = 0
        print("create")
        messages = await ctx.channel.history(limit=200).flatten()
        await ctx.message.delete()
        for event in messages:
            if event.content.find("Event")>-1:
                print("1")
                marker = 1
                await ctx.channel.send("Już jest wydarzenie na tym kanale.",delete_after=5)
                break
        if marker==0:
            message_info = await ctx.send(content=word)
            message_id = message_info.id
            message_channel_id = message_info.channel.id
            message_author = ctx.author.mention
            channel_name = message_info.channel.name
            print(message_id)
            print(message_channel_id)
            print(channel_name)
            print(str(message_author))
            create_event(str(message_channel_id),str(message_id),str(channel_name),str(message_author),str(ctx.author.name))


def setup(client):
    client.add_cog(Create(client))

