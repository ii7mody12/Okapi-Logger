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
emoji_name1 = (":blob0w0:", ":blobamused:", ":blobangel:", ":blobangery:", ":blobangry:", ":blobastonished:", ":blobawkward:", ":blobaww:", ":blobconfounded:", ":blobconfused:", ":blobcool:", ":blobcry:", ":blobdead:", ":blobderpy:", ":blobdetective:", ":blobdevil:", ":blobdizzy:", ":blobdrool:", ":blobexpressionless:", ":blobeyes:", ":blobfacepalm:", ":blobfearful:", ":blobfrown:", ":blobfrowningbig:", ":blobgentle:")
emoji_name2 = (":blobglare:", ":blobidea:", ":blobkir:", ":bloblul:", ":blobmoustache:", ":blobnauseated:", ":blobnelly:", ":blobnogood:", ":blobokhand:", ":blobonfire:", ":blobowoevil:", ":blobrain:", ":blobrick:", ":blobsleeping:", ":blobsleepless:", ":blobsmile:", ":blobsmirk:", ":blobspy:", ":blobthinking:", ":blobthumbsdown:", ":blobtilt:", ":blobunsure:", ":blobwoah:", ":discord:", ":python:")
emoji_id1 = ("<:blob0w0:417370606921711616>", "<:blobamused:417370692837965834>", "<:blobangel:417370783061639170>", "<:blobangery:417370804620361739>", "<:blobangry:417370828334825482>", "<:blobastonished:417370990054604820>", "<:blobawkward:417370961332011028>", "<:blobaww:417370941421781005>", "<:blobconfounded:417434303933186049>", "<:blobconfused:417371065220726784>", "<:blobcool:417371114239688704>", "<:blobcry:417371183592505344>", "<:blobdead:417371212474482699>", "<:blobderpy:417373351888027648>", "<:blobdetective:417371304669347855>", "<:blobdevil:417371368959508481>", "<:blobdizzy:417371345060626443>", "<:blobdrool:417371457622900737>", "<:blobexpressionless:417371486542626818>", "<:blobeyes:417371513860259841>", "<:blobfacepalm:417371534517207044>", "<:blobfearful:417371561243181077>", "<:blobfrown:417371640612126725>", "<:blobfrowningbig:417371683230318602>", "<:blobgentle:417373047649992716>")
emoji_id2 = ("<:blobglare:417371723986370570>", "<:blobidea:417371832740610048>", "<:blobkir:417433992351055872>", "<:bloblul:417371886738210827>", "<:blobmoustache:417371932858646549>", "<:blobnauseated:417370910325080064>", "<:blobnelly:417373712254369797>", "<:blobnogood:417433715338117121>", "<:blobokhand:417372042866851851>", "<:blobonfire:417372080464723994>", "<:blobowoevil:417372388737548289>", "<:blobrain:417373379289415690>", "<:blobrick:417373415167492104>", "<:blobsleeping:417372438137929729>", "<:blobsleepless:417372530047713280>", "<:blobsmile:417372558275641345>", "<:blobsmirk:417372610515566602>", "<:blobspy:417372667323219968>", "<:blobthinking:417372736529235989>", "<:blobthumbsdown:417372896248463360>", "<:blobtilt:417372292260298762>", "<:blobunsure:417373235554942986>", "<:blobwoah:417438617083052128>", "<:discord:417169255629455371>", "<:python:417167904342278155>")
colors = [discord.Colour.red(), discord.Colour.orange(), discord.Colour.gold(), discord.Colour.teal(), discord.Colour.green(), discord.Colour.blue(), discord.Colour.purple()]
bot = commands.Bot(command_prefix=commands.when_mentioned_or('.'))
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
async def play(ctx):
    embed = discord.Embed(color=random.choice(colors))
    embed.add_field(name=".playing game name", value="Set Status To Playing")
    embed.add_field(name=".listening song name", value="Set Status To Listening")
    embed.add_field(name=".watching video name", value="Set Status To Watching")
    embed.set_footer(text="Just An Okapi", icon_url=okapiicon)
    await ctx.send(embed=embed)

