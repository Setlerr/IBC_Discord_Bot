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

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)
class Register(commands.Cog):
    
    def __init__(self,client):
        self.client=client
#register
    @commands.command(name='re',aliases=['zapis','register','zapisz'])
    async def re(self, ctx, arg: str): 
        if arg.find("slot") == -1:
            await ctx.message.delete()
            await ctx.channel.send("Nie ma takiej roli",delete_after=5)
        elif arg.find("slot") > -1:
            if has_numbers(arg)==True:
                await ctx.message.delete()
                messages = await ctx.channel.history(limit=200).flatten()
                for event in messages:
                    if "Event" in event.content:
                        mess = event.content
                        check_position = mess.find("Created by: ")
                        check_text = mess[:check_position]
                        print(check_text)
                        if check_text.find(str(ctx.author.name))>-1:
                            await ctx.channel.send("Już jesteś zapisany!",delete_after=5)
                        else:
                            mess = mess.replace(arg,("**"+str(ctx.author.name)+"**"),1)
                            await event.edit(content=mess)
            else:
                await ctx.message.delete()
                await ctx.channel.send("Podaj numer slota",delete_after=5)

def setup(client):
    client.add_cog(Register(client))

