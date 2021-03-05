import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands
import app


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


intents = discord.Intents.default()
intents.members = True


# client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!',intents=intents)
bot_respond_emoji = "🤖"

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    print(
        f"{bot.user.name} has connected to Discord!")

@bot.command(name='99', help='Responds with the random quote from Brooklyn 99')
async def ninety_nine(ctx):
    brooklyn_99_quotes = [
    "I\'m the human form of 💯 emoji ",
    "Bingpot!",
    (
        "cool cool cool cool cool cool cool,"
        "no doubt no doubt no doubt no doubt"
    ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.message.add_reaction(bot_respond_emoji)
    await ctx.send(response)

@bot.command(name='upload', help='Upload the Image')
async def upload_image(ctx):
    guild = ctx.guild
    author = ctx.author
    daily_updates_channel = discord.utils.get(guild.channels,name="daily-updates")
    await ctx.message.add_reaction(bot_respond_emoji)
    await daily_updates_channel.send(file=discord.File("./images/fig1.png"))
    await author.send(file=discord.File("./images/fig1.png"))

@bot.command(name='roll-dice', help='Stimulates rolling dice')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice=[
    str(random.choice(range(1,number_of_sides+1)))
    for _ in range(number_of_dice)
    ]
    await ctx.message.add_reaction(bot_respond_emoji)
    await ctx.send(', '.join(dice))

@bot.command(name='create-channel', help = "Create new channel (Only Admins)")
@commands.has_role('Admin')
async def create_channel(ctx, channel_name):
    await ctx.message.add_reaction(bot_respond_emoji)
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f"Creating a new channel: {channel_name}")
        await guild.create_text_channel(channel_name)
        await ctx.send(f'Channel created : {channel_name}')

@bot.command(name="status", help="Current Status of the Stock")
async def stock_status(ctx):
    await ctx.message.add_reaction(bot_respond_emoji)
    data = f"""TCS EOD Data\n--Date: {app.stock_data["date"]}
--Open: {app.stock_data["open"]}\n--High: {app.stock_data["high"]}
--Low: {app.stock_data["low"]}\n--Close: {app.stock_data["close"]}
--Adj Close: {app.stock_data["adjclose"]}\n--Volume: {app.stock_data["volume"]}
"""
    await ctx.send(data)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.message.add_reaction(bot_respond_emoji)
        await ctx.send("You do not have Correct Role(permissions) for this command")


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Hi {member.name}, welcome to my Discord Server!"
    )
    guild = discord.utils.get(bot.guilds,name=GUILD)
    general_channel = discord.utils.get(guild.channels,name="general")
    await general_channel.send(f"Hi {member.name}, Welcome to the Server!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'happy birthday' in message.content.lower():
        await message.add_reaction(bot_respond_emoji)
        await message.channel.send('Happy Birthday! 🎈🎉')
    elif message.content == 'raise-exception':
        raise discord.DiscordException
    await bot.process_commands(message)

@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise





bot.run(TOKEN)
