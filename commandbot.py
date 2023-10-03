import discord, random, os
from discord.ext import commands
from bot_logic import gen_combat, gen_emodji, gen_faction, gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot i only can sending a meme :>{bot.user}!')

@bot.command()
async def meme(ctx):
    image_name = random.choice(os.listdir('images'))
    with open(f'images/{image_name}', 'rb') as f:  
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("MTE1MTQ5NTg4NjM4MDIwODEyOA.GwyhOi.PFMJY44fLtGtHLvg3RyxYVARQQSjXFYnZV3wNQ")
