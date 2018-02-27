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



setnl = ":blob0w0: :blobamused: :blobangel: :blobangery: :blobangry: :blobastonished: :blobawkward: :blobaww: :blobconfounded: :blobconfused: :blobcool: :blobcry: :blobdead: :blobderpy: :blobdetective: :blobdevil: :blobdizzy: :blobdrool: :blobexpressionless: :blobeyes: :blobfacepalm: :blobfearful: :blobfrown: :blobfrowningbig: :blobgentle: :blobglare: :blobidea: :blobkir: :bloblul: :blobmoustache: :blobnauseated: :blobnelly: :blobnogood: :blobokhand: :blobonfire: :blobowoevil: :blobrain: :blobrick: :blobsleeping: :blobsleepless: :blobsmile: :blobsmirk: :blobspy: :blobthinking: :blobthumbsdown: :blobtilt: :blobunsure: :blobwoah: :discord: :python:"
setn00,setn01,setn02,setn03,setn04,setn05,setn06,setn07,setn08,setn09,setn10,setn11,setn12,setn13,setn14,setn15,setn16,setn17,setn18,setn19,setn20,setn21,setn22,setn23,setn24,setn25,setn26,setn27,setn28,setn29,setn30,setn31,setn32,setn33,setn34,setn35,setn36,setn37,setn38,setn39,setn40,setn41,setn42,setn43,setn44,setn45,setn46,setn47,setn48,setn49 = setnl.split(" ")

seidl = "<:blob0w0:417370606921711616> <:blobamused:417370692837965834> <:blobangel:417370783061639170> <:blobangery:417370804620361739> <:blobangry:417370828334825482> <:blobastonished:417370990054604820> <:blobawkward:417370961332011028> <:blobaww:417370941421781005> <:blobconfounded:417434303933186049> <:blobconfused:417371065220726784> <:blobcool:417371114239688704> <:blobcry:417371183592505344> <:blobdead:417371212474482699> <:blobderpy:417373351888027648> <:blobdetective:417371304669347855> <:blobdevil:417371368959508481> <:blobdizzy:417371345060626443> <:blobdrool:417371457622900737> <:blobexpressionless:417371486542626818> <:blobeyes:417371513860259841> <:blobfacepalm:417371534517207044> <:blobfearful:417371561243181077> <:blobfrown:417371640612126725> <:blobfrowningbig:417371683230318602> <:blobgentle:417373047649992716> <:blobglare:417371723986370570> <:blobidea:417371832740610048> <:blobkir:417433992351055872> <:bloblul:417371886738210827> <:blobmoustache:417371932858646549> <:blobnauseated:417370910325080064> <:blobnelly:417373712254369797> <:blobnogood:417433715338117121> <:blobokhand:417372042866851851> <:blobonfire:417372080464723994> <:blobowoevil:417372388737548289> <:blobrain:417373379289415690> <:blobrick:417373415167492104> <:blobsleeping:417372438137929729> <:blobsleepless:417372530047713280> <:blobsmile:417372558275641345> <:blobsmirk:417372610515566602> <:blobspy:417372667323219968> <:blobthinking:417372736529235989> <:blobthumbsdown:417372896248463360> <:blobtilt:417372292260298762> <:blobunsure:417373235554942986> <:blobwoah:417438617083052128> <:discord:417169255629455371> <:python:417167904342278155>"
seid00,seid01,seid02,seid03,seid04,seid05,seid06,seid07,seid08,seid09,seid10,seid11,seid12,seid13,seid14,seid15,seid16,seid17,seid18,seid19,seid20,seid21,seid22,seid23,seid24,seid25,seid26,seid27,seid28,seid29,seid30,seid31,seid32,seid33,seid34,seid35,seid36,seid37,seid38,seid39,seid40,seid41,seid42,seid43,seid44,seid45,seid46,seid47,seid48,seid49 = seidl.split(" ")

