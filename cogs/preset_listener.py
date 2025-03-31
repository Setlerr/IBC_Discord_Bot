import nextcord
import os

from nextcord.ext import commands

intents = nextcord.Intents.all()
FOLDER_PBO = 'E:/Games/Arma/Server_Install/mpmissions'
FOLDER_HTML = 'C:/Users/Administrator/Desktop/Presety'
ROLE_UPRAWNIONE = ["Admin", "Technik", "Mission Maker", "Moderator"]
channel_id = 1289597864384663693 #test 1079691391082451014
class FileListener(commands.Cog):
    def __init__(self, client, channel_id):
        self.client = client
        self.channel_id = channel_id
        self.temp = ""

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id != channel_id:
            return
        if message.author.bot:
            return
        if not any(role.name in ROLE_UPRAWNIONE for role in message.author.roles):
            await message.channel.send("Nie masz uprawnień do wysyłania plików tutaj.")
            return

        # Obsługa załączników
        for attachment in message.attachments:
            if attachment.filename.endswith(".pbo"):
                folder = FOLDER_PBO
            elif attachment.filename.endswith(".html"):
                folder = FOLDER_HTML
            else:
                continue  # Jeśli plik nie jest .pbo lub .html, pomiń go

            file_path = os.path.join(folder, attachment.filename)
            file_exists = os.path.isfile(file_path)

            # Jeśli plik już istnieje i użytkownik jest Mission Makerem
            if file_exists and "Mission Maker" in [role.name for role in message.author.roles]:
                technik_role = nextcord.utils.get(message.guild.roles, name="Technik")
                if technik_role:
                    # Wysłanie wiadomości z prośbą o zatwierdzenie
                    confirm_msg = await message.channel.send(f"{technik_role.mention} Czy nadpisać plik `{attachment.filename}`?")
                    await confirm_msg.add_reaction("✅")  # Tak
                    await confirm_msg.add_reaction("❌")  # Nie

                    def check(reaction, user):
                        # Upewnienie się, że reakcja pochodzi od Technika na właściwą wiadomość
                        return user in technik_role.members and str(reaction.emoji) in ["✅", "❌"] and reaction.message.id == confirm_msg.id

                    try:
                        # Czekanie na reakcję Technika
                        reaction, user = await self.client.wait_for("reaction_add", check=check, timeout=60.0)
                        if str(reaction.emoji) == "✅":
                            await attachment.save(file_path)
                            await message.channel.send("Plik nadpisany.")
                        else:
                            await message.channel.send("Nadpisanie anulowane.")
                    except TimeoutError:
                        await message.channel.send("Brak odpowiedzi od Technika. Nadpisanie anulowane.")
                else:
                    await message.channel.send("Nie znaleziono roli Technik.")
            else:
                # Jeśli plik nie istnieje lub użytkownik ma inne uprawnienia, zapisz plik bez zatwierdzenia
                await attachment.save(file_path)
                await message.channel.send("Plik zapisany.")    


def setup(client):
    
    client.add_cog(FileListener(client, channel_id))
