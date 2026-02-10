import discord, os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True 

bot = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True)

@bot.event
async def on_ready():
    print(f'✅ {bot.user} ONLINE E PRONTO PARA A FAXINA!')

@bot.command()
async def reformar(ctx):
    await ctx.send("🧹 *INICIANDO FAXINA TOTAL...*")
    for canal in ctx.guild.channels:
        try: await canal.delete()
        except: continue
    # Criando estrutura
    sc = await ctx.guild.create_category("🛡️ STAFF")
    await ctx.guild.create_text_channel("🔒-admin", category=sc)
    pc = await ctx.guild.create_category("🌎 COMUNIDADE")
    await ctx.guild.create_text_channel("💬-geral", category=pc)
    await ctx.guild.create_text_channel("✅-reforma-pronta")

@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send(member.avatar.url)

@bot.command()
async def limpar(ctx, quantidade: int):
    await ctx.channel.purge(limit=quantidade + 1)
    await ctx.send(f"🧹 Limpei {quantidade} mensagens!", delete_after=5)

@bot.command()
async def comandos(ctx):
    await ctx.send("📜 Comandos: !reformar, !limpar, !avatar, !servidor")

bot.run(os.getenv('DISCORD_TOKEN'))
