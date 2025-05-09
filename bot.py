import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'機器人已上線：{bot.user}')

@bot.command()
async def 新番推薦(ctx):
    file = discord.File("A.txt", filename="新番推薦.txt")
    await ctx.send("以下是本季新番推薦：", file=file)

bot.run('MTM3MDQwODAxNTQ3OTU3NDUzOA.GItiX9.mfdMpv-odDc3fhmOW_29ZbzZxNJdcL1ysF4AFU')

