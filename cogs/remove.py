import nextcord
import json

from nextcord.ext import commands
from pathlib import Path
intents = nextcord.Intents.all()
intents.members = True
intents.messages = True

class Remove(commands.Cog):
    
    def __init__(self,client):
        self.client=client
#remove
    @commands.command(name='rm',aliases=['wypis','remove'])
    async def rm(self, ctx,word: str,arg2: nextcord.User = None):
        print("remove")                   
        channel_id = ctx.channel.id
        raw_data = Path("./data.json").read_text()
        print(raw_data)
        Current_games = json.loads(raw_data)
        print("current_Games")
        print(Current_games)
        message_id = Current_games[str(channel_id)]["message_id"]
        print(message_id)
        msg = await ctx.fetch_message(message_id)
        print(msg)
        mess = msg.content
        check_slot = msg.content
        author_id = Current_games[str(channel_id)]["Author"]
        print(message_id)
        user_to_remove = ctx.author.name
        if arg2 is not None:
            if ctx.author.mention == author_id:
                user_to_remove = arg2.name
            else:
                await ctx.channel.send("Musisz być właścicielem zapisów, żeby kogoś wpisać!",delete_after=5)
        if word.find("slot") == -1:               
            await ctx.channel.send("Musisz nazwać slota z którego chcesz się wypisać np. slot5",delete_after=5)
        elif check_slot.find(word+" ")>-1:
            await ctx.channel.send("Taki slot już istnieje",delete_after=5)
        elif word.find("slot")>-1:
            if word.find(" ")>-1:
                await ctx.channel.send("Bez spacji!",delete_after=5)
            else:
                text = msg.content
                text = text.replace("**"+str(user_to_remove)+"**",word,1)
                await msg.edit(content=text)
                Current_games[str(channel_id)]["Players"].remove(str(user_to_remove))
                with open('data.json', 'w') as f:
                    json.dump(Current_games, f)
        await ctx.message.delete()


def setup(client):
    client.add_cog(Remove(client))

