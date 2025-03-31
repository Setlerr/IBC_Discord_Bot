# -*- coding: utf-8 -*-
import nextcord
import json
import asyncio
from nextcord.ext import commands
from pathlib import Path
from settings.settings import sign_up_logs
from funcs.role_check import check_for_admin

intents = nextcord.Intents.all()


class Remove(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.locks = {}

    # remove
    @commands.command(name="rm", aliases=["wypis", "remove"])
    async def rm(self, ctx, word: str, arg2: nextcord.User = None):
        await ctx.message.delete()
        # author = ctx.author.id
        # if author in self.locks:
        #    await asyncio.sleep(25)
        #    await self.locks[author].acquire()
        # self.locks[author] = asyncio.Lock()
        # await asyncio.sleep(5)

        print("remove")
        channel_id = ctx.channel.id
        raw_data = Path("./data.json").read_text()
        print(raw_data)
        flag = 0
        Current_games = json.loads(raw_data)
        print("current_Games")
        print(Current_games)
        message_id = Current_games[str(channel_id)]["message_id"]
        print(message_id)
        msg = await ctx.fetch_message(message_id)
        print(msg)
        mess = msg.content
        check_slot = msg.content
        author_id = Current_games[str(channel_id)]["Author"]
        print(message_id)
        user_to_remove = ctx.author.id
        if arg2 is not None:
            if ctx.author.id == author_id or check_for_admin(ctx) is True:
                user_to_remove = arg2.id
            else:
                await ctx.channel.send(
                    "Musisz być właścicielem zapisów, żeby kogoś wypisać!",
                    delete_after=5,
                )
                return
        if word.find("slot") == -1:
            await ctx.channel.send(
                "Musisz nazwać slota z którego chcesz się wypisać np. slot5",
                delete_after=5,
            )
            return
        elif check_slot.find(word + " ") > -1:
            await ctx.channel.send("Taki slot już istnieje", delete_after=5)
            return
        elif word.find("slot") > -1:
            if word.find(" ") > -1:
                await ctx.channel.send("Bez spacji!", delete_after=5)
                return
            else:
                ##RESIGN LOG
                Message_content = f"{ctx.author.name} Wypisał się z {ctx.channel.name} ze slota {word}"
                print(Message_content)
                ###
                text = msg.content
                text = text.replace("<@" + str(user_to_remove) + ">", word, 1)
                await msg.edit(content=text)
                Current_games[str(channel_id)]["Players"].remove(str(user_to_remove))
                with open("data.json", "w") as f:
                    json.dump(Current_games, f)
                try:
                    channel = ctx.guild.get_thread(sign_up_logs)
                    await channel.send(Message_content)
                except:
                    print("sign out logs error")
        # await asyncio.sleep(25)
        # await self.locks[author].release()


def setup(client):
    client.add_cog(Remove(client))
