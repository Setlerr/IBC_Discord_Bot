import nextcord
import json

from nextcord.ext import commands
from pathlib import Path
intents = nextcord.Intents.all()


class Remove(commands.Cog):
    
    def __init__(self,client):
        self.client=client
#remove
    @commands.command(name='rm',aliases=['wypis','remove'])
    async def rm(self, ctx,word: str,arg2: nextcord.User = None):
        await ctx.message.delete()
        print("remove")                   
        channel_id = ctx.channel.id
        raw_data = Path("./data.json").read_text()
        print(raw_data)
        flag = 0
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
        while True:
            if arg2 is not None:
                role1 = nextcord.utils.get(ctx.guild.roles, name="Admin")
                role2 = nextcord.utils.get(ctx.guild.roles, name="Technik")
                role3 = nextcord.utils.get(ctx.guild.roles, name="Moderator")
                roles_check = [role1,role2,role3] 

                for role in roles_check:
                    if role in ctx.author.roles:
                        has_permission = 1
                if ctx.author.mention == author_id or has_permission == 1:
                    user_to_remove = arg2.name
                else:
                    await ctx.channel.send("Musisz być właścicielem zapisów, żeby kogoś wypisać!",delete_after=5)
                    flag = 1
                    break
                
            if word.find("slot") == -1:               
                await ctx.channel.send("Musisz nazwać slota z którego chcesz się wypisać np. slot5",delete_after=5)
                flag = 1
                break
            elif check_slot.find(word+" ")>-1:
                await ctx.channel.send("Taki slot już istnieje",delete_after=5)
                flag = 1
                break
            elif word.find("slot")>-1:
                if word.find(" ")>-1:
                    await ctx.channel.send("Bez spacji!",delete_after=5)
                    flag = 1
                    break
                else:
                    text = msg.content
                    text = text.replace("**"+str(user_to_remove)+"**",word,1)
                    await msg.edit(content=text)
                    Current_games[str(channel_id)]["Players"].remove(str(user_to_remove))
                    with open('data.json', 'w') as f:
                        json.dump(Current_games, f)
        


def setup(client):
    client.add_cog(Remove(client))

