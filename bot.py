import inspect
import os
import hashlib
import async_timeout
import asyncio
import random
import psutil
import discord
from discord.ext import commands
from pkg_resources import get_distribution
from sys import version_info
from collections import OrderedDict
from datetime import datetime

okapiicon = """https://orig02.deviantart.net/d6e5/f/2013/184/5/6/56c80607908d203f4b516480701586af-d6bsxy5.png"""

colors = [discord.Colour.red(), discord.Colour.orange(), discord.Colour.gold(), discord.Colour.teal(), discord.Colour.green(), discord.Colour.blue(), discord.Colour.purple()]
bot = commands.Bot(command_prefix='.')
bot.remove_command('help')

@bot.event
async def on_ready():
    print(' ------------------------------')
    print(' ------------------------------')
    print('NDEOGJ BOT IS ONLINE AND WORKING')
    print(' ------------------------------')
    print(' ------------------------------')
    print('')

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
async def rules(ctx):
    embed=discord.Embed(color=random.choice(colors))
    embed.add_field(name="Rule #1", value="NSFW Content Belongs In #not-safe-for-school", inline=False)
    embed.add_field(name="Rule #2", value="Only Spam Bots In #bot-spam", inline=False)
    embed.add_field(name="Rule #3", value="No Real Or Close To Real Names In Chat", inline=False)
    embed.add_field(name="Rule #4", value="Requests Go In #requests", inline=False)
    embed.add_field(name="Rule #5", value="No More Rules", inline=False)
    embed.set_footer(text="Just An Okapi", icon_url=okapiicon)
    await ctx.send(embed=embed)

@bot.command()
async def about(ctx, user: discord.Member):
    member = ctx.author
    roles = [role.name.replace('@', '@\u200b') for role in member.roles]
    embed = discord.Embed(title="About {}".format(user.name), description="Here's what info I could find.", color=random.choice(colors))
    embed.add_field(inline=True, name="ID", value=user.id)
    embed.add_field(inline=True, name="Name", value=user.name)
    embed.add_field(inline=True, name="Joined", value=user.joined_at)
    embed.add_field(inline=True, name="Status", value=user.status)
    embed.add_field(inline=True, name='Roles', value=', '.join(roles) if len(roles) < 10 else f'{len(roles)} roles')
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def info(ctx):
    embed=discord.Embed(color=random.choice(colors))
    embed.add_field(name=".botinfo", value="To See Information About The Bot", inline=False)
    embed.add_field(name=".serverinfo", value="To See Information About The Server", inline=False)
    embed.add_field(name=".info", value="To See This Message", inline=False)
    embed.set_footer(text="Just An Okapi", icon_url=okapiicon)
    await ctx.send(embed=embed)

@bot.command(aliases=['stats'])
async def serverinfo(ctx):
    process = psutil.Process()
    total_members = sum(1 for _ in bot.get_all_members())
    total_servers = len(bot.guilds)
    total_channels = sum(1 for _ in bot.get_all_channels())
    cpu_usage = process.cpu_percent() / psutil.cpu_count()
    ram_usage = process.memory_full_info().uss / 1024**2
    embed = discord.Embed(color=random.choice(colors))
    embed.add_field(name="#\u20e3 Server Statistics:", value="**Guilds**: {}\n**Channels**: {}\n**Users**: {}".format(total_servers, total_channels, total_members))
    embed.add_field(name="💻 Resource Usage:", value="CPU: {:.2f} %\nRAM: {:.2f} MiB".format(cpu_usage, ram_usage))
    py_e = bot.get_emoji(417167904342278155)
    disc_e = bot.get_emoji(417169255629455371)
    embed.add_field(name="Running On:", value=f"""{py_e}: {".".join([str(v) for v in version_info[:3]])}  {disc_e}: {get_distribution('discord.py').version} [discord.py]""")
    embed.set_footer(text="Just An Okapi", icon_url=okapiicon)
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Prefix Is `.`", color=random.choice(colors))
    embed.add_field(name=".help", value="Explains how to use commands.", inline=False)
    embed.add_field(name=".info", value="Tells what the info commands are.", inline=False)
    embed.add_field(name=".rules", value="Tells what the current rules are.", inline=False)
    embed.add_field(name=".play game", value="Sets the bots current playing status.", inline=False)
    embed.add_field(name=".ping", value="Checks latency of the bot.", inline=False)
    embed.add_field(name=".emoji (NOT WORKING)", value="Shows a list of all the server emoji.", inline=False)
    embed.add_field(name=".about @username#0000", value="Tells about a user.", inline=False)
    embed.set_footer(text="Just An Okapi", icon_url=okapiicon)
    await ctx.send(embed=embed)






bot.run('NDE1MjY5NzczODg3NDA2MDgw.DW18-w.rWFfcZzfeqDIYalhhASvGzfFiss')
