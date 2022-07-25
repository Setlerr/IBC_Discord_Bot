import nextcord
import nextcord.utils

from nextcord.ext import commands
intents = nextcord.Intents.all()
intents.members = True
intents.messages = True

class Wolny(commands.Cog):
    
    def __init__(self,client):
        self.client=client

    @commands.command()
    @commands.has_role("HR")
    async def wolny(self, ctx, user : nextcord.Member):
        await ctx.message.delete()
        role1 = ctx.guild.get_role(825527599203614720)
        role2 = ctx.guild.get_role(944364213692944404)
        await user.add_roles(role1)
        await user.add_roles(role2)
def setup(client):
    client.add_cog(Wolny(client))
