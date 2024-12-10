import discord
import random

TOKEN = "MTMxNjA2ODEzMjA2MTg0MzQ4Ng.GY4ek0.Kh3pmsj2SAsUBjo0fcibUrxt87yyQsakq4pljk"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

valorant_characters = [
    "ジェット", "フェニックス", "セージ", "ブリムストーン", "ソーヴァ", 
    "サイファー", "オーメン", "ヴァイパー", "レイナ", "キルジョイ",
    "スカイ", "ヨル", "アストラ", "KAY/O", "チェンバー",
    "ネオン", "フェイド", "ハーバー", "ゲッコー", "デットロック",
    "ヴァイス"
]

@client.event
async def on_ready():
    print(f'Botがログインしました: {client.user}')

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    if message.content.lower() in ["!valocharacterpickup", "!vcp"]:
        selected_character = random.choice(valorant_characters)
        await message.channel.send(f"今日は: {selected_character} をやれ！")

client.run(TOKEN)
