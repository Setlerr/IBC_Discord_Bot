from email import message
import numbers
import nextcord
import nextcord.utils
import linecache as lc
import json
from pathlib import Path
from nextcord.ext import tasks, commands

intents = nextcord.Intents.all()


class Reminder(commands.Cog):
    
    def __init__(self,client):
        self.client=client
#register
    @commands.command(name='reminder',aliases=['powiadom','alert','remind','przypomnij'])
    @commands.has_any_role("Moderator","Admin","Technik")
    async def remind(self, ctx):
        await ctx.message.delete()
        users_in_message = []
        users_to_ping = "Przypominam o misji!\n"
        channel_id = ctx.channel.id
        raw_data = Path("./data.json").read_text()
        print(raw_data)
        Current_games = json.loads(raw_data)
        print("current_Games")
        print(Current_games)
        Players = Current_games[str(channel_id)]["Players"]
        for word in Players:
            if nextcord.utils.get(ctx.guild.members, name=word) != None:
                user = nextcord.utils.get(ctx.guild.members, name=word)
                users_in_message.append(user.mention)
                print(user)
        for user in users_in_message:
            users_to_ping += str(f"{user}")
        await ctx.channel.send(content = users_to_ping)


                


def setup(client):
    client.add_cog(Reminder(client))
