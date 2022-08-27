import discord
from discord.ext import commands

token = 'MTAxMTYxMTc4NzU1MDAxOTY2NA.GIl8qt.posAj1tSWjILPPwTaDp5EDdqCc3AAs7qVQFSGI'
prefix = '.'

bot = commands.Bot(command_prefix=prefix)
@bot.command()
async def say(ctx, txt ):
    await ctx.message.delete()
    await ctx.send(text)

client.run(token)