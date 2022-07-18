import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="?" , intents = intents)

@bot.event
async def on_ready():
	print("開啟成功~")

@bot.commansd()
async def hello(ctx):
	return await ctx.send("你好呀")

bot.run("bot token")
