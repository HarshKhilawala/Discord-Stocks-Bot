import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f"{client.user} has connected to Discord!")


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Hi {member.name}, welcome to my Discord Server!"
    )

@client.event
async def on_message(message):
    if message.author==client.user:
        return
    brooklyn_99_quotes = [
    "I\'m the human form of 💯 emoji ",
    "Bingpot!",
    (
        "cool cool cool cool cool cool cool,"
        "no doubt no doubt no doubt no doubt"
    ),
    ]

    if message.content=="99!":
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
    elif 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday!🎉🎈')
    elif message.content=='raise-exception':
        raise discord.DiscordException
        

client.run(TOKEN)
