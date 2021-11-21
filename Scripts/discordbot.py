# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'OTExODE0MjU2MTg4NTkyMTY4.YZm3Mw.V1txcjMn5dWTSVnKiQcvPQ0_5y8'
MUSIC_CHANNEL_ID = '911872105350594580';
YOUTUBE_URL = 'https://www.youtube.com/watch?v=dLFuHKqWLG8&t=1002s'

voice = None
player = None

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):

    if message.author.bot:
        return

    global voice, player
    msg = message.content

    # ボイスチャンネル参加
    if msg == '!connect':
            if message.author.voice is None:
                await message.channel.send("あなたはボイスチャンネルに接続していません。")
                return

            # ボイスチャンネルに接続する
            await message.author.voice.channel.connect()

            await message.channel.send("接続しました。")

    if msg == '!disconnect':
        if message.guild.voice_client is None:
            await message.channel.send("接続していません。")
            return

        # 切断する
        await message.guild.voice_client.disconnect()

        await message.channel.send("切断しました。")


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)