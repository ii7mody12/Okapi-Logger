import discordbot
import asyncio

bot = discordbot.DiscordBot()

@bot.event
async def on_member_join(member):
    await bot.send_message(member.server, "Welcome {0.mention}, would you like to introduce yourself?".format(member))

@bot.command(pass_context=True)
async def greet(ctx):
    await bot.responses.say("Hi there, {0.mention}, how are you?".format(ctx.message.author))
bot.run()
