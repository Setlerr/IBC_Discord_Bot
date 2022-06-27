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
class Reminder(commands.Cog):
    
    def __init__(self,client):
        self.client=client
#reminder
    @commands.Cog.listener()
    async def re(self, member): 
        #code








        #end of code
def setup(client):
    client.add_cog(Reminder(client))



