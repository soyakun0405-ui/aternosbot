from discord.ext import commands
import discord
from aternos import Client
import os

# 環境変数から情報を読み込み
TOKEN = os.getenv("DISCORD_TOKEN")
EMAIL = os.getenv("AT_EMAIL")
PASS = os.getenv("AT_PASS")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Aternos サーバー取得
def get_server():
    at = Client.from_credentials(EMAIL, PASS)
    return at.list_servers()[0]

@bot.command()
async def start(ctx):
    await ctx.send("🔄 サーバー起動中…")
    srv = get_server()
    srv.start()
    await ctx.send("✅ サーバーを起動しました！")

@bot.command()
async def stop(ctx):
    await ctx.send("⏹ サーバー停止中…")
    srv = get_server()
    srv.stop()
    await ctx.send("✅ サーバーを停止しました！")

@bot.command()
async def ping(ctx):
    await ctx.send("pong! 🏓")

bot.run(TOKEN)
