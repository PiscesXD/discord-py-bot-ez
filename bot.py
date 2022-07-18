import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="?" , intents = intents)

@bot.event
async def on_ready():
	print("開啟成功~")
	activity = discord.Game('Pisces') 
	status = discord.Status.idle
	await bot.change_presence(status=status , activity=activity)

#指令觸發 ?嗨嗨
@bot.commansd()
async def 嗨嗨(ctx):
	return await ctx.send("嗨~")

#文字觸發 早安
@bot.event
async def on_message(message):
	if message.content == '早安':
		await message.channel.send('早安ㄚ~')

bot.run("bot token")
