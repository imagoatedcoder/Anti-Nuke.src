import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def enable(ctx):
  await ctx.send("ANTI NUKE ENABLED")

token = os.environ['MTA3NDEzNTE1ODE3NDc4MTUyMA.GWszHY.BZuuQc4TJAVRHt-SQY9AlmpZPAavDKXtntjiuU']
bot.run(token)
