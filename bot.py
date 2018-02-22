import discord
from discord.ext import commands

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

bot.run('NDE1MjY5NzczODg3NDA2MDgw.DW18-w.rWFfcZzfeqDIYalhhASvGzfFiss')
