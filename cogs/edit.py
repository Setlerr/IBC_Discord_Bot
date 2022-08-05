import nextcord

from nextcord.ext import commands


intents = nextcord.Intents.all()
intents.members = True
intents.messages = True

class Edit(commands.Cog):
    
    def __init__(self,client):
        self.client=client
#edit event by creator
    @commands.command()
    async def edit(self, ctx, *, word: str): #edit
        messages = await ctx.channel.history(limit=200).flatten()
        for event in messages:
            if "Event" in event.content:
                await ctx.message.delete()
                text = event.content
                check_position = text.find("Created by: ")
                check_text = text[check_position:]
                if check_text.find(str(ctx.author.mention)) > -1:
                    await event.edit(content="Event\n"+ word + "\nCreated by: " + str(ctx.author.mention))
                else:
                    await ctx.channel.send("Nie możesz edytować tej wiadomości!",delete_after=5)


def setup(client):
    client.add_cog(Edit(client))


