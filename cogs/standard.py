import nextcord
import nextcord.utils
import os
import subprocess
from nextcord.ext import commands

# import psutil


intents = nextcord.Intents.all()
intents.members = True
intents.messages = True


class Standard(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_any_role("Moderator", "Admin", "Technik", "Mission Maker")
    async def standard(self, ctx):
        await ctx.message.delete()
        # ścieżka do folderu, w którym znajduje się plik .exe
        folder_path = "E:\Games\Arma\Server_Install"

        # nazwa pliku .exe i argumenty
        filename = "arma3serverprofiling_x64.exe"
        arg1 = '-port=2302 "-config=E:\Games\Arma\Server_Install\Servers\_5bc4a2cc2a5b476597450a6f3a14312d\server_config.cfg" "-cfg=E:\Games\Arma\Server_Install\Servers\_5bc4a2cc2a5b476597450a6f3a14312d\server_basic.cfg" "-profiles=E:\Games\Arma\Server_Install\Servers\_5bc4a2cc2a5b476597450a6f3a14312d" -name=_5bc4a2cc2a5b476597450a6f3a14312d "-mod=@CBA_A3;@CUP_Weapons;@CUP_Terrains__Core;@RHSUSAF;@RHSAFRF;@CUP_Units;@CUP_Terrains__Maps;@ace;@Jbad;@RHSGREF;@CJTF_No_Helmet_Req_IR_Strobe;@L3_GPNVG18_Panoramic_Night_Vision;@FIR_AWS_AirWeaponSystem_;@RHSSAF;@CUP_Vehicles;@PSZ_Polish_Armed_Forces;@Enhanced_Movement;@No_40mm_Smoke_Bounce;@Zeus_Enhanced;@CUP_Terrains__CWA;@LAMBS_RPG;@LAMBS_Suppression;@LAMBS_Turrets;@UnderSiege_Flags__Markers;@CH_View_Distance;@KAT__Advanced_Medical;@_MP_Ragdoll_Physics_Plus_;@Queen_and_Country;@VSM_All_In_One_Collection;@Redd_n_Tank_Vehicles;@Splendid_Smoke;@F_A_18E_F_Super_Hornet_2020;@G_O_S_Al_Rayak;@G_O_S_Dariyah;@G_O_S_Gunkizli;@G_O_S_Kalu_Khan;@G_O_S_Leskovets;@G_O_S_N_Djenahoud;@Hellanmaa;@Ihantala;@Kastellorizo;@Kunduz_Afghanistan__Doors__Multiplayer_Fix;@Maksniemi;@Suursaari;@Tembelan_Island;@Thirsk_Winter_;@Vinjesvingen;@Sennoe;@LYTHIUM;@Mutambara;@Interiors_for_CUP;@Kimmirut;@UMB_Colombia;@IBC_Main;@ACE_Compat__RHS_AFRF;@ACE_Compat__RHS_USAF;@ACE_Compat__RHS_GREF;@Gruppe_Adler_Trenches;@Alpha_Group_Equipment;@LAMBS_Danger_fsm;@PSZ_Compatibility_with_ACE;@No_More_Aircraft_Bouncing;@CUP_ACE3_Compatibility_Addon__Terrains;@ACE_Compat__RHS_SAF;@DUI__Squad_Radar;@CUP_ACE3_Compatibility_Addon__Vehicles;@CUP_ACE3_Compatibility_Addon__Weapons;@Ctab_Devastator_Edition;@Enhanced_Movement_Rework;@ACRE2;@Community_Factions_Project_CFP_;@MAAWS_Additional_Ammo_Types;@Anthrax_s_OPFOR_LDF_RHS_;@LAMBS_RPG_CUP;@BackpackOnChest__Redux;@No_40mm_Smoke_Bounce_RHS_compat_;@Freestyles_Crash_Landing;@Ratnik_2035;@Zeus_Enhanced__ACE3_Compatibility;@Anizay;@Beketov;@Cold_War_Rearmed_III__Eilte;@Cold_War_Rearmed_III__Poseidon;@Cold_War_Rearmed_III__Saint_David;@Fapovo_Island;@G_O_S_N_ziwasogo_v2_APEX;@Hunters_Valley_map;@Ihantala_Winter;@Isla_Abramia;@Isla_Duala;@Island_Panthera;@Khoramshahr_Beta_;@Kidal;@Kingdom_of_Regero;@Kujari;@Lingor_Dingor_Island;@Napf_Island_A3;@Pecher;@Reshmaan_Province;@Rosche_Germany;@Ruha;@Scottish_Highlands;@Sugar_Lake;@Summa;@Virolahti__Valtatie_7;@Al_Salman_Iraq_legacy_;@VET_Unflipping;@Knock_On_Vehicles;@PSZ_Compatibility_with_RHS;@LAMBS_RPG_RHS;@PLCUP_Polish_retexture_of_CUP;@Individual_First_Aid_Kit;@VSM__ACE3_Compatibility;@North_Takistan;@Miroslavl;@Aliabad_Region;@Niakala;@3CB_Factions;@Prone_Launcher;" -enableHT -netlog "-servermod=E:\Games\Arma\LocalMods\@ocap"'
        flag = 0

        for proc in psutil.process_iter():
            if proc.name() == "arma3server_x64.exe":
                await ctx.message.channel.send(
                    "Serwer jest już uruchomiony, poproś Administracje o jego wyłączenie.",
                    delete_after=7,
                )
                flag = 1
            if proc.name() == "arma3serverprofiling_x64":
                await ctx.message.channel.send(
                    "Serwer jest już uruchomiony, poproś Administracje o jego wyłączenie.",
                    delete_after=7,
                )
                flag = 1
        # pełna ścieżka do pliku .exe
        print(flag)
        if flag == 0:
            file_path = os.path.join(folder_path, filename)
            try:
                subprocess.Popen([file_path] + arg1)
                await ctx.send(f"Program został uruchomiony.", delete_after=5)
            except Exception as e:
                await ctx.send(f"Wystąpił błąd podczas uruchamiania Serwera: {e}")


def setup(client):
    client.add_cog(Standard(client))
