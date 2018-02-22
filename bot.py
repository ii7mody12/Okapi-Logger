import discord
from discord.ext import commands
import time

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------')

@bot.command()
async def play(ctx, *, play: str):
    await bot.change_presence(game=discord.Game(name=play))
    await ctx.send(f"Thanks to {ctx.author.mention} I'm playing {play}.")

@bot.command(pass_context=True)
async def ping(ctx):
    t1 = time.perf_counter()
    t2 = time.perf_counter()
    await ctx.send("Pong! Round Trip Took: {}ms".format(round((t2-t1)*1000)))

bot.run('NDE1MjY5NzczODg3NDA2MDgw.DW18-w.rWFfcZzfeqDIYalhhASvGzfFiss')
