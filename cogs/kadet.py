import nextcord
import nextcord.utils

from nextcord.ext import commands

intents = nextcord.Intents.all()
intents.members = True
intents.messages = True


class Kadet(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_any_role("Rekruter", "Admin", "Technik")
    async def kadet(self, ctx, user: nextcord.Member):
        await ctx.message.delete()
        role1 = ctx.guild.get_role(865191541940027452)  # kadet
        role2 = ctx.guild.get_role(944364213692944404)  # grane presety
        role3 = ctx.guild.get_role(1051554343171670056)  # posiadane dlc
        role4 = ctx.guild.get_role(1104390583092531260)  # posiadane gry
        role5 = ctx.guild.get_role(933040601073582140)  # specjalizacje
        await user.add_roles(role1, role2, role3, role4, role5)
        Message_content = f"{user.name} dostał kadeta"
        print(Message_content)
        channel = ctx.guild.get_thread(1204875945442283570)
        await channel.send(Message_content)


def setup(client):
    client.add_cog(Kadet(client))
