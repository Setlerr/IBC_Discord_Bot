# -*- coding: utf-8 -*-
from queue import Empty
import nextcord
import json
from nextcord.ext import commands
from pathlib import Path
from funcs.role_check import check_for_admin
import asyncio
from settings.settings import sign_up_logs

intents = nextcord.Intents.all()


def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


class Register(commands.Cog):
    def __init__(self, client):
        self.client = client
        # self.locks = {}

    @commands.command(name="re", aliases=["zapis", "register", "zapisz"])
    async def re(self, ctx, arg1: str, arg2: nextcord.User = None):
        await ctx.message.delete()
        # author = ctx.author.id
        # if author in self.locks:
        #    await asyncio.sleep(25)
        #    await self.locks[author].acquire()
        # self.locks[author] = asyncio.Lock()
        # await asyncio.sleep(5)
        print(arg2)
        if arg1.find("slot") == -1:
            await ctx.channel.send("Nie ma takiej roli", delete_after=5)
        elif arg1.find("slot") > -1:
            if has_numbers(arg1) == True:
                flag = 0

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
                    await ctx.channel.send("Nie ma takiej roli", delete_after=5)
                    flag = 1
                else:
                    author_id = Current_games[str(channel_id)]["Author"]
                    print(message_id)
                    user_to_register = ctx.author.id
                    # register someone as a Author/Admin/Technic/Moderator
                    if arg2 is not None:
                        if ctx.author.id == author_id or check_for_admin(ctx) is True:
                            user_to_register = arg2.id
                        else:
                            await ctx.channel.send(
                                "Musisz być właścicielem zapisów, żeby kogoś wpisać!",
                                delete_after=5,
                            )
                            flag = 1
                    # end of ^
                    if mess.find(str(user_to_register)) > -1:
                        await ctx.channel.send("Już jesteś zapisany!", delete_after=5)
                        flag = 1
                    if flag == 0:
                            ###SIGN UP LOG
                            Message_content = f"{ctx.author.name} Zapisał się na {ctx.channel.name} ze slota {arg1}"
                            print(Message_content)
                            ###
                            mess = mess.replace(
                                (arg1 + " "), ("<@" + str(user_to_register) + "> "), 1
                            )
                            await msg.edit(content=mess)
                            Current_games[str(channel_id)]["Players"].append(
                                str(user_to_register)
                            )
                            with open("data.json", "w") as f:
                                json.dump(Current_games, f)
                            try:
                                channel = ctx.guild.get_thread(sign_up_logs)
                                print("signup logs error")
                                await channel.send(Message_content)
                            except:
                                print("register log error")
                            

            else:
                await ctx.channel.send("Podaj numer slota", delete_after=5)

    # await asyncio.sleep(25)
    # await self.locks[author].release()


def setup(client):
    client.add_cog(Register(client))
