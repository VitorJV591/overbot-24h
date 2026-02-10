import discord, os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True)

@bot.event
async def on_ready():
    print(f'✅ {bot.user} ONLINE E PRONTO PARA A FAXINA!')

@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send(member.avatar.url)

# AQUI ESTÁ A LINHA PULADA ABAIXO
@bot.command()
@commands.has_permissions(manage_messages=True)
async def limpar(ctx, quantidade: int):
    await ctx.channel.purge(limit=quantidade + 1)
    await ctx.send(f"🧹 Limpei {quantidade} mensagens!", delete_after=5)

bot.run(os.getenv('DISCORD_TOKEN'))
