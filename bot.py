import discord
from discord.ext import commands
import asyncio
import random

colors = [discord.Colour.red(), discord.Colour.orange(), discord.Colour.gold(), discord.Colour.teal(), discord.Colour.green(), discord.Colour.blue(), discord.Colour.purple()]
bot = commands.Bot(command_prefix='.')
bot.remove_command('help')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------')

@bot.command()
async def play(ctx, *, play: str):
    await bot.change_presence(game=discord.Game(name=play))
    embed = discord.Embed(color=random.choice(colors))
    embed.add_field(name=f"I'm Now Playing `{play}`,", value=f"Thanks To {ctx.author.mention}!")
    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    embed = discord.Embed(color=random.choice(colors))
    embed.add_field(name="Pong!", value=f"Latency: `{bot.latency * 1000:.0f}ms`")
    await ctx.send(embed=embed)

@bot.command()
async def embed(ctx):
    embed=discord.Embed(title="Title", url="https://Embed.Title.Link", description="Description", color=random.choice(colors))
    embed.set_author(name="Author Name", url="https://Author.Link.com", icon_url="https://Author.Icon.Link")
    embed.set_thumbnail(url="https://Icon.Link.com")
    embed.add_field(name="Field Name", value="Field Value", inline=False)
    embed.set_footer(text="Footer")
    await ctx.send(embed=embed)

@bot.command()
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=random.choice(colors))
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def rules(ctx):
    embed=discord.Embed(color=random.choice(colors))
    embed.add_field(name="Rule #1", value="NSFW Content Belongs In #not-safe-for-school", inline=False)
    embed.add_field(name="Rule #2", value="Only Spam Bots In #bot-spam", inline=False)
    embed.add_field(name="Rule #3", value="No Real Or Close To Real Names In Chat", inline=False)
    embed.add_field(name="Rule #4", value="Requests Go In #requests", inline=False)
    embed.add_field(name="Rule #5", value="No More Rules", inline=False)
    embed.set_footer(text="Just An Okapi", icon_url="https://orig02.deviantart.net/d6e5/f/2013/184/5/6/56c80607908d203f4b516480701586af-d6bsxy5.png")
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Prefix Is `.`", color=random.choice(colors))
    embed.add_field(name=".help", value="Explains how to use commands.", inline=False)
    embed.add_field(name=".rules", value="Tells what the current rules are.", inline=False)
    embed.add_field(name=".play game", value="Sets the bots current playing status.", inline=False)
    embed.add_field(name=".ping", value="Checks latency of the bot.", inline=False)
    embed.add_field(name=".info @username#0000", value="Tells info about user.", inline=False)
    embed.set_footer(text="Just An Okapi", icon_url="https://orig02.deviantart.net/d6e5/f/2013/184/5/6/56c80607908d203f4b516480701586af-d6bsxy5.png")
    await ctx.send(embed=embed)


bot.run('NDE1MjY5NzczODg3NDA2MDgw.DW18-w.rWFfcZzfeqDIYalhhASvGzfFiss')
