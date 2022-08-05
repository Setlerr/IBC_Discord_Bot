from email import message
import numbers
import nextcord
import nextcord.utils
import linecache as lc

from nextcord.ext import tasks, commands

intents = nextcord.Intents.all()
intents.members = True
intents.messages = True

class Reminder(commands.Cog):
    
    def __init__(self,client):
        self.client=client
#register
    @commands.command(name='reminder',aliases=['powiadom','alert','remind','przypomnij'])
    #@commands.has_role("Admin")
    #@commands.has_role("MM","Admin")
    async def remind(self, ctx):
        await ctx.message.delete()
        #if ctx.author.guild_permissions.administrator:
        messages = await ctx.channel.history(limit=400).flatten()
        users_in_message = []
        users_to_ping = "Przypominam o misji!\n"
        for event in messages:
            if "Event" in event.content:
                mess = event.content
                mess = mess.replace("**","")
                print(mess)
                mess = mess.split()
                for word in mess:
                    if nextcord.utils.get(ctx.guild.members, name=word) != None:
                        user = nextcord.utils.get(ctx.guild.members, name=word)
                        users_in_message.append(user.mention)
                        print(user)
                for user in users_in_message:
                    users_to_ping += str(f"{user}")
                await ctx.channel.send(content = users_to_ping)


                


def setup(client):
    client.add_cog(Reminder(client))
