import discord
#client = discord.Client()
default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)

@client.event
async def on_ready():
    print("Le bot est prêt !")

@client.event
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





#client = discord.Client(command_prefix=',', intents=default_intents)

#@client.event
#async def on_member_join(member):
#    general_channel:discord.TextChannel = client.get_channel(964428441673928717)
#    await general_channel.send(f"Bienvenue sur le serveur {member.display_name} !")
 #   await member.send("hi")

@client.event
async def on_member_join(member):
    general_channel:discord.TextChannel= client.get_channel(964428441673928717)
    await general_channel.send(f"Bienvenue sur le serveur {member.display_name} !")
    print(f"L'utilisateur {member.display_name} a rejoint le serveur !")


client.run("OTY0NDIwNjAxMzUzNzMyMTE2.YlkYrQ.betMiUVNVh24EaFqTXSN6EbSTaA")
