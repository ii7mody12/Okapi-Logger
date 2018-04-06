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

def decode(inp):
    return "".join(map(lambda x: chr(ord(x) - 7), inp))

colors = [discord.Colour.red(), discord.Colour.orange(), discord.Colour.gold(), discord.Colour.teal(), discord.Colour.green(), discord.Colour.blue(), discord.Colour.purple()]
bot = commands.Bot(command_prefix=commands.when_mentioned_or('log.'))
bot.remove_command('help')

@bot.event
async def on_ready():
    print(' ------------------------------')
    print(' ------------------------------')
    print('LOGGER BOT IS ONLINE AND WORKING')
    print(' ------------------------------')
    print(' ------------------------------')
    print('')

@bot.command()
async def log(ctx):
    await guild.create_text_channel('Log')
    await ctx.send("Chanel Created!")

bot.run(decode("UKT~VKL\x81TKL~V[r<V[H\x80TqH<5KhsyaH5QkIHT||\x81<~`|O@ZnhmhqkI{W]8P"))
