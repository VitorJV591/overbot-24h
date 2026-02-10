import discord, os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True # ESSA LINHA PRECISA ESTAR AQUI!
intents.guilds = True
intents.members = True 

bot = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True)

@bot.event
async def on_ready():
    print(f'✅ {bot.user} ONLINE E PRONTO PARA A FAXINA!')

@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send(member.avatar.url)

@bot.command()
async def comandos(ctx):
    await ctx.send("📜 Comandos ativos: !avatar, !reformar, !limpar")

@bot.command()
async def reformar(ctx):
    await ctx.send("🧹 *Limpando tudo...*")
    for canal in ctx.guild.channels:
        try: await canal.delete()
        except: continue
    await ctx.guild.create_text_channel("💬-geral")

bot.run(os.getenv('DISCORD_TOKEN'))