@bot.command()
async def playing(ctx, *, text: str):
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=text))
    embed = discord.Embed(color=random.choice(colors))
    embed.add_field(name=f"I'm Now Playing `{text}`,", value=f"Thanks To {ctx.author.mention}!")
    await ctx.send(embed=embed)

@bot.command()
async def listening(ctx, *, text: str):
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=text))
    embed = discord.Embed(color=random.choice(colors))
    embed.add_field(name=f"I'm Now Listening To `{text}`,", value=f"Thanks To {ctx.author.mention}!")
    await ctx.send(embed=embed)

@bot.command()
async def watching(ctx, *, text: str):
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=text))
    embed = discord.Embed(color=random.choice(colors))
    embed.add_field(name=f"I'm Now Watching `{text}`,", value=f"Thanks To {ctx.author.mention}!")
    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    embed = discord.Embed(color=random.choice(colors))
    embed.add_field(name="Pong! <a:loading:418291364221157386>", value=f"Latency: `{bot.latency * 1000:.0f}ms`")
    await ctx.send(embed=embed)

@bot.command()
async def about(ctx, user: discord.Member):
    member = user
    roles = [role.name.replace('@', '@\u200b') for role in member.roles]
    roleslist = ', '.join(roles) if len(roles) < 10 else f'{len(roles)} roles'
    created = user.created_at.strftime("%A %B %d, %Y")
    joined = user.joined_at.strftime("%A %B %d, %Y")
    embed = discord.Embed(color=random.choice(colors), description=f"**Name** {user.name}\n**Created** {created}\n**Id** {user.id}\n**Joined** {joined}\n**Roles** {roleslist}")
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def info(ctx):
    embed=discord.Embed(color=random.choice(colors), description="**.botinfo** To See Information About The Bot.\n**.serverinfo** To See Information About The Server.\n**.info** To See This Message.")
    embed.set_footer(text="Just An Okapi", icon_url=okapiicon)
    await ctx.send(embed=embed)

@bot.command()
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
async def say(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(f'"{text}" -Anonymous')

@bot.command()
async def embed(ctx, *, text):
    await ctx.message.delete()
    embed=discord.Embed(title=f'"{text}"', description="-Anonymous")
    await ctx.send(embed=embed)

@bot.command()
async def emoji(ctx):
    embed=discord.Embed(color=random.choice(colors))
    indexval = 0
    for indexval in range(25):
        embed.add_field(inline=True, value=emoji_name1[indexval], name=emoji_id1[indexval])
    embed.set_footer(text="Just An Okapi", icon_url=okapiicon)
    await ctx.message.author.send(embed=embed)
    embed=discord.Embed(color=random.choice(colors))
    indexval = 0
    for indexval in range(25):
        embed.add_field(inline=True, value=emoji_name2[indexval], name=emoji_id2[indexval])
    embed.set_footer(text="Just An Okapi", icon_url=okapiicon)
    await ctx.message.author.send(embed=embed)
    embed=discord.Embed(color=random.choice(colors))
    embed.add_field(inline=False, value="There You Go!", name="<:blob0w0:417370606921711616>")
    embed.set_footer(text="Just An Okapi", icon_url=okapiicon)
    await ctx.message.author.send(embed=embed)
    embed=discord.Embed(description=f"{ctx.author.mention} Check Your DM's!",color=random.choice(colors))
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed=discord.Embed(color=random.choice(colors), description="**.help** Explains how to use commands.\n**.info** Tells what the info commands are.\n**.play** Tells what the play commands are.\n**.say text** Says what you want it to.\n**.embed text** Says what you want it to in an embed.\n**.ping** Checks latency of the bot.\n**.emoji** Shows a list of all the ndeogj emojis.\n**.about @username#0000** Tells about a user.")
    embed.set_footer(text="Just An Okapi", icon_url=okapiicon)
    await ctx.send(embed=embed)

bot.run('NDE1MjY5NzczODg3NDA2MDgw.DW18-w.rWFfcZzfeqDIYalhhASvGzfFiss')
