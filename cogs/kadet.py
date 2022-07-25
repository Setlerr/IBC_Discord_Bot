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
        role1 = ctx.guild.get_role(865191541940027452)
        role2 = ctx.guild.get_role(933040601073582140)
        role3 = ctx.guild.get_role(944364213692944404)
        await user.add_roles(role1)
        await user.add_roles(role2)
        await user.add_roles(role3)
def setup(client):
    client.add_cog(Kadet(client))
