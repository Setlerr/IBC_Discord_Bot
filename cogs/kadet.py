import nextcord
import nextcord.utils

from nextcord.ext import commands
intents = nextcord.Intents.all()
intents.members = True
intents.messages = True

class Kadet(commands.Cog):
    
    def __init__(self,client):
        self.client=client

    @commands.command()
    @commands.has_role("HR")
    async def kadet(self, ctx, user : nextcord.Member):
        await ctx.message.delete()
        role1 = ctx.guild.get_role(1001216779177181314)
        role2 = ctx.guild.get_role(1001232354523746364)
        await user.add_roles(role1,role2)
def setup(client):
    client.add_cog(Kadet(client))