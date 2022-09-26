from queue import Empty
import nextcord
import json
from nextcord.ext import commands
from pathlib import Path
intents = nextcord.Intents.all()

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

class Register(commands.Cog):
    
    def __init__(self,client):
        self.client=client
#register
    @commands.command(name='re',aliases=['zapis','register','zapisz'])
    async def re(self, ctx, arg1:str, arg2: nextcord.User = None): 
        print(arg2)
        if arg1.find("slot") == -1:
            await ctx.message.delete()
            await ctx.channel.send("Nie ma takiej roli",delete_after=5)
        elif arg1.find("slot") > -1:
            if has_numbers(arg1)==True:
                flag = 0
                await ctx.message.delete()
                channel_id = ctx.channel.id
                raw_data = Path("./data.json").read_text()
                print(raw_data)
                Current_games = json.loads(raw_data)
                print("current_Games")
                print(Current_games)
                message_id = Current_games[str(channel_id)]["message_id"]
                print(message_id)
                msg = await ctx.fetch_message(message_id)
                mess = msg.content

                if mess.find(arg1) == -1:
                    await ctx.channel.send("Nie ma takiej roli",delete_after=5)
                    flag = 1
                else:
                    author_id = Current_games[str(channel_id)]["Author"]
                    print(message_id)
                    user_to_register = ctx.author.name
                    #register someone as a Author/Admin/Technic/Moderator
                    if arg2 is not None:
                        role1 = nextcord.utils.get(ctx.guild.roles, name="Admin")
                        role2 = nextcord.utils.get(ctx.guild.roles, name="Technik")
                        role3 = nextcord.utils.get(ctx.guild.roles, name="Moderator")
                        roles_check = [role1,role2,role3]

                        for role in roles_check:
                            if role in ctx.author.roles:
                                has_permission = 1
                        if ctx.author.mention == author_id or has_permission == 1:
                            user_to_register = arg2.name
                        else:
                            await ctx.channel.send("Musisz być właścicielem zapisów, żeby kogoś wpisać!",delete_after=5)
                            flag=1
                    #end of ^        
                    if mess.find(str(user_to_register))>-1:
                        await ctx.channel.send("Już jesteś zapisany!",delete_after=5)
                        flag = 1
                    if flag==0:
                        mess = mess.replace(arg1,("**"+str(user_to_register)+"**"),1)
                        await msg.edit(content=mess)
                        Current_games[str(channel_id)]["Players"].append(str(user_to_register))
                        with open('data.json', 'w') as f:
                            json.dump(Current_games, f)
            else:
                await ctx.message.delete()
                await ctx.channel.send("Podaj numer slota",delete_after=5)

def setup(client):
    client.add_cog(Register(client))

