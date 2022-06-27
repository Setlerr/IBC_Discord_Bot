from email import message
import numbers
import nextcord
import linecache as lc

from nextcord.ext import tasks, commands
from nextcord.utils import get
from datetime import datetime
from time import gmtime, strftime
from array import array

intents = nextcord.Intents.all()
intents.members = True
intents.messages = True

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
            await ctx.send(content="Event\n"+ word + "\nCreated by: " + str(ctx.author.mention))


def setup(client):
    client.add_cog(Create(client))

