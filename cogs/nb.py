import nextcord

from nextcord.ext import commands

intents = nextcord.Intents.all()

class NB(commands.Cog):
    
    def __init__(self,client):
        self.client=client
#Ping someone x times
    @commands.command(name='nb',aliases=['urlop'])
    async def nb(self, ctx, *, word: str): #edit
        channel = ctx.guild.get_thread(1008094444660203540)
        await channel.send(word)
        await channel.send("<@322821699278077952> Kolejny urlop!")
        await ctx.message.delete()
def setup(client):
    client.add_cog(NB(client))
