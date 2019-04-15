import discord
from discord import Member
from discord import Status
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
from collections import Counter
from discord.utils import get


TOKEN = "BOT TOKEN"
bot = commands.Bot(command_prefix='-')
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f"Im Ready {len(bot.servers)}")
    print(f"Bot Members {len(set(bot.get_all_members()))}")
    print(f"Bot Channels {len(set(bot.get_all_channels()))}")
    print(f"Bot Server {len(bot.servers)}")

@bot.command(pass_context=True)
async def join(ctx, channel: discord.Channel):
        await bot.send_message(ctx.message.channel, 'لا')
        msg = await bot.wait_for_message(author=ctx.message.author, content='بليز')
        await bot.send_message(ctx.message.channel, 'لا')
        msg = await bot.wait_for_message(author=ctx.message.author, content='بليز')
        await bot.send_message(ctx.message.channel, 'لا')
        msg = await bot.wait_for_message(author=ctx.message.author, content='ليز')     
        await bot.send_message(ctx.message.channel, 'K')                   
        await bot.join_voice_channel(channel)


bot.run(TOKEN)
