import discord
from discord.ext import commands
from discord import app_commands
from io import StringIO
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'機器人已上線：{bot.user}')

@bot.tree.command(name="新番推薦", description="私下收到本季動畫推薦")
async def new_anime(interaction: discord.Interaction):
    content = """【2025 春季新番推薦】

--熱血--
・我英 - 非法英雄  
・搖滾樂是淑女的嗜好  
・防風少年 S2  
・賽馬娘 - 灰髮灰姑娘  

--黨爭--
・紫雲寺家的兄弟姊妹  
・男女之間存在純友誼?

--戀愛帶奇幻--
・完美到難以接近的聖女  
・受到猩猩之神庇佑的大小姐受到王立騎士團寵愛  

--休閒--
・Lycoris Recoil: 友誼是時間的竊賊  
・歲月流逝飯菜依舊美味  

--搞笑--
・魔女守護者（喜歡銀魂必看）

--誤會流--
・鄉下大叔成為劍聖  

--其他--
・藥師少女 S2  
・轉生為白豬貴族的我"""

    file = discord.File(fp=StringIO(content), filename="2025春季新番推薦.txt")

    await interaction.response.send_message(
        content="🎬 以下是依分類整理的推薦動畫清單：", 
        ephemeral=True,
        file=file
    )

bot.run(os.environ["DISCORD_TOKEN"])


