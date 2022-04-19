import discord
from discord import Client
from discord.ext import commands
from discord import Intents
#default_intents = discord.Intents.default()
#default_intents.members = True
#client = discord.Client(intents=default_intents)

class MyBot(commands.Bot):
    def __init__(self):
       intents = Intents.default()
       intents.members = True
       super().__init__(command_prefix="!", intents=intents)


    async def on_ready(self):
        self.log.infolog(f"{self.user} has connected to Discord!")



    #@client.event
    async def on_message(message):
        if message.content == "Ping":
            await message.channel.send("Pong")

        if message.content == "hello":
            emoji = '\N{THUMBS UP SIGN}'
            await message.add_reaction(emoji)

        if message.content.startswith("!del"):
            number = int(message.content.split()[1])
            messages = await message.channel.history(limit=number + 1).flatten()
            for each_message in messages:
                await each_message.delete()

        if message.content.startswith("!help"):
            await message.channel.send("les commandes sont:")
            await message.channel.send("- Ping")
            await message.channel.send("- hello")
            await message.channel.send("- !del")
            await message.channel.send("- !help")

    #@client.event
    async def on_member_join(self, member):
        general_channel:discord.TextChannel= self.get_channel(964428441673928717)
        await general_channel.send(f"Bienvenue sur le serveur {member.display_name} !")
        print(f"L'utilisateur {member.display_name} a rejoint le serveur !")

bot_instance=MyBot()