@bot.command()
async def emoji(ctx):
    embed=discord.Embed(color=random.choice(colors))
    embed.add_field(inline=True, name=seid00, value=setn00)
    embed.add_field(inline=True, name=seid01, value=setn01)
    embed.add_field(inline=True, name=seid02, value=setn02)
    embed.add_field(inline=True, name=seid03, value=setn03)
    embed.add_field(inline=True, name=seid04, value=setn04)
    embed.add_field(inline=True, name=seid05, value=setn05)
    embed.add_field(inline=True, name=seid06, value=setn06)
    embed.add_field(inline=True, name=seid07, value=setn06)
    embed.add_field(inline=True, name=seid08, value=setn08)
    embed.add_field(inline=True, name=seid09, value=setn09)
    embed.add_field(inline=True, name=seid10, value=setn10)
    embed.add_field(inline=True, name=seid11, value=setn11)
    embed.add_field(inline=True, name=seid12, value=setn12)
    embed.add_field(inline=True, name=seid13, value=setn13)
    embed.add_field(inline=True, name=seid14, value=setn14)
    embed.add_field(inline=True, name=seid15, value=setn15)
    embed.add_field(inline=True, name=seid16, value=setn16)
    embed.add_field(inline=True, name=seid17, value=setn16)
    embed.add_field(inline=True, name=seid18, value=setn18)
    embed.add_field(inline=True, name=seid19, value=setn19)
    embed.add_field(inline=True, name=seid20, value=setn20)
    embed.add_field(inline=True, name=seid21, value=setn21)
    embed.add_field(inline=True, name=seid22, value=setn22)
    embed.add_field(inline=True, name=seid23, value=setn23)
    embed.add_field(inline=True, name=seid24, value=setn24)
    embed.add_field(inline=True, name=seid25, value=setn25)
    embed.set_footer(text="Just An Okapi", icon_url=okapiicon)
    await ctx.message.author.send(embed=embed)
    embed=discord.Embed(color=random.choice(colors))
    embed.add_field(inline=True, name=seid26, value=setn26)
    embed.add_field(inline=True, name=seid27, value=setn26)
    embed.add_field(inline=True, name=seid28, value=setn28)
    embed.add_field(inline=True, name=seid29, value=setn29)
    embed.add_field(inline=True, name=seid30, value=setn30)
    embed.add_field(inline=True, name=seid31, value=setn31)
    embed.add_field(inline=True, name=seid32, value=setn32)
    embed.add_field(inline=True, name=seid33, value=setn33)
    embed.add_field(inline=True, name=seid34, value=setn34)
    embed.add_field(inline=True, name=seid35, value=setn35)
    embed.add_field(inline=True, name=seid36, value=setn36)
    embed.add_field(inline=True, name=seid37, value=setn36)
    embed.add_field(inline=True, name=seid38, value=setn38)
    embed.add_field(inline=True, name=seid39, value=setn39)
    embed.add_field(inline=True, name=seid40, value=setn40)
    embed.add_field(inline=True, name=seid41, value=setn41)
    embed.add_field(inline=True, name=seid42, value=setn42)
    embed.add_field(inline=True, name=seid43, value=setn43)
    embed.add_field(inline=True, name=seid44, value=setn44)
    embed.add_field(inline=True, name=seid45, value=setn45)
    embed.add_field(inline=True, name=seid46, value=setn46)
    embed.add_field(inline=True, name=seid47, value=setn46)
    embed.add_field(inline=True, name=seid48, value=setn48)
    embed.add_field(inline=True, name=seid49, value=setn49)
    embed.set_footer(text="Just An Okapi", icon_url=okapiicon)
    await ctx.message.author.send(embed=embed)
    await ctx.message.author.send("Here's all the emojis!")
    embed=discord.Embed(description=f"I Sent You A DM {ctx.author.mention} With All The Emoji.",color=random.choice(colors))
    await ctx.send(embed=embed)


bot.run('NDE1MjY5NzczODg3NDA2MDgw.DW18-w.rWFfcZzfeqDIYalhhASvGzfFiss')
