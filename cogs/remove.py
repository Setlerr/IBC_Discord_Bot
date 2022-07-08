import nextcord

from nextcord.ext import commands

intents = nextcord.Intents.all()
intents.members = True
intents.messages = True

class Remove(commands.Cog):
    
    def __init__(self,client):
        self.client=client
#remove
    @commands.command(name='rm',aliases=['wypis','remove'])
    async def rm(self, ctx,*,word: str):
        print("remove")                   
        messages = await ctx.channel.history(limit=200).flatten()
        for event in messages:
            if "Event" in event.content:
                check_slot = event.content
                if word.find("slot") == -1:               
                    await ctx.channel.send("Musisz nazwać slota z którego chcesz się wypisać np. slot5",delete_after=5)
                    break
                elif check_slot.find(word+" ")>-1:
                    await ctx.channel.send("Taki slot już istnieje",delete_after=5)
                    break
                elif word.find("slot")>-1:
                    if word.find(" ")>-1:
                        await ctx.channel.send("Bez spacji!",delete_after=5)
                    else:
                        text = event.content
                        check_position = text.find("Created by: ")
                        check_text = text[check_position:]
                        text = text[:check_position]
                        text = text.replace(str(ctx.author.mention),word,1) #this line is temporary
                        text = text.replace(str(ctx.author.name),word,1)
                        await event.edit(content=text+check_text)
        await ctx.message.delete()


def setup(client):
    client.add_cog(Remove(client))

